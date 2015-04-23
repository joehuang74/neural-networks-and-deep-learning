
FEATURE_DIR_ROOT = "D:\\";

# Feature file directories
SVMDATA_10minPrecAsLabel = "svmdata.10minPrecipAsLabel";
SVMDATA_10minPrecAsLabel_HourlyAggr = "svmdata.10minPrecipAsLabel.HourlyAggr";
SVMDATA_10minPrecAsLabel_FuzzyLabel = "svmdata.10minPrecipAsLabel.FuzzyLabel";
SVMDATA_10minPrecAsLabel_HourlyAggr_FuzzyLabel = "svmdata.10minPrecipAsLabel.HourlyAggr.FuzzyLabel";

SVMDATA_10minPrecAsLabel_TRAINSET = "svmdata.10minPrecipAsLabel.trainset";
SVMDATA_10minPrecAsLabel_TESTSET = "svmdata.10minPrecipAsLabel.testset";
SVMDATA_10minPrecAsLabel_HourlyAggr_TRAINSET = "svmdata.10minPrecipAsLabel.HourlyAggr.trainset";
SVMDATA_10minPrecAsLabel_HourlyAggr_TESTSET = "svmdata.10minPrecipAsLabel.HourlyAggr.testset";
SVMDATA_10minPrecAsLabel_FuzzyLabel_TRAINSET = "svmdata.10minPrecipAsLabel.FuzzyLabel.trainset";
SVMDATA_10minPrecAsLabel_FuzzyLabel_TESTSET = "svmdata.10minPrecipAsLabel.FuzzyLabel.testset";
SVMDATA_10minPrecAsLabel_HourlyAggr_FuzzyLabel_TRAINSET = "svmdata.10minPrecipAsLabel.HourlyAggr.FuzzyLabel.trainset";
SVMDATA_10minPrecAsLabel_HourlyAggr_FuzzyLabel_TESTSET = "svmdata.10minPrecipAsLabel.HourlyAggr.FuzzyLabel.testset";

# Feature file sub-directories for various cases
# CASE1_SINGLE+".withObsTime" is where the raw files are placed and should not be removed,
# all the other directories can be derived by using the featureiomanager project.
CASE1_SINGLE = "svm_case1_merged_all_single";
CASE2_1_STAT = "svm_case2.1_merged_all_stat";
CASE2_2_1_JOINED_MID_MEAN = "svm_case2.2.1_merged_all_joined_mid_mean";
CASE2_2_2_JOINED_MID_MEAN_ELEV = "svm_case2.2.2_merged_all_joined_mid_mean_elev";
CASE2_2_3_JOINED_MID_MEAN_PROD = "svm_case2.2.3_merged_all_joined_mid_mean_prod";
CASE2_3_1_JOINED_MID_MEAN_MAX5 = "svm_case2.3.1_merged_all_joined_mid_mean_max5";
CASE2_3_2_JOINED_MID_MEAN_MAX5_ELEV = "svm_case2.3.2_merged_all_joined_mid_mean_max5_elev";
CASE2_3_3_JOINED_MID_MEAN_MAX5_PROD = "svm_case2.3.3_merged_all_joined_mid_mean_max5_prod";
CASE2_4_1_JOINED_MID_MEAN_MIN5 = "svm_case2.4.1_merged_all_joined_mid_mean_min5";
CASE2_4_2_JOINED_MID_MEAN_MIN5_ELEV = "svm_case2.4.2_merged_all_joined_mid_mean_min5_elev";
CASE2_4_3_JOINED_MID_MEAN_MIN5_PROD = "svm_case2.4.3_merged_all_joined_mid_mean_min5_prod";
CASE2_5_1_JOINED_MID_MEAN_MAX50 = "svm_case2.5.1_merged_all_joined_mid_mean_max50";
CASE2_5_2_JOINED_MID_MEAN_MAX50_ELEV = "svm_case2.5.2_merged_all_joined_mid_mean_max50_elev";
CASE2_5_3_JOINED_MID_MEAN_MAX50_PROD = "svm_case2.5.3_merged_all_joined_mid_mean_max50_prod";
CASE2_6_1_JOINED_MID_MEAN_MIN50 = "svm_case2.6.1_merged_all_joined_mid_mean_min50";
CASE2_6_2_JOINED_MID_MEAN_MIN50_ELEV = "svm_case2.6.2_merged_all_joined_mid_mean_min50_elev";
CASE2_6_3_JOINED_MID_MEAN_MIN50_PROD = "svm_case2.6.3_merged_all_joined_mid_mean_min50_prod";
CASE2_7_1_JOINED_MID_MEAN_MAX50_MIN50 = "svm_case2.7.1_merged_all_joined_mid_mean_max50_min50";
CASE2_7_2_JOINED_MID_MEAN_MAX50_MIN50_ELEV = "svm_case2.7.2_merged_all_joined_mid_mean_max50_min50_elev";
CASE2_7_3_JOINED_MID_MEAN_MAX50_MIN50_PROD = "svm_case2.7.3_merged_all_joined_mid_mean_max50_min50_prod";
CASE3_1_JOINED_ELEV = "svm_case3.1_merged_all_joined_elev";
CASE3_2_JOINED_PROD = "svm_case3.2_merged_all_joined_prod";


