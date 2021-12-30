'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

def addTwoNumbers(l1, l2):
    while len(l1) != len(l2): # Make the lists the same length.
        min(l1,l2).append(0)
    prevNum = 0
    for idx, num in enumerate(l1):
        if prevNum >= 10:
            num += 1
        if num + l2[idx] >= 10:
            l1[idx] = num + l2[idx] - 10
        else:
            l1[idx] = num + l2[idx]
        prevNum = num + l2[idx]
    if prevNum >= 10:
        l1.append(1)
    print(l1)
    return l1

print(addTwoNumbers([2,4,3], [5,6,4]) == [7,0,8])
print(addTwoNumbers([0],[0]) == [0])
print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]) == [8,9,9,9,0,0,0,1])