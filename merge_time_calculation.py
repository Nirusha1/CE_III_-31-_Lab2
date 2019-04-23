from merge1 import merge_sort
import random
from time import time
 
print("n                   ", "Time taken")
for i in range(1000,10000,1000):
    randomvalues=random.sample(range(i),i)
    start_time=time()
    merge_sort(randomvalues)
    end_time=time()
    total_time=end_time-start_time
    x=' '
    
    print(i,10*x,total_time)
    
