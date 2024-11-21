Game of Life Kata
-----------------

# Description
The Game of Life kata challenges you to implement Conway's Game of Life, a zero-player cellular automaton, where the next generation of a grid evolves based on a simple set of rules. The game illustrates how complexity can emerge from simplicity and offers a great opportunity to practice software design and test-driven development.

The goal is to simulate the evolution of the grid over multiple generations, adhering to the rules of the game. The kata provides opportunities to explore patterns, scalability, and extendability.

# Objective
Implement the Game of Life with the following functionality:

* Initialize a grid of cells (alive or dead).
* Evolve the grid according to the rules.
* Produce the state of the grid after any number of generations.

The implementation should support flexible grid sizes and optionally account for edge wrapping or custom rules.

# Rules of the Game
* Each cell in the grid can be either alive (1) or dead (0).
* A cell's state in the next generation is determined by its 8 neighbors:
  * Underpopulation: A live cell with fewer than 2 live neighbors dies.
  * Survival: A live cell with 2 or 3 live neighbors survives.
  * Overpopulation: A live cell with more than 3 live neighbors dies.
  * Reproduction: A dead cell with exactly 3 live neighbors becomes alive.

# Requirements
Your solution should:

* Input: Accept an initial grid (2D array) representing the state of each cell (alive or dead).
* Output: Return a grid representing the next generation.
* Include an evolution function that computes the grid state over multiple generations.
* Support both finite and wrapping grids (where edges connect like a torus).
* Allow for optional custom rules (e.g., different neighbor counts for survival or reproduction).

# Constraints
* The grid size can be any finite size.
* Wrapping behavior (on/off) should be configurable.
* The implementation should be efficient for larger grids but prioritize correctness.

# Bonus points
* Custom Rules:
  * Support custom birth/survival conditions to create alternative cellular automata.
* Infinite Grids:
  * Implement a sparse representation for infinite grids.
* Visualisation:
  * Add a simple visualization of the grid using text output, graphics, or animation.