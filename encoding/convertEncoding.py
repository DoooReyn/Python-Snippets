#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

def convertEncoding(from_encode,to_encode,old_filepath,target_file):  
    # read lines from from_encode to to_encode as content
    fp = file(old_filepath)  
    content = []  
    while True:  
        line = fp.readline()  
        content.append(line.decode(from_encode).encode(to_encode))  
        if len(line) == 0:  
            break  
    fp.close()  
        
    # write content to new file   
    fp=file(target_file,'w')  
    fp.writelines(content)  
    fp.close()  

    print('saves as ' + target_file)
  
def convertFromGBK2utf8(filepath):  
    convertEncoding("GBK", "UTF-8", filepath, filepath+".bak")  
  
def convertFromUTF82gbk(filepath):  
    convertEncoding("UTF-8", "GBK", filepath, filepath+".bak")  

def get_method():
    isMethodRight = True
    while(isMethodRight):
        encoding = raw_input('input target encoding :\n0 - UTF8\t->\tGBK \n1 - GBK\t\t->\tUTF8\n')
        if encoding == '0' or encoding == '1':
            isMethodRight = False
    return encoding

def get_filepath():
    isPathRight = True
    while(isPathRight):
        path = raw_input('input target file path:')
        if os.path.isfile(path):
            isPathRight = False
    return path    

if __name__ == '__main__':   
    path   = get_filepath()
    method = get_method()

    if method == '0':
        convertFromUTF82gbk(path)
    elif method == '1':
        convertFromGBK2utf8(path)
    else:
        print('wrong target encoding')
        