# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:05:20 2023

@author: eg01246
"""
# import packages

import re
import numpy as np
import pandas as pd


# function for read checkshot
def load_checkshot(target_file):
    ###############################################
    # a Checkshot example exported from Petrel 2021:
    # # Petrel checkshots format
    # # Unit in x and Y direction: m
    # # Unit in depth: m
    # VERSION 1
    # BEGIN HEADER
    # x
    # Y
    # Z
    # TWT picked
    # MD
    # Well
    # Average velocity
    # Interval velocity
    # END HEADER
    ##############################################

    # read checkshot
    with open(target_file, encoding=('utf-8')) as file:
        content = file.readlines()
        file.close()
    # look for end header
    for i in range(0, len(content)):
        if "END HEADER" in content[i]:
            header_lines = i
            break

    # prepare the data arrays
    read_data = content[header_lines+1:]

    col_x = np.zeros((len(read_data),))
    col_y = np.zeros((len(read_data),))
    col_z = np.zeros((len(read_data),))
    col_twt = np.zeros((len(read_data),))
    col_md = np.zeros((len(read_data),))
    col_well = []
    col_average_velocity = np.zeros((len(read_data),))
    col_interval_velocity = np.zeros((len(read_data),))

    # write arrays using read data
    for i in range(0, len(read_data)):
        temp = re.split(r"[ ]+", read_data[i])
        col_x[i] = float(temp[0])
        col_y[i] = float(temp[1])
        col_z[i] = float(temp[2])
        col_twt[i] = float(temp[3])
        col_md[i] = float(temp[4])
        col_well.append(temp[5])
        col_average_velocity[i] = float(temp[6])
        col_interval_velocity[i] = float(temp[7])

    # combine arrays into a dataframe
    df_result = pd.DataFrame({'X': col_x, 'Y': col_y, 'Z': col_z,
                              'TWT': col_twt, 'MD': col_md, 'Well': col_well,
                              'Average_velocity': col_average_velocity,
                              'Interval_velocity': col_interval_velocity})
    return df_result
# end def


# example
FILE_NAME = 'TDR_LF12-3-1_LF03_PSDM_v2_focus_welltie_section'
data = load_checkshot(FILE_NAME)
