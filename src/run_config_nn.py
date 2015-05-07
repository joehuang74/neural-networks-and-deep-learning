# -*- coding: utf-8 -*-
# Setup the features files to run.
# For each case_dir in CASE_LIST_TO_RUN,
#     the features files are placed in {FEATURE_DIR_ROOT + WORKING_SVMDATA_DIR}/{case_dir}.
#
from case_config import *

###WORKING_SVMDATA_DIR = SVMDATA_10minPrecAsLabel
###WORKING_SVMDATA_DIR = SVMDATA_10minPrecAsLabel_HourlyAggr
WORKING_SVMDATA_DIR = SVMDATA_10minPrecAsLabel_FuzzyLabel
#WORKING_SVMDATA_DIR = SVMDATA_10minPrecAsLabel_HourlyAggr_FuzzyLabel
#WORKING_SVMDATA_DIR = SVMDATA_10minPrecAsLabel_EqualSize_FuzzyLabel
#WORKING_SVMDATA_DIR = SVMDATA_10minPrecAsLabel_EqualSize_HourlyAggr_FuzzyLabel

CASE_LIST_TO_RUN = CASE_LIST_BASIC


