#!/usr/bin/python
#!-*-coding:utf-8 -*-

#快速排序
#时间复杂度：O(nlog2n)
#空间复杂度：O(nlog2n)
#稳定性：不稳定

def quick_sort(qlist):
    if qlist == []:
        return []
    else:
        qfirst = qlist[0]
        qless = quick_sort([l for l in qlist[1:] if l < qfirst])
        qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
        return qless + [qfirst] + qmore

if __name__ == "__main__":
    qlist = quick_sort([4,5,6,7,3,2,6,9,1])
    print(qlist)