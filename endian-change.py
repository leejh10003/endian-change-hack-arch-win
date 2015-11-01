input_string = input("Input the string you want to change the endian: ")

trim_whitespace = input_string.replace(" ", "")
i = len(trim_whitespace)
ret_string = ""
f = open("changed.txt",'w')
while(i>0):
    ret_string+= trim_whitespace[i-2:i]
    ret_string+= " "
    i-=2
ret_string = ret_string.upper()
f.write("for windows: ")
f.write(ret_string)
ret_string_no_whitespace = ret_string.replace(" ", "");
f.write("\nfor linux: ")
f.write(ret_string_no_whitespace)
print(ret_string)
