import os
from pathlib import Path
import logging

#logging string: see messages of project operations. An Alternative to print statement

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier' #This is a template we will be using for any cnn classification task


list_of_files = [
    ".github/workflows/.gitkeep", # we added this empty .gitkeep file to be able to upload future folders in the workflows folder, but for now we won't.
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)  # The Path function is OS independet and will work for any path string with / or \ for all OPs
    filedir, filename = os.path.split(filepath) #seperates folders from files


    if filedir !="":
        os.makedirs(filedir, exist_ok=True) #creates the folders, if the folder exists it wont be created
        logging.info(f"Creating directory; {filedir} for the file: {filename}") #message output in terminal

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #creating the files, if the file exists it wont be created
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")