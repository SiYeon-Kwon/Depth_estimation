import torch
import os
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import random
import numpy as np

class DepthDataset(torch.utils.data.Dataset):
    def __init__(self, df):

        self.images = list(df['image'].values)
        self.labels = list(df['label'].values)
        
        '''# load image
        random_sample_image = random.choice([i for i in range(len(self.images) - 1)])
        image = Image.open(self.images[random_sample_image])
        depth = Image.open(self.labels[random_sample_image])'''
        
        #load npy
        
        path = "/home/kwon/sparse/data/custom/train/"
        file_list = os.listdir(path)
        random_sample_image = random.choice([i for i in range(len(self.images) - 1)])
        image = Image.open(self.images[random_sample_image])
        depth = [file for file in file_list if file.endswith(".png.npy")]
        image = np.array(image)
        
        #plt.imshow(image)
        #plt.title("Image")
        #plt.show()
        
        # Denormaling Image
        #plt.imshow(np.asarray(depth) * 256)
        #plt.title("Depth")
        #plt.show()

    def __getitem__(self, index):
        # load image
        image = np.load(self.images[index])
        depth = np.load(self.labels[index])
        
       
        # transformation
        comm_trans = transforms.Compose([
            transforms.Resize((240, 320)),
            transforms.CenterCrop((224, 224)),
            transforms.RandomHorizontalFlip()
        ])
        image_trans = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
        depth_trans = transforms.Compose([
            transforms.Resize((224,224)),
            transforms.ToTensor(),
            transforms.Lambda(lambda x: x.float()),
            transforms.Lambda(lambda x: torch.div(x, 65535.0)),
            #transforms.Normalize((0.5, ), (0.5, ))
        ])
        #image = image_trans(comm_trans(image))
        #depth = depth_trans(comm_trans(depth))
        return image, depth

    def __len__(self):
        return len(self.images)