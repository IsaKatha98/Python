def calculadora (num1, num2, oper):
    res=0

    if oper==1:
        res= num1+num2
    
    elif oper==2:
        res=num1-num2

    elif oper==3:
        res=num1*num2
    
    elif oper==4:
        res= num1/num2

    return res