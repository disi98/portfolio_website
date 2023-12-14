import pandas as pd
import random
import numpy as np

data1 = {
    'Layout_x': [0, 504, 1008, 252, 756, 1260, 0, 504, 1008, 1512],
    'Layout_y': [0, 0, 0, 252, 252, 252, 504, 504, 504, 504]
}
Population1 = pd.DataFrame(data1)

data2 = {
    'Layout_x': [0, 378, 756, 252, 630, 1008, 0, 378, 756, 1134],
    'Layout_y': [0, 0, 0, 252, 252, 252, 504, 504, 504, 504]
}
Population2 = pd.DataFrame(data2)

data3 = {
    'Layout_x': [0, 630, 1260, 315, 945, 1575, 0, 630, 1260],
    'Layout_y': [0, 0, 0, 630, 630, 630, 1260, 1260, 1260]
}
Population3 = pd.DataFrame(data3)

populations = [Population1, Population2, Population3]


def calculate_fitness(df, target_coverage_area, turbine_diameter):
    total_coverage_area = sum(np.pi * (turbine_diameter / 2)**2 for _ in range(len(df)))
    fitness = total_coverage_area / target_coverage_area
    return fitness

def tournament_selection(populations, tournament_size, target_coverage_area, turbine_diameter):
    tournament_dataframes = random.sample(populations, tournament_size)
    winner = max(tournament_dataframes, key=lambda df: calculate_fitness(df, target_coverage_area, turbine_diameter))
    return winner

def crossover(parent1, parent2):
    child = parent1.copy()
    for column in child.columns:
        child[column] = np.where(np.random.rand(len(child)) < 0.5, parent1[column], parent2[column])
    return child

def mutate(df, mutation_rate):
    for column in df.columns:
        df[column] = np.where(np.random.rand(len(df)) < mutation_rate, np.random.rand(len(df)), df[column])
    return df

def next_generation(populations, tournament_size, target_coverage_area, turbine_diameter, mutation_rate):
    next_gen = []
    for _ in range(len(populations)):
        parent1 = tournament_selection(populations, tournament_size, target_coverage_area, turbine_diameter)
        parent2 = tournament_selection(populations, tournament_size, target_coverage_area, turbine_diameter)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        next_gen.append(child)
    return next_gen

# Initialize parameters
tournament_size = 3
target_coverage_area = 800000
turbine_diameter = 100
mutation_rate = 0.01

# Create a list of DataFrames
populations = [Population1, Population2, Population3]

# Evolve the generation
for i in range(100):
    populations = next_generation(populations, tournament_size, target_coverage_area, turbine_diameter, mutation_rate)

# Get the best layout
best_layout = max(populations, key=lambda df: calculate_fitness(df, target_coverage_area, turbine_diameter))
print(best_layout)

import matplotlib.pyplot as plt

def plot_layout(df):
    plt.figure(figsize=(10, 10))
    plt.scatter(df['Layout_x'], df['Layout_y'], c='b', s=200)
    plt.title('Wind Farm Layout')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.show()

# Plot the best layout
# best_layout = max(populations, key=lambda df: calculate_fitness(df, target_coverage_area, turbine_diameter))
# plot_layout(best_layout)

plot_layout(best_layout)
