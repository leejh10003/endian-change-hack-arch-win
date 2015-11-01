from endianchange import endianConversion
testArray = [["asdf", False],["AbCED", False],["01A3cd", "CD A3 01"],["A3 2D BB","BB 2D A3"]]
testResult = True
for [testCase, result] in testArray:
    caseResult = endianConversion(testCase)
    if caseResult != result:
        testResult = False
        break
