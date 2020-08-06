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
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import DataScraper

if __name__ == "__main__":

    # import data
    data = DataScraper.Scrape().scrapeFromHLTV()
    print(data)


    # transform data to work as dataset
    #data['Date'] = data['Date'].apply(lambda x: x.toordinal())

    # Split-out validation dataset from training set
    array = data.values
    X = array[:,0:2]
    # TODO: y data needs to be seperated with semicolon
    y = array[:,3:4]
    y= y.astype('int')


    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y.ravel(), test_size=0.20, random_state=1, shuffle=True)

    # training and testing sets
    #print(X_train,Y_train, "training data")
    #print(X_validation, Y_validation, "testing data")

    # initialize different models to test which one works the best
    models = []
    models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    #models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(gamma='auto')))

    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        kfold = KFold(n_splits=10, random_state=0, shuffle=True)
        cv_results = cross_val_score(model, X_train, Y_train, cv = kfold, scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
        
    # Compare Algorithms
    plt.boxplot(results, labels=names)
    plt.title('Algorithm Comparison')
    plt.show()


    