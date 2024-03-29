import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
import numpy as np
from torchvision import datasets, transforms
from torchvision import models

from torch.utils.data.sampler import SubsetRandomSampler
# from datasets.cifar_dataloader import CIFARSel
from cifar_dataloader import CIFARSel
batch_size = 200
lr = 1e-3
seed = 1
log_schedule = 10
cuda = True

torch.manual_seed(seed)
if cuda:
    print('Using cuda')
    torch.cuda.manual_seed(seed)
    #torch.cuda.set_device(1)

kwargs = {'num_workers': 1, 'pin_memory': True} if cuda else {}
transform = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    #transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

trainset = datasets.CIFAR10(root='./', train=True,download=True, transform=transforms.Compose([
                       transforms.RandomCrop(32, padding=4),
                       transforms.RandomHorizontalFlip(),
                       transforms.ToTensor(),
                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]))

devset = datasets.CIFAR10(root='./', train=False,download=True, transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                       ]))

trainset_size = len(trainset)
indices = list(range(trainset_size))
split = int(np.floor(0.5 * trainset_size))
np.random.seed(230)
np.random.shuffle(indices)

train_sampler = SubsetRandomSampler(indices[:split])

train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,sampler=train_sampler)

test_loader = torch.utils.data.DataLoader(devset, batch_size=batch_size,shuffle=False)


# train_loader = torch.utils.data.DataLoader(
#     datasets.CIFAR10('./', train=True, download=True,
#                    transform=transforms.Compose([
#                        transforms.RandomCrop(32, padding=4),
#                        transforms.RandomHorizontalFlip(),
#                        transforms.ToTensor(),
#                        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
#                        #transforms.Normalize((0.491399689874, 0.482158419622, 0.446530924224), (0.247032237587, 0.243485133253, 0.261587846975))
#                    ])),
#     batch_size=batch_size, shuffle=True, **kwargs)
# test_loader = torch.utils.data.DataLoader(
#     datasets.CIFAR10('./', train=False, transform=transforms.Compose([
#                        transforms.ToTensor(),
#                        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
#                        #transforms.Normalize((0.491399689874, 0.482158419622, 0.446530924224), (0.247032237587, 0.243485133253, 0.261587846975))
#                    ])),
#     batch_size=batch_size, shuffle=False, **kwargs)

'''
train_loader = torch.utils.data.DataLoader(datasets.ImageFolder(root='./cifar10/train_car/',
                                           transform=transforms.Compose([
                                                transforms.RandomCrop(32, padding=4),
                                                transforms.RandomHorizontalFlip(),
                                                transforms.ToTensor(),
                                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])),batch_size=batch_size,shuffle=True)

test_loader = torch.utils.data.DataLoader(datasets.ImageFolder(root='./cifar10/train_car/',transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                       #transforms.Normalize((0.491399689874, 0.482158419622, 0.446530924224), (0.247032237587, 0.243485133253, 0.261587846975))
                   ])),batch_size=batch_size,shuffle=False)
'''
'''
name_class = {'airplane':0,
                    'automobile':1,
                    'bird':2,
                    'cat':3,
                    'deer':4,
                    'dog':5,
                    'frog':6,
                    'horse':7,
                    'ship':8,
                    'truck':9}

names =['automobile','cat']
names=list(name_class.keys())
# names=['bird','cat','deer','dog','frog','horse']
names=['airplane','automobile','ship','truck']
print(names)
# cifar selected load 
train_sampler = SubsetRandomSampler(indices[:split])
train_loader = torch.utils.data.DataLoader(CIFARSel(root='./',names=names,name_class=name_class,train =True,transform=transforms.Compose([
                                                transforms.RandomCrop(32, padding=4),
                                                transforms.RandomHorizontalFlip(),
                                                transforms.ToTensor(),
                                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])),batch_size=batch_size,shuffle=True)

test_loader =torch.utils.data.DataLoader(CIFARSel(root='./',names=names,name_class=name_class,train=False,transform=transforms.Compose([
                                                transforms.ToTensor(),
                                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])),batch_size=batch_size,shuffle=True)

print(len(train_loader.dataset))
print(len(test_loader.dataset))
'''
# using the 55 epoch learning rule here
def paramsforepoch(epoch):
    p = dict()
    regimes = [[1, 18, 5e-3, 5e-4],
               [19, 29, 1e-3, 5e-4],
               [30, 43, 5e-4, 5e-4],
               [44, 52, 1e-4, 0],
               [53, 1e8, 1e-5, 0]]
    # regimes = [[1, 18, 1e-4, 5e-4],
    #            [19, 29, 5e-5, 5e-4],
    #            [30, 43, 1e-5, 5e-4],
    #            [44, 52, 5e-6, 0],
    #            [53, 1e8, 1e-6, 0]]
    for i, row in enumerate(regimes):
        if epoch >= row[0] and epoch <= row[1]:
            p['learning_rate'] = row[2]
            p['weight_decay'] = row[3]
    return p

avg_loss = list()
best_accuracy = 0.0

def adjustlrwd(params):
    for param_group in optimizer.state_dict()['param_groups']:
        param_group['lr'] = params['learning_rate']
        param_group['weight_decay'] = params['weight_decay']

# train the network
optimizer = None
def train(epoch):
    global optimizer
    if epoch == 1:
        optimizer = optim.Adam(net.parameters(), lr=lr, weight_decay=1e-4)

    global avg_loss
    correct = 0
    net.train()
    for b_idx, (data, targets) in enumerate(train_loader):

        if cuda:
            data, targets = data.cuda(), targets.cuda()
        # convert the data and targets into Variable and cuda form
        data, targets = Variable(data), Variable(targets)

        # train the network
        optimizer.zero_grad()
        scores = net.forward(data)
        loss = F.nll_loss(scores, targets)

        # compute the accuracy
        pred = scores.data.max(1)[1] # get the index of the max log-probability
        correct += pred.eq(targets.data).cpu().sum()

        avg_loss.append(loss.data[0])
        loss.backward()
        optimizer.step()

        if b_idx % log_schedule == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, (b_idx+1) * len(data), len(train_loader.dataset),
                100. * (b_idx+1)*len(data) / len(train_loader.dataset), loss.data[0]))

    # now that the epoch is completed plot the accuracy
    train_accuracy = correct / float(len(train_loader.dataset))
    print("training accuracy ({:.2f}%)".format(100*train_accuracy))
    return (train_accuracy*100.0)


def test():
    net.eval()
    global best_accuracy
    correct = 0
    for idx, (data, target) in enumerate(test_loader):
        if cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data, volatile=True), Variable(target)

        # do the forward pass
        score = net.forward(data)
        pred = score.data.max(1)[1] # got the indices of the maximum, match them
        correct += pred.eq(target.data).cpu().sum()

    print("predicted {} out of {}".format(correct, len(test_loader.dataset)))
    val_accuracy = correct / float(len(test_loader.dataset)) * 100.0
    print("accuracy = {:.2f}".format(val_accuracy))

    # now save the model if it has better accuracy than the best model seen so forward
    return val_accuracy/100.0

