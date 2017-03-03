num=input()
try:
    num=int(num)
    if num>0:
        return num[::-2]
    if num<0:
        return 0
    if num==0:
        return 0
except typeerror():
    return string input
