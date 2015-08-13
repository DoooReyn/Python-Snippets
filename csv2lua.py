#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
import os
import csv
import types

def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return

def get_lua_fp(luapath):
    fp = open(luapath, "wt")
    return fp

def write_lua_head(fp):
    fp.write('local data = {\n')


def write_lua_tail(fp):
    fp.write('}\n\nreturn data')


def write_lua_key(key, fp):
    fp.write('\t')
    if key.isdigit():
        fp.write('[')
        fp.write(key)
        fp.write(']')
    else:
        fp.write(key)
    fp.write(' = ')


def write_lua_value(value, fp):
    if value.isdigit():
        fp.write(value)
    else:
        fp.write('"')
        fp.write(value)
        fp.write('"')
    fp.write(',\n')


def csv2lua(csvpath,luapath):
    filecount = 0
    for filename in os.listdir(csvpath):
        csvfilepath = os.path.join(csvpath, filename)
        extendname = os.path.splitext(filename)[1]

        if os.path.isfile(csvfilepath) and extendname == '.csv':
            csvReader = csv.reader(file(csvfilepath, 'rt'))
            luafilename = os.path.splitext(filename)[0]+'.lua'
            luatargetpath = os.path.join(luapath, luafilename)

            fp = get_lua_fp(luatargetpath)
            if not fp:
                print(luafilename + ' write error')
                break
            else:
                print('converting ' + filename + ' to ' + luafilename)
                filecount += 1
                write_lua_head(fp)
                for line in csvReader:
                    key   = line[0]
                    value = line[1]
                    write_lua_key(key,fp)
                    write_lua_value(value, fp)

                write_lua_tail(fp)
            fp.close()

    if filecount == 0:
        print('no csv file to convert')
    else:
        print('[done] Converted ' + str(filecount) + ' files')



if __name__ == '__main__':
    csvpath = os.getcwd() + '/csv/'
    luapath = os.getcwd() + '/lua/'
    check_path(csvpath)
    check_path(luapath)
    
    csv2lua(csvpath,luapath)
