from abc import ABC, abstractmethod
from typing import Callable, Any
import json, base64, os

class LessonProxy:
    """
    decides if a request gets processed in the LessonMaster. For now only first listening is hardcoded with video, the rest of listening is generated by models.
    """

    DATA_PATH = 'agent_service/utils/res/'
    def __init__(self, service_text: Callable[[], Any], service_exercises: Callable[[], Any]) -> None:
        self.service_text = service_text
        self.service_exercises = service_exercises

    def create_text(self, request: str):
        """
        reads text from a JSON file if the request starts with a specific
        string (mocking first listening with a video), otherwise it calls create_exercise function from the LessonMaster
        
        """
        if request.startswith("[Listening][Ich stelle mich vor."):
            video_path = os.path.join(self.DATA_PATH, "layla.mp4")
            encoded_video = self.encode_video_to_base64(video_path)
            self.request = request
            return encoded_video
        else:
            self.request = request
            return self.service_text(request)
        
    def create_exercises(self):
        """
        reads tasks from a JSON file if the request starts with a specific
        string, otherwise it calls create_exercise function from the LessonMaster
        
        """
        if self.request.startswith("[Listening][Ich stelle mich vor."):
            with open(self.DATA_PATH + 'layla/tasks.json', 'r') as f:
                tasks = json.load(f)
            return {'tasks' :tasks }
        else: 
            return self.service_exercises()
        
    def encode_video_to_base64(self, video_path):
        with open(video_path, "rb") as video_file:
            encoded_string = base64.b64encode(video_file.read()).decode('utf-8')
        return encoded_string