# OPAL (Ordinary People Accelerating Learning)

*OPAL* makes deep learning easy.  *OPAL* is design tool that uses artificial neural networks (ANN) to automate the design and optimization of other ANNs: neural networks designing neural networks.  Conventional ANN design requires machine learning expertise, and time: with the right background and enough effort, custom solutions can be developed for a variety of learning problems.  However, not everyone has a computer science degree; if you don't, *OPAL* is for you.

<img align="right" alt="OPAL exposes trade-offs in ANN design spaces." src="http://rssl.ece.mcgill.ca/~bhm/images/opal-tradeoffs.png">

Traditional ANN design is focused on prediction accuracy.  Consider the example graph on the right, which plots design complexity (e.g., computational cost) versus prediction accuracy.  After a lengthy optimization process, the black diamond is found: the design with the least error.  However, computational cost is a concern in large ANN: e.g., every additional network layer adds delay, power consumption, and design cost.  Often, cheaper solutions are available that sacrifice little or no accuracy; unfortunately, it is difficult to find these by hand.

*OPAL* uses machine learning to find the best possible trade-offs for your machine learning problem, whether you're solving a new one, or simply trying to find a more efficient implementation, e.g., for a mobile platform.  Rather than target the most accurate implementation, OPAL searches for the best trade-offs (or Pareto points, the red diamonds), allowing ANN designers to select the implementation that strikes the most appropriate balance between different design constraints.  OPAL then generates the [theano](http://deeplearning.net/software/theano/) or [TensorFlow](https://www.tensorflow.org/) configuration file required to put your ANN into use.

*OPAL* is available for download as a compiled library (developed in python3) for educational and research purposes. Source code is available for educational and research purposes upon request at [opal@campus.mcgill.ca](mailto:opal@campus.mcgill.ca); for commercialization options, [contact us](mailto:opal@campus.mcgill.ca).

