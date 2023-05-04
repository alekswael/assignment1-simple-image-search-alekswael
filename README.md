<!-- PROJECT LOGO -->
<br />
  <h1 align="center">Visual Analytics Portfolio</h1> 
  <h2 align="center">Assignment 2: Classification benchmarks with Logistic Regression and Neural Networks</h2> 
  <h3 align="center">Cultural Data Science, 2023</h3> 
  <p align="center">
  Auther: Aleksander Moeslund Wael <br>
  Student no. 202005192
  </p>
</p>

## Assignment notes (Ross)
For this assignment, you'll be using ```OpenCV``` to design a simple image search algorithm.

The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).

For this exercise, you should write some code which does the following:

- Define a particular image that you want to work with
- For that image
  - Extract the colour histogram using ```OpenCV```
- Extract colour histograms for all of the **other* images in the data
- Compare the histogram of our chosen image to all of the other histograms 
  - For this, use the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric
- Find the five images which are most simlar to the target image
  - Save a CSV file to the folder called ```out```, showing the five most similar images and the distance metric:

|Filename|Distance]
|---|---|
|target|0.0|
|filename1|---|
|filename2|---|

## Introduction
Hi there! This repo contains a Python script ```top_five_similar.py```. This script is used to calculate the colour histogram of an image and compare it to all other images in a folder. It returns a .csv file with top 5 most similar images in the folder (when comparing colour histograms), and the distance metric for these images compared to the target image (as calculated by chi-squared).

### Repository structure
In your working directory, you should have two folders: data and out. The data-folder should contain a subfolder with the images. The out-folder is the save location for the output .csv file.

```
│   README.md
│   requirements.txt
│   run.sh
│
├───data
│   └───flowers
│
├───out
│       target_image_0001.csv
│       target_image_0009.csv
│
├───src
│       top_five_similar.py
│
├───utils
│       imutils.py
│       __init__.py
```

### Running from terminal
When run from the terminal, the script takes two arguments:
- ```folder```, which is the name of image-containing folder located in the data folder. The default is "flowers", which is a folder containing 1360 images of flowers.
- ```image```, which is the name of the image you want to compare to the remaining images in the folder. The default is "image_0001.jpg", an image in the "flowers" folder.

## Requirements

## Assignment notes (Ross)

For this assignment, you'll be using ```OpenCV``` to design a simple image search algorithm.

The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/17/).

For this exercise, you should write some code which does the following:

- Define a particular image that you want to work with
- For that image
  - Extract the colour histogram using ```OpenCV```
- Extract colour histograms for all of the **other* images in the data
- Compare the histogram of our chosen image to all of the other histograms 
  - For this, use the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric
- Find the five images which are most simlar to the target image
  - Save a CSV file to the folder called ```out```, showing the five most similar images and the distance metric:

|Filename|Distance]
|---|---|
|target|0.0|
|filename1|---|
|filename2|---|
