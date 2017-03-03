num=input()
try:
    num=int(num)
    if num>0:
        return 'positive'
    if num<0:
        return 'negative'
    if num==0:
        return 'zero'
except typeerror():
    return string input
