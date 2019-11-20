"""
Explanation:
    
    Given that the data observed is generated by any distribution/model, when we are tasked with finding the mean value it is given by the expected 
    mean value (EMV) which is specified using the formula:
    sum(x*p(x)), where p(x) denotes the prob of occurence of that particular data point.
    The above explanation also factors the case when a distribution experiences skewness. Depending on the occurence of the observed values and their
    contribution to the skewedness of the distribution, the middle value(expected value) shifts value accordingly.
"""

l = [1,1,1,6,6,6] # observed values
n = len(l)
ev=0 # expected value
prob = float(1/n) # prob of occurence of each individual data point observed
for i in l:
    val = i * prob
    ev+=val
print(ev)