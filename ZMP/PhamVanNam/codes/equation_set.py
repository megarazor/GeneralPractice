def solve_set_of_equations():
    print("Enter equations line by line (enter empty line to stop):")
    # Getting equations from keyboard input
    eqs= []
    new_eq= input()
    while(new_eq != ""):
        eqs.append(new_eq)
        new_eq= input()
    eqs_cnt= len(eqs)

    # Getting a list of variables
    vars= []
    for eq in eqs:
        for c in eq:
            if c >= 'a' and c <= 'z':
                if c not in vars:
                    vars.append(c)

    vars_cnt= len(vars)
    vars= sorted(vars)

    # Impossible if there are more variables than equations
    if vars_cnt != eqs_cnt:
        print("Number of variables and number of equations must be the same")
        return

    # Solving using Gaussian Elimination
    # Parse the equations into matrix

    matrix = [[0]* (vars_cnt + 1) for _ in range(vars_cnt)]

    for i in range(eqs_cnt):
        var= '.'
        sole_num= 0
        on_left_side= 1
        sign= 1
        num= 0
        eq= eqs[i]
        eq_len= len(eq)
        for j in range(eq_len):
            c= eq[j]
            if c == '-' or c == '+' or c == '=':
                if j != 0:
                    if eq[j - 1] != '=':
                        if var != '.':
                            if num == 0:
                                num = 1
                            var_index= vars.index(var)
                            matrix[i][var_index]+= on_left_side * sign * num
                        else:
                            sole_num+= sign * on_left_side * num
                        var= '.'
                        num= 0
                        sign= 1                        
                if c == '-':
                    sign= -1
                elif c == '+':
                    sign= 1
                else:
                    on_left_side = -1
            elif c >= 'a' and c <= 'z':
                var= c
            elif c >= '0' and c <= '9':
                num*= 10
                num+= int(c)
        if var != '.':
            if num == 0:
                num = 1
            var_index= vars.index(var)
            matrix[i][var_index]+= on_left_side * sign * num
        else:
            sole_num+= sign * on_left_side * num
        matrix[i][vars_cnt]= -1 * sole_num

    # Turn the matrix into row echelon form

    for col in range(vars_cnt):
        for row in range(col, eqs_cnt):
            if row == col:
                n= matrix[row][col]
                if n == 0:
                    for i in range(row + 1, eqs_cnt):
                        if matrix[i][col] != 0:
                            tmp= matrix[i]
                            matrix[i]= matrix[row]
                            matrix[row]= tmp
                            n= matrix[row][col]
                for i in range(vars_cnt + 1):
                    matrix[row][i]/= n
            else:
                n= matrix[row][col]
                for i in range(vars_cnt + 1):
                    matrix[row][i]-= n * matrix[col][i]

    # Plugging variables to equations

    res= [0] * vars_cnt
    for i in range(vars_cnt - 1, -1, -1):
        n= 0
        for j in range(i + 1, vars_cnt):
            n+= matrix[i][j] * res[j]
        res[i]= matrix[i][vars_cnt] - n

    # Print the results

    for i in range(vars_cnt):
        print("{} = {}".format(vars[i], res[i]))

solve_set_of_equations()