# FlappyBirdAI
This project is a wonderful application of the ***Genetic Algorithm*** which is a topic in 3rd year course **Optimization Methods in Engineering** of my B.Tech programme.
<br/>

## Description
Created a basic functional Flappy Bird Game and trained the AI birds using the ***Genetic Algorithm*** from **NEAT (NeuroEvolution of Augmenting Topologies)** Framework.
The best evolved AI bird after training can then be stored and used to play the game by itself.
<br/>

## Modules Used
* ***NEAT (NeuroEvolution of Augmenting Topologies)*** Framework for implementation of **Genetic Algorithm**
* ***Pygame*** to construct the game
* ***Pickle*** to serialize and de-serialize python objects and store them in file

## Methodology
1. Train and allow the AI Birds to evolve over Generations using the Genetic Algorithm from NEAT Framework
2. Store the best performed AI Bird which reaches the sufficient Fitness Threshold or Score in a *.pickle* file
3. Use the best evolved and stored AI bird to play the game

## Training the AI Birds
Take a look at the video at the end of this README file to see how the birds are being trained over generations using the built-in Genetic Algorithm in NEAT Framework.<br/>

  
## AI playing the game
Now, take a look at the best evolved AI bird playing the game all by itself perfectly.<br/>
[*Click here to view the best evolved AI Bird play the game*](https://www.youtube.com/watch?v=NecLPV8-MXU&list=PL2-kFUJJfnYCEXIVPzlZN53putIU-oVP2&index=2)
<br/>

## Open the Project in GitPod
Simply change the  ***training***  boolean variable in line 12 of  ***flappy_bird.py***  python script to switch between the training and AI Game Play modes.<br/>
Click the button below to open the project in cloud-based development environment (GitPod).<br/><br/>
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/SaiPrakashGit/FlappyBirdAI/blob/main/flappy_bird.py)<br/>
<video src="https://user-images.githubusercontent.com/75234723/169683424-ffd7a329-0870-4328-8289-30d56f5b426d.mp4">
