import numpy as np

name = 'GENERIC'


def load(train_input_file, train_output_file, test_input_file, test_output_file):
    global inputsize
    global inputdim
    global outputsize

    train_input = np.load(train_input_file)
    train_output = np.load(train_output_file)
    test_input = np.load(test_input_file)
    test_output = np.load(test_output_file)
    
    if(np.size(np.shape(train_input)) == 1):
        inputsize = 1
        inputdim = (1,)
    else:
        inputsize = np.prod(np.shape(train_input)[1:])
        inputdim = np.shape(train_input)[1:]

    if(np.size(np.shape(train_output)) == 1):
        outputsize = 1
    else:
        outputsize = np.prod(np.shape(train_output)[1:])

    return(train_input, train_output, test_input, test_output)
    
