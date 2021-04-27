from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate

np.set_printoptions(suppress=True)

def funding_round(cap_table_array, round_data_array):
    #Provide round data
    #founders_shares_i, others_shares_i, tachyon_shares_i, ESOP_shares_i, 
    #pre_money_amount, round_amount, tachyon_amount, ESOP
    
    founders_shares_i = cap_table_array[0]
    others_shares_i = cap_table_array[1]
    tachyon_shares_i = cap_table_array[2]
    ESOP_shares_i = cap_table_array[3]
    pre_money_amount = round_data_array[0]*1000000
    round_amount = round_data_array[1]*1000000
    tachyon_amount = round_data_array[2]*1000000
    ESOP = round_data_array[3]
    #print ("ESOP=" round_data_array[3])
    
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
    
    
    print ("founders_shares_i, others_shares_i, tachyon_shares_i, ESOP_shares_i")
    print (cap_table_array)
    print ("#pre_money_amount ($M), round_amount ($M), tachyon_amount ($M), ESOP (%)")
    print (round_data_array)
    
    cap_table_array = np.array([founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f],dtype='i')
    price_array = np.array([pps, dilution]) 
    
    
    
    print ("founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
    print (cap_table_array)
    print ("pps, dilution")
    print (price_array)
    
    return np.array([cap_table_array, price_array])
    #cap_table_array, round_data_array
    
    
    
Prob_Matrix = np.array([[0.7,0.2,0.1],[0.7,0.2,0.1],[0.7,0.2,0.1],[0.7,0.2,0.1],[0.7,0.2,0.1],[0.7,0.2,0.1]])


Round_data_matrix_2 = np.array([[[12,5,0,0.1],[5,2,0,0.1],[2,0.5,0,0.1]],#seed - high, medium, low
                              [[25,15,0,0.1],[15,8,0,0.1],[8,4,0,0.1]],#A
                              [[75,25,0,0.1],[40,20,0,0.1],[25,8,0,0.1]],#B
                              [[250,75,0,0.1],[120,30,0,0.1],[75,25,0,0.1]],#C
                              [[500,150,0,0.1],[250,75,0,0.1],[150,75,0,0.1]],#D
                              [[1000,0,0,0.1],[500,0,0,0.1],[250,0,0,0.1]]])#exit
                              

                              
Step_up_matrix = np.matrix([[4,3,2],#seed to A - high, medium, low
                              [2.5,2,0.7],#A to B
                              [2,1,0.5],#B to C
                              [1.5,1,0.5],#C to D
                              [1.2,1,0.5]]),#D to exit
                              
Pre_money_matrix = np.matrix([[10,4,2],#seed - high, medium, low
                              [40,25,15],#A
                              [100,50,35],#B
                              [150,120,75],#C
                              [250,150,100]])#D
                              #[1000,500,150]]),#Exit
                              
Size_matrix = np.matrix([[4,1.5,0.6],#seed - high, medium, low
                        [15,10,4],#A
                        [20,15,6],#B
                        [40,25,10],#C
                        [40,20,10]])#D
                              
Pool_matrix = np.matrix([[0.1],#seed - high, medium, low
                              [0.1],#A
                              [0.1],#B
                              [0.1],#C
                              [0.1]])#D
                              
Tachyon_matrix = np.matrix([[0.2,0,0],#seed - high, medium, low
                              [2,2,0],#A
                              [2,2,0],#B
                              [0,0,0],#C
                              [0,0,0]])#D
                              
print (Pre_money_matrix.shape)
print (Size_matrix.shape)
print (Pool_matrix.shape)
print (Tachyon_matrix.shape)

Round_data_matrix = np.zeros((5,4))
print (Round_data_matrix)
print (Size_matrix[:,0])
print (Pre_money_matrix[:,0])
print (Tachyon_matrix[:,0])
print (Pool_matrix)
Round_data_matrix = np.concatenate((Size_matrix[:,0],Pre_money_matrix[:,0],Tachyon_matrix[:,0], Pool_matrix),axis=1)

print (Round_data_matrix.shape)
print (Round_data_matrix)

print ("round data matrix")
print (Round_data_matrix[0,0])#Seed - high
print (Round_data_matrix[2,1])#Seed - medium

print ("Seed Round")
cap_table_array = np.array([1000000,0,0,0],dtype='i') #founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f
Seed_round_data_array = Round_data_matrix[0][0] #pre_money_amount, round_amount, tachyon_amount_i, ESOP
Seed_array = funding_round(cap_table_array,Seed_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (Seed_array[0])
print ("price data: PPS, dilution")
print (Seed_array[1])

print ("Series A")
SeriesA_round_data_array = Round_data_matrix[1][0] #pre_money_amount, round_amount, tachyon_amount_i, ESOP
SeriesA_array = funding_round(Seed_array[0],SeriesA_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesA_array[0])
print ("price data: PPS, dilution")
print (SeriesA_array[1])

print ("Series B")
SeriesB_round_data_array = Round_data_matrix[2][0] #pre_money_amount, round_amount, tachyon_amount_i, ESOP
SeriesB_array = funding_round(SeriesA_array[0],SeriesB_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesB_array[0])
print ("price data: PPS, dilution")
print (SeriesB_array[1])

print ("Series C")
SeriesC_round_data_array = Round_data_matrix[3][0] #pre_money_amount, round_amount, tachyon_amount_i, ESOP
SeriesC_array = funding_round(SeriesB_array[0],SeriesC_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesC_array[0])
print ("price data: PPS, dilution")
print (SeriesC_array[1])

print ("Series D")
SeriesD_round_data_array = Round_data_matrix[4][0] #pre_money_amount, round_amount, tachyon_amount_i, ESOP
SeriesD_array = funding_round(SeriesC_array[0],SeriesD_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesD_array[0])
print ("price data: PPS, dilution")
print (SeriesD_array[1])

#Series Seed, Series A, Series B, Series C, Series D, Exit
#High
#Medium
#Low


