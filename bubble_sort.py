#!/usr/bin/python
#!-*-coding:utf-8 -*-

#冒泡排序
#时间复杂度：O(n^2)
#空间复杂度：O(1)
#稳定性：稳定

def bubble_sort(blist):
    count = len(blist)
    for i in range(0, count):
        for j in range(i + 1, count):
            if blist[i] > blist[j]:
                blist[i], blist[j] = blist[j], blist[i]
    return blist

if __name__ == "__main__":
    blist = bubble_sort([4,5,6,7,3,2,6,9,8])
    print(blist)