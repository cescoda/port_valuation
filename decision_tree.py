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
    
    print ("Cap_table_initial: founders, others, tachyon, ESOP")
    print (cap_table_array)
    
    cap_table_array = np.array([founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f],dtype='i')
    price_array = np.array([pps, dilution]) 
  
    print ("Cap_table_final: founders, others, tachyon, ESOP")
    print (cap_table_array)
  
    print ("#pre_money ($M), round_size ($M), tachyon_inv. ($M), ESOP (%)")
    print (round_data_array)
    print ("pps, dilution")
    print (price_array)
    print ("post-money ($M)")
    print (post_money_amount)
    
    return np.array([cap_table_array, price_array, post_money_amount])
    #cap_table_array, round_data_array
    
    
def Create_Round_Array(Post_money_previous, Step_up_matrix, Size_percentage_matrix, Tachyon_matrix, Pool_matrix, path, N_Round):
  
##  Round_data_matrix = np.concatenate((Pre_money_matrix[:,path[0]],Size_matrix[:,path[1]],Tachyon_matrix[:,path[2]], Pool_matrix),axis=1)
    
    Scenario = path[N_Round]
    print (" Scenario (high=0, medium=1,low=2):")
    print (Scenario)
    
    Pre_money = Step_up_matrix[N_Round,Scenario]*Post_money_previous
    Size = Size_percentage_matrix[N_Round,Scenario]*Pre_money/(1-Size_percentage_matrix[N_Round,Scenario])
    Round_data_array = np.array((Pre_money,#Pre_money_matrix[N_Round,Scenario],
                                        Size,#Size_matrix[N_Round,Scenario],
                                        Tachyon_matrix[N_Round,Scenario],
                                        Pool_matrix[N_Round]))

    #print ("Round_data_array = Pre_money, Round_Size, Tachyon_Size, Pool")
    #print (Round_data_array)
    return Round_data_array
    
    

## INPUT MATRICES
    
    
Prob_Matrix = np.array([[0.7,0.2,0.1],#seed - high, medium, low
                        [0.7,0.2,0.1],#A
                        [0.7,0.2,0.1],#B
                        [0.7,0.2,0.1],#C
                        [0.7,0.2,0.1],#D
                        [0.7,0.2,0.1]])#exit

                              
Step_up_matrix = np.matrix([[2,1.5,1],#founding to Seed
                              [4,3,2],#seed to A - high, medium, low
                              [2.5,2,0.7],#A to B
                              [2,1,0.5],#B to C
                              [1.5,1,0.5],#C to D
                              [1.2,1,0.5]])#D to exit
                              
print ("step-up matrix")
print (Step_up_matrix)

Size_percentage_matrix = np.matrix([[0.3,0.3,0.4],#seed - high, medium, low
                              [0.25,0.35,0.45],#A
                              [0.25,0.35,0.45],#B
                              [0.25,0.35,0.45],#C
                              [0.25,0.35,0.45],#D
                               [0,0,0]])#Exit
                              
print ("size percentage matrix")
print (Size_percentage_matrix)

Pre_money_matrix = np.matrix([[10,4,2],#seed - high, medium, low
                              [40,25,15],#A
                              [100,50,35],#B
                              [150,120,75],#C
                              [250,150,100],#D
                              [1000,500,150]]),#Exit
                              
print ("pre_money matrix")
print (Pre_money_matrix)

                              
Size_matrix = np.matrix([[4,1.5,0.6],#seed - high, medium, low
                        [15,10,4],#A
                        [20,15,6],#B
                        [40,25,10],#C
                        [40,20,10],#D
                        [0,0,0],])#Exit
                        

print ("Size_matrix")
print (Size_matrix)
                              
Pool_matrix = np.matrix([[0.1],#seed - high, medium, low
                              [0.1],#A
                              [0.1],#B
                              [0.1],#C
                              [0.1],#D
                              [0]])#Exit
                   
