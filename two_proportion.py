# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:47:45 2023
@author: BRGUBO

Should be installed before the module spicy.stat


Example how to use it:
    
value = Two_proportion(p1, p2, 80 - power(%), 2 (side - 1 or 2))
n= value.sample_size()
print(n)

value = Two_proportion(.2, .1, 80, 2)  --> p1=20%, p2=10%, power=80%, two-sides





This module uses the following formula for the sample size n:

n = (Zα/2+Zβ)2 * (p1(1-p1)+p2(1-p2)) / (p1-p2)2,

where Zα/2 is the critical value of the Normal distribution at α/2 (e.g. for a confidence level of 95%, α is 0.05 and the critical value is 1.96), Zβ is the critical value of the Normal distribution at β (e.g. for a power of 80%, β is 0.2 and the critical value is 0.84) and p1 and p2 are the expected sample proportions of the two groups.

Note: A reference to this formula can be found in the following paper (pages 3-4; section 3.1 Test for Equality).
Wang, H. and Chow, S.-C. 2007. Sample Size Calculation for Comparing Proportions. Wiley Encyclopedia of Clinical Trials.



Confidence level - FLOAT
This reflects the confidence with which you would like to detect a significant 
difference between the two proportions.  If your confidence level is 95%, then this
 means you have a 5% probability of incorrectly detecting a significant
 difference when one does not exist, i.e., a false positive result
 (otherwise known as type I error).

Standard is 95% confidence level

Power - FLOAT
The power is the probability of detecting a signficant difference when one exists.  If your power is 80%, then this means that you have a 20% probability of failing to detect a significant difference when one does exist, i.e.,
 a false negative result (otherwise known as type II error).
Standard is 80% of power => .84


Sample Proportions - INT or FLOAT

The sample proportions are what you expect the results to be. 
This can often be determined by using the results from a previous survey,
 or by running a small pilot study. If you are unsure, use proportions near to 50%,
 which is conservative and gives the largest sample size. Note that this sample size
 calculation uses the Normal approximation to the Binomial distribution.
 If, one or both of the sample proportions are close to 0 or 1 then this
 approximation is not valid and you need to consider an alternative sample size 
 calculation method.



Sample size
This is the minimum sample size for each group to detect whether the
 stated difference exists between the two proportions 
 (with the required confidence level and power). Note that if some people
 choose not to respond they cannot be included in your sample and so if
 non-response is a possibility your sample size will have to be increased
 accordingly. In general, the higher the response rate the better the estimate,
 as non-response will often lead to biases in you estimate.


ONE SIDE or TWO SIDES (INT)

one side = 1      Prop 2 is bigger or smaller then prop 1
two sides = 2     Proportions are different



"""

import scipy.stats as st
      
class Two_proportion:
    
    
#    def __init__(self, p1, p2, z_alfa = 1.96 ,z_beta = 0.84):
     def __init__(self, p1, p2, p_z_alfa = .05, p_z_beta = .2, side=2):
         
                  
        assert isinstance(p1, (int, float)), 'p1 should be Integer or Float'
        assert  p1 > 0 and p1 < 1, 'p1 value should be 0 < and < 1'
        assert isinstance(p2, (int, float)), 'p1 should be Integer or Float'
        assert  p1 > 0 and p2 < 1, 'p1 value should be 0 < and < 1'
        assert isinstance(side, (int)), 'SIDE should be Integer. Valid values: 1 or 2 (defaut)'
        assert  side == 1 or side ==2, 'SIDE should be either 1 or 2.'
        #assert  sidep <= 0  and p2 < 1, 'p1 value should be 0 < and < 1'
        
        self.p1 = p1
        self.p2 = p2
        self.side = side
        self.z_alfa = abs(st.norm.ppf(1-p_z_alfa/self.side))
        self.z_beta = abs(st.norm.ppf(1-p_z_beta))
        
            
        
        
     def sample_size(self, p_lost=0):
        
        z_factor = (self.z_alfa + self.z_beta)**2
        self.n= z_factor * (self.p1 * (1-self.p1) + (self.p2*(1-self.p2))) / (self.p1 - self.p2)**2
        return self.n * (1+p_lost)
    