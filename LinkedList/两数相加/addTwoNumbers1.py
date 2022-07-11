# 递归法

class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    total = 0 #当前两个节点之和
    next1 = 0 # 上一位的进位
    res = ListNode() # 结果链表节点，记录头节点
    cur = res # 当前结果节点，用于移动结果链表节点
    while l1 and l2:
      total = l1.val + l2.val + next1  # 当前节点两数相加+前一个进位数
      cur.next = ListNode(total % 10)  # 除余，得到结果位,并创建当前位的节点
      next1 = total / 10  # 进位
      # 移到下一位
      l1 = l1.next
      l2 = l2.next
      cur = cur.next
    # 特殊判断
    while l1:  # l2先走到头
      total = l1.val + next1
      cur.next = ListNode(total % 10)
      next1 = total / 10
      l1 = l1.next
      cur = cur.next
    while l2:  # l1先走到头
      total = l2.val + next1
      cur.next = ListNode(total % 10)
      next1 = total / 10
      l2 = l2.next
      cur = cur.next
    if next1 != 0:  # 两链表都遍历完，仍有进位的情况
      cur.next = ListNode(next1)
    return res.next  # res头节点是空
      
      
