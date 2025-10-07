import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE) 
os.makedirs(log_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

## Configuing the logging format
logging.basicConfig(
  filename = LOG_FILE_PATH,
  format = "[ %(asctime)s ] %(lineno)d  %(name)s - %(levelname)s - %(message)s",
  level = logging.INFO,
  
)



'''
[ %(asctime)s ] : timestamp of when the log was recorded
%(lineno)d : Line number in the code where the log was written
%(name)s : Name of the module or file
- %(levelname)s :  Log Level (INFO, ERROR, WARNING, etc)
- %(message)s : Actual log message

'''