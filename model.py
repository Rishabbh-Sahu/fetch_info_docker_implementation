# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 2022
@author: Rishabbh sahu
"""
import re

# Dacorator definition to log in text to be processed
def logging_info(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(txt: str):
        logging.info('Text processed: {}'.format(txt))
        return orig_func(txt)

    return wrapper

# Implemented decorator to log details without impacting the actual 
# functionality of the predict function 
@logging_info
def predict(input_text: str) -> str:
    """
    this function returns all the alphanumeric characters present in the input string
    :param input_text: input text
    :return: alphanumeric string
    """
    return re.sub(r'\W', '', str(input_text))
