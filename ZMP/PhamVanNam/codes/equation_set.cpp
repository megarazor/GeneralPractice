#include <iostream>
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>
#include <algorithm>
using namespace std;

const int EQ_NUM= 100;

int getIndex(char c, char arr[], int size){
    for (int i= 0; i < size; i++){
        if (arr[i] == c){
            return i;
        }
    }
    return -1;
}

void solveSetOfEquations(){
    // Getting equations from keyboard input
    int eqs_cnt= 0;
    string eqs[EQ_NUM];
    cout << "Enter number of equations: " << endl;
    cin >> eqs_cnt;
    for (int i= 0; i < eqs_cnt; i++){
        cout << "Enter equation " << i + 1 << ": " << endl;
        cin >> eqs[i];
    }
    
    // Getting a list of variables
    char vars[EQ_NUM];
    int vars_i= 0;
    for (int i= 0; i < eqs_cnt; i++){
        string eq= eqs[i];
        int len= eq.length();
        for (int j= 0; j < len; j++){
            char c= eq[j];
            if (c >= 'a' && c <= 'z'){
                int index= getIndex(c, vars, vars_i);
                if (index == -1){
                    vars[vars_i++]= c;
                }
            } 
        }
    }
    int vars_cnt= vars_i;    

    // Impossible if there are more variables than equations
    if (eqs_cnt != vars_cnt){
        cout << "Impossible" << endl;
        return;
    }

    // Solving using Gaussian Elimination
    // Allocate a matrix
    float** matrix= (float**) malloc(sizeof(float*) * eqs_cnt);
    for (int i= 0; i < eqs_cnt; i++){
        matrix[i]= (float*) malloc(sizeof(float) * (vars_cnt + 1));
    }

    for (int i= 0; i < eqs_cnt; i++){
        for (int j= 0; j < vars_cnt + 1; j++){
            matrix[i][j]= 0;
        }
    }

    // Parse the equations into matrix

    for (int i= 0; i < eqs_cnt; i++){
        char var= '.';
        string eq= eqs[i];
        int sole_num= 0, on_left_side= 1, sign= 1, num= 0, eq_len= eq.length();        
        for (int j= 0; j < eq_len; j++){
            char c= eq[j];
            if (c == '-' || c == '+' || c == '='){
                if (j != 0){
                    if (eq[j - 1] != '='){
                        if (var != '.'){
                            if (num == 0){
                                num= 1;
                            }
                            int var_index= getIndex(var, vars, vars_cnt);
                            matrix[i][var_index]+= on_left_side * sign * num;
                        }
                        else{
                            sole_num+= sign * on_left_side * num;
                        }
                        var= '.';
                        num= 0;
                        sign= 1;
                    }
                }
                if (c == '-'){
                    sign= -1;
                }
                else if (c == '+'){
                    sign= 1;
                }
                else{
                    on_left_side= -1;
                }
            }
            else if (c >= 'a' && c <= 'z'){
                var= c;
            }
                
            else if (c >= '0' && c <= '9'){
                num*= 10;
                num+= c - '0';
            }  
        }
        if (var != '.'){
            if (num == 0){
                num = 1;
            }
            int var_index= getIndex(var, vars, vars_cnt);
            matrix[i][var_index]+= on_left_side * sign * num;
        }
        else{
            sole_num+= sign * on_left_side * num;
        }
        matrix[i][vars_cnt]= -1 * sole_num;         
        
    }

    // Turn the matrix into row echelon form

    for (int col= 0; col < vars_cnt; col++){
        for (int row= col; row < eqs_cnt; row++){
            if (col == row){
                float n= matrix[row][col];
                if (n == 0){
                    for (int i= row + 1; i < eqs_cnt; i++){
                        if (matrix[i][col] != 0){
                            float temp;
                            for (int j= 0; j < vars_cnt + 1; j++){
                                temp= matrix[i][j];
                                matrix[i][j]= matrix[row][j];
                                matrix[row][j]= temp;
                            }
                            n= matrix[row][col];
                        }                            
                    }
                }
                for (int i= 0; i < vars_cnt + 1; i++){
                    matrix[row][i]/= n;
                }
            }
            else{
                float n= matrix[row][col];
                for (int i= 0; i < vars_cnt + 1; i++){
                    matrix[row][i]-= n * matrix[col][i];
                }
            }
        }
    }

    // Plugging variables to equations

    float* res= (float*) malloc(sizeof(float) * vars_cnt);
    for (int i= vars_cnt - 1; i >= 0; i--){
        float n= 0;
        for (int j= i + 1; j < vars_cnt; j++){
            n+= matrix[i][j] * res[j];
        }            
        res[i]= matrix[i][vars_cnt] - n;
    }
        
    // Print the results

    for (int i= 0; i < vars_cnt; i++){
        printf("%c = %f\n", vars[i], res[i]);
    }
}

int main(){
    solveSetOfEquations();
    return 0;
}