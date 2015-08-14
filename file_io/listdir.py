import os

def listdir(targetPath):
    fileList = []
    dirList  = []

    for f in os.listdir(targetPath):
        fileRealPath = os.path.join(targetPath,f)

        if os.path.isfile(fileRealPath):
            fileList.append(f)
        elif os.path.isdir(fileRealPath):
            dirList.append(f)

    return fileList, dirList


def inputPath():
    isPathRight = True
    while(isPathRight):
        targetPath = str(raw_input("input target path (/) :"))
        if os.path.exists(targetPath):
            isPathRight = False
    return targetPath

def outputResult():
    targetPath = inputPath()

    fileList,dirList = listdir(targetPath)

    for filename in fileList:
        print('[file] '+filename)

    print('##########got %d files' % len(fileList))


    for filename in dirList:
        print('[dir] '+filename)

    print('##########got %d directories' % len(dirList))

if __name__ == '__main__':
    outputResult()
