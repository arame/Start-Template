###############################################   LAB 6   ##############################################
################### Script written by Dr Alex Ter-Sarkisov@City, University of London, 2020 ############
##################### DEEP LEARNING CLASSIFICATION, MSC IN ARTIFICIAL INTELLIGENCE #####################
########################################################################################################

from PIL import Image as PILImage
from resizeimage import resizeimage
import os,sys,time
import torch
import torch.nn
import torch.optim
import torchvision.models as models
from config import Config
from deviceGpu import DeviceGpu
from deviceGpu import DeviceType
from start import Start
from start import Finish
from start import Hyperparam

# Remember to update start info
Start.start()
DeviceGpu.get()
# Put code in here

# Example code:
#device = DeviceGpu.device
#lr = Hyperparam.lrate



Finish.finish()



