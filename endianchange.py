#This Function check string's length of hex string
def stringLengthCheck(str):
    if len(str) % 2 != 0:
        return False
    else:
        return True
#This Function check weather string has character not in Hex string's character range
def charRange(str):
    charset = "0123456789ABCDE"
    for i in str:
        if not i in charset:
            return False
    return True
#This function check exception and do conversion
def endianConversion(str):
    #Remove whitespace and change to uppercase
    trim_whitespace = str.replace(" ", "")
    upper_converted = trim_whitespace.upper()
    #Check exception
    if not(stringLengthCheck(upper_converted) and charRange(upper_converted)):
        return False
    #Do conversion! LOL:)
    else:
        ret_string = ""
        i = len(upper_converted)
        while(i>0):
            ret_string+= upper_converted[i-2:i]
            ret_string+= " "
            i-=2
        return ret_string[0:len(ret_string)-1];
#This function write the result to text file
def writeResult(str):
    f = open("changed.txt",'w')
    f.write("With whitespace: ")
    f.write(str)
    f.write("\nWithout whitespace: ")
    str_removed_whitespace = str.replace(" ","")
    f.write(str_removed_whitespace)
