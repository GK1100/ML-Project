import sys
from src.logger import logging
import yaml

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name: [{0}] at line number: [{1}] error message: [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    file_name, exc_tb.tb_lineno, str(error)

    return error_message



class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    


def read_params(path="params.yaml"):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)

    except Exception as e:
        raise CustomException(e, sys)