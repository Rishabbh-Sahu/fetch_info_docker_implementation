# -*- coding: utf-8 -*-
"""
Created on Wed May 30 2022
@author: Rishabbh sahu
"""
import pytest

from model import predict


@pytest.mark.parametrize('text, preprocessed_text',
                         [
                             ('4&&9', '49'),
                             ('alph@a£numeric', 'alphanumeric'),
                             ('((&*(text', 'text'),
                         ],
                         )
def test_model(text, preprocessed_text):
    assert predict(text) == preprocessed_text