*OPAL* is a joint effort between the Reliable Silicon Systems Lab (RSSL) directed by Professor [Brett H. Meyer](http://rssl.ece.mcgill.ca) and the Integrated Systems for Information Processor (ISIP) Lab directed by Professor [Warren J. Gross](http://www.isip.ece.mcgill.ca). If you use *OPAL* in your research, please cite [our paper](https://arxiv.org/abs/1611.02120):
> Sean C. Smithson, Guang Yang, Warren J. Gross, and Brett H. Meyer, "Neural networks designing neural networks: Multi-objective hyper-parameter optimization," 2016 International Conference On Computer Aided Design (ICCAD’16), November 2016.


## Overview

The design of ANN hyper-parameters has long been considered unwieldy, unintuitive, and as a consequence, ideal for automated hyper-parameter optimization techniques. Most current approaches focus on optimizing accuracy, with little regard to the resulting computational resource requirements. *OPAL* uses response surface modelling to learn the relationship between ANN hyper-parameters and network accuracy, and further employs a model of the cost of network implementation (e.g., in C or CUDA) to direct ANN design space exploration and expose the best accuracy-cost trade-offs possible.


## Usage

The tool can be used by simply executing the *OPAL* terminal script followed by a configuration file as input (e.g. ./OPAL example.cfg). The outputs generated by the tool are in a human readable plain text format, containing the complete exploration results (input hyper-parameter and resulting cost/accuracy  pairs) as well as the Pareto-optimal results.


## Configuration Files

The general structure of the configuration files is split up into five distinct sections: [General], [DSE], [Cost], [Parameters], and [RSM]. The possible parameters and values for each section are outlined below.


### [General] Section:

The [General] section contains the configuration options pertinent to the input and output file locations, and type of design problem. The possible input to this section are:

Parameter | Description | Possible Values
--------- | ----------- | ---------------
verbose | Whether to print out details to standard output or not | *True* or *False*
experiment_name | Name that will be included in the results files generated | Any value that can be valid file name
results_dir | Location directory where the results are to be stored in (must exist) | Any value that is a valid directory name
dataset | Name of the dataset used | Can be *GENERIC* if working with a supplied dataset in formatted .npy files. Otherwise, standard image datasets which can be used are *MNIST*, *CIFAR-10*, or *SVHN* using their distributed files.
dataset_dir | If the dataset is not *GENERIC*, then this is the directory where the files are stored | Any value that is a valid directory name
train_input_filename | File name of the training set inputs, the arrays must be structured such that the size of the first dimension is the number of samples | Any value that is a valid file name
train_output_filename | Same as above, but the training outputs | Any value that is a valid file name
test_input_filename | Same as above, but the testing inputs | Any value that is a valid file name
test_output_filename | Same as above, but the testing outputs | Any value that is a valid file name
network_type | Type of neural network being designed | *MLP* or *CNN*


### [DSE] Section:

The [DSE] section contains the details of the design space exploration algorithm configuration, including how long to run for. The possible input to this section are:

Parameter | Description | Possible Values
--------- | ----------- | ---------------
max_samples | The maximum samples predicted from the design space; if the true Pareto-optimal front is found by the tool, without a value for *max_samples* the algorithm will run forever re-sampling the same solutions over and over. | Any numerical value, notations such as *1e6* will be converted to integers internally.
max_iterations | The maximum number of solutions that will be trained and tested, this is what determines the algorithm run time. | Any valid integer value.
initial_iterations | The number of solutions to be trained and tested before the RSM neural network is trained. | Any valid integer value.
storage_period | The number of solutions evaluated between periodically saving the results to disk. The saving process searches through all explored solutions to build the Pareto-optimal front; it is best to limit this when exploring very large design spaces. | Any valid integer value.
sigma | Parameter controlling how far from a solution the next point is sampled from. The next point in the chain will be sampled from a normal distribution centred around the previous point, where larger *sigma* values will result in narrower distributions. | Any valid floating point value; the default is assumed to be 3 if not defined.
alpha | The probability with which solutions that are predicted to be Pareto-dominated are accepted with; solutions which are predicted to be Pareto-optimal are therefore accepted with probability *1-alpha*.  | Any valid floating point value, notations such as *1e-4* will be evaluated internally.


### [Cost] Section:

The [Cost] section.

Parameter | Description | Possible Values
--------- | ----------- | ---------------
weight_cost | The weighted cost given to network weights. | Any valid floating point value.
mac_cost | The weighted cost given to the need for a multiply-accumulate operation. | Any valid floating point value.
max_cost | The maximum network cost that will be evaluated; useful when exploring very deep architectures. | Any valid floating point value, notations such as *1e5* will be evaluated internally.


### [Parameters] and [RSM] Sections:

Note that care should be taken when writing the [Parameters] and [RSM] sections of configuration files, as the parameter strings are executed by the Python interpreter. This ability was added for convenience when specifying parameters with many values to be explored; it is a given that the tool should not be run with root privileges.

<!--
The [Parameters] section.

Parameter | Description | Possible Values
--------- | ----------- | ---------------
 |  | 
 |  | 


### [RSM] Section:

The [RSM] section.

Parameter | Description | Possible Values
--------- | ----------- | ---------------
network_type |  | 
loss |  | 
epochs |  | 
learning_rate |  | 
learning_alg |  | 
fc_layers |  | 
fc_dropouts |  | 
fc_activation |  | 
conv_filters |  | 
conv_kernels |  | 
conv_strides |  | 
conv_pads |  | 
conv_pools |  | 
conv_dropouts |  | 
conv_activation |  | 
out_activation |  | 
-->


## Dependencies

Aside from a working Python installation (>= 3.5), the following libraries are required:
 - [numpy](http://www.numpy.org/)
 - [scipy](http://www.scipy.org/)
 - [matplotlib](http://matplotlib.org/)
 - [tensorflow](https://www.tensorflow.org/)
 - [keras](https://keras.io/)

The provided AMD64 builds have been tested on Ubuntu versions 14.04 and 16.04, with numpy 1.11.3, scipy 0.18.1, matplotlib 2.0.0, tensorflow 1.0.0, and keras 1.2.2. However, the release may still function with earlier versions.

<!-- ## Frequently Asked Questions -->
