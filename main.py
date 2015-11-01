from endianchange import endianConversion


input_string = input("Input the string you want to change the endian: ")
ret_string = endianConversion(input_string)
writeResult(ret_string)
print(ret_string)
