# Import Huggingface API library
from huggingface_hub import HfApi

# Import OS for operating system functionality
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="self_paced_courses_1_mlops/deployment",
    repo_id="ccwizard/PIMA-Diabetes-Prediction",
    repo_type="space",
    path_in_repo="",
)
