"""
import numpy as np

def roulette_wheel_selection(population):
  
    # Computes the totallity of the population fitness
    population_fitness = sum([chromosome.fitness for chromosome in population])
    
    # Computes for each chromosome the probability 
    chromosome_probabilities = [chromosome.fitness/population_fitness for chromosome in population]
    
    # Selects one chromosome based on the computed probabilities
    return np.random.choice(population p=chromosome_probabilities)




import numpy as np

def roulette_wheel_selection(population):
  
    # Computes the totallity of the population fitness
    population_fitness = sum([chromosome.fitness for chromosome in population])
    
    # Computes for each chromosome the probability 
    chromosome_probabilities = [chromosome.fitness/population_fitness for chromosome in population]
    
    # Making the probabilities for a minimization problem
    chromosome_probabilities = 1 - np.array(chromosome_probabilities)
    
    # Selects one chromosome based on the computed probabilities
    return np.random.choice(population p=chromosome_probabilities)
 
import numpy as np
import random as rand
 
roulette_wheel = np.array((0))
slot_count = 0
 
def init_roul_wheel(value_array):
 
    slot_count = 0
    i=0
    arrsize = value_array.size
    while i < arrsize/2:
        slot_count = slot_count + value_array[2*i+1]
        i = i + 1
    roulette_wheel = np.zeros((slot_count),dtype=np.int)
    #print(roulette_wheel)
    i = 0
 
    while i < arrsize/2:
        rv = value_array[2*i]
        bv = value_array[2*i+1]
        j = 0
        while j<span                 data-mce-type="bookmark"                id="mce_SELREST_start"              data-mce-style="overflow:hidden;line-height:0"              style="overflow:hidden;line-height:0"           ></span><span               data-mce-type="bookmark"                id="mce_SELREST_start"              data-mce-style="overflow:hidden;line-height:0"              style="overflow:hidden;line-height:0"           ></span><span               data-mce-type="bookmark"                id="mce_SELREST_start"              data-mce-style="overflow:hidden;line-height:0"              style="overflow:hidden;line-height:0"           ></span><bv:
            t = rand.randint(0,slot_count-1)
            wheel_alloc = roulette_wheel[t]
            if wheel_alloc == 0:
                roulette_wheel[t] = rv
                j = j + 1
        i = i + 1
    return (roulette_wheel)
 
def spin(rw):
    slot_count = rw.size
    randno = rand.randint(0,10000)
    rot_degree = randno%360
    rot_unit = 360/slot_count
    rol_no = (rot_degree - (rot_degree%(rot_unit)))/rot_unit
    rol_value = rw[int(rol_no)]
    return rol_value    
 
wheel_vector = np.array([10,1,20,2,30,2,40,4,50,5,60,4,70,3,80,2,90,2])
x = init_roul_wheel(wheel_vector)
print (spin(x))
"""
import itertools
#from __future__import division
import numpy as np
import random,pdb
import operator
def roulette_selection(weights):
    sorted_indexed_weights=sorted(enumerate(weights),key=operator.itemgetter(1))
    indices,sorted_weights=zip(*sorted_indexed_weights)
    tot_sum=sum(sorted_indexed_weights)
    prob=[x/tot_sum for x in sorted_weights]
    cum_prob=np.cumsum(prob)
    random_sum=random.random()
    for index_value, cum_prob_value in zip(indices,cum_prob):
        if random_num<cum_prob_value:
            return index_value
xanhdo=[87,3,20]
for i in range(20):
    print(roulette_selection(1))

