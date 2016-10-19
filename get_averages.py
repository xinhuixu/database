# Compute and record the average for each student

def average(d):
    for name in d:
        sum = 0
        for grade in d[name][0]:
            sum += grade
        d[name][2] =  sum / ( len(d[name][0]) * 1.0 )
