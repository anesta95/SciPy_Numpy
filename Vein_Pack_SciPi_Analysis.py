import os
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import ttest_1samp
from scipy.stats import chi2_contingency


os.chdir('C:/Users/Adrian/Documents/Data Journalism/Datacamp Lesson'
         'Datafiles/')

vein_pack_lifespans = np.loadtxt('vein_pack_lifespans.txt', delimiter=",")

vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test.pvalue)

if vein_pack_test.pvalue < 0.05:
    print("The Vein Pack Is Proven To Make You Live Longer!")
else:
    print("The Vein Pack Is Probably Good For You Somehow!")

artery_pack_lifespans = np.loadtxt('artery_pack_lifespans.txt', delimiter=", ")

package_comparison_results = ttest_ind(vein_pack_lifespans,
                                       artery_pack_lifespans)

print(package_comparison_results.pvalue)

if package_comparison_results.pvalue < 0.05:
    print("The Artery Package guarantees even stronger results!")
else:
    print("The Artery Pack is also a great product!")

iron_contingency_table = [[140, 29], [40, 87], [20, 29]]

_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

if iron_pvalue < 0.05:
    print("The Artery Package Is Proven To Make You Healthier!")
else:
    print("""While We Can't Say The Artery Package Will Help You, I Bet It is
          Nice!""")
