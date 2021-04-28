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
    print ("here")
    
    total_shares_i = tachyon_shares_i + founders_shares_i + others_shares_i
    
    others_amount = round_amount - tachyon_amount
    pps = pre_money_amount/total_shares_i
    founders_shares_f = founders_shares_i
    others_shares_f = others_amount/pps+others_shares_i
    tachyon_shares_f = tachyon_amount/pps+tachyon_shares_i
    total_shares_f = (tachyon_shares_f + founders_shares_f + others_shares_f)/(1-ESOP)
    ESOP_shares_f = ESOP*total_shares_f+ESOP_shares_i
    
    post_money_amount = (pre_money_amount+round_amount)/1000000
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
    print ("post-money valuation ($M)")
    print (post_money_amount)
    
    return np.array([cap_table_array, price_array, post_money_amount])
    #cap_table_array, round_data_array
    
    
def Create_Round_Array(Pre_money_matrix, Size_matrix, Tachyon_matrix, Pool_matrix, path, N_Round):
  
##  Round_data_matrix = np.concatenate((Pre_money_matrix[:,path[0]],Size_matrix[:,path[1]],Tachyon_matrix[:,path[2]], Pool_matrix),axis=1)
    Scenario = path[N_Round]
    Round_data_array = np.array((Pre_money_matrix[N_Round,Scenario],
                                        Size_matrix[N_Round,Scenario],
                                        Tachyon_matrix[N_Round,Scenario],
                                        Pool_matrix[N_Round]))
    print ("N_Round, Scenario")
    print (N_Round)
    print (Scenario)
    print ("Round_data_array")
    print (Round_data_array)
    return Round_data_array
    
    
## INPUT MATRICES
    
    
Prob_Matrix = np.array([[0.7,0.2,0.1],#seed - high, medium, low
                        [0.7,0.2,0.1],#A
                        [0.7,0.2,0.1],#B
                        [0.7,0.2,0.1],#C
                        [0.7,0.2,0.1],#D
                        [0.7,0.2,0.1]])#exit


#Round_data_matrix_2 = np.array([[[12,5,0,0.1],[5,2,0,0.1],[2,0.5,0,0.1]],#seed - high, medium, low
#                              [[25,15,0,0.1],[15,8,0,0.1],[8,4,0,0.1]],#A
#                              [[75,25,0,0.1],[40,20,0,0.1],[25,8,0,0.1]],#B
#                              [[250,75,0,0.1],[120,30,0,0.1],[75,25,0,0.1]],#C
#                              [[500,150,0,0.1],[250,75,0,0.1],[150,75,0,0.1]],#D
#                              [[1000,0,0,0.1],[500,0,0,0.1],[250,0,0,0.1]]])#exit
                              

                              
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
                              
print ("pre_money matrix")
print (Pre_money_matrix)

                              
Size_matrix = np.matrix([[4,1.5,0.6],#seed - high, medium, low
                        [15,10,4],#A
                        [20,15,6],#B
                        [40,25,10],#C
                        [40,20,10]])#D
                        

print ("Size_matrix")
print (Size_matrix)
                              
Pool_matrix = np.matrix([[0.1],#seed - high, medium, low
                              [0.1],#A
                              [0.1],#B
                              [0.1],#C
                              [0.1]])#D
                   
print ("Pool_matrix")                   
print (Pool_matrix)

Tachyon_matrix = np.matrix([[0.2,0,0],#seed - high, medium, low
                              [2,2,0],#A
                              [2,2,0],#B
                              [0,0,0],#C
                              [0,0,0]])#D
                              
print ("Tachyon_matrix")                   
print (Tachyon_matrix)
                              
path = np.array([0,0,0,0,0,0])#0=high, 1=medium, 2=low

print ("path: 0=high, 1=medium, 2=low")
print("seed, seriesA, seriesB, seriesC, seriesD, exit")
print (path)



print ("************")
print ("************")
print ("Seed Round")
cap_table_array = np.array([1000000,0,0,0],dtype='i') #founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f
print ("Cap table array")
print (cap_table_array)
#print(Pre_money_matrix[path[0],0])
#print(Size_matrix[path[1],0])
#print(Tachyon_matrix[path[2],0])

#print (Pool_matrix[0].size)


N_Round = 0 #Seed=0,A=1,B=2,C=3,D=4,Exit=5

Seed_round_data_array = Create_Round_Array(Pre_money_matrix, Size_matrix, Tachyon_matrix, Pool_matrix, path, N_Round)

print ("Seed round array")
print (Seed_round_data_array)                                        
                              
#Round_data_matrix[0] #pre_money_amount, round_amount, tachyon_amount_i, ESOP

Seed_array = funding_round(cap_table_array,Seed_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (Seed_array[0])
print ("price data: PPS, dilution")
print (Seed_array[1])
print ("post-money valuation")
print (Seed_array[2])


print ("************")
print ("************")
print ("Series A")
N_Round = 1
SeriesA_round_data_array = Create_Round_Array(Pre_money_matrix, Size_matrix, Tachyon_matrix, Pool_matrix, path, N_Round)

SeriesA_array = funding_round(Seed_array[0],SeriesA_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesA_array[0])
print ("price data: PPS, dilution")
print (SeriesA_array[1])

print ("************")
print ("************")

print ("Series B")
N_Round = 2
SeriesB_round_data_array = Create_Round_Array(Pre_money_matrix, Size_matrix, Tachyon_matrix, Pool_matrix, path, N_Round)
SeriesB_array = funding_round(SeriesA_array[0],SeriesB_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesB_array[0])
print ("price data: PPS, dilution")
print (SeriesB_array[1])

print ("************")
print ("************")

print ("Series C")
N_Round = 3
SeriesC_round_data_array = Create_Round_Array(Pre_money_matrix, Size_matrix, Tachyon_matrix, Pool_matrix, path, N_Round)
SeriesC_array = funding_round(SeriesB_array[0],SeriesC_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesC_array[0])
print ("price data: PPS, dilution")
print (SeriesC_array[1])


print ("************")
print ("************")


print ("Series D")
N_Round = 4
SeriesD_round_data_array = Create_Round_Array(Pre_money_matrix, Size_matrix, Tachyon_matrix, Pool_matrix, path, N_Round)
SeriesD_array = funding_round(SeriesC_array[0],SeriesD_round_data_array)
print ("cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
print (SeriesD_array[0])
print ("price data: PPS, dilution")
print (SeriesD_array[1])

#Series Seed, Series A, Series B, Series C, Series D, Exit
#High
#Medium
#Low


