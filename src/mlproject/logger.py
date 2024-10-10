import logging
from datetime import datetime
import os
import sys

# Define log file name with correct string formatting
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory and path
log_dir = os.path.join(os.getcwd(), 'logs')

# Ensure that the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create the logger object
logger = logging.getLogger("mlProjectLogger")

# if __name__ == "__main__":
#     logging.info("Logging started")
