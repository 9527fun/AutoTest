def deleteDuplication(self, pHead):
    if pHead == None:
        return 0
    preHead = None
    pNode = pHead
    while pNode != None:
        needDelete = False
        nextNode = pNode.next
        if nextNode != None and nextNode.val == pNode.val:
            needDelete = True
        if needDelete == False:
            preHead = pNode
            pNode = pNode.next
        else:
            nodeVal = pNode.val
            pToBeDel = pNode
            while pToBeDel != None and pToBeDel.val == nodeVal:
                pToBeDel = pToBeDel.next

            if preHead == None:
                pHead = pToBeDel
                pNode = pToBeDel
                continue
            else:
                preHead.next = pToBeDel
            pNode = preHead
    return pHead