# List of all cases
CASE_LIST_ALL = []
CASE_LIST_ALL.append(CASE1_SINGLE)
CASE_LIST_ALL.append(CASE2_1_STAT)
CASE_LIST_ALL.append(CASE2_2_1_JOINED_MID_MEAN)
CASE_LIST_ALL.append(CASE2_2_2_JOINED_MID_MEAN_ELEV)
CASE_LIST_ALL.append(CASE2_2_3_JOINED_MID_MEAN_PROD)
CASE_LIST_ALL.append(CASE2_3_1_JOINED_MID_MEAN_MAX5)
CASE_LIST_ALL.append(CASE2_3_2_JOINED_MID_MEAN_MAX5_ELEV)
CASE_LIST_ALL.append(CASE2_3_3_JOINED_MID_MEAN_MAX5_PROD)
CASE_LIST_ALL.append(CASE2_4_1_JOINED_MID_MEAN_MIN5)
CASE_LIST_ALL.append(CASE2_4_2_JOINED_MID_MEAN_MIN5_ELEV)
CASE_LIST_ALL.append(CASE2_4_3_JOINED_MID_MEAN_MIN5_PROD)
CASE_LIST_ALL.append(CASE2_5_1_JOINED_MID_MEAN_MAX50)
CASE_LIST_ALL.append(CASE2_5_2_JOINED_MID_MEAN_MAX50_ELEV)
CASE_LIST_ALL.append(CASE2_5_3_JOINED_MID_MEAN_MAX50_PROD)
CASE_LIST_ALL.append(CASE2_6_1_JOINED_MID_MEAN_MIN50)
CASE_LIST_ALL.append(CASE2_6_2_JOINED_MID_MEAN_MIN50_ELEV)
CASE_LIST_ALL.append(CASE2_6_3_JOINED_MID_MEAN_MIN50_PROD)
CASE_LIST_ALL.append(CASE2_7_1_JOINED_MID_MEAN_MAX50_MIN50)
CASE_LIST_ALL.append(CASE2_7_2_JOINED_MID_MEAN_MAX50_MIN50_ELEV)
CASE_LIST_ALL.append(CASE2_7_3_JOINED_MID_MEAN_MAX50_MIN50_PROD)
CASE_LIST_ALL.append(CASE3_1_JOINED_ELEV)
CASE_LIST_ALL.append(CASE3_2_JOINED_PROD)

