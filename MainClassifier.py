# Main Classifier for CSGO Matches
# i will mainly be using tensorflow


# Importing libraries to use

# TensorFlow and Keras
import tensorflow as tf
from tensorflow import keras

# helper libraries
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt


class MainClassifier():
    
    def __init__(self):
        self.params = None

    #Firstly import data from the training and testing folders (TODO scrape training and testing data of csgo matches (make new class))
    def importData():
        pass

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(url, names=names)
    print(dataset.shape)
    print(dataset.head(3))