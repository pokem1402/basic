"""

    example.py
    example generator and plot
    made by Wonbin Kim

"""
import numpy as np
import matplotlib.pyplot as plt
from os import path, stat, makedirs

# plotting 함수
def example(bias_add, n_observations, r, ratio):
    np.random.seed(2018)
    xs = np.linspace(-r, r, n_observations)[:, np.newaxis]
    xs = np.hstack([xs, np.ones([n_observations, 1])]) if bias_add else xs
    noise = np.random.uniform(-0.5, 0.5, n_observations)
   
    test = np.random.choice(np.arange(n_observations), int(n_observations*ratio))
    train = np.setdiff1d(np.arange(n_observations), test)    
    return xs, train, test, noise

def plotting(x,y, plot_style=None, label=None):
    '''
        Args
        - x : list of numpy arrays
        - y : list of numpy arrays
        - plot_style : By this, you can emphasis specific lines or curves
        - label : names of lines or curves
    '''
    if plot_style == None:
        plot_style=['.' if i < 2 else '-' for i in range(len(y))]
    if label == None:
        label=[None for i in range(len(y))]
    for i in range(len(x)):
        x[i] = x[i][:,0] if len(x[i].shape) == 2 else x[i]
        plt.plot(x[i],y[i], plot_style[i], label=label[i])
    plt.xlabel('x')
    plt.ylabel('y')
    if len(y) >= 3 :
        ymin = min(np.min(y[0]), np.min(y[1]))*1.5
        ymax = max(np.max(y[0]), np.max(y[1]))*1.5
        plt.ylim((ymin, ymax))    
    plt.legend(bbox_to_anchor=(1,1), borderaxespad=0.3)
    plt.axis
    plt.show()
    
def example1(bias_add = False, n_observations=50, r=10., ratio=0.3):
    '''
        Args
        - bias_add : if True, one vector is add
        - n_observations : the number of observation
    '''
    xs, train, test, noise = example(bias_add, n_observations,r,ratio)
    ys = np.sin(xs[:,0]) + noise 
    
    return xs[train],ys[train],xs[test],ys[test], xs, ys


def example2(bias_add = False, n_observations=50, r=10.,ratio=0.3):
    """
        Args
        - bias_add : if True, one vector is add
        - n_observations : the number of observation    
    """
    xs, train, test, noise = example(bias_add, n_observations,r,ratio)
    ys = - xs[:,0] + np.cos(xs[:,0]) + noise   
    return xs[train],ys[train],xs[test],ys[test], xs, ys

def example3(bias_add = False, n_observations=50, r=10.,ratio=0.3):
    """
        Args
        - bias_add : if True, one vector is add
        - n_observations : the number of observation    
    """
    xs, train, test, noise = example(bias_add, n_observations,r, ratio)
    ys = xs[:,0] * np.sin(xs[:,0]) + noise 
    
    return xs[train],ys[train],xs[test],ys[test], xs, ys

def example4(bias_add = False, n_observations=50, r=10.,ratio=0.3):
    """
        Args
        - bias_add : if True, one vector is add
        - n_observations : the number of observation    
    """
    xs, train, test, noise = example(bias_add, n_observations,r,ratio)
    ys = -xs[:,0] + 2*np.cos(xs[:,0]) + noise 
    
    return xs[train],ys[train],xs[test],ys[test], xs, ys

def example5(bias_add = False, n_observations=50, r=10.,ratio=0.3):
    """
        Args
        - bias_add : if True, one vector is add
        - n_observations : the number of observation    
    """
    xs, train, test, noise = example(bias_add, n_observations,r,ratio)
    ys = np.sin(xs[:,0]) + noise 
    
    return xs[train],ys[train],xs[test],ys[test], xs, ys


def example6(bias_add = False, n_observations=50, r=10.,ratio=0.3):
    """
        Args
        - bias_add : if True, one vector is add
        - n_observations : the number of observation    
    """
    xs, train, test, noise = example(bias_add, n_observations,r,ratio)
    ys = -xs[:,0] - np.sin(xs[:,0]) + noise 
    
    return xs[train],ys[train],xs[test],ys[test], xs, ys