def expandMacro(parent):
    print "MDT: ", parent.MDT
    print "MNT: ", parent.MNT
    print "PNTAB: ", parent.PNTAB
    print "APTAB: ", parent.APTAB
    print "CALLS: ", parent.calls
    print "EVTAB: ", parent.EVTAB
    ans = ""
    tb1 = str(parent.plainTextEdit_4.toPlainText())
    if len(parent.calls) > 0:
        lines = tb1.split('\n')
        for lineNum in range(len(lines)):
            try:
                probableFuncName = lines[lineNum].split()[0]
                if probableFuncName in parent.MNT and ("MACRO" not in lines[lineNum-1]):
                    toReplace = parent.MDT[parent.MNT.index(probableFuncName)]
                    for APTIND in range(len(parent.APTAB)):
                        for ind in range(len(parent.APTAB[APTIND])):
                            #print "&&&",parent.PNTAB[parent.MNT.index(parent.calls[APTIND])], parent.APTAB[APTIND]
                            toReplace = toReplace.replace(parent.PNTAB[parent.MNT.index(parent.calls[APTIND])][ind] , parent.APTAB[APTIND][ind])
                    toReplace = toReplace.strip().split('\n')
                    lines = lines[:lineNum] +  toReplace + lines[lineNum+1:]
            except:
                continue
        for i in lines:
            ans += (i + "\n")
    else:
        ans = tb1
    return ans
