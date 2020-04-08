#!/usr/bin/python
#!-*-coding:utf-8 -*-
#二分查找

def binary_search(lists, item):
    #low和high用于跟踪要在其中查找的列表部分
    low = 0
    high = len(lists)-1

    while low <= high:
        mid = (low+high) // 2   
        guess = lists[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return mid    #返回元素位置
    return -1

if __name__ == "__main__":
    mylist = [11, 23, 33, 51, 76, 80, 90]
    print(binary_search(mylist, 34))
    print(binary_search(mylist, 51))

