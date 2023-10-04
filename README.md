# The Traveling Salesman Problem (TSP) with Genetic Algorithm

**Imagine you have a set of cities represented by their (x, y) coordinates on a Cartesian plane. The goal is to find the shortest route that visits all these cities exactly once and returns to the starting city. Let's illustrate this with an example:**

- City A: (0, 0)
- City B: (2, 4)
- City C: (5, 2)

**To tackle this problem, I followed these steps:**

1. **Define a Fitness Function and Generate an Initial Population**: First, I defined a fitness function, which is a crucial component of solving the TSP with a genetic algorithm. Next, I generated an initial population of potential solutions, where each solution represents a permutation of the cities.

2. **Develop a Genetic Algorithm**: I then developed a genetic algorithm capable of evolving this population over multiple generations. This algorithm includes fundamental genetic operations:
   - **Selection**: This operation chooses individuals from the population based on their fitness, favoring better-performing routes.
   - **Crossover (Recombination)**: It combines genetic information from selected routes to create offspring, simulating genetic recombination.
   - **Mutation**: Occasionally, random changes are introduced into offspring's routes to diversify the population.

3. **Algorithm Execution**: The genetic algorithm runs for a predetermined number of generations. Throughout this process, the algorithm keeps track of the best individual found, which corresponds to the shortest route discovered.

This approach to the Traveling Salesman Problem with a Genetic Algorithm is a computational technique that mimics the process of natural selection and evolution to discover the optimal or near-optimal route that visits all cities exactly once. It provides a robust and efficient way to solve complex instances of the TSP and is applicable to various real-world scenarios requiring route optimization.


> Necessary matplotlib to make the final graphs