# List of cases in experiment 1
CASE_LIST_EXP1 = []
CASE_LIST_EXP1.append(CASE1_SINGLE)
#CASE_LIST_EXP1.append(CASE2_1_STAT)
#CASE_LIST_EXP1.append(CASE2_2_1_JOINED_MID_MEAN)
#CASE_LIST_EXP1.append(CASE2_2_2_JOINED_MID_MEAN_ELEV)
###CASE_LIST_EXP1.append(CASE2_2_3_JOINED_MID_MEAN_PROD)
CASE_LIST_EXP1.append(CASE2_3_1_JOINED_MID_MEAN_MAX5)
CASE_LIST_EXP1.append(CASE2_3_2_JOINED_MID_MEAN_MAX5_ELEV)
###CASE_LIST_EXP1.append(CASE2_3_3_JOINED_MID_MEAN_MAX5_PROD)
#CASE_LIST_EXP1.append(CASE2_4_1_JOINED_MID_MEAN_MIN5)
#CASE_LIST_EXP1.append(CASE2_4_2_JOINED_MID_MEAN_MIN5_ELEV)
###CASE_LIST_EXP1.append(CASE2_4_3_JOINED_MID_MEAN_MIN5_PROD)
CASE_LIST_EXP1.append(CASE3_1_JOINED_ELEV)
CASE_LIST_EXP1.append(CASE3_2_JOINED_PROD)


# List of cases in experiment 2
CASE_LIST_EXP2 = []
#CASE_LIST_EXP2.append(CASE1_SINGLE)
CASE_LIST_EXP2.append(CASE2_1_STAT)
CASE_LIST_EXP2.append(CASE2_2_1_JOINED_MID_MEAN)
CASE_LIST_EXP2.append(CASE2_2_2_JOINED_MID_MEAN_ELEV)
###CASE_LIST_EXP2.append(CASE2_2_3_JOINED_MID_MEAN_PROD)
#CASE_LIST_EXP2.append(CASE2_3_1_JOINED_MID_MEAN_MAX5)
#CASE_LIST_EXP2.append(CASE2_3_2_JOINED_MID_MEAN_MAX5_ELEV)
###CASE_LIST_EXP2.append(CASE2_3_3_JOINED_MID_MEAN_MAX5_PROD)
CASE_LIST_EXP2.append(CASE2_4_1_JOINED_MID_MEAN_MIN5)
CASE_LIST_EXP2.append(CASE2_4_2_JOINED_MID_MEAN_MIN5_ELEV)
###CASE_LIST_EXP2.append(CASE2_4_3_JOINED_MID_MEAN_MIN5_PROD)
#CASE_LIST_EXP2.append(CASE3_1_JOINED_ELEV)
#CASE_LIST_EXP2.append(CASE3_2_JOINED_PROD)


# List of cases in experiment 3
CASE_LIST_EXP3 = []
CASE_LIST_EXP3.append(CASE1_SINGLE)
CASE_LIST_EXP3.append(CASE2_5_1_JOINED_MID_MEAN_MAX50)
CASE_LIST_EXP3.append(CASE2_5_2_JOINED_MID_MEAN_MAX50_ELEV)
#CASE_LIST_EXP3.append(CASE2_5_3_JOINED_MID_MEAN_MAX50_PROD)
CASE_LIST_EXP3.append(CASE2_6_1_JOINED_MID_MEAN_MIN50)
CASE_LIST_EXP3.append(CASE2_6_2_JOINED_MID_MEAN_MIN50_ELEV)
#CASE_LIST_EXP3.append(CASE2_6_3_JOINED_MID_MEAN_MIN50_PROD)
CASE_LIST_EXP3.append(CASE2_7_1_JOINED_MID_MEAN_MAX50_MIN50)
CASE_LIST_EXP3.append(CASE2_7_2_JOINED_MID_MEAN_MAX50_MIN50_ELEV)
#CASE_LIST_EXP3.append(CASE2_7_3_JOINED_MID_MEAN_MAX50_MIN50_PROD)
CASE_LIST_EXP3.append(CASE3_1_JOINED_ELEV)
CASE_LIST_EXP3.append(CASE3_2_JOINED_PROD)


#  All the file names should start with this prefix string
#FEATURE_FILE_PREFIX = "svm_traindata.txt.1a";

