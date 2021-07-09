import matplotlib.pyplot as plt
import numpy as np

with open("fitness_information.txt", "r") as fitness_file:
    min_fitness_generations = []
    avg_fitness_generations = []
    max_fitness_generations = []
    
    while True:
        
        information = fitness_file.readline().split()
        try:
            min_fitness_generations.append(information[2])
            avg_fitness_generations.append(information[1])
            max_fitness_generations.append(information[0])
        except IndexError:
            break

generation_list = list(range(1, len(min_fitness_generations)+1))

plt.plot(generation_list, min_fitness_generations, label='Min Fitness')
plt.plot(generation_list, avg_fitness_generations, label='Average Fitness')
plt.plot(generation_list, max_fitness_generations, label='Max Fitness')

plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Learning Curve')
plt.legend()

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=1, color='k')
plt.yticks(np.arange(0, 500, 50))

plt.tight_layout(pad=1, rect=(4, 4, 4, 4))
plt.show()
    
