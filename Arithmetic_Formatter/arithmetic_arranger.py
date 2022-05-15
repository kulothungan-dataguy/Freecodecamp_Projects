def arithmetic_arranger(problems,boo=False):
    flag = 0
    a=[]
    b=[]
    c=[]
    i1 = ''
    i2 = ''
    i3 = ''
    i4 = ''
    if len(problems) > 5 :
        flag = 1
        arranged_problems = 'Error: Too many problems.'
    if flag == 0 :
        for p in problems:
            n = p.split()
            a.append(n[0])
        for p in problems:
            n = p.split()
            b.append(n[1])
        for p in problems:
            n = p.split()
            c.append(n[2])
        for k in b:
            if (k != '+') and (k != '-'):
                flag = 1
                arranged_problems = "Error: Operator must be '+' or '-'."

    digits = a + c
    if flag == 0 :
        for i in range(len(digits)):
            if digits[i].isdigit() != True:
                flag = 1
                arranged_problems = 'Error: Numbers must only contain digits.'


    if flag == 0 :
        for i in range(len(digits)):
            if len(digits[i]) > 4:
                flag = 1
                arranged_problems = 'Error: Numbers cannot be more than four digits.'
    if flag == 0 :
        for i in range(len(problems)-1):
            t = max(len(a[i]),len(b[i]),len(c[i]))
            t = t + 2
            i1 = i1 + ' '*(t-len(a[i]))+a[i]+'    '
            i2 = i2 + b[i]+' '*(t-len(c[i])-1)+c[i]+'    '
            i3 = i3 + '-'*t+'    '
        t = max(len(a[len(problems)-1]),len(b[len(problems)-1]),len(c[len(problems)-1]))
        t=t+2
        i1 = i1 + ' '*(t-len(a[len(problems)-1]))+a[len(problems)-1]+ '\n'
        i2 = i2 + b[len(problems)-1]+' '*(t-len(c[len(problems)-1])-1)+c[len(problems)-1]+ '\n'
        i3 = i3 + '-'*t
        arranged_problems = i1  + i2 + i3
        if boo == True:
            i3 = i3 + '\n'
            for i in range(len(problems)-1):
                t = max(len(a[i]),len(b[i]),len(c[i]))
                t = t + 2
                if b[i]=='+':
                    r = str(int(a[i]) + int(c[i]))
                    i4 = i4 + " " * (t-len(r)) + (str(int(a[i]) + int(c[i])))+'    '
                else:
                    r = str(int(a[i]) - int(c[i]))
                    i4 = i4 + " " * (t-len(r)) + (str(int(a[i]) - int(c[i])))+'    '
            t = max(len(a[len(problems)-1]),len(b[len(problems)-1]),len(c[len(problems)-1]))
            t=t+2
            if b[len(problems)-1]=='+':
                r = str(int(a[len(problems)-1]) + int(c[len(problems)-1]))
                i4 = i4 + " " * (t-len(r)) + (str(int(a[len(problems)-1]) + int(c[len(problems)-1])))
            else:
                r = str(int(a[len(problems)-1]) - int(c[len(problems)-1]))
                i4 = i4 + " " * (t-len(r)) + (str(int(a[len(problems)-1]) - int(c[len(problems)-1])))
            arranged_problems = i1  + i2 + i3 + i4


    return arranged_problems
