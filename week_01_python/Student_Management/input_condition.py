def numCheck_withoutError(num):
    num = num.strip()
    if len(num)>0 and num.isnumeric():
        num = int(num)
        return num


def numCheck_withError(num):
    num = num.strip()
    if len(num)>0 and num.isnumeric():
        num = int(num)
        return num
    elif len(num)>0 and num.replace(".","").isnumeric() and "." in num:
        num = float(num)
        return num
    else:
        raise Exception
    
def numCheck_withError2(num):
    num = num.strip()
    if len(num)>0 and num.isnumeric():
        num = int(num)
        return num
    else:
        raise Exception
    
def strCheck_withError(str1):
    str1 = str1.strip()
    if len(str1) >0 :
        return str1
    else:
        raise Exception