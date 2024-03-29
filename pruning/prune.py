import torch
from torch.autograd import Variable
from torchvision import models
import cv2
import sys
import numpy as np
import time
import pdb
 
#  author :_commoner_

def replace_layers(model, i, indexes, layers):
	if i in indexes:
		return layers[indexes.index(i)]
	return model[i]

def prune_vgg16_conv_layer(model, layer_index, filter_index):
	# print(layer_index)
	_, conv = list(model.features._modules.items())[layer_index]
	bn_layer_index = layer_index + 1
	relu_layer_index =layer_index+2
	_, bn = list(model.features._modules.items())[bn_layer_index]
	_, relu = list(model.features._modules.items())[relu_layer_index]
	next_conv = None
	next_bn= None
	offset = 1
	boffset = 1
	while bn_layer_index + boffset <  len(list(model.features._modules.items())):
		res =  list(model.features._modules.items())[bn_layer_index+boffset]
		if isinstance(res[1], torch.nn.modules.BatchNorm2d):
			next_bname, next_bn = res
			break
		boffset = boffset + 1
	while layer_index + offset <  len(list(model.features._modules.items())):
		res =  list(model.features._modules.items())[layer_index+offset]
		if isinstance(res[1], torch.nn.modules.conv.Conv2d):
			next_name, next_conv = res
			break
		offset = offset + 1
	
	new_conv = \
		torch.nn.Conv2d(in_channels = conv.in_channels, \
			out_channels = conv.out_channels - 1,
			kernel_size = conv.kernel_size, \
			stride = conv.stride,
			padding = conv.padding,
			dilation = conv.dilation,
			groups = conv.groups,
			bias = True if conv.bias is not None else False)

	old_weights = conv.weight.data.cpu().numpy()
	new_weights = new_conv.weight.data.cpu().numpy()

	new_weights[: filter_index, :, :, :] = old_weights[: filter_index, :, :, :]
	new_weights[filter_index : , :, :, :] = old_weights[filter_index + 1 :, :, :, :]
	
	if torch.cuda.is_available():
		new_conv.weight.data = torch.from_numpy(new_weights).cuda()
	else:
		new_conv.weight.data = torch.from_numpy(new_weights)

	bias_numpy = conv.bias.data.cpu().numpy()

	bias = np.zeros(shape = (bias_numpy.shape[0] - 1), dtype = np.float32)
	bias[:filter_index] = bias_numpy[:filter_index]
	bias[filter_index : ] = bias_numpy[filter_index + 1 :]
	
	if torch.cuda.is_available():
		new_conv.bias.data = torch.from_numpy(bias).cuda()
	else:
		new_conv.bias.data = torch.from_numpy(bias)
	# batchnorm
	new_bn =torch.nn.BatchNorm2d(num_features = conv.out_channels - 1, eps=1e-05, momentum=0.1, affine=True)
	old_bweights = bn.weight.data.cpu().numpy()
	new_bweights = new_bn.weight.data.cpu().numpy()
	# print('obnw')
	# print(old_bweights.shape)
	# print('nbnw')
	# print(new_bweights.shape)
	for i in range(0,filter_index):
		if i < new_bweights.shape[0]:
			new_bweights[i] = old_bweights[i]
	# new_bweights[:filter_index] = old_bweights[:filter_index]
	# new_bweights[filter_index :new_bweights.shape[0]] = old_bweights[filter_index + 1 : old_bweights.shape[0]]
	for i in range(filter_index,new_bweights.shape[0]-1):
		new_bweights[i] = old_bweights[i+1]
	
	if torch.cuda.is_available():
		# print('hi2')
		new_bn.weight.data = torch.from_numpy(new_bweights).cuda()
	else:
		new_bn.weight.data = torch.from_numpy(new_bweights)

	bn_bias_numpy = bn.bias.data.cpu().numpy()

	bias = np.zeros(shape = (bn_bias_numpy.shape[0] - 1), dtype = np.float32)
	bias[:filter_index] = bn_bias_numpy[:filter_index]
	bias[filter_index : ] = bn_bias_numpy[filter_index + 1 :]
	
	if torch.cuda.is_available():
		# print('hi')
		new_bn.bias.data = torch.from_numpy(bias).cuda()
	else:
		new_bn.bias.data = torch.from_numpy(bias)	

	runavg_numpy = bn.running_mean.cpu().numpy()

	running_mean = np.zeros(shape = (runavg_numpy.shape[0] - 1), dtype = np.float32)
	running_mean[:filter_index] = runavg_numpy[:filter_index]
	running_mean[filter_index : ] = runavg_numpy[filter_index + 1 :]
	
	if torch.cuda.is_available():
		new_bn.running_mean= torch.from_numpy(running_mean).cuda()
	else:
		new_bn.running_mean= torch.from_numpy(running_mean)
	
	runvar_numpy = bn.running_var.cpu().numpy()

	running_var = np.zeros(shape = (runvar_numpy.shape[0] - 1), dtype = np.float32)
	running_var[:filter_index] = runvar_numpy[:filter_index]
	running_var[filter_index : ] = runvar_numpy[filter_index + 1 :]
	
	if torch.cuda.is_available():
		new_bn.running_var= torch.from_numpy(running_var).cuda()
	else:
		new_bn.running_var= torch.from_numpy(running_var)

	
	if not next_conv is None:
		next_new_conv = \
			torch.nn.Conv2d(in_channels = next_conv.in_channels - 1,\
				out_channels =  next_conv.out_channels, \
				kernel_size = next_conv.kernel_size, \
				stride = next_conv.stride,
				padding = next_conv.padding,
				dilation = next_conv.dilation,
				groups = next_conv.groups,
				bias = True if next_conv.bias is not None else False)

		old_weights = next_conv.weight.data.cpu().numpy()
		new_weights = next_new_conv.weight.data.cpu().numpy()

		new_weights[:, : filter_index, :, :] = old_weights[:, : filter_index, :, :]
		new_weights[:, filter_index : , :, :] = old_weights[:, filter_index + 1 :, :, :]
		
		if torch.cuda.is_available():
			next_new_conv.weight.data = torch.from_numpy(new_weights).cuda()
		else:
			next_new_conv.weight.data = torch.from_numpy(new_weights)

		next_new_conv.bias.data = next_conv.bias.data
		# next_new_conv.running_mean.data = next_conv.running_mean.data
		# next_new_conv.running_var.data = next_conv.running_var.data
	
	if not next_bn is None:
		# print('next_conv.out_channels')
		# print(next_conv.out_channels)
		next_new_bn = torch.nn.BatchNorm2d(num_features = next_new_conv.out_channels - 1, eps=1e-05, momentum=0.1, affine=True)

		bold_weights = next_bn.weight.data.cpu().numpy()
		bnew_weights = next_new_bn.weight.data.cpu().numpy()
		i=0
		
		while i<filter_index & i < bnew_weights.shape[0]:
			print(i)
			print('i)')
			bnew_weights[i] = bold_weights[i]
			i=i+1
			# pdb.pdb.set_trace()
		# bnew_weights[:filter_index] = bold_weights[:filter_index]	
		for i in range(filter_index,bnew_weights.shape[0]-1):
			bnew_weights[i] = bold_weights[i+1]
		print('here i am ')
		# print(bnew_weights.shape)
		if torch.cuda.is_available():
			next_new_bn.weight.data = torch.from_numpy(bnew_weights).cuda()
		else:
			next_new_bn.weight.data = torch.from_numpy(bnew_weights)

		next_new_bn.bias.data = next_bn.bias.data
		next_new_bn.running_mean = next_bn.running_mean
		next_new_bn.running_mean= next_bn.running_mean
	
	if not next_bn is None:
	 	features = torch.nn.Sequential(
	            *(replace_layers(model.features, i, [bn_layer_index, bn_layer_index+boffset], \
	            	[new_bn, next_bn]) for i, _ in enumerate(model.features)))
	 	del model.features
	 	del bn

	 	model.features = features

	if not next_conv is None:
	 	features = torch.nn.Sequential(
	            *(replace_layers(model.features, i, [layer_index, layer_index+offset], \
	            	[new_conv, next_new_conv]) for i, _ in enumerate(model.features)))
	 	del model.features
	 	del conv

	 	model.features = features
	
	else:
		#Prunning the last conv layer. This affects the first linear layer of the classifier.
		model.features = torch.nn.Sequential(
				*(replace_layers(model.features, i, [layer_index], \
					[new_conv]) for i, _ in enumerate(model.features)))
		model.features = torch.nn.Sequential(
				*(replace_layers(model.features, i, [bn_layer_index], \
					[new_bn]) for i, _ in enumerate(model.features)))
		layer_index = 0
		bn_layer_index = layer_index +1
		old_linear_layer = None
		for _, module in model.classifier._modules.items():
			if isinstance(module, torch.nn.Linear):
				old_linear_layer = module
				break
			layer_index = layer_index  + 1

		if old_linear_layer is None:
			raise BaseException("No linear layer found in classifier")
		params_per_input_channel = old_linear_layer.in_features/conv.out_channels
		print(old_linear_layer.out_features)
		new_linear_layer = \
			torch.nn.Linear(int(old_linear_layer.in_features - params_per_input_channel), 
				int(old_linear_layer.out_features))

		old_weights = old_linear_layer.weight.data.cpu().numpy()
		new_weights = new_linear_layer.weight.data.cpu().numpy()	 	

		new_weights[:, : int(filter_index * params_per_input_channel)] = \
			old_weights[:, : int(filter_index * params_per_input_channel)]
		new_weights[:, int(filter_index * params_per_input_channel ):] = \
			old_weights[:, int((filter_index + 1) * params_per_input_channel) :]

		new_linear_layer.bias.data = old_linear_layer.bias.data

		
		if torch.cuda.is_available():
			new_linear_layer.weight.data = torch.from_numpy(new_weights).cuda()
		else:
			new_linear_layer.weight.data = torch.from_numpy(new_weights)

		classifier = torch.nn.Sequential(
			*(replace_layers(model.classifier, i, [layer_index], \
				[new_linear_layer]) for i, _ in enumerate(model.classifier)))

		del model.classifier
		del next_conv
		del conv
		model.classifier = classifier

	return model

if __name__ == '__main__':
	# model = models.vgg16(pretrained=True)
	model = torch.load('vgg11cifar.net')
	model.train()

	t0 = time.time()
	model = prune_vgg16_conv_layer(model, 0, 10)
	print ("The prunning took", time.time() - t0)