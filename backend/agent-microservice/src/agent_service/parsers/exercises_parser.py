from typing import Dict
import re
from agent_service.parsers.agent_step_parser import Parser
class ExercisesParser(Parser):
    """
    parses exercises generated by task generator
    """

    def __init__(self):
        pass

    def parse(self, input: str) -> Dict[str, str]:
        """
        parses exercises generated by task generator

        Parameters:
        -----------
        input: str
            a string containing task definition, a generated text and generated exercises
        """
        # [Reading][2][0][1]
        # [Grammar][Präteritum][None][1][1][1]
        contents_pattern = r'\[(.*?)\]'
        task_def_contents = re.findall(contents_pattern, input, re.DOTALL)
        if task_def_contents[0] == "Grammar":
            exercises_text = task_def_contents[6]
        else:
            exercises_text = task_def_contents[4]

        # Remove the last sentence from exercises_text and ensure the result ends with a period.
        exercises_text = '.'.join(exercises_text.strip().split('.')[:-1]) + '.'

        exercises_pattern = r'\[START\](.*?)\[END\]'
        exercises_raw_str = re.findall(exercises_pattern, input, re.DOTALL)

        lesson = {"text": exercises_text}
        exercises = []
        for exercise in exercises_raw_str:
            content = re.findall(contents_pattern, exercise, re.DOTALL)
            type = content[0]
            question = content[1]
            answer_options = []
            solution = []

            if type == "single-choice":
                pattern = r'\s+[a-z]\)\s+'
                segments = re.findall(r'\b[a-z]\)\s(.*?)(?=\s+[a-z]\)|$)', content[2])
                answer_options.append(segments)
                solution.append(content[3][2:])
            elif type == "gaps":
                # Regex pattern to find lists within brackets
                pattern = r'\((.*?)\)'
                # Extract lists
                found_lists = re.findall(pattern, content[2])
                # Convert string lists to list of lists
                answer_options = [item.split(', ') for item in found_lists]
                # Replace the bracketed lists with '__' in the original string
                question = re.sub(pattern, '__', content[2])
                solution.append(content[3].split(', '))
            elif type == "open":
                answer_options = [['']]
                solution.append('')

            exercises.append({"type": type, "question": question, "answer_options": answer_options, "solution": solution})
        lesson['tasks'] = exercises
        return lesson

