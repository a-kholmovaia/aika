from typing import List, Union
from agent_service.agent.agent_step import (
    AgentStep,
    AgentValidationStep,
    AgentFinalStep,
)
import json, uuid
from pathlib import Path
import os, logging


class ReasoningLogger:
    """
    represents a trace of agent steps with methods to add steps, store
    exceptions, and generate JSON output.
    """

    def __init__(self, task_type, model_id: str = None) -> None:
        self.query_id = None
        self.model_id = model_id
        self.task_type = task_type.value
        self.trace: List[Union[AgentStep, AgentValidationStep, AgentFinalStep]] = []
        self.query = None
        self.errors: List[Exception] = []

    def set_query_id(self, query_id: str):
        self.query_id = query_id

    def add_exception(self, e: Exception):
        """
        adds an exception to the errors list
        """
        self.errors.append(e)

    def add_step(self, step: Union[AgentStep, AgentValidationStep, AgentFinalStep]):
        """
        adds a step to the trace list
        """
        self.trace.append(step)

    def remove_step(self, index: int) -> None:
        """
        removes a step from the trace list by its index.

        Parameters
        ----------
        index : int
            an index that points to a step in the trace list
        """
        if 0 <= index < len(self.trace):
            self.trace.pop(index)

    def get_last_step(self) -> Union[AgentStep, AgentValidationStep, AgentFinalStep]:
        """
        returns the last step object from the trace list.
        """
        if self.trace:
            return self.trace[-1]
        return None

    def get_last_observation(self) -> str:
        """
        retrieves the observation from the last AgentStep object.
        """
        step = self.get_last_agent_step()
        if step is not None:
            return step.observation
        return ""

    def get_last_agent_step(self) -> AgentStep:
        """
        retrieves the last AgentStep object.
        """
        for i in reversed(self.trace):
            if isinstance(i, AgentStep):
                return i
        return None

    def __str__(self) -> str:
        res = ""
        if len(self.trace) == 0:
            return res
        for step in self.trace:
            res += str(step) + "\n"
        return res

    def to_json(self):
        """
        converts the trace into JSON and writes it to the out file
        """
        if self.query_id is None:
            self.query_id = str(uuid.uuid4())
        dict_f = {"query": self.query}
        dict_f["reasoning_steps"] = [step.model_dump() for step in self.trace]
        dict_f["final_answer"] = self.final_answer
        dict_f["errors"] = self.errors
        dict_f["model"] = self.model_id
        dict_f["task_type"] = self.task_type
        dict_f["query_id"] = self.query_id

        # remove all dots in the model ID
        clean_model_id = self.model_id.replace(".", "_").replace(":", "_")

        filepath = Path("out/" + self.query_id + "_" + clean_model_id + ".json")
        logging.info(filepath)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w", encoding="utf8") as file:
            json.dump(dict_f, file, indent=4, ensure_ascii=False)

    def set_query(self, query: str):
        """
        sets the query

        Parameters
        ----------
        query : str
            the provided query
        """
        self.query = query

    def get_final_answer(self, reached_max_iterations: bool):
        """
        builds an AgentFinalStep instance with the observation of the last AgentStep instance as the final answer,
        """
        step = self.get_last_agent_step()
        if not reached_max_iterations or step.action.startswith("Keine Ant"):
            observation = step.observation
        else:
            observation = "Etwas ist fehlgeschlagen. Versuche es erneut!"
        self.form_final_answer(observation)

    def form_final_answer(self, observation):
        self.final_answer = observation
        step = AgentFinalStep(final_answer=observation)
        self.add_step(step)
