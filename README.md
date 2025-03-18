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

## Snapshots
<div align="center">

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/2e7a4bdb-d272-4fd8-8f7c-2a7530512111" alt="Img1" width="300" style="border:1px solid #ccc; border-radius:10px;"/>
      <br/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/655844a0-a836-47ae-a79e-6524f7a04885" alt="Img2" width="300" style="border:1px solid #ccc; border-radius:10px;"/>
      <br/>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/0f2f65ae-cf03-4160-853d-edc273b481ed" alt="Img3" width="300" style="border:1px solid #ccc; border-radius:10px;"/>
      <br/>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/35122794-8943-4682-afbb-9feeca1c2409" alt="Img4" width="300" style="border:1px solid #ccc; border-radius:10px;"/>
      <br/>
    </td>
  </tr>
</table>

</div>

## Demo
[Watch the Demo](https://drive.google.com/file/d/1mNyq5P5Hm5k3kmofFgcWlmx4erYQlnqW/view?usp=drive_link)
