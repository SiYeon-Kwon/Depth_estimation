#이미지의 shape 찍기
import PIL
import torchvision.transforms as transforms
import numpy as np

'''img = PIL.Image.open("/home/kwon/sparse/data/custom/depth/filename_time.struct_time(tm_year=2022, tm_mon=7, tm_mday=14, tm_hour=8, tm_min=34, tm_sec=29, tm_wday=3, tm_yday=195, tm_isdst=0).png")
numpyimg = np.array(img, dtype='f4')
print(numpyimg)
print(numpyimg.max())
print(numpyimg.shape)

tf = transforms.ToTensor()
img_t = tf(img)

print(img_t)
print(img_t.max())
print(img_t.size())'''

#npy의 shape 찍기
y = np.load('/home/kwon/sparse/data/custom/depth/filename_time.struct_time(tm_year=2022, tm_mon=7, tm_mday=15, tm_hour=0, tm_min=49, tm_sec=56, tm_wday=4, tm_yday=196, tm_isdst=0).png.npy')
npy = np.array(y, dtype='f4')
print(npy)
print(npy.shape)

#h5 파일의 shape 찍기
'''import h5py
import torch
import numpy as np

f = h5py.File('/home/kwon/data/nyudepthv2/train/basement_0001a/00001.h5', 'r')
file = np.array(f['depth'])
print(file)

torch_file = torch.from_numpy(file)
print(torch_file)
print(torch_file.max())
print(torch_file.size())'''