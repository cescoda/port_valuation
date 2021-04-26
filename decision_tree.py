from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate

def funding_round(founders_shares_i, others_shares_i, tachyon_shares_i, ESOP_shares_i, pre_money_amount, round_amount, tachyon_amount, ESOP):
    #Provide round data

    total_shares_i = tachyon_shares_i + founders_shares_i + others_shares_i
    others_amount = round_amount - tachyon_amount
    pps = pre_money_amount/total_shares_i
    tachyon_shares_f = tachyon_amount/pps+tachyon_shares_i
    post_money_amount = pre_money_amount+round_amount
    others_shares_f = others_amount/pps+others_shares_i
    founders_shares_f = founders_shares_i
    total_shares_f = (tachyon_shares_f + founders_shares_f + others_shares_f)/(1-ESOP)
    ESOP_shares_f = ESOP*total_shares_f+ESOP_shares_i
    dilution = round_amount / (pre_money_amount+round_amount)
        
    return founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f, total_shares_f, pps, dilution
 
    
    

#Seed Round 
stage = "Seed Round"
founders_shares_i=1000000
others_shares_i=0
tachyon_shares_i=0
ESOP_shares_i=0
pre_money_amount=8000000
round_amount=4000000
tachyon_amount=150000
ESOP=0.1
    
founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,total_shares_i,pps,dilution = funding_round(founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,pre_money_amount,round_amount,tachyon_amount,ESOP)
print ("Stage=", stage)
print ("founders_shares=", founders_shares_i)
print ("others_shares=", others_shares_i)
print ("tachyon_shares=", tachyon_shares_i)
print ("ESOP_shares=", ESOP_shares_i)
print ("total_shares=", total_shares_i)
print ("pps=", pps)
print ("dilution=", dilution)


#Series A 
stage = "Series A"
pre_money_amount=25000000
round_amount=10000000

founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,total_shares_i,pps,dilution = funding_round(founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,pre_money_amount,round_amount,tachyon_amount,ESOP)
print ("Stage=", stage)
print ("founders_shares=", founders_shares_i)
print ("others_shares=", others_shares_i)
print ("tachyon_shares=", tachyon_shares_i)
print ("ESOP_shares=", ESOP_shares_i)
print ("total_shares=", total_shares_i)
print ("pps=", pps)
print ("dilution=", dilution)


#Series B 
stage = "Series B"
pre_money_amount=50000000
round_amount=20000000

founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,total_shares_i,pps,dilution = funding_round(founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,pre_money_amount,round_amount,tachyon_amount,ESOP)

print ("Stage=", stage)
print ("founders_shares=", founders_shares_i)
print ("others_shares=", others_shares_i)
print ("tachyon_shares=", tachyon_shares_i)
print ("ESOP_shares=", ESOP_shares_i)
print ("total_shares=", total_shares_i)
print ("pps=", pps)
print ("dilution=", dilution)
