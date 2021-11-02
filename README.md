## How to run
1. Clone this repository using
```
https://github.com/RamitPahwa/DDC_modelcompression.git 
```

## Methods Under Study 
1. Prunning :We compare our method to the popular ranking based pruning method .
We remove 512 lters on each iteration of pruning heuristically followed by
10 epochs of ne-tuning to recover the network.
2. KD: Knowledge Distillation : Another popular approach for model compression is Knowledge Distil-
lation. It requires a specic student architecture to train. We use a 7 layer
deep CNN architecture inspired by the VGG architecture for the student
architecture.
3. Network to Network COmpresiion: This method systematically nds a compressed optimal architecture by
searching within the teacher's architecture. The number of reinforcement
learning iterations have been xed at 100. In each iteration, 5 new student
architectures are being trained using Knowledge distillation.
4. Auto-Keras is a popular tool for architecture search which uses
Bayesian optimization and searches a model from scratch given a dataset.
5. Data Driven Compression [DDC] This is our proposed method.
