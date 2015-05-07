# NOTE1: Modify result_log_dir, training_data_dir to switch between feature directories.
# NOTE2: Modify case_list to set the list of cases for doing the experiments.
# NOTE3: To save the standard output to a file(eg. test_network_radar.stdout.log),
#        Run -> Run Configurations... -> Common tab -> Standard input and output -> File; also check the "append" checkbox.
import light_format_feature_loader
import network
import glob
import os
import shutil
from case_config import *
from run_config_nn import *

rainfall_min_value = 0
rainfall_max_value = 100
n_rainfall_indexes = 100 # for use in vectorized form of rainfall label (number of neurons for output layer)
size_hidden_layer = 30 # Number of neurons for hidden layer

case_list = CASE_LIST_TO_RUN # Refer to run_config_nn.py case_config.py
result_log_dir = "../log/" + WORKING_SVMDATA_DIR

if not os.path.exists(result_log_dir):
    os.makedirs(result_log_dir)
else:
    shutil.rmtree(result_log_dir)
    os.makedirs(result_log_dir)

previous_case_dir = case_list[0]
result_log_file = result_log_dir + "/" + case_list[0] + ".log"
log_fp = open(result_log_file, 'a')
for case_dir in case_list:
    feature_data_dir = FEATURE_DIR_ROOT + WORKING_SVMDATA_DIR + "\\" + case_dir
    result_log_file = result_log_dir + "/" + case_dir + ".log"
    
    if previous_case_dir != case_dir:
        log_fp.close()
    if log_fp.closed:
        log_fp = open(result_log_file, 'a')

    filepath_list = glob.glob(feature_data_dir + "\svm_traindata.txt.1a.*")

    filename_list = []
    print "==== Training file list ===="
    for filepath in filepath_list:
        if os.path.basename(filepath).find("log") != -1:
            continue
        if os.path.basename(filepath).find(".model") != -1:
            continue
        if os.path.basename(filepath).find(".scaledData") != -1:
            continue
        filename_list.append(os.path.basename(filepath))

    # Manual setting of training files
    #filename_list = []
    #filename_list.append("svm_traindata.txt.1a.Z_0.5_0.5")
    #filename_list.append("svm_traindata.txt.1a.V_0.5_0.5")
    #filename_list.append("svm_traindata.txt.2b.9999.0_-9999.0")
    log_fp.write("===== Training file list =====\n")
    for filename in filename_list:
        print filename
        log_fp.write(filename + "\n")
    print ""

    """
    Hyper-parameters
    """
    epoches = 50
    mini_batch_size = 10
    training_rate = 2.0

    log_fp.write("feature_data_dir: {0}\n".format(feature_data_dir))
    log_fp.write("rainfall_min_value: {0}\n".format(rainfall_min_value))
    log_fp.write("rainfall_max_value: {0}\n".format(rainfall_max_value))
    log_fp.write("n_rainfall_indexes(Number of neurons for output-layer): {0}\n".format(n_rainfall_indexes))
    log_fp.write("size_hidden_layer(Number of neurons for hidden-layer): {0}\n".format(size_hidden_layer))
    log_fp.write("kernel type: Sigmoid\n")
    log_fp.write("epoches: {0}\n".format(epoches))
    log_fp.write("mini_batch_size: {0}\n".format(mini_batch_size))
    log_fp.write("training_rate: {0}\n\n".format(training_rate))

    """
    Train and evaluate the network for the given list of training files
    """
    for filename in filename_list:
        feature_file = feature_data_dir + "/" + filename
        training_data, validation_data, test_data, dimension = \
        light_format_feature_loader.load_data_wrapper(feature_file, rainfall_min_value, rainfall_max_value, n_rainfall_indexes)
   
        if training_data == None:
            print "[ERROR] Training data in {0} is None, skipped training task".format(feature_file)
            continue

        log_fp.write("===== {0} =====\n".format(filename));
        log_fp.write("dimension(Number of neurons for input layer) : {0}\n".format(dimension))
        log_fp.write("number of training examples: {0}  test examples: {1}\n".format(len(training_data), len(test_data)))

        """ 
        Build a three-layer neural network given the number of neurons for each layer
        Parameters:
        [number of neurons for input layer], [number of neurons for hidden layer], [number of neurons for output layer]
        """
        net = network.Network([dimension, size_hidden_layer, n_rainfall_indexes])

        """
        Perform stochastic gradient descent algorithm given necessary hyper-parameters
        Parameters:
        [training_data], [number of epoches], [mini-batch size], [training rate], [test_data]
        net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
        """
        print "===== Start training  for {0} =====".format(filename)
        net.SGD(training_data, epoches, mini_batch_size, training_rate, log_file_pointer=log_fp, test_data=test_data)
        correctly_classified = net.evaluate(test_data)
        print "Result after {0} epoches: {1} / {2}  ({3}%)\n".format(
                    epoches, correctly_classified, len(test_data), 100*correctly_classified/len(test_data))
        log_fp.write("Result after {0} epoches: {1} / {2}  ({3}%)\n".format(
                    epoches, correctly_classified, len(test_data), 100*correctly_classified/len(test_data)))
        log_fp.write("\n")

    log_fp.flush()
    previous_case_dir = case_dir

