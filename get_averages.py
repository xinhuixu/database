import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(q)    #run SQL query
fObj = open("peeps.csv") 
d=csv.DictReader(fObj)
for k in d:
    p = "INSERT INTO students VALUES ('%s', %s, %s)"%(k['name'], k['age'], k['id'])
    c.execute(p)


q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(q)
fObj = open("courses.csv")
d=csv.DictReader(fObj)
for k in d:
    p = "INSERT INTO courses VALUES ('%s', %s, %s)"%(k['code'], k['mark'], k['id'])
    c.execute(p)

fObj.close()

#==========================================================
# Look up the grades for each student.

cmd = "SELECT name, mark, students.id FROM students, courses WHERE students.id = courses.id"
sel = c.execute(cmd)
d = {}
for record in sel:
    if record[0] not in d: # if the name is not in the dictionary
        d[record[0]] = [[], record[2], 0] # [] is the placeholder for grades, 0 is the placeholder for avg
    d[record[0]][0].append(record[1]) # add an entry... { name : [ [list of grades], id, avg ] }

# Compute average
def average(d):
    for name in d:
        sum =0
        for grade in d[name][0]:
            sum += grade
        d[name][2]  = sum / ( len(d[name][0]) * 1.0 )
        
# Display each students name, id and average.
for name in d:
    print "%s, %d, %f"%(name, d[name][1], d[name][2])

#==========================================================
db.commit() #save changes
db.close()  #close database
