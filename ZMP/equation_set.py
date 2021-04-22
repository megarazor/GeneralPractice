
eqs= []
new_eq= input()
while(new_eq != ""):
    eqs.append(new_eq)
    new_eq= input()

eqs_cnt= len(eqs)
var_cnt= eqs_cnt

vars= []

for eq in eqs:
    for c in eq:
        if c >= 'a' and c <= 'z':
            if c not in vars:
                vars.append(c)
vars= sorted(vars)
matrix = [[0]* (var_cnt + 1) for _ in range(var_cnt)]

for i in range(len(eqs)):
    left= 1
    eq= eqs[i]
    # print("at equation:", eq)
    for j in range(len(eq)):
        if eq[j] >= 'a' and eq[j] <= 'z':
            var= eq[j]    
            sign= 1
            num= 1        
            if j > 1:
                # print("getting num/sign for var {0} mid sentence".format(var))
                # print("before {0}: {1}".format(var, eq[j-1]))
                if eq[j - 1] == '-':
                    sign= -1
                elif eq[j - 1] >= '0' and eq[j - 1] <= '9':
                    # print("got num {0} for var {1}".format(eq[j-1], var))
                    num= int(eq[j - 1])
                    if eq[j - 2] >= '-':
                        sign= -1
            elif j > 0:
                if eq[j - 1] >= '0' and eq[j - 1] <= '9':
                    num= int(eq[j - 1])
                    # print("got num {0} for var {1}".format(num, var))
                elif eq[j - 1] >= '-':
                    sign= -1
            index= vars.index(var)
            # print("sign, num, left:", sign, num, left)

            matrix[i][index]= sign * num * left
            # print("matrix[{0}][{1}]= {2}*{3}*{4}   {5}".format(i, index, sign, num, left, var))
            # print(var, "has factor:", sign * num * left)
        elif eq[j] == '=':
            left= -1
        elif eq[j] >= '0' and eq[j] <= '9':
            sign= 1
            if j < len(eq) - 1:
                if eq[j + 1] < 'a' or eq[j + 1] > 'z':
                    if eq[j - 1] == '-':
                        sign= -1
                    matrix[i][var_cnt]= int(eq[j]) * sign * left * -1
                    # print("matrix[{0}][{1}]= {2}".format(i, var_cnt, eq[j]))
            elif j == len(eq) - 1:
                if eq[j - 1] == '-':
                    sign= -1
                matrix[i][var_cnt]= int(eq[j]) * sign * left * -1
                # print("matrix[{0}][{1}]= {2}".format(i, var_cnt, eq[j]))
    # print()     
            
print(matrix)

for col in range(len(matrix[0]) - 1):
    for row in range(col, len(matrix)):
        if row == col:
            n= matrix[row][col]
            if n == 0:
                for i in range(row + 1, len(matrix)):
                    if matrix[i][col] != 0:
                        tmp= matrix[i]
                        matrix[i]= matrix[row]
                        matrix[row]= tmp
                        n= matrix[row][col]
            for i in range(len(matrix[row])):
                matrix[row][i]/= n
        else:
            n= matrix[row][col]
            for i in range(len(matrix[row])):
                matrix[row][i]-= n * matrix[col][i]

print(matrix)
        
res= [0] * var_cnt
for i in range(len(res) - 1, -1, -1):
    n= 0
    for j in range(i + 1, len(matrix[i]) - 1):
        n+= matrix[i][j] * res[j]
    res[i]= matrix[i][len(matrix[i]) - 1] - n

print(res)