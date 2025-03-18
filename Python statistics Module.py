"""
#Calculate the  harmonic mea of the given data:
import statistics

#calculate harmonic mean

print(statistics.harmonic_mean([40,60,80]))
print(statistics.harmonic_mean([10,30,50,70,90]))

from pandas.compat import is_platform_power

#import statistics  Libray

import statistics

#calculate average valuse
print (statistics.mean([1, 3, 5, 7, 9, 11, 13]))
print(statistics.mean([1, 3, 5, 7, 9, 11,]))
print(statistics.mean([-11,5.5,-3.4,7.1,-9,22]))


import statistics
#calculate the middle value
print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median([1, 3, 5, 7, 9, 11]))
print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))

import statistics
#calculated the median of grouped continuous data

print(statistics.median_grouped([1, 2, 3, 4]))
print(statistics.median_grouped([1, 2, 3, 4, 5]))
print(statistics.median_grouped([1, 2, 3, 4], 2))
print(statistics.median_grouped([1, 2, 3, 4], 3))
print(statistics.median_grouped([1, 2, 3, 4], 5))
"""
import statistics

#calculate the mode
print(statistics.mode([1, 3, 3, 3, 5, 7, 7 ,9, 11]))
print(statistics.mode([1, 1, 3, -5, 7, -9, 11]))
print(statistics.mode(['red', 'green', 'blue', 'red']))
