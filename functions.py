# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:12:26 2024

@author: jakob
"""

def remove_substr(string, to_remove=["£",","]):
    """
    Parameters
    ----------
    string : str
        a string.
    to_remove : list, optional
        These are things we want to strip from the string. The default is ["£",","].

    The string with the items removed
    -------
    remove_substr('hello, £ world')

    """
    
    for item in to_remove:
        string = string.replace(item, "")
        
    return(string)

def plot_over_time(df, col):
    """
    Parameters
    ----------
    df : Data Frame
        A DF with a "Date" column to plot against
    col : string
        Name of column to plot on the Y axis

    a line graph
    -------
    None.

    """
    plt.plot(df['Date'],
             df[col])
    plt.axhline(y=0)
    plt.show()