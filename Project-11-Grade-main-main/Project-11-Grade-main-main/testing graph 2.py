import matplotlib.pyplot as plt

subjects = ['Computer','English','Physics','Chemistry','Biology','Maths','History']
marks = [80,70,60,65,90,80,77]

plt.plot(subjects,marks,label='My marks',marker = 'o', markerfacecolor='yellow',linestyle='dotted')

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks')

plt.show()