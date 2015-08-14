# -*- coding: utf-8 -*-
import os

def getTargetPath():
    isPathRight = True
    while(isPathRight):
        targetPath = raw_input('input target path (/) : ')
        if os.path.exists(targetPath) and os.path.isdir(targetPath):
            isPathRight = False
        else:
            print('wrong target path !')
    return targetPath


def del_file(targetPath):
    for filename in os.listdir(targetPath):
        filePath = os.path.join(targetPath, filename)
        if os.path.isfile(filePath):
            print('remove file : ' + filePath)
            os.remove(path)
        elif os.path.isdir(path):
            print('enter dir : ' + filePath)
            del_file(path)

    isEmpty = False
    for filename in os.listdir(targetPath):
        path = os.path.join(targetPath, filename)
        if os.path.isfile(path):
            isEmpty = False
        else:
            isEmpty = True
    return isEmpty


def del_dir(targetPath):
    for filename in os.listdir(targetPath):
        filePath = os.path.join(targetPath, filename)
        if os.path.isdir(filePath):
            print('remove dir : ' + filePath)
            os.rmdir(filePath)
        else:
            print('dir is not empty')


def removeDir(targetPath):
    if not os.path.isdir(targetPath):
        return
    files = os.listdir(targetPath)
    try:
        for filename in files:
            filePath = os.path.join(targetPath, filename)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                removeDir(filePath)
        os.rmdir(dirPath)
    except Exception, e:
        print e


if __name__ == '__main__':
    #### method one #####
    targetPath = getTargetPath()
    if del_file(targetPath):
        del_dir(targetPath)


    ##### method two #####
    # targetPath = getTargetPath()
    # removeDir(targetPath)


    ##### method three #####
    ##### recommended  #####
    # import shutil
    # targetPath = getTargetPath()
    # shutil.rmtree(targetPath)
