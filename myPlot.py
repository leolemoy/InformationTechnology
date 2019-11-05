import matplotlib.pyplot as plt

ylist = [10,12,34,29,23,0,2,3,4,66]
xlist = ['Caleb', 'Liam', 'Nick', 'Isaac', 'Ed', 'James', 'David', 'John', 'Danny', 'Buddy']

plt.xlabel('This is the X label')
plt.ylabel('This is the Y label')

plt.title('This is the title!')

plt.polar(xlist,ylist)  # s ^ -- x

plt.show()