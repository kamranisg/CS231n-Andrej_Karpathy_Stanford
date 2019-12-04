# CS-231n Winter 2016 ( Convolutional Neural Networks for Visual Recognition )

[Course-Description](http://cs231n.stanford.edu/)

   #### **`Cs-231n encountered its second series in 2016 taught by Prof Lei Fei Fei and Andrej Karpathy at Stanford University.`**

## Lecture 1 : Data-driven approach, kNN, Linear Classification

**1. Python** 

First of all, understanding the process of building neural networks requires a basic understanding of Python. I have compiled some important fundamentals in [Python_Basics.py](https://github.com/kamranisg/CS231n-Andrej_Karpathy_Stanford/blob/master/Python_Basics.py) to get started.

Useful Links to get started :

- [Python-Numpy Tutorial of CS-231N](http://cs231n.github.io/python-numpy-tutorial/)
- [Python-Lists](https://docs.python.org/3.5/tutorial/datastructures.html#more-on-lists)
- [Python-Dictionaries](https://docs.python.org/3.5/library/stdtypes.html#dict)
- [Python-Sets](https://docs.python.org/3.5/library/stdtypes.html#set)
- [Python-Tuples](https://docs.python.org/3.5/tutorial/datastructures.html#tuples-and-sequences)
- [Numpy](https://numpy.org/)

**2. Image Classification- A core task in Computer Vision**

![Perception](Com.jfif)

`An image is composed of a 2d matrix of numbers also called pixels . For a colored picture we have 3 layers of Red, Green, Blue 2d matrices stacked together one by one.`

What is Data Driven Approach ? 

  1. Collect a dataset of images and labels.
  2. Use Machine Learning to train an image classifier.
  3. Evaluate the classifier on a withheld set of images.
  
  Lets start :
  
  **Classifier 1: K Nearest Neighbor**
  
  
