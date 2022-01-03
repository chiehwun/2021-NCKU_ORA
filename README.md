# Path Planning For Manipulator Based On Metaheuristic Algorithm

[ToC]

## Introduction

In this project, we compared two metaheuristic algorithm for path planning and made a brief conclusion and comments for this project.

### What is Path Planning?

Path planning is commonly used in robotics and manufacturing,

#### Manipulator Forward Kinematics

#### Manipulator Inverse Kinematics

##### Singularity Issues

### What is Metaheuristic Algorithm?

In computer science and mathematical optimization, a metaheuristic is a higher-level procedure or heuristic designed to find, generate, or select a heuristic (partial search algorithm) that may provide a sufficiently good solution to an optimization problem, especially with incomplete or imperfect information or limited computation capacity.[5]

#### Particle Swarm Optimization (PSO)

Particle Swarm Optimization was proposed by Kennedy and Eberhart in 1995 [1]. As mentioned in the original paper, sociobiologists believe a school of fish or a flock of birds that moves in a group “can profit from the experience of all other members”. In other words, while a bird flying and searching randomly for food, for instance, all birds in the flock can share their discovery and help the entire flock get the best hunt. [4]

- Math Expression

  <img src="http://latex.codecogs.com/gif.latex?{{{\bf{v}}_{\bf{i}}} = w{{\bf{v}}_{\bf{i}}} + {c_1}{r_1}\left( {{\bf{pbes}}{{\bf{t}}_{\bf{i}}} - {{\bf{x}}_{\bf{i}}}} \right) + {c_2}{r_2}\left( {{\bf{gbest}} - {{\bf{x}}_{\bf{i}}}} \right)}" />

  <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}_{\bf{i}}} = {{\bf{x}}_{\bf{i}}} + {{\bf{v}}_{\bf{i}}}" />

  <!-- $$
  \left\{ \begin{array}{l}
  {{\bf{v}}_{\bf{i}}} = w{{\bf{v}}_{\bf{i}}} + {c_1}{r_1}\left( {{\bf{pbes}}{{\bf{t}}_{\bf{i}}} - {{\bf{x}}_{\bf{i}}}} \right) + {c_2}{r_2}\left( {{\bf{gbest}} - {{\bf{x}}_{\bf{i}}}} \right)\\
  {{\bf{x}}_{\bf{i}}} = {{\bf{x}}_{\bf{i}}} + {{\bf{v}}_{\bf{i}}}
  \end{array} \right.
  $$ -->

  where

  - <img src="https://render.githubusercontent.com/render/math?math=c_1"> and <img src="https://render.githubusercontent.com/render/math?math=c_2"> are parameters to the PSO algorithm
  - <img src="https://render.githubusercontent.com/render/math?math=r_1"> and <img src="https://render.githubusercontent.com/render/math?math=r_2"> are random numbers between 0 and 1.
  - <img src="https://render.githubusercontent.com/render/math?math=w"> is inertia weight which determines how much should the particle keep on with its previous velocity.
  - <img src="https://render.githubusercontent.com/render/math?math={\bf{pbes}}{{\bf{t}}_{\bf{i}}}"> and <img src="https://render.githubusercontent.com/render/math?math={\bf{gbest}}"> are the positions that gives the best cost function value ever explored by particle i and the whole partlcles respectively.

- Advantages: converge quickly
- Disadvantages: easily trapped into local minimum

#### Beetle Antennae Search (BAS)

This idea was inspired by th nature of the beetles. The beetle explores nearby area randomly using both antennae. Further more, when the antennae in one side detects a higher concentration of odour, the beetle would turn to the direction towards the same side, otherwise, it would turn to the other side.

- Math Expression

  $$
   \left\{ \begin{array}{l}
  {{\bf{x}}_r} = {{\bf{x}}^t} + {d^t}{\bf{b}}\\
  {{\bf{x}}_l} = {{\bf{x}}^t} - {d^t}{\bf{b}}\\
  {{\bf{x}}^t} = {{\bf{x}}^{t - 1}} - {\delta ^t}{\bf{b}}sign\left( {f\left( {{{\bf{x}}_r}} \right) - f\left( {{{\bf{x}}_l}} \right)} \right)
  \end{array} \right.
  $$

  where

  - $d^t$ is the sensing length of antennae corresponding to the exploit ability
  - $\bf{b}$ is a random unit vector

## Experiment

## Result

## Reference

[1] J. Kennedy and R. Eberhart, "Particle swarm optimization, " Proceedings of ICNN'95 - _International Conference on Neural_ Networks, 1995, pp. 1942-1948 vol.4

[2] X. Jiang, S. Li, "BAS: Beetle Antennae Search Algorithm for Optimization Problems, " in arXiv conference, 2017

[3] Y. Cheng, C. Li, S. Li, Z. Li, "Motion Planning of Redundant Manipulator With Variable Joint Velocity Limit Based on Beetle Antennae Search Algorithm, " in _IEEE Access_, vol. 8, pp. 138788-138799, 2020

[4] https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/

[5] https://en.wikipedia.org/wiki/Metaheuristic
