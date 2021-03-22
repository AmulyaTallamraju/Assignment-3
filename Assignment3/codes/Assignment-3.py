import numpy as np 
from scipy.stats import binom

#number of simulations 
simlen = 10000000

#number of articles produced in single simulation(sample space)
n = 10

#probabilty of a defective article occuring
p = 0.6

#binomial distrubution
data_binom = binom.rvs(n,p,size = simlen)

#calculating proabilty for 9 defective articles to be produced

count = 0

for i in range(simlen):
    if data_binom[i] == 6:
        count+=1
prob_sim = count/simlen


#calculating theoretical probabilty using probability mass function
prob_theo = binom.pmf(6,n,p)

cases = ["X=0"]

x = np.arange(len(cases))
plt.bar(x + 0.00, prob_theo, color = 'b', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, prob_sim, color = 'g', width = 0.25, label = 'Sim')
#plt.xlabel('X=0')
plt.ylabel('Probability')
plt.xticks(x  + 0.25/2,['Pr(X=6)'])
plt.legend()
plt.show()
#formatting probabilities to scinetific notation
    
formatted_prob_sim =  format(prob_sim,"e")
formatted_prob_theo =  format(prob_theo,"e")

print("The simulated probabilty is "+formatted_prob_sim)
print("The theorietical probability is "+formatted_prob_theo)