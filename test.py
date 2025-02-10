import numpy as np
import matplotlib.pyplot as plt

# Define the fitness function
def fitness_function(x):
    return x * np.sin(10 * np.pi * x) + 1  # Objective function

# Generate the initial population
def initialize_population(size):
    return np.random.uniform(0, 1, size)  # Random values in range [0,1]

# Selection using tournament selection
def selection(population, fitness, num_parents):
    selected_parents = []
    for _ in range(num_parents):
        i, j = np.random.choice(len(population), 2, replace=False)
        winner = population[i] if fitness[i] > fitness[j] else population[j]
        selected_parents.append(winner)
    return np.array(selected_parents)

# Crossover (single-point crossover)
def crossover(parents):
    offspring = []
    for i in range(0, len(parents), 2):
        if i+1 < len(parents):
            alpha = np.random.rand()
            child1 = alpha * parents[i] + (1 - alpha) * parents[i+1]
            child2 = alpha * parents[i+1] + (1 - alpha) * parents[i]
            offspring.extend([child1, child2])
    return np.array(offspring)

# Mutation (small random change)
def mutation(offspring, mutation_rate=0.1):
    for i in range(len(offspring)):
        if np.random.rand() < mutation_rate:
            offspring[i] += np.random.uniform(-0.05, 0.05)
            offspring[i] = np.clip(offspring[i], 0, 1)  # Ensure it stays in [0,1]
    return offspring

# Genetic Algorithm
def genetic_algorithm(pop_size=20, generations=50):
    population = initialize_population(pop_size)
    best_fitness_history = []

    for gen in range(generations):
        fitness = fitness_function(population)
        best_fitness_history.append(np.max(fitness))

        parents = selection(population, fitness, num_parents=pop_size // 2)
        offspring = crossover(parents)
        offspring = mutation(offspring)

        # Replace population with new offspring
        population = np.concatenate((parents, offspring))

    # Get the best solution
    best_idx = np.argmax(fitness_function(population))
    best_solution = population[best_idx]
    
    # Plot the fitness evolution
    plt.plot(best_fitness_history)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Evolutionary Algorithm Optimization")
    plt.show()

    return best_solution, fitness_function(best_solution)

# Run the algorithm
best_x, best_fitness = genetic_algorithm()
print(f"Best solution found: x = {best_x}, f(x) = {best_fitness}")
