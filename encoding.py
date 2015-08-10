# encoding=utf8
import sys

def setEnconding()
    reload(sys)
    sys.setdefaultencoding('utf8')


'''
python在安装时，默认的编码是ascii，当程序中出现非ascii编码时，python的处理常常会报这样的错:
>>> UnicodeDecodeError: 'ascii' codec can't decode byte 0x?? in position 1: ordinal not in range(128)
python没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。

查询系统默认编码可以在解释器中输入以下命令：
>>> sys.getdefaultencoding()

设置默认编码时使用：
>>> sys.setdefaultencoding('utf8')

但还是可能会报：
>>> AttributeError: 'module' object has no attribute 'setdefaultencoding'
的错误，执行reload(sys)，在执行以上命令就可以顺利通过。

此时在执行sys.getdefaultencoding()就会发现编码已经被设置为utf8的了，但是在解释器里修改的编码只能保证当次有效，
在重启解释器后，会发现，编码又被重置为默认的ascii了，那么有没有办法一次性修改程序或系统的默认编码呢?

很简单，单独写一个模块出来，每次都加载不就好了嘛。
'''

'''
如果没有此文件编码类型的声明，则python默认以ASCII编码去处理
如果你没声明编码，但是文件中又包含非ASCII编码的字符的话，python解析器去解析的python文件，自然就会报错了。
必须放在python文件的第一行或第二行
支持的格式，可以有三种：
    带等于号的：
        # coding=<encoding name>

    最常见的，带冒号的（大多数编辑器都可以正确识别的）：
        #!/usr/bin/python
        # -*- coding: <encoding name> -*-

    vim的：
        #!/usr/bin/python
        # vim: set fileencoding=<encoding name> :

    更加精确的解释是符合正则表达式：
        "coding[:=]\s*([-\w.]+)"
    的都可以，很明显，如果你熟悉正则表达式，也就可以写出来，其他一些合法的编码声明，以utf-8为例，比如：
        coding:         utf-8
        coding=utf-8
        coding=                  utf-8
        encoding:utf-8
        crifanEncoding=utf-8

    Notes:
        为了照顾特殊的Windows中的带BOM（’\xef\xbb\xbf’）的UTF-8：
            如果你的python文件本身编码是带BOM的UTF-8，即文件前三个字节是：’\xef\xbb\xbf’，那么：
            即使你没有声明文件编码，也自动当做是UTF-8的编码

            如果你声明了文件编码，则必须是声明了（和你文件编码本身相一致的）UTF-8
            否则（由于声明的编码和实际编码不一致，自然）会报错
'''
