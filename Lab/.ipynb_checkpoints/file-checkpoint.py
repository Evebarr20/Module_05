#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 20:15:02 2026

@author: evebarr20
"""
# import easygui
import easygui as g

def file_choose():
    """
    open file browser window and allow user to select any file

    Returns
    -------
    filename : STR
        returns file path the user selects.

    """
    title = "Please select a File"
    return g.fileopenbox(title) 
