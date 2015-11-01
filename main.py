from endianchange import endianConversion
from endianchange import writeResult

input_string = str(input("Input the string you want to change the endian: "))
ret_string = endianConversion(input_string)
if ret_string != False:
    writeResult(ret_string)
    print(ret_string)
else:
    print("wrong HEX text!")
