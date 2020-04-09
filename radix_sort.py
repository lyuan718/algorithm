#!/usr/bin/python
#!-*-coding:utf-8 -*-

#基数排序:
# 构建一个足够大的数组hashArray[],数组大小保证把所有元素都包含在内
# 原理将整体按位数切割或不同的数字
# 然后按每个位数分别比较，然后再排倒数第二位，第三位。。
#时间复杂度：O(d(r+n))
#空间复杂度：O(rd+n)
#稳定性：稳定

def radix_sort(array):
    i = 0 #记录当前正在排哪一位，最低位为1
    max_num = max(array)  #最大值
    j = len(str(max_num))  #记录最大值的 位数
    while i < j:
        bucket_list = [[] for _ in range(10)] #初始化桶数组
        for x in array:
            bucket_list[int(x / (10 ** i)) % 10].append(x)   #找到位置放入桶数组
        print(bucket_list)
        array.clear()
        for x in bucket_list:
             for y in x:
                 array.append(y)
        i += 1

if __name__ == "__main__":
    a = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
    radix_sort(a)
    print(a)