#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib

def get_md5(url):
    #因为python3 所有str编码都是Unicode
    if(isinstance(url, str)):
        url = url.encode("utf-8")

    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == '__main__':
    print(get_md5("你好啊"))