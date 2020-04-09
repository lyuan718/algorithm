#!/usr/bin/python
#!-*-coding:utf-8 -*-

#堆排序
#时间复杂度：O(nlog₂n)
#空间复杂度：O(1)
#稳定性：不稳定

import copy

def heap_sort(hlist):
    def heap_adjust(parent):
        child = 2 * parent + 1
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child+1] > heap[child]:
                    child += 1
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, hlist = copy.copy(hlist), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        hlist.insert(0, heap.pop())
        heap_adjust(0)
    return hlist


if __name__ == "__main__":
    hlist = heap_sort([4,5,12,72,13,45,10])
    print(hlist)