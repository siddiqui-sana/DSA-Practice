def max_task(tasks):
    tasks_sorted=sorted(tasks,key = lambda kv:kv[1])
    c=1
    prev_task=tasks_sorted[0]
    for i in range(1,len(tasks)):
        if tasks_sorted[i][0]>=prev_task[1]:
            c += 1
            prev_task=tasks_sorted[i]
        else:
            continue
    return c
        
print(max_task([[2,6],[4,6],[7,8],[8,9],[0,1],[3,4]]))
