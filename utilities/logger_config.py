import logging
import time
import os


def setup_logger(logger_name):
    timestamp = time.strftime('%Y-%m-%d_%H-%M')
    filename = f'automation_{timestamp}.log'
    logs_directory = "../logs/"
    relative_file_path = logs_directory + filename
    current_directory = os.path.dirname(__file__)
    destination_file = os.path.join(current_directory, relative_file_path)

    destination_directory = os.path.join(current_directory, logs_directory)
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(destination_file)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: - %(name)s: - %(levelname)s: - %(message)s', datefmt="%m-%d-%Y %I:%M:%S %p")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
