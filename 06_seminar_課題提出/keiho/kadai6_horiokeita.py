#課題1
a=['m','c','i','e','p','r','e','t','o','','o','o','i','s','g','o','p']
b=['a','h','n','','e','c','p','i','n','r','b','t','c','-','r','u','!']

text=[x + y for x,y in zip(a,b)]

#for ch in text:
   #print(ch,end="")

print(text)

#課題2
import numpy as np
import scipy.stats

math=np.array([40,15,72,22,43,82,75,7,34,49,95,75,85,47,63])

Pass = sum([i >= 70 for i in math])
Pass

Z = scipy.stats.zscore(math)
Z

#課題3
import matplotlib.pyplot as plt
import numpy as np
def sigmoid(x):
 return 1 / (1 + np.exp(-x))
def softmax(x):
 return np.exp(x) / np.sum(np.exp(x))

x = np.arange(-5.0, 5.0, 0.1)
sig = sigmoid(x)
soft = softmax(x)
tanh = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

plt.plot(x,sig,label="sigmoid")
plt.plot(x,soft,label="softmax")
plt.plot(x,tanh,label="tanh")

plt.plot(x, y)
plt.ylim(-1.2, 1.2)

plt.title("graph")

plt.grid()
plt.legend()

plt.show()