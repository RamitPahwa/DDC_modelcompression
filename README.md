## How to run
1. Clone this repository using
```
https://github.com/RamitPahwa/DDC_modelcompression.git 
```
## Directory Structure 
```
DDC_modelcompression/
├── DDC
│   ├── LICENSE
│   ├── Layer.py
│   ├── Model.py
│   ├── README.md
│   ├── architecture.py
│   ├── config.py
│   ├── controllers
│   │   ├── ActorCriticLSTM.py
│   │   ├── Autoregressive.py
│   │   ├── AutoregressiveLayer.py
│   │   ├── AutoregressiveParam.py
│   │   ├── EncoderDecoder.py
│   │   ├── LSTM.py
│   │   └── __init__.py
│   ├── datasets
│   │   ├── __init__.py
│   │   ├── cifar10.py
│   │   ├── cifar100.py
│   │   ├── cifar10_old.py
│   │   ├── cifar10_original.py
│   │   ├── cifar_dataloader.py
│   │   └── mnist.py
│   ├── draw_graph.py
│   ├── experiments
│   │   ├── ar_run_layer_clean.py
│   │   ├── ar_run_param_clean.py
│   │   ├── bd_run_layer_clean.py
│   │   ├── ed_run_layer_general.py
│   │   ├── resnet_actor_critic_layer.py
│   │   ├── resnet_ar_run_layer_clean.py
│   │   ├── resnet_ar_run_param_clean.py
│   │   └── resnet_db_run_layer_clean.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── cifar_new.py
│   │   ├── densenet.py
│   │   ├── googlenet.py
│   │   ├── lenet.py
│   │   ├── mnistnet.py
│   │   ├── mnistnetv2.py
│   │   ├── resnet.py
│   │   ├── ssd.py
│   │   └── vgg.py
│   ├── plot
│   │   ├── acc_time_trans.png
│   │   ├── animals_new_loss_acc.png
│   │   ├── animals_new_loss_comp.png
│   │   ├── animals_new_loss_rew_acc.png
│   │   ├── animals_new_loss_rew_ratio.png
│   │   ├── animals_new_loss_rew_time.png
│   │   ├── animals_new_loss_reward.png
│   │   ├── animals_new_lowtemp_acc.png
│   │   ├── animals_new_lowtemp_comp.png
│   │   ├── animals_new_lowtemp_rew_acc.png
│   │   ├── animals_new_lowtemp_rew_ratio.png
│   │   ├── animals_new_lowtemp_rew_time.png
│   │   ├── animals_new_lowtemp_reward.png
│   │   ├── animals_new_lowtemp_shitreward.png
│   │   ├── animals_orig_loss.png
│   │   ├── animals_orig_lossacc.png
│   │   ├── animals_orig_losscomp.png
│   │   ├── file_vehicles_new.csv
│   │   ├── models_all_resnet_cifar100_acc.png
│   │   ├── models_all_resnet_cifar100_comp.png
│   │   ├── models_all_resnet_cifar100_rew_acc.png
│   │   ├── models_all_resnet_cifar100_rew_ratio.png
│   │   ├── models_all_resnet_cifar100_rew_time.png
│   │   ├── models_all_resnet_cifar100_reward.png
│   │   ├── models_all_resnet_orig_acc.png
│   │   ├── models_all_resnet_orig_comp.png
│   │   ├── models_all_resnet_orig_rew_acc.png
│   │   ├── models_all_resnet_orig_rew_ratio.png
│   │   ├── models_all_resnet_orig_rew_time.png
│   │   ├── models_all_resnet_orig_reward.png
│   │   ├── models_animals_3_classes_resnet_cifar10
│   │   │   ├── models_animals_3_classes_resnet_cifar10_acc.png
│   │   │   ├── models_animals_3_classes_resnet_cifar10_comp.png
│   │   │   ├── models_animals_3_classes_resnet_cifar10_rew_acc.png
│   │   │   ├── models_animals_3_classes_resnet_cifar10_rew_ratio.png
│   │   │   ├── models_animals_3_classes_resnet_cifar10_rew_time.png
│   │   │   ├── models_animals_3_classes_resnet_cifar10_reward.png
│   │   │   └── results_normal.txt.out
│   │   ├── models_animals_resnet_new_reward_acc.png
│   │   ├── models_animals_resnet_new_reward_comp.png
│   │   ├── models_animals_resnet_new_reward_rew_acc.png
│   │   ├── models_animals_resnet_new_reward_rew_ratio.png
│   │   ├── models_animals_resnet_new_reward_rew_time.png
│   │   ├── models_animals_resnet_new_reward_reward.png
│   │   ├── models_fruits_resnet_PT_acc.png
│   │   ├── models_fruits_resnet_PT_comp.png
│   │   ├── models_fruits_resnet_PT_rew_acc.png
│   │   ├── models_fruits_resnet_PT_rew_ratio.png
│   │   ├── models_fruits_resnet_PT_rew_time.png
│   │   ├── models_fruits_resnet_PT_reward.png
│   │   ├── models_fruits_resnet_acc.png
│   │   ├── models_fruits_resnet_comp.png
│   │   ├── models_fruits_resnet_rew_acc.png
│   │   ├── models_fruits_resnet_rew_ratio.png
│   │   ├── models_fruits_resnet_rew_time.png
│   │   ├── models_fruits_resnet_reward.png
│   │   ├── models_insects_resnet_PT_cifar100_acc.png
│   │   ├── models_insects_resnet_PT_cifar100_comp.png
│   │   ├── models_insects_resnet_PT_cifar100_rew_acc.png
│   │   ├── models_insects_resnet_PT_cifar100_rew_ratio.png
│   │   ├── models_insects_resnet_PT_cifar100_rew_time.png
│   │   ├── models_insects_resnet_PT_cifar100_reward.png
│   │   ├── models_insects_resnet_PT_fruits_cifar100_acc.png
│   │   ├── models_insects_resnet_PT_fruits_cifar100_comp.png
│   │   ├── models_insects_resnet_PT_fruits_cifar100_rew_acc.png
│   │   ├── models_insects_resnet_PT_fruits_cifar100_rew_ratio.png
│   │   ├── models_insects_resnet_PT_fruits_cifar100_rew_time.png
│   │   ├── models_insects_resnet_PT_fruits_cifar100_reward.png
│   │   ├── models_insects_resnet_new_reward_acc.png
│   │   ├── models_insects_resnet_new_reward_cifar100_acc.png
│   │   ├── models_insects_resnet_new_reward_cifar100_comp.png
│   │   ├── models_insects_resnet_new_reward_cifar100_rew_acc.png
│   │   ├── models_insects_resnet_new_reward_cifar100_rew_ratio.png
│   │   ├── models_insects_resnet_new_reward_cifar100_rew_time.png
│   │   ├── models_insects_resnet_new_reward_cifar100_reward.png
│   │   ├── models_insects_resnet_new_reward_comp.png
│   │   ├── models_insects_resnet_new_reward_rew_acc.png
│   │   ├── models_insects_resnet_new_reward_rew_ratio.png
│   │   ├── models_insects_resnet_new_reward_rew_time.png
│   │   ├── models_insects_resnet_new_reward_reward.png
│   │   ├── models_mamamals_resnet_acc.png
│   │   ├── models_mamamals_resnet_cifar100_acc.png
│   │   ├── models_mamamals_resnet_cifar100_comp.png
│   │   ├── models_mamamals_resnet_cifar100_rew_acc.png
│   │   ├── models_mamamals_resnet_cifar100_rew_ratio.png
│   │   ├── models_mamamals_resnet_cifar100_rew_time.png
│   │   ├── models_mamamals_resnet_cifar100_reward.png
│   │   ├── models_mamamals_resnet_comp.png
│   │   ├── models_mamamals_resnet_rew_acc.png
│   │   ├── models_mamamals_resnet_rew_ratio.png
│   │   ├── models_mamamals_resnet_rew_time.png
│   │   ├── models_mamamals_resnet_reward.png
│   │   ├── models_people_resnet_cifar100_acc.png
│   │   ├── models_people_resnet_cifar100_comp.png
│   │   ├── models_people_resnet_cifar100_rew_acc.png
│   │   ├── models_people_resnet_cifar100_rew_ratio.png
│   │   ├── models_people_resnet_cifar100_rew_time.png
│   │   ├── models_people_resnet_cifar100_reward.png
│   │   ├── models_reptiles_resnet_acc_tanh_cifar100_acc.png
│   │   ├── models_reptiles_resnet_acc_tanh_cifar100_comp.png
│   │   ├── models_reptiles_resnet_acc_tanh_cifar100_rew_acc.png
│   │   ├── models_reptiles_resnet_acc_tanh_cifar100_rew_ratio.png
│   │   ├── models_reptiles_resnet_acc_tanh_cifar100_rew_time.png
│   │   ├── models_reptiles_resnet_acc_tanh_cifar100_reward.png
│   │   ├── models_reptiles_resnet_acc_tanh_tranfer_vehicles_cifar100_acc.png
│   │   ├── models_reptiles_resnet_acc_tanh_tranfer_vehicles_cifar100_comp.png
│   │   ├── models_reptiles_resnet_acc_tanh_tranfer_vehicles_cifar100_rew_acc.png
│   │   ├── models_reptiles_resnet_acc_tanh_tranfer_vehicles_cifar100_rew_ratio.png
│   │   ├── models_reptiles_resnet_acc_tanh_tranfer_vehicles_cifar100_rew_time.png
│   │   ├── models_reptiles_resnet_acc_tanh_tranfer_vehicles_cifar100_reward.png
│   │   ├── models_reptiles_resnet_cifar100_acc.png
│   │   ├── models_reptiles_resnet_cifar100_comp.png
│   │   ├── models_reptiles_resnet_cifar100_rew_acc.png
│   │   ├── models_reptiles_resnet_cifar100_rew_ratio.png
│   │   ├── models_reptiles_resnet_cifar100_rew_time.png
│   │   ├── models_reptiles_resnet_cifar100_reward.png
│   │   ├── models_reptiles_resnet_inverse_time_cifar100_acc.png
│   │   ├── models_reptiles_resnet_inverse_time_cifar100_comp.png
│   │   ├── models_reptiles_resnet_inverse_time_cifar100_rew_acc.png
│   │   ├── models_reptiles_resnet_inverse_time_cifar100_rew_ratio.png
│   │   ├── models_reptiles_resnet_inverse_time_cifar100_rew_time.png
│   │   ├── models_reptiles_resnet_inverse_time_cifar100_reward.png
│   │   ├── models_resnet_animals_PT_newloss_cifar10_acc.png
│   │   ├── models_resnet_animals_PT_newloss_cifar10_comp.png
│   │   ├── models_resnet_animals_PT_newloss_cifar10_rew_acc.png
│   │   ├── models_resnet_animals_PT_newloss_cifar10_rew_ratio.png
│   │   ├── models_resnet_animals_PT_newloss_cifar10_rew_time.png
│   │   ├── models_resnet_animals_PT_newloss_cifar10_reward.png
│   │   ├── models_resnet_animals_transfered_acc.png
│   │   ├── models_resnet_animals_transfered_comp.png
│   │   ├── models_resnet_animals_transfered_rew_acc.png
│   │   ├── models_resnet_animals_transfered_rew_ratio.png
│   │   ├── models_resnet_animals_transfered_rew_time.png
│   │   ├── models_resnet_animals_transfered_reward.png
│   │   ├── models_resnet_vehicles_PT_newloss_cifar10_acc.png
│   │   ├── models_resnet_vehicles_PT_newloss_cifar10_comp.png
│   │   ├── models_resnet_vehicles_PT_newloss_cifar10_rew_acc.png
│   │   ├── models_resnet_vehicles_PT_newloss_cifar10_rew_ratio.png
│   │   ├── models_resnet_vehicles_PT_newloss_cifar10_rew_time.png
│   │   ├── models_resnet_vehicles_PT_newloss_cifar10_reward.png
│   │   ├── models_resnet_vehicles_transfered_acc.png
│   │   ├── models_resnet_vehicles_transfered_comp.png
│   │   ├── models_resnet_vehicles_transfered_rew_acc.png
│   │   ├── models_resnet_vehicles_transfered_rew_ratio.png
│   │   ├── models_resnet_vehicles_transfered_rew_time.png
│   │   ├── models_resnet_vehicles_transfered_reward.png
│   │   ├── models_vehicles_resnet_3_classes_cifar10
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_acc.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_comp.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_rew_acc.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_rew_ratio.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_rew_time.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_reward.png
│   │   │   └── results_normal.out
│   │   ├── models_vehicles_resnet_3_classes_cifar10_PT_cifar10
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_PT_cifar10_acc.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_PT_cifar10_comp.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_PT_cifar10_rew_acc.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_PT_cifar10_rew_ratio.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_PT_cifar10_rew_time.png
│   │   │   ├── models_vehicles_resnet_3_classes_cifar10_PT_cifar10_reward.png
│   │   │   └── results_PT.txt.out
│   │   ├── models_vehicles_resnet_acc_tanh_cifar100_acc.png
│   │   ├── models_vehicles_resnet_acc_tanh_cifar100_comp.png
│   │   ├── models_vehicles_resnet_acc_tanh_cifar100_rew_acc.png
│   │   ├── models_vehicles_resnet_acc_tanh_cifar100_rew_ratio.png
│   │   ├── models_vehicles_resnet_acc_tanh_cifar100_rew_time.png
│   │   ├── models_vehicles_resnet_acc_tanh_cifar100_reward.png
│   │   ├── models_vehicles_resnet_cifar100_acc.png
│   │   ├── models_vehicles_resnet_cifar100_comp.png
│   │   ├── models_vehicles_resnet_cifar100_rew_acc.png
│   │   ├── models_vehicles_resnet_cifar100_rew_ratio.png
│   │   ├── models_vehicles_resnet_cifar100_rew_time.png
│   │   ├── models_vehicles_resnet_cifar100_reward.png
│   │   ├── models_vehicles_resnet_inverse_time_cifar100_acc.png
│   │   ├── models_vehicles_resnet_inverse_time_cifar100_comp.png
│   │   ├── models_vehicles_resnet_inverse_time_cifar100_rew_acc.png
│   │   ├── models_vehicles_resnet_inverse_time_cifar100_rew_ratio.png
│   │   ├── models_vehicles_resnet_inverse_time_cifar100_rew_time.png
│   │   ├── models_vehicles_resnet_inverse_time_cifar100_reward.png
│   │   ├── models_vehicles_resnet_original_reward_cifar100_acc.png
│   │   ├── models_vehicles_resnet_original_reward_cifar100_comp.png
│   │   ├── models_vehicles_resnet_original_reward_cifar100_rew_acc.png
│   │   ├── models_vehicles_resnet_original_reward_cifar100_rew_ratio.png
│   │   ├── models_vehicles_resnet_original_reward_cifar100_rew_time.png
│   │   ├── models_vehicles_resnet_original_reward_cifar100_reward.png
│   │   ├── models_vehicles_resnet_original_reward_sqrt_cifar100_acc.png
│   │   ├── models_vehicles_resnet_original_reward_sqrt_cifar100_comp.png
│   │   ├── models_vehicles_resnet_original_reward_sqrt_cifar100_rew_acc.png
│   │   ├── models_vehicles_resnet_original_reward_sqrt_cifar100_rew_ratio.png
│   │   ├── models_vehicles_resnet_original_reward_sqrt_cifar100_rew_time.png
│   │   ├── models_vehicles_resnet_original_reward_sqrt_cifar100_reward.png
│   │   ├── models_vehicles_resnet_tranfer_fruits_cifar100_acc.png
│   │   ├── models_vehicles_resnet_tranfer_fruits_cifar100_comp.png
│   │   ├── models_vehicles_resnet_tranfer_fruits_cifar100_rew_acc.png
│   │   ├── models_vehicles_resnet_tranfer_fruits_cifar100_rew_ratio.png
│   │   ├── models_vehicles_resnet_tranfer_fruits_cifar100_rew_time.png
│   │   ├── models_vehicles_resnet_tranfer_fruits_cifar100_reward.png
│   │   ├── plot.png
│   │   ├── plot2.png
│   │   ├── preprocess.py
│   │   ├── presentation
│   │   │   ├── acc_fruit_normal_acc.png
│   │   │   ├── acc_fruit_normal_comp.png
│   │   │   ├── acc_fruit_normal_same.png
│   │   │   ├── acc_fruit_transfer_acc.png
│   │   │   ├── acc_fruit_transfer_comp.png
│   │   │   ├── acc_fruit_transfer_same.png
│   │   │   ├── animals_new_lowtemp_acc.png
│   │   │   ├── animals_new_lowtemp_comp.png
│   │   │   ├── animals_new_lowtemp_rew_acc.png
│   │   │   ├── animals_new_lowtemp_rew_ratio.png
│   │   │   ├── animals_new_lowtemp_rew_time.png
│   │   │   ├── animals_new_lowtemp_reward.png
│   │   │   ├── animals_new_lowtemp_shitreward.png
│   │   │   ├── g1_acc.png
│   │   │   ├── g2_acc.png
│   │   │   ├── models_fruits_resnet_PT_acc.png
│   │   │   ├── models_fruits_resnet_PT_comp.png
│   │   │   ├── models_fruits_resnet_PT_rew_acc.png
│   │   │   ├── models_fruits_resnet_PT_rew_ratio.png
│   │   │   ├── models_fruits_resnet_PT_rew_time.png
│   │   │   ├── models_fruits_resnet_PT_reward.png
│   │   │   ├── models_fruits_resnet_acc.png
│   │   │   ├── models_fruits_resnet_comp.png
│   │   │   ├── models_fruits_resnet_rew_acc.png
│   │   │   ├── models_fruits_resnet_rew_ratio.png
│   │   │   ├── models_fruits_resnet_rew_time.png
│   │   │   ├── models_fruits_resnet_reward.png
│   │   │   ├── models_resnet_animals_transfered_acc.png
│   │   │   ├── models_resnet_animals_transfered_comp.png
│   │   │   ├── models_resnet_animals_transfered_rew_acc.png
│   │   │   ├── models_resnet_animals_transfered_rew_ratio.png
│   │   │   ├── models_resnet_animals_transfered_rew_time.png
│   │   │   ├── models_resnet_animals_transfered_reward.png
│   │   │   ├── result_newloss_animals_orig.txt.out
│   │   │   ├── results_animals_transfer.out
│   │   │   ├── results_fruits_orig.out
│   │   │   └── results_fruits_transfer.out
│   │   ├── test.png
│   │   ├── transform_acc.png
│   │   ├── transform_at_c_no_time.png
│   │   ├── vehicles_new_loss_acc.png
│   │   ├── vehicles_new_loss_comp.png
│   │   ├── vehicles_orig_loss_acc.png
│   │   └── vehicles_orig_loss_comp.png
│   ├── rl.py
│   ├── run.py
│   ├── test_model.py
│   └── utils.py
├── DDC_paper
│   ├── Outline.txt
│   ├── bibs
│   │   ├── sample.bib
│   │   └── sub.bib
│   ├── images
│   │   └── png
│   │       ├── rewardplot.png
│   │       └── system.png
│   ├── llncs.cls
│   ├── main.tex
│   ├── named.bst
│   ├── sections
│   │   ├── abstract.tex
│   │   ├── acknowledgements.tex
│   │   ├── approach-updated.tex
│   │   ├── approach.tex
│   │   ├── conclusions.tex
│   │   ├── experiments-old.tex
│   │   ├── experiments-updated.tex
│   │   ├── experiments.tex
│   │   ├── intro-old.tex
│   │   ├── introduction.tex
│   │   └── related-work.tex
│   ├── splncs04.bst
│   ├── styles
│   │   ├── AuxCommandsICLR.sty
│   │   ├── AuxCommandsIJCAI.sty
│   │   ├── AuxCommandsLNCS.sty
│   │   ├── aistats2019.sty
│   │   ├── iclr2019_conference.sty
│   │   ├── ijcai19.sty
│   │   └── math_commands.tex
│   └── tables
│       ├── comparision.tex
│       ├── datasets.tex
│       ├── res18-c10.tex
│       ├── res18-c100.tex
│       ├── res18-c10_exp-2+3.tex
│       ├── resnet18_cifar100_fullonsub.tex
│       ├── resnet18_cifar100_pt.tex
│       ├── resnet18_cifar10_fullonsub.tex
│       ├── resnet18_cifar10_pt.tex
│       ├── vgg11-c10.tex
│       ├── vgg11-c10_exp-2+3.tex
│       ├── vgg11-prun.tex
│       ├── vgg11_cifar10_fulltosub.tex
│       └── vgg11_cifar10_pt.tex
├── N2N
│   ├── LICENSE
│   ├── Layer.py
│   ├── Model.py
│   ├── README.md
│   ├── architecture.py
│   ├── controllers
│   │   ├── ActorCriticLSTM.py
│   │   ├── Autoregressive.py
│   │   ├── AutoregressiveLayer.py
│   │   ├── AutoregressiveParam.py
│   │   ├── EncoderDecoder.py
│   │   ├── LSTM.py
│   │   └── __init__.py
│   ├── datasets
│   │   ├── __init__.py
│   │   ├── caltech256.py
│   │   ├── cifar10.py
│   │   ├── cifar100.py
│   │   ├── cifar10_old.py
│   │   ├── imagenet.py
│   │   ├── mnist.py
│   │   └── svhn.py
│   ├── experiments
│   │   ├── ar_run_layer_clean.py
│   │   ├── ar_run_param_clean.py
│   │   ├── bd_run_layer_clean.py
│   │   ├── ed_run_layer_general.py
│   │   ├── resnet_actor_critic_layer.py
│   │   ├── resnet_ar_run_layer_clean.py
│   │   ├── resnet_ar_run_param_clean.py
│   │   └── resnet_db_run_layer_clean.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── cifar_new.py
│   │   ├── densenet.py
│   │   ├── googlenet.py
│   │   ├── lenet.py
│   │   ├── mnistnet.py
│   │   ├── mnistnetv2.py
│   │   ├── resnet.py
│   │   ├── ssd.py
│   │   └── vgg.py
│   ├── rl.py
│   ├── run.py
│   ├── test_model.py
│   └── utils.py
├── README.md
├── autokeras
│   ├── README.md
│   ├── main.py
│   └── main_cifar100.py
├── docker
│   ├── Dockerfile_PyTorch0.2
│   ├── Dockerfile_PyTorch0.3
│   ├── Dockerfile_Pytorch0.2p
│   └── README.md
├── kd
│   ├── Layer.py
│   ├── Model.py
│   ├── Untitled.ipynb
│   ├── __pycache__
│   │   ├── Layer.cpython-36.pyc
│   │   ├── Model.cpython-36.pyc
│   │   └── utils.cpython-36.pyc
│   ├── cifar-10-python.tar.gz
│   ├── data_loader.py
│   ├── datasets
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── caltech256.cpython-36.pyc
│   │   │   ├── cifar10.cpython-36.pyc
│   │   │   ├── cifar100.cpython-36.pyc
│   │   │   └── cifar_dataloader.cpython-36.pyc
│   │   ├── caltech256.py
│   │   ├── cifar10.py
│   │   ├── cifar100.py
│   │   ├── cifar10_old.py
│   │   ├── cifar10_original.py
│   │   ├── cifar_dataloader.py
│   │   ├── dataset.py
│   │   ├── imagenet.py
│   │   ├── mnist.py
│   │   └── svhn.py
│   ├── kd-code.py
│   ├── kd.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── densenet.cpython-36.pyc
│   │   │   ├── googlenet.cpython-36.pyc
│   │   │   ├── lenet.cpython-36.pyc
│   │   │   ├── net.cpython-36.pyc
│   │   │   ├── net2.cpython-36.pyc
│   │   │   ├── resnet.cpython-36.pyc
│   │   │   └── vgg.cpython-36.pyc
│   │   ├── cifar_new.py
│   │   ├── densenet.py
│   │   ├── googlenet.py
│   │   ├── lenet.py
│   │   ├── mnistnet.py
│   │   ├── mnistnetv2.py
│   │   ├── net.py
│   │   ├── net2.py
│   │   ├── resnet.py
│   │   ├── ssd.py
│   │   └── vgg.py
│   ├── params.json
│   └── utils.py
├── pruning
│   ├── Model.py
│   ├── README.md
│   ├── __pycache__
│   │   ├── data_loader.cpython-36.pyc
│   │   ├── data_loader.cpython-37.pyc
│   │   ├── dataset.cpython-36.pyc
│   │   ├── dataset.cpython-37.pyc
│   │   ├── prune.cpython-36.pyc
│   │   └── prune.cpython-37.pyc
│   ├── ai-assignment.cpp
│   ├── ashok_vgg19.txt
│   ├── data
│   │   └── cifar-10-batches-py
│   │       ├── batches.meta
│   │       ├── data_batch_1
│   │       ├── data_batch_2
│   │       ├── data_batch_3
│   │       ├── data_batch_4
│   │       ├── data_batch_5
│   │       ├── readme.html
│   │       └── test_batch
│   ├── data_loader.py
│   ├── dataset.py
│   ├── finetune.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── cifar_new.py
│   │   ├── densenet.py
│   │   ├── densenet.pyc
│   │   ├── googlenet.py
│   │   ├── googlenet.pyc
│   │   ├── lenet.py
│   │   ├── lenet.pyc
│   │   ├── mnistnet.py
│   │   ├── mnistnetv2.py
│   │   ├── resnet.py
│   │   ├── resnet.pyc
│   │   ├── ssd.py
│   │   ├── vgg.py
│   │   └── vgg.pyc
│   ├── prune.py
│   └── test.py
└── resnet_pruning
    ├── README.md
    ├── ashok.txt
    ├── data_loader.py
    ├── dataset.py
    ├── finetune.py
    ├── model
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── cifar_new.py
    │   ├── densenet.py
    │   ├── densenet.pyc
    │   ├── googlenet.py
    │   ├── googlenet.pyc
    │   ├── lenet.py
    │   ├── lenet.pyc
    │   ├── mnistnet.py
    │   ├── mnistnetv2.py
    │   ├── resnet.py
    │   ├── resnet.pyc
    │   ├── ssd.py
    │   ├── vgg.py
    │   └── vgg.pyc
    ├── prune.py
    └── resnet.txt

37 directories, 486 files
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