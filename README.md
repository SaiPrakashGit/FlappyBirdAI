# FlappyBirdAI
This project is a wonderful application of the ***Genetic Algorithm*** which is a topic in my 3rd year Bachelor's in Technology course **Optimization Methods in Engineering**.

## Description
Created a basic functional Flappy Bird Game and trained the AI birds using the ***Genetic Algorithm*** from **NEAT (NeuroEvolution of Augmenting Topologies)** Framework.
The best evolved AI bird after training can then be stored and used to play the game by itself.

## Modules Used
* ***NEAT (NeuroEvolution of Augmenting Topologies)*** Framework for implementation of **Genetic Algorithm**
* ***Pygame*** to construct the game
* ***Pickle*** to serialize and de-serialize python objects and store them in file

## Methodology
1. Train and allow the AI Birds to evolve over Generations using the Genetic Algorithm from NEAT Framework
2. Store the best performed AI Bird which reaches the sufficient Fitness Threshold or Score in a *.pickle* file
3. Use the best evolved and stored AI bird to play the game

## Training the AI Birds
Take a look at the video below to see how the birds are being trained using the built-in Genetic Algorithm in NEAT Framework.

## AI playing the game
Now, take a look at the best evolved AI bird playing the game all by itself perfectly.