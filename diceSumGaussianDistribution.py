import matplotlib.pyplot as plt
import numpy as np

list2 = []

np.random.seed(3)

for i in range(4000): 
 
 list = []

 for i in range(30):
    rand = np.random.randint(1,7) # dice simulation
    list.append(rand)

 list = np.array(list)
 list2.append(np.sum(list)) # sums in list 2

arr = np.array(list2) # array so plottable and easier to work with

plt.hist(arr,
         bins = range(30,181),
        density=True) # plotting histogram

plt.ylabel("Probability Density of each sum")
plt.xlabel("Sums of the results of rolling 30 dice")

x = np.linspace(30, 180, 500) # generating array of x values for gaussian distribution line

mu = 105 # theoretical mean
sigma = np.sqrt(30*(35/12)) # theoretical standard deviation

pdf = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-(x - mu)**2 / (2*sigma**2)) # formula for gaussian distribution

plt.plot(x, pdf, color='red', linewidth=2) # plotting line

plt.show()