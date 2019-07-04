import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import binom_test
from scipy.stats import chi2_contingency
import os
os.chdir('C:/Users/Adrian/Documents/Data Journalism/Datacamp \
         Lesson Datafiles/')

ages = np.array([32,  34,  29,  29,  22,  39,  38,  37,  38,  36,  30,  26,
                 22, 22])

ages_mean = np.mean(ages)
print(ages_mean)

tstat, pval = ttest_1samp(ages, 30)
print(pval)

week_1 = np.genfromtxt('week1.txt', delimiter="  ", dtype=float)
week2 = np.genfromtxt('week2.txt', delimiter="  ", dtype=float)
week1 = np.insert(week_1, 0, 23.90506824)
week1 = week1[~np.isnan(week1)]
print(week1)
print(week2)
week1_mean = np.mean(week1)
week2_mean = np.mean(week2)
print(week1_mean)
print(week2_mean)
week1_std = np.std(week1)
week2_std = np.std(week2)

tstatistic, pval = ttest_ind(week1, week2)
print(pval)

a = np.genfromtxt("a.csv")
b = np.genfromtxt("b.csv")
c = np.genfromtxt("c.csv")
#c = np.append(c, 42.06368881)
c = c[~np.isnan(c)]
c = np.reshape(c, (30, 5))

a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)

a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)

fstat, pval = f_oneway(a, b, c)
print(pval)

pval1 = binom_test(510, n=10000, p=0.06)
print(pval1)
pval2 = binom_test(590, n=10000, p=0.06)
print(pval2)

X = [[30, 10],
     [35, 5],
     [28, 12],
     [20, 20]]
chi2, pval3, dof, expected = chi2_contingency(X)
print(pval3)
