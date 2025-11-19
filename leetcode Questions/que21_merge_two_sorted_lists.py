# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result=[]
        n,m=len(list1),len(list2)
        i,j=0,0
        while i<n and j<m:
            if list1[i]<list2[j]:
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1
        if(i<n):
            while i<n:
                result.append(list1[i])
                i+=1
        if(j<m):
            while j<m:
                result.append(list2[j])
                j +=1
        return result


# I had written the code corretly but , according to leetcode it is done through linked list so leaving it behind , and will come bak to it when had learned linked list
