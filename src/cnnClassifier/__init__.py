import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs" #creates log folder 
log_filepath = os.path.join(log_dir,"running_logs.log") #log file that contains all the logs of the project
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #prints the logs in the file log and 
        logging.StreamHandler(sys.stdout)  # the terminal
    ]
)

logger = logging.getLogger("cnnClassifierLogger") #use this object and import it in  scripts to view loggings