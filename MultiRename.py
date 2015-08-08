import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# import encoding

def getTargetPath():
    isPathRight = True
    while(isPathRight):
        targetPath = str(raw_input('input target path (/) : '))
        if not os.path.exists(targetPath):
            print('path error')
        else:
            isPathRight = False
    return targetPath


def getTargetName():
    isNameEmpty = True
    while(isNameEmpty):
        targetName = str(raw_input('input target name (a) : '))
        if targetName != '':
            isNameEmpty = False
        else:
            print('empty name error')
    return targetName


def multi_rename(targetPath, targetName):
    fileCount = 0

    for rootDir, subFolder, files in os.walk(targetPath):
        for f in files:
            if rootDir == targetPath:
                filename = os.path.join(rootDir, f)
                if os.path.isfile(filename):
                    print('filename: %s' % filename)
                    fileCount += 1
                    extendName = os.path.splitext(filename)[1]
                    newName = os.path.join(rootDir, targetName+'_'+str(fileCount)+extendName)
                    print('newname: %s' % newName)
                    os.rename(filename, newName)
                elif os.path.isdir(filename):
                    print('directory: %s' % filename)
                else:
                    print('other')


if __name__ == '__main__':
    targetPath = getTargetPath()
    targetName = getTargetName()
    multi_rename(targetPath, targetName)
