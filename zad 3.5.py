# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:26:26 2023

@author: student
"""


def does_list_contain_value(input_list, value):
    return value in input_list


# Przykład użycia funkcji
my_list = [1, 2, 3, 4, 5, 21]
value_to_check = 21
result = does_list_contain_value(my_list, value_to_check)
print(result)
