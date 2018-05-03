#!/usr/bin/python
# -*- coding: utf-8 -*-
from mainsite import models
import re

regx = re.compile('[\s\S.]+?src="(/data/[\s\S.]+?[gif|png|jpeg|jpg])">')

def fix_the_picpath(item):

    f = False
    if(isinstance(item, models.Problem)):
        results_set = regx.findall(item.context)
        if (results_set is not None):
            for it in results_set:
                if (f or item.context.find("http") == -1):
                    item.context = item.context.replace(it, 'http://acm.hdu.edu.cn' + str(it))
                    f = True

        results_set = regx.findall(item.Input)
        f = False
        if (results_set is not None):
            for it in results_set:
                if (f or item.Input.find("http") == -1):
                    item.Input = item.Input.replace(it, 'http://acm.hdu.edu.cn' + str(it))

        results_set = regx.findall(item.Output)
        f = True
        if (results_set is not None):
            for it in results_set:
                if (f or item.Output.find("http") == -1):
                    item.Output = item.Output.replace(it, 'http://acm.hdu.edu.cn' + str(it))

    return item

if __name__ == '__main__':
    pass