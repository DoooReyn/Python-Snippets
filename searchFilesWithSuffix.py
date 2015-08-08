########################################
# function : search files with suffix  #
########################################

import os

def searchFileWithSuffix(targetPath='/', targetSuffix='.py'):
    if targetPath == '':
        targetPath = '/'
        print('target path is (/)')

    if targetSuffix == '':
        targetSuffix = ''
        print('search all files')

    fileCount = 0

    if targetSuffix == '':
        for rootDir, subFolder, files in os.walk(targetPath):
            for f in files:
                print(f)
                fileCount += 1
    else:
        for rootDir, subFolder, files in os.walk(targetPath):
            for f in files:
                beforeIdx= f.find(targetSuffix)
                afterIdx = len(f)-len(targetSuffix)
                if beforeIdx != 1 and afterIdx == beforeIdx :
                    print(f)
                    fileCount += 1
                    # print(os.path.join(rootDir, f))

    print('[search results ] get %d files' % fileCount)

if __name__ == '__main__':
    targetPath = str(raw_input('input target path (/) : '))
    targetSuffix = str(raw_input('input target suffix (.py) : '))

    searchFileWithSuffix(targetPath, targetSuffix)
