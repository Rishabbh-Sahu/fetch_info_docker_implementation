# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 2022
@author: Rishabbh sahu
"""
import re


def predict(input_text: str) -> str:
    """
    this function returns all the alphanumeric characters present in the input string
    :param input_text: input text
    :return: alphanumeric string
    """
    return re.sub(r'\W', '', str(input_text))
