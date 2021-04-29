N = input()
arr_str = input()
dep_str = input()
N = int(N)
arr_str= arr_str.split(" ")
dep_str= dep_str.split(" ")
times= []
for i in range(len(arr_str)):
    times.append((int(arr_str[i]), int(dep_str[i])))

# print(N)
# print(times)

# sorted= -1
# print(times[0][0])
for i in range(N):
    min = times[i][0]
    min_pos= i
    for j in range(i, N):
        print(type(min))
        print(type(times[j][0]))
        if times[j][0] < min:
            min= times[j]
            min_pos= j
    if min_pos != i:
        tmp= times[i]
        times[i]= times[min_pos]
        times[min_pos]= tmp
    

print(times)
