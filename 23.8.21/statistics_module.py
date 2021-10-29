import statistics    
# list of positive integer numbers   
datasets = [5, 2, 7, 4, 2, 6, 8]     
x = statistics.mean(datasets)
y = sum(datasets)/len(datasets)
# Printing the mean   
print("Mean is :", x)  
print("Avg : ", y)

print("Median of data-set is : %s "  %(statistics.median(datasets)))  

print("Calculated Mode % s" % (statistics.mode(datasets)))  

print("Standard Deviation of sample is % s "   
                % (statistics.stdev(datasets)))   