import os, sys  
import logging

log_dir = "logs"

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging_filepath = os.path.join(log_dir, "continous_logs.log")

os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(logging_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("summarixerlogger")