# -*- coding:utf-8 -*-

import heapq
import random

rand = random.sample(xrange(1000), 10)    # 生成随机数序列。
# rand
# [572, 758, 737, 738, 412, 755, 507, 734, 479, 374]

heap = []
for x in rand: 
    heapq.heappush(heap, x)    # 将随机数压入堆。
# heap    # 堆是树，并非排序列表。
# [374, 412, 507, 572, 479, 755, 737, 758, 734, 738]

while heap: 
    print heapq.heappop(heap)     # 总是弹出最小元素。
# 374
# 412
# 479
# 507
# 572
# 734
# 737
# 738
# 755
# 758


# 其他相关函数
d = random.sample(xrange(10), 10)
# d
# [9, 7, 3, 4, 0, 2, 5, 1, 8, 6]


heapq.heapify(d)     # 将列表转换为堆。
# d
# [0, 1, 2, 4, 6, 3, 5, 9, 8, 7]


heapq.heappushpop(d, -1)      # 先 push(item)，后 pop。弹出值肯定小于或等于 item。
# -1
heapq.heapreplace(d, -1)      # 先 pop，后 push(item)。弹出值可能大于 item。
# 0


a = range(1, 10, 2)
b = range(2, 10, 2)
[x for x in heapq.merge(a, b)]  # 合并有序序列。
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = a + b
# c.sort()

# 与直接用集合不同
# >>> a = range(10)
# >>> b = range(10)
# >>> [x for x in heapq.merge(a, b)]
# [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
# >>>
# >>> list(set(a) | set(b))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>>



d = random.sample(range(10), 10)
# d
# [9, 0, 3, 4, 5, 6, 1, 2, 8, 7]

heapq.nlargest(5, d)    # 从列表(不一定是堆)有序返回最大的 n 个元素。
[9, 8, 7, 6, 5]

heapq.nsmallest(5, d)    # 有序返回最小的 n 个元素。
[0, 1, 2, 3, 4]




# ------------------------------------------------------------------

# 利用元组 __cmp__，用数字表示对象优先级，实现优先级队列。
import string 
data = map(None, random.sample(xrange(100), 10), random.sample(string.letters, 10))
# data
# [(31, 'Z'),
# (71, 'S'),
# (94, 'r'),
# (65, 's'),
# (98, 'B'),
# (10, 'U'),
# (8, 'u'),
# (25, 'p'),
# (11, 'v'),
# (29, 'i')]

for item in data: 
    heapq.heappush(heap, item)
# heap
# [(8, 'u'),
# (11, 'v'),
# (10, 'U'),
# (25, 'p'),
# (29, 'i'),
# (94, 'r'),
# (31, 'Z'),
# (71, 'S'),
# (65, 's'),
# (98, 'B')]

while heap: 
    print heapq.heappop(heap)
# (8, 'u')
# (10, 'U')
# (11, 'v')
# (25, 'p')
# (29, 'i')
# (31, 'Z')
# (65, 's')
# (71, 'S')
# (94, 'r')
# (98, 'B')


>>> sorted(data, key=lambda result: result[0])
[(1, 'n'), (24, 'Y'), (29, 'x'), (43, 'N'), (53, 'j'), (71, 'z'), (74, 'q'), 
(85, 'i'), (86, 'a'), (87, 'A')]
>>>

>>> sorted(data, key=lambda result: result[1])
[(87, 'A'), (43, 'N'), (24, 'Y'), (86, 'a'), (85, 'i'), (53, 'j'), (1, 'n'), 
(74, 'q'), (29, 'x'), (71, 'z')]
>>>