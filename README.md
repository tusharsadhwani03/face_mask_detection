1. This repo contains face_mask detection Project.

2. I have used the pretrained yolov8n model for training on the dataset.

3. The model is imported from ultralytics.

4. Two Training model notebooks(colab, Kaggle) are present in the repo. 
Initially trained the model in colab but gpu time exhausted. Hence trained the model on Kaggle and used the trained model in colab for inferencing and preparing the csv file for test data.

Colab notebook link: "https://colab.research.google.com/drive/1iqum7H_F0h72E1zTYqTVFsLrhYEI7td9?usp=sharing"

5. 'detect folder' contains the weights, metrics and results on train & validation data.
 
6. There are two csv files prepared from best and last weights.

7. The python script for detection of masks in videos is 'detect.py' and it generate the output in 'Output Videos' folder during the runtime.

8. The videos generated from the script are present in 'Output' folder.

Thanks