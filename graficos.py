import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [1.500,1300,2100,4560,5678,4300]
plt.plot (x,y)
plt.show()

legenda = ['Jan','Fev','Março','Abril','Maio','junho']
plt.xticks (x,legenda)
plt.plot(x,y)
plt.show