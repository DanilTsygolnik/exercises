def SynchronizingTables(N, ids, salary):
    s_ids = list(ids)
    s_ids.sort()
    s_salary = list(salary)
    s_salary.sort()
    emp_dict = {}
    cnt = 0
    while cnt < N:
        emp_dict[s_ids[cnt]] = s_salary[cnt]
        cnt += 1
    sal_fixed = []
    for id in ids:
        sal_fixed += [emp_dict[id]]
    return sal_fixed
