# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

#used to track a moving object. updating relies on measurements which ALWAYS 
#increase the certainty (decreasing the variance of the resultant gaussian 
#distribution of ie the position of the object)

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
musig = []
for i in range(len(motion)):
    musig = update(mu, sig, measurements[i], measurement_sig)
    mu=musig[0]
    sig=musig[1]
    musig = predict(mu, sig, motion[i], motion_sig)
    mu=musig[0]
    sig=musig[1]
print [mu, sig]
