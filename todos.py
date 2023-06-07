todos = open ('todos.txt', 'a')
print ('put out the trash. ', file=todos)
print ('Feed the cat. ', file=todos)
print ('prepare tax return. ', file=todos)

todos.close()

tasks = open('todos.txt')
for task in tasks:
    print (task)