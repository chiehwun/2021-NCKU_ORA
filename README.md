# Path Planning For Manipulator Based On Metaheuristic Algorithm

## Outline

- [Introduction](#introduction)
  - [What is Motion Planning?](#what-is-motion-planning)
    - [Forward Kinematics](#forward-kinematics)
  - [What is Metaheuristic Algorithm?](#what-is-metaheuristic-algorithm)
    - [Particle Swarm Optimization (PSO)](#particle-swarm-optimization-pso)
    - [Beetle Antennae Search (BAS)](#beetle-antennae-search-bas)
- [Experiment](#experiment)
- [Result](#result)
- [Conclusion](#conclusion)
- [Reference](#reference)

## Introduction

In this project, we compared two metaheuristic algorithms for path planning and made a brief comment for our experiment.

### What is Motion Planning?

![](https://control.com/uploads/articles/image18.jpg)
Motion planning is commonly used in robotics and manufacturing. For example, industrial robots and CNC machine tools have multiple positioning axes that must move in a coordinated fashion along precisely defined paths to accomplish their program tasks.

#### Forward Kinematics

Forward kinematics performs the transformation from **joint space** to **cartesian space**.

:bulb: Watch [this video](https://youtu.be/rA9tm0gTln8) for more information

### What is Metaheuristic Algorithm?

In computer science and mathematical optimization, a metaheuristic is a higher-level procedure or heuristic designed to find, generate, or select a heuristic (partial search algorithm) that may provide a sufficiently good solution to an optimization problem, especially with incomplete or imperfect information or limited computation capacity. [[1]](#1-httpsenwikipediaorgwikimetaheuristic)

In order to formulate the problem, there exists a function <img src="http://latex.codecogs.com/gif.latex?f(\bf{x})" /> called **Fitness Function** which is a type of objective function to guide the simulations towards optimal design solution.

#### Particle Swarm Optimization (PSO)

Particle Swarm Optimization was proposed by Kennedy and Eberhart in 1995 [[2]](#2-j-kennedy-and-r-eberhart-particle-swarm-optimization--proceedings-of-icnn95---international-conference-on-neural-networks-1995-pp-1942-1948-vol4). As mentioned in the original paper, sociobiologists believe a school of fish or a flock of birds that moves in a group “can profit from the experience of all other members”. In other words, while a bird flying and searching randomly for food, for instance, all birds in the flock can share their discovery and help the entire flock get the best hunt. [[3]](#3-httpsmachinelearningmasterycoma-gentle-introduction-to-particle-swarm-optimization)

**Math Expression for PSO**

- <img src="http://latex.codecogs.com/gif.latex?{{{\bf{v}}_{\bf{i}}} = w{{\bf{v}}_{\bf{i}}} + {c_1}{r_1}\left( {{\bf{pbes}}{{\bf{t}}_{\bf{i}}} - {{\bf{x}}_{\bf{i}}}} \right) + {c_2}{r_2}\left( {{\bf{gbest}} - {{\bf{x}}_{\bf{i}}}} \right)}" />
- <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}_{\bf{i}}} = {{\bf{x}}_{\bf{i}}} + {{\bf{v}}_{\bf{i}}}" />

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

#### Beetle Antennae Search (BAS)

This idea was inspired by th nature of the beetles. The beetle explores nearby area randomly using both antennae. Further more, when the antennae in one side detects a higher concentration of odour, the beetle would turn to the direction towards the same side, otherwise, it would turn to the other side. [[4]](#4-x-jiang-s-li-bas-beetle-antennae-search-algorithm-for-optimization-problems--in-arxiv-conference-2017)

**Math Expression for BAS**

- <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}_r} = {{\bf{x}}^t} + {d^t}{\bf{b}}">
- <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}_l} = {{\bf{x}}^t} - {d^t}{\bf{b}}">
- <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}^t} = {{\bf{x}}^{t - 1}} - {\delta ^t}{\bf{b}}sign\left( {f\left( {{{\bf{x}}_r}} \right) - f\left( {{{\bf{x}}_l}} \right)} \right)">

  <!-- $$
    \left\{ \begin{array}{l}
  {{\bf{x}}_r} = {{\bf{x}}^t} + {d^t}{\bf{b}}\\
  {{\bf{x}}_l} = {{\bf{x}}^t} - {d^t}{\bf{b}}\\
  {{\bf{x}}^t} = {{\bf{x}}^{t - 1}} - {\delta ^t}{\bf{b}}sign\left( {f\left( {{{\bf{x}}_r}} \right) - f\left( {{{\bf{x}}_l}} \right)} \right)
  \end{array} \right.
  $$ -->

where

- <img src="https://render.githubusercontent.com/render/math?math={d^t}"> is the sensing length of antennae corresponding to the exploit ability
- <img src="https://render.githubusercontent.com/render/math?math=\bf{b}"> is a random unit vector

## Experiment

We reproduce parts of the expiriments in paper [[5]](#5-y-cheng-c-li-s-li-z-li-motion-planning-of-redundant-manipulator-with-variable-joint-velocity-limit-based-on-beetle-antennae-search-algorithm--in-ieee-access-vol-8-pp-138788-138799-2020).

### Our Model

<br>
<div align=center>
<img src="https://github.com/chiehwun/2021-NCKU_ORA/blob/main/Final_Project/MyRobot_Model.png" width="400" height="285">
</div>
<br>

- 6 axes

## Result

- PSO

- BAS

## Reference

###### [1] https://en.wikipedia.org/wiki/Metaheuristic

###### [2] J. Kennedy and R. Eberhart, "Particle swarm optimization, " Proceedings of ICNN'95 - _International Conference on Neural Networks_, 1995, pp. 1942-1948 vol.4

###### [3] https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/

###### [4] X. Jiang, S. Li, "BAS: Beetle Antennae Search Algorithm for Optimization Problems, " in arXiv conference, 2017

###### [5] Y. Cheng, C. Li, S. Li, Z. Li, "Motion Planning of Redundant Manipulator With Variable Joint Velocity Limit Based on Beetle Antennae Search Algorithm, " in _IEEE Access_, vol. 8, pp. 138788-138799, 2020
