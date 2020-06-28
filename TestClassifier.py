# Test Classifier will be used to learn/build example classifiers with example data to see how tensorflow operates
# following tutorial from datacamp.com

# Importing libraries to use

# TensorFlow and Keras
import tensorflow as tf
from tensorflow import keras

# helper libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import skimage

# Learning tensorflow
if __name__ == "__main__":
    
    # you can multiply two constant tensors
    # initialize two tensors
    x1 = tf.constant([1,2,3,4])
    x2 = tf.constant([6,7,8,9])

    # multiply the two tensors
    mult = tf.multiply(x1,x2)

    print("multiplication of %s and %s gives %s " % (x1.numpy(), x2.numpy(), mult.numpy()))

    # importing data from example files
    def load_data(data_directory):
        directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
        labels = []
        images = []
        for d in directories:
            label_directory = os.path.join(data_directory, d)
            file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if f.endswith(".ppm")]
            for f in file_names:
                images.append(skimage.data.imread(f))
                labels.append(int(d))
        return images, labels

    ROOT_PATH = "/Users/Frede/Desktop/Projects/git/MachineLearningMatchPrediction"
    train_data_directory = os.path.join(ROOT_PATH, "/Users/Frede/Desktop/Projects/git/MachineLearningMatchPrediction/Training")
    test_data_directory = os.path.join(ROOT_PATH, "/Users/Frede/Desktop/Projects/git/MachineLearningMatchPrediction\Testing")

    # load data using load_data function
    images, labels = load_data(train_data_directory)

    images = np.array(images)
    labels = np.array(labels)

    # Print the `images` dimensions
    print(images.ndim)

    # Print the number of `images`'s elements
    print(images.size)

    # Print the first instance of `images`
    images[0]

    # Make a histogram with 80 bins of the `labels` data (sees distribution of traffic sign labels)
    # each data is of type (traffic sign type: labels)
    plt.hist(labels, 80)

    # Show the plot
    plt.show()


