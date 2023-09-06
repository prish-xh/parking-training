%pwd # prints your directory
# %cd content
# %ls
%cd /content/drive/MyDrive
# %cd ..
# %cd Batch\ C
# %mkdir Test
# %cd Batch\ C
# # %cd content/
# %rm -r yolov5/

#clone YOLOv5 and 
# %cd MyDrive/
!git clone https://github.com/ultralytics/yolov5  # clone repo
#%cd yolov5
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow
%pip install wandb

import torch
import os
from IPython.display import Image, clear_output  # to display images

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

%pwd
#%cd yolov5/
# # running this cell as it is here should download your data into the content/yolov5 folder
# # must change directory using %cd until you find yourself in the desired folder
# # !pip install roboflow

# # crashes severity dataset (https://universe.roboflow.com/razan/traffic-accident-detection-final-dataset/dataset/4)
# !pip install roboflow

# from roboflow import Roboflow 
# rf = Roboflow(api_key="r24t8KwoUGkkyaEtsQtF")
# project = rf.workspace("razan").project("traffic-accident-detection-final-dataset")
# dataset = project.version(4).download("yolov5")

# # stanford car dataset (https://universe.roboflow.com/search?q=object%2520detection%2520cars&t=metadata)
# !pip install roboflow

# from roboflow import Roboflow
# rf = Roboflow(api_key="r24t8KwoUGkkyaEtsQtF")
# project = rf.workspace("openglpro").project("stanford_car")
# dataset = project.version(3).download("yolov5")

# !pip install roboflow

# from roboflow import Roboflow
# rf = Roboflow(api_key="r24t8KwoUGkkyaEtsQtF")
# project = rf.workspace("razan").project("traffic-accident-detection-final-dataset")
# dataset = project.version(4).download("yolov5")
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="eZgbkOIRk8d8gFLJR0mU")
project = rf.workspace("personal-ai").project("klop")
dataset = project.version(1915).download("yolov5")

from google.colab import drive
drive.mount('/content/drive')

# ran 36min nothing
%cd /content/drive/MyDrive/yolov5
!pip install wandb
#%cd yolov5
%pwd
# may need to play around with the paths to 
# 1. train.py (should be located within the yolov5 folder)
# 2. data.yaml
# 3. the weights file (EX: yolov5s.pt)

#!-- resume
# !python train.py --img 416 --batch 64 --epochs 150 --data TRAFFIC-ACCIDENT-DETECTION-FINAL-DATASET-4/data.yaml --weights models/yolov5s.pt --cache
!python train.py --img 416 --batch 100 --epochs 350 --data klop-1915/data.yaml --weights models/yolov5s.pt --cache


