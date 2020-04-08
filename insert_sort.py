#!/usr/bin/python
#!-*-coding:utf-8 -*-
#插入排序
#时间复杂度：O(n^2)
#空间复杂度: O(1)
#稳定性：稳定

def inser_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i):
            if ilist[i] < ilist[j]:
                ilist.insert(j, ilist.pop(i))
                break
    return ilist

if __name__ == "__main__":
    ilist = inser_sort([4,5,6,10,3,2,9])
    print(ilist)