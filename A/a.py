def calc(a: list) -> tuple:
    s = 0
    max = 0
    for i in a:
        s +=i
        a1 = s/len(a)
        if max<i:
            max = i
    return(a1,max)        
print(calc([2,20]))        