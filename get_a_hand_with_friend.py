import cv2
import pyzed.sl as sl
import math
import numpy as np
import sys

zed = sl.Camera()

#Create a InitParameters object and set configuration parameters
init_params = sl.InitParameters()
init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE #Use PERFORMANCE depth mode
init_params.coordinate_units = sl.UNIT.METER #Use meter unit(for depth measurements)
init_params.camera_resolution = sl.RESOLUTION.HD1080

#Open the camera
err = zed.open(init_params)
image_size = zed.get_camera_information().camera_resolution
image_zed = sl.Mat(image_size.width, image_size.height, sl.MAT_TYPE.U8_C4)
depth_zed = sl.Mat(image_size.width, image_size.height, sl.MAT_TYPE.F32_C1)

while(1):
    if zed.grab() == sl.ERROR_CODE.SUCCESS :
        #Retrieve depth data(32-bit)
        zed.retrieve_image(image_zed, sl.VIEW.LEFT) # Retrieve left image
        zed.retrieve_measure(depth_zed, sl.MEASURE.DEPTH) # Retrieve depth
        #Load depth data into a numpyarray
        image_ocv = image_zed.get_data().astype(np.uint8)
        depth_ocv = depth_zed.get_data()
        depth_ocv = (depth_ocv*10).astype(np.uint8)
        get_min = np.min(depth_ocv)
        get_max = np.min(depth_ocv)
        
        #depth_ocv = cv2.normalize(depth_ocv, None, get_min, get_max)
        #depth_ocv = cv2.normalize(depth_ocv, None, 0, 255, cv2.NORM_MINMAX)
        depth_ocv = cv2.normalize(depth_ocv, None, get_min, get_max, cv2.NORM_MINMAX)
        #print(depth_ocv.shape, image_ocv.shape)
        alpha = 0.4
        added_image = cv2.addWeighted(image_ocv[:,:,0],alpha,depth_ocv,(1-alpha),0)
        #cv2.imshow("Image",image_ocv)
        
        added_image = cv2.circle(added_image,(int(depth_ocv.shape[1]/2),int(depth_ocv.shape[0]/2)),3,(255,0,0),3)
        cv2.imshow('video',added_image)
        
        #Print the depth value at the center of the image
        #print(depth_ocv[int(len(depth_ocv)/2)][int(len(depth_ocv[0])/2)])
        print(depth_ocv[int(depth_ocv.shape[0]/2)][int(depth_ocv.shape[1]/2)]/10.0,'m')
        #print(int(depth_ocv.shape[1]/2),int(depth_ocv.shape[0]/2))
        #print(depth_ocv.shape)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.destroyAllWindows()