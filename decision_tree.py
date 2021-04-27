from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate

def funding_round(cap_table_array, round_data_array):
    #Provide round data
    #founders_shares_i, others_shares_i, tachyon_shares_i, ESOP_shares_i, 
    #pre_money_amount, round_amount, tachyon_amount, ESOP
    
    founders_shares_i = cap_table_array[0]
    others_shares_i = cap_table_array[1]
    tachyon_shares_i = cap_table_array[2]
    ESOP_shares_i = cap_table_array[3]
    pre_money_amount = round_data_array[0]
    round_amount = round_data_array[1]
    tachyon_amount = round_data_array[2]
    ESOP = round_data_array[3]

    
    total_shares_i = tachyon_shares_i + founders_shares_i + others_shares_i
    
    others_amount = round_amount - tachyon_amount
    pps = pre_money_amount/total_shares_i
    founders_shares_f = founders_shares_i
    others_shares_f = others_amount/pps+others_shares_i
    tachyon_shares_f = tachyon_amount/pps+tachyon_shares_i
    total_shares_f = (tachyon_shares_f + founders_shares_f + others_shares_f)/(1-ESOP)
    ESOP_shares_f = ESOP*total_shares_f+ESOP_shares_i
    
    post_money_amount = pre_money_amount+round_amount
    dilution = round_amount / (pre_money_amount+round_amount)
    
    
    cap_table_array = np.array([founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f],dtype='i')
    price_array = np.array([pps, dilution]) 
    print (cap_table_array)
    print (price_array)
    
    return np.array([cap_table_array, price_array])
    #cap_table_array, round_data_array
 
cap_table_array = np.array([1000000,0,0,0],dtype='i') #founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f
Seed_round_data_array = np.array([8000000,4000000,150000,0.1]) #pre_money_amount, round_amount, tachyon_amount_i, ESOP
Seed_array = funding_round(cap_table_array,Seed_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (Seed_array[0])
print ("price data: PPS, dilution")
print (Seed_array[1])

print ("Series A")
SeriesA_round_data_array = np.array([20000000,10000000,0,0.1]) #pre_money_amount, round_amount, tachyon_amount_i, ESOP
SeriesA_array = funding_round(Seed_array[0],SeriesA_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesA_array[0])
print ("price data: PPS, dilution")
print (SeriesA_array[1])


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


