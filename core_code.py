cell_list = [[1, 1, 1], [0, 1, 0], [1, 0, 0]]

def live_or_dead(cell_list):
    new_cell_list = [[0,0,0],[0,0,0],[0,0,0]]
    len_y = len(cell_list)
    len_x = len(cell_list[0])
    for i in range(len_x):
        print(i)
        for j in range(len_y):
            # print(cell_list[i][j])
            sum = cell_surround_count(cell_list,i,j)
            print(sum)
            if sum < 2 or sum > 3:
                new_cell_list[i][j] = 0
            elif sum==3:
                new_cell_list[i][j] = 1
            else:
                new_cell_list[i][j] = cell_list[i][j]
    return new_cell_list



def is_on_edge(cell_list,i,j):
    if i < 0:
        i = len(cell_list[0])-1
    elif i > len(cell_list[0])-1:
        i = i-1
    if j < 0:
        j = len(cell_list)-1
    elif j > len(cell_list)-1:
        j = j - 1
    return [i,j]

def cell_surround_count(cell_list,i,j):
    count = 0
    for k in [i-1,i,i+1]:
        for g in [j-1,j,j+1]:
            if k==i and g==j:
                continue
            print(k,g)
            fresh = is_on_edge(cell_list,k,g)
            print(fresh)
            count += cell_list[fresh[0]][fresh[1]]
    return count
a = cell_surround_count(cell_list,1,1)
#a = live_or_dead(cell_list)
print(a)

