# Food Detection Network Training
This project contains the code for training the food detector for the [smart fridge project](https://github.com/Zilinghan/smart-fridge).

## Dataset
We have collected custom training and validation sets for food detection. The dataset contains six types of foods (Apple, Banana, Orange, Tomato, Green Pepper, Broccoli), and you can download this dataset [here](https://drive.google.com/file/d/19EGoY_qxgSeUN2Lem37novVmaeiC9Dx_/view?usp=sharing). 

## Training Code
The code for fine-tuning the model is available on google Colab, you need to change the training and validation set to the food detection dataset. <a href="https://colab.research.google.com/github/khanhlvg/tflite_raspberry_pi/blob/main/object_detection/Train_custom_model_tutorial.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Results
We have trained 5 different food detection models of various sizes. We start from EfficientDet-LiteX object detection models pretrained on COCO dataset, and fine-tune them on the custom food dataset. The following table lists the detailed information of the fine-tuned models as well as the corresponding download links.

| Models             | AP    | AP50  | AP75  | Size   |
|--------------------|-------|-------|-------|--------|
| [EfficientDet-Lite0](https://drive.google.com/file/d/1U_H1PA00m9cZJfpr018TNLx6190MA43D/view?usp=sharing) | 54.00 | 75.03 | 66.02 | 4.24MB |
| [EfficientDet-Lite1](https://drive.google.com/file/d/1fTjnSW6K7JSbjZSKKfhJJ2BIv-JWFNoM/view?usp=sharing) | 55.83 | 75.11 | 62.77 | 5.66MB |
| [EfficientDet-Lite2](https://drive.google.com/file/d/1aYQkU1r-Pqgi5W8O9ZAv7Fh3dAtwhhFp/view?usp=sharing) | 66.46 | 82.66 | 77.15 | 7.05MB |
| [EfficientDet-Lite3](https://drive.google.com/file/d/16Isz62Jy4u5VlfmEHU2hgFv--c5o7J7B/view?usp=sharing) | 81.36 | 96.23 | 89.70 | 11.1MB |
| [EfficientDet-Lite4](https://drive.google.com/file/d/1Os3VKh_Ho-76pTy6atoyrIZjXGJpwRse/view?usp=sharing) | 79.41 | 94.30 | 84.23 | 19.6MB |


## Collect Your Own Dataset
Currently, our collected dataset is relatively small and only contains six types of foods, so if you want to collect more labeled data, we suggest using the [Label Studio](https://github.com/heartexlabs/label-studio), and export your annotations in **Pascal VOC XML** format. 

Since the code in the above Colab requires JPEG-format images, you can first use [png2jpg.py](utils/png2jpg.py) in the utils folder to convert all your images to the required format before labeling. 

After exporting your annotations, you need to run [xml-process.py](utils/xml-process.py) to delete the first line of each annotation file to make it a suitable format for training.


