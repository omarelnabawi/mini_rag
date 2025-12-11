from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
from .ProjectController import ProjectController
import re
import os
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale=1024 * 1024  # Convert MB to Bytes

    def validate_uploaded_file(self, file: UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False ,ResponseSignal.FILE_TYPE_NOT_SUPPORTED
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXCEEDED
        return True ,ResponseSignal.FILE_UPLOAD_SUCCESS
    def generate_unique_filepath(self,original_filename: str,project_id: str):
        
        random_filename=self.Generate_random_name()
        project_path=ProjectController().get_project_path(project_id)

        cleaned_filename=self.get_clean_file_name(
            orig_filename=original_filename)

        new_file_path=os.path.join(
            project_path,
            random_filename+"_"+cleaned_filename
        )

        while os.path.exists(new_file_path):
             random_filename=self.Generate_random_name()
             new_file_path=os.path.join(
                project_path,
                random_filename+"_"+cleaned_filename
            )
        return new_file_path , random_filename+"_"+cleaned_filename

    def get_clean_file_name(self,orig_filename:str):
        # Remove special characters and spaces from the filename
        clean_filename = re.sub(r'[^\w.]', '', orig_filename.strip())

        #replace spaces with underscores
        clean_file_name= clean_filename.replace(" ","_")
        return clean_file_name