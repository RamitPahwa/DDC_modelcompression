# DDC: Data-Driven Compression of Convolutional Neural Networks 
This is the code to run the model compression algorithm described in the paper.
It currently supports trained models in pytorch. If you would like to use it with a model in another deep learning framework, it would have to be converted to pytorch first.

## Dependencies
There are some dependencies for running this
1. [python](https://www.python.org/) >= 2.7
2. [pytorch](http://pytorch.org/) >= 0.2
3. [torchvision](http://pytorch.org/) >= 0.19

Layer removal and Layer shrinkage instructions are described below 
Additional detailed instructions can be found in the help menu in run.py
### Removal
Here is an example command to train the layer removal policy on the cifar10 dataset using the resnet-18 model
```
python run.py removal cifar10 teacher_models/resnet18_cifar10.net --cuda True 
```

### Shrinkage
NOTE: To run shrinkage, specify both teacher model and reduced model from stage1
```
python run.py shrinkage cifar10 teacher_models/resnet18_cifar10.net --model Stage1_cifar10/reduced_model1.net --cuda True 
```
### Pre-trained teacher models
The teacher models are to be specified to run.py to train.
### Pre-trained student models
The pre-trained student models are given to show the performance of the models described in the paper. They can be tested using test\_model.py
Test using 
```
python test_model.py student_models/resnet18_cifar10.net cifar10
```
### Pre-trained policies
The pre-trained polcies are specified to run the transfer learning experiments

