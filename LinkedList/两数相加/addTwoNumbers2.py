# 递归法

class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    total = l1.val + l2.val  # 当前两个节点之和，l1中包含前一位进位
    res = ListNode(total % 10)  # 当前的节点，因为最浅层会记录res头节点，所以不用新建cur节点
    next1 = total / 10  # 进位
    if l1.val or l2.val or next1 != 0:  # 终止条件判断
      if l1.next:
        l1 = l1.next
      else:
        l1 = ListNode(0)  # l1先走完，创建0节点进入一下层递归
      if l2.next:
        l2 = l2.next
      else:
        l2 = ListNode(0)
      l1.val = l1.val + next1
      res.next = self.addTwoNumbers(l1, l2)
    return res