print ("Pool_matrix")                   
print (Pool_matrix)

Tachyon_matrix = np.matrix([[0.2,0,0],#seed - high, medium, low
                              [2,2,0],#A
                              [2,2,0],#B
                              [0,0,0],#C
                              [0,0,0],#D
                              [0,0,0]])#Exit
                              
print ("Tachyon_matrix")                   
print (Tachyon_matrix)

Round_name = np.array(["Seed", "Series A", "Series B", "Series C", "Series D", "Exit"])
print ("Round_names")
print (Round_name)
                              
path = np.zeros(6)#0=high, 1=medium, 2=low

total_paths = np.power(3,6)
print (total_paths)
Tachyon_inv_matrix = np.zeros(shape=(total_paths,6))
Tachyon_value_matrix = np.zeros(shape=(total_paths,6))
Tachyon_multiple_matrix = np.zeros(shape=(total_paths,6))



path_number = 0

for x0 in range(0,2):
  for x1 in range(0,2):
    for x2 in range (0,2):
      for x3 in range (0,2):
        for x4 in range (0,2):
            for x5 in range (0,2):
              path = np.array([x0,x1,x2,x3,x4,x5])
              print (" ")
              print (" ")
              print ("*************************************   NEW PATH *********")
              print ("path: 0=high, 1=medium, 2=low")
              print(x0,x1,x2,x3,x4,x5)
              
              cap_table_array = np.array([1000000,0,0,0],dtype='i') #founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f
              print ("Initial cap table (# shares): Founders, Others, Tachyon, Pool")
              print (cap_table_array)

              N_Round = 0 #Seed=0,A=1,B=2,C=3,D=4,Exit=5
              Post_money_previous = 2 #pre-seed post-money valuation
              tachyon_inv = 0
              print ("Initial Valuation - Pre-seed ($M)")
              print (Post_money_previous)
              
              Tachyon_inv_array = np.zeros(6)
              Tachyon_value_array = np.zeros(6)
              Tachyon_multiple_array = np.zeros(6)
              
              while N_Round < 6:
                print (" ")
                print ("************************************")
                print ("Round")
                print (N_Round, Round_name[N_Round])
                round_data_array = Create_Round_Array(Post_money_previous, Step_up_matrix, Size_percentage_matrix, Tachyon_matrix, Pool_matrix, path, N_Round)
                Round_array = funding_round(cap_table_array,round_data_array)
                #print ("ending cap table: founders_shares_f, others_shares_f, tachyon_shares_f, ESOP_shares_f")
                #print (Round_array[0])
                #print ("round price data: PPS, dilution")
                #print (Round_array[1])
                #print ("post-money valuation")
                #print (Round_array[2])
                Post_money_previous = Round_array[2]
                cap_table_array = Round_array[0]
                tachyon_inv = tachyon_inv + round_data_array[2]
                Tachyon_inv_array[N_Round] = tachyon_inv
                print ("Tachyon Return ($M)")
                tachyon_inv_value = Round_array[0][2]*Round_array[1][0]/1000000
                print (tachyon_inv_value)
                print ("Tachyon multiple")
                tachyon_multiple = tachyon_inv_value/tachyon_inv
                print (tachyon_multiple)
                Tachyon_value_array[N_Round] = tachyon_inv_value
                Tachyon_multiple_array[N_Round] = tachyon_multiple
                N_Round +=1
              
              print ("path")
              print (path)
              print ("tachyon cumulative invested amount")
              print (Tachyon_inv_array)
              print ("tachyon value array")
              print (Tachyon_value_array)
              print ("tachyon multiple array")
              print (Tachyon_multiple_array)
              
              Tachyon_inv_matrix[path_number,:] = Tachyon_inv_array
              Tachyon_value_matrix[path_number,:] = Tachyon_value_array
              Tachyon_multiple_matrix[path_number,:] = Tachyon_multiple_array
              
              path_number =+ 1
              
              





