from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate

def funding_round(funding_array):
    #Provide round data
    #founders_shares_i, others_shares_i, tachyon_shares_i, ESOP_shares_i, pre_money_amount, round_amount, tachyon_amount, ESOP
    founders_shares_i =funding_array[0]
    others_shares_i=funding_array[1]
    tachyon_shares_i=funding_array[2]
    ESOP_shares_i=funding_array[3]
    pre_money_amount=funding_array[4]
    round_amount=funding_array[5]
    tachyon_amount=funding_array[6]
    ESOP=funding_array[7]

    
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
    
    funding_ar= np.array([founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f]) 
    funding_ar_2=np.array([pps, dilution])
    funding_round_ar = np.array([funding_ar, funding_ar_2])
    print (funding_round_ar[0])
    
    return funding_round_ar
 
 
cap_table = np.array([1000000,0,0,0])
funding_data = np.array([8000000000,4000000,150000,0.1])
funding_array = np.concatenate((cap_table,funding_data))
#funding_round(funding_array)
print (funding_array[0])
funding_round_Seed=funding_round(funding_array)

funding_data_seriesA=



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

Seed_Round=
Seed_Round = (founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,pre_money_amount,round_amount, tachyon_amount, ESOP)
print (Seed_Round)
#A_Round = funding_round(Seed_Round)

    
founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,total_shares_i,pps,dilution = funding_round(founders_shares_i,others_shares_i,tachyon_shares_i,ESOP_shares_i,pre_money_amount,round_amount,tachyon_amount,ESOP)
print ("Stage=", stage)
print ("founders_shares=", founders_shares_i)
print ("others_shares=", others_shares_i)
print ("tachyon_shares=", tachyon_shares_i)
print ("ESOP_shares=", ESOP_shares_i)
print ("total_shares=", total_shares_i)
print ("pps=", pps)
print ("dilution=", dilution)
print ("-----")

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
print ("-----")

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
print ("-----")


