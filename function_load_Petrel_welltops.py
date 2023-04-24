# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:40:22 2023

@author: eg01246
"""

import pandas as pd
import re
# import numpy as np


def load_welltops(input_file):
    # %% basic reading
    # read welltops
    content = []
    with open(input_file, encoding='utf-8') as file:
        content = file.readlines()

    # look for end header
    for i in range(0, len(content)):
        if "BEGIN HEADER" in content[i]:
            header_begin = i
            break

    # look for end header
    for i in range(0, len(content)):
        if "END HEADER" in content[i]:
            header_end = i
            break

    header_type = []
    header_list = []
    for i in content[header_begin+1: header_end]:
        if ',' in i:
            header_type.append(i)
        if ',' not in i:
            i = i.replace('\n', '').replace(' ', '_').replace('.', '_')
            header_list.append(i)

    length = len(content[header_end+1:])
    # basic reading

    # %% dynamic variable naming
    for var_name in header_list:
        j = header_list.index(var_name)
        locals()[var_name] = []
        # locals
        for i in range(0, length):
            locals()[var_name].append(re.split(' +',
                                               content[header_end+1:][i])[j])
    # end of dynamic naming

    # %% create pandas data frame
    # Creating a dictionary of lists whose names are in list_names
    dict_of_lists = {}
    for name in header_list:
        dict_of_lists[name] = eval(name)

    # Creating the DataFrame
    df = pd.DataFrame(dict_of_lists)
    return df
# end def


# example
input_file = 'Well_Tops_SK.asc'
df = load_welltops(input_file)
