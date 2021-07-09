import random
from player import Player
import numpy as np
from config import CONFIG
from copy import deepcopy
from random import shuffle, choices

class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
        # child: an object of class `Player`
        probability_mutation = 0.05
        mu, sigma = 0, 0.4

        parameters = [child.nn.W1, child.nn.b1, child.nn.W2, child.nn.b2]
        for parameter in parameters:
            for i in range(parameter.shape[0]):
                for j in range(parameter.shape[1]):
                    rand_number = np.random.rand(1,1)
                    if rand_number < probability_mutation:
                        parameter[i][j] += np.random.normal(mu, sigma, [1,1])[0][0]


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # prev_players.sort(key=lambda x: x.fitness, reverse=True)
            # new_players = deepcopy(prev_players)
            # new_players = new_players[: num_players]
            
            # for player in new_players:
            #     self.mutate(player)
                
            # TODO (additional): a selection method other than `fitness proportionate`
            
            carrousel_list = []
            selected_players = []
            for player in prev_players:
                for chance in range(int(player.fitness/100)):
                    carrousel_list.append(player)
            shuffle(carrousel_list)
            step_size = int(len(carrousel_list) / num_players)
            for i in range(num_players):
                selected_players.append(carrousel_list[i*step_size])
            
            # TODO (additional): implementing crossover

            new_players = []
            for child in range(num_players):
                parents = choices(selected_players, k=2)

                child = deepcopy(parents[0])

                child.nn.W1[:, :8] = deepcopy(parents[1].nn.W1[:, :8])
                child.nn.b1[:10, :] = deepcopy(parents[1].nn.b1[:10, :])
                child.nn.W2[:, :10] = deepcopy(parents[1].nn.W2[:, 0:10])
                
                new_players.append(child)
            
            for player in new_players:
                self.mutate(player)
            
            return new_players

    def next_population_selection(self, players, num_players):

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects
        
        # 'top-k method' 
        # players.sort(key=lambda x: x.fitness, reverse=True)
        # return players[: num_players]
        
        # TODO (additional): a selection method other than `top-k`
        # SUS method
        carrousel_list = []
        selected_players = []
        for player in players:
            for chance in range(int(player.fitness/100)):
                carrousel_list.append(player)
        shuffle(carrousel_list)
        step_size = int(len(carrousel_list) / num_players)
        for i in range(num_players):
            selected_players.append(carrousel_list[i*step_size])
        

        # TODO (additional): plotting
        players.sort(key=lambda x: x.fitness, reverse=True)
        min_fitness = players[len(players)-1].fitness
        max_fitness = players[0].fitness
        total_fitness = 0
        for player in players:
            total_fitness += player.fitness
        avg_fitness = total_fitness / len(players)

        with open("fitness_information.txt", "a") as fitness_file:
            fitness_file.write(f"{max_fitness} {avg_fitness} {min_fitness}\n")

        return selected_players


