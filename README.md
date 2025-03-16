# Flappy Bird AI - NEAT Algorithm

## Overview
This project implements an AI that learns to play **Flappy Bird** using the **NEAT (NeuroEvolution of Augmenting Topologies) algorithm**. The AI evolves over multiple generations, improving its ability to navigate through pipes and survive longer.

## Features
- Uses **NEAT algorithm** for evolving neural networks.
- Starts with an initial population of 100 birds.
- Implements **crossover** between high-performing birds.
- Neural networks mutate and evolve over generations.
- Visual representation of AI learning progress.

## Installation
To run this project, make sure you have Python installed along with the required dependencies.

### Install Dependencies
```bash
pip install pygame neat-python
```
## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flappy-bird-ai.git
2. Navigate to the project directory:
   ```bash
   cd flappy-bird-ai
3. Run the main script:
   ```bash
   python main.py
## How It Works
- The AI starts with a **random population** of birds.
- Each bird has a neural network that determines its actions (flap or do nothing).
- After each generation, the **best-performing birds** (those that survived the longest) are selected for crossover.
- NEAT handles mutations and adjustments to the network architecture automatically.
- Over time, the AI improves its strategy to navigate the pipes effectively.

## Tweaks & Customization
You can modify **NEAT configuration settings** in the `config-feedforward.txt` file to experiment with different population sizes, mutation rates, and speciation behavior.

## Future Improvements
- Adding **reinforcement learning** as an alternative to NEAT.
- Implementing **different difficulty levels**.
- Enhancing the **visualization of AI progress** over generations.

## Demo
*(Add a link to a demo video or GIF showcasing the AI in action.)*

## Author
**Kshitij Kumar Sona**

## License
This project is open-source and available under the **MIT License**.
