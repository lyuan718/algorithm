#!/usr/bin/python
#!-*-coding:utf-8 -*-

#选择排序
#时间复杂度：O(n²)
#空间复杂度：O(1)
#稳定性：不稳定

def select_sort(slist):
    for i in range(len(slist) - 1):
        x = i
        for j in range(i, len(slist)):
            if slist[j] < slist[x]:
                x = j
        slist[i], slist[x] = slist[x], slist[i]
    return slist

if __name__ == "__main__":
    slist = select_sort([4,5,6,7,3,26,19])
    print(slist)