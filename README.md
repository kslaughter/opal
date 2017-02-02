# OPAL

*OPAL* is design tool that uses artificial neural networks (ANN) to automate the design and optimization of other ANN: neural networks designing neural networks.  *OPAL* is available for download as a compiled library (developed in python3) for educational and research purposes.  Source code is available for educational and research purposes upon request at [opal@ece.mcgill.ca](mailto:opal@ece.mcgill.ca); for commercialization options, [contact us](mailto:opal@ece.mcgil.ca).

*OPAL* is a joint effort between the Reliable Silicon Systems Lab (RSSL) directed by Professor [Brett H. Meyer](http://rssl.ece.mcgill.ca) and the Integrated Systems for Information Processor (ISIP) Lab directed by Professor [Warren J. Gross](http://www.isip.ece.mcgill.ca).  If you use *OPAL* in your research, please cite
> Sean C. Smithson, Guang Yang, Warren J. Gross, and Brett H. Meyer, "Neural networks designing neural networks: Multi-objective hyper-parameter optimization," 2016 International Conference On Computer Aided Design (ICCAD’16), November 2016.

## Overview

The design of ANN hyper-parameters has long been considered unwieldy, unintuitive, and, as a consequence, ideal for automated hyper-parameter optimization techniques.  Most current approaches focus on optimizing accuracy, with little regard to the resulting computational resource requirements.  *OPAL* uses response surface modeling to learn the relationship between ANN hyper-parameters and network accuracy, and further employs a model of the cost of network implementation (e.g., in C or CUDA) to direct ANN design space exploration and expose the best accuracy-cost trade-offs possible.

## Usage



## Frequently Asked Questions

