import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/Adrian/Documents/Data Journalism/Datacamp \
         Lesson Datafiles/')

b_data = np.random.normal(6.7, 0.7, size=1000)

f_data = np.random.normal(7.7, 0.3, size=1000)

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()

emails = np.random.binomial(500, .05, size=10000)

plt.hist(emails)
plt.show()

sunflowers = np.loadtxt('sunflowers.txt')
print(sunflowers)

sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)
print(sunflowers_mean)
print(sunflowers_std)

sunflowers_normal = np.random.normal(13, 1.12, size=5000)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
         label='observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
         label='normal', normed=True)
plt.legend()
plt.show()

experiments = np.random.binomial(200, .10, size=5000)

prob = np.mean(experiments < 20)
print(prob)
