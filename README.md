# Motion Planning For Manipulator Based On Metaheuristic Algorithm

## Outline

- [Introduction](#introduction)
  - [What is Motion Planning?](#what-is-motion-planning)
    - [Forward Kinematics](#forward-kinematics)
  - [What is Metaheuristic Algorithm?](#what-is-metaheuristic-algorithm)
    - [Particle Swarm Optimization (PSO)](#particle-swarm-optimization-pso)
    - [Beetle Antennae Search (BAS)](#beetle-antennae-search-bas)
- [Experiment](#experiment)
- [Result](#result)
- [Reference](#reference)

## Introduction

In this project, we compared two metaheuristic algorithms with motion planning and made a brief comment for our experiment.

### What is Motion Planning?

![](https://control.com/uploads/articles/image18.jpg)
Motion planning is commonly used in robotics and manufacturing. For example, industrial robots and CNC machine tools have multiple positioning axes that must move in a coordinated fashion along precisely defined paths to accomplish their program tasks.

#### Forward Kinematics

Forward kinematics performs the transformation from **joint space** <img src="http://latex.codecogs.com/gif.latex?{\bf{\theta}}" /> to **cartesian space** <img src="http://latex.codecogs.com/gif.latex?{\bf{p}}"/>. i.e.,

### <img src="http://latex.codecogs.com/gif.latex?F\left( {\bf{\theta }} \right) = {\bf{p}}" />

:bulb: Watch [this video](https://youtu.be/rA9tm0gTln8) for more information

### What is Metaheuristic Algorithm?

In computer science and mathematical optimization, a metaheuristic is a higher-level procedure or heuristic designed to find, generate, or select a heuristic (partial search algorithm) that may provide a sufficiently good solution to an optimization problem, especially with incomplete or imperfect information or limited computation capacity. [[1]](#1-httpsenwikipediaorgwikimetaheuristic)

In order to formulate the problem, there exists a function <img src="http://latex.codecogs.com/gif.latex?f(\bf{x})" /> called **fitness function** which is a type of objective function to guide the simulations towards optimal design solution.

##### In our case, the fitness function was defined as following.

### <img src="http://latex.codecogs.com/gif.latex?f\left( {{\bf{\theta }}(t)} \right) = {\left\| {{{\bf{p}}_{\bf{d}}}(t) - F\left( {{\bf{\theta }}(t)} \right)} \right\|^2}" />

It means the distance between **desired** position and **real** one.

#### Particle Swarm Optimization (PSO)

Particle Swarm Optimization was proposed by Kennedy and Eberhart in 1995 [[2]](#2-j-kennedy-and-r-eberhart-particle-swarm-optimization--proceedings-of-icnn95---international-conference-on-neural-networks-1995-pp-1942-1948-vol4). As mentioned in the original paper, sociobiologists believe a school of fish or a flock of birds that moves in a group “can profit from the experience of all other members”. In other words, while a bird flying and searching randomly for food, for instance, all birds in the flock can share their discovery and help the entire flock get the best hunt. [[3]](#3-httpsmachinelearningmasterycoma-gentle-introduction-to-particle-swarm-optimization)

**Math Expression for PSO**

### <img src="http://latex.codecogs.com/gif.latex?{{{\bf{v}}_{\bf{i}}} = w{{\bf{v}}_{\bf{i}}} + {c_1}{r_1}\left( {{\bf{pbes}}{{\bf{t}}_{\bf{i}}} - {{\bf{x}}_{\bf{i}}}} \right) + {c_2}{r_2}\left( {{\bf{gbest}} - {{\bf{x}}_{\bf{i}}}} \right)}" />

### <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}_{\bf{i}}} = {{\bf{x}}_{\bf{i}}} + {{\bf{v}}_{\bf{i}}}" />

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

This idea was inspired by the nature of the beetles. The beetle explores nearby area randomly using both antennae. Further more, when the antennae in one side detects a higher concentration of odour, the beetle would turn to the direction towards the same side, otherwise, it would turn to the other side. [[4]](#4-x-jiang-s-li-bas-beetle-antennae-search-algorithm-for-optimization-problems--in-arxiv-conference-2017)

**Math Expression for BAS**

### <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}_r} = {{\bf{x}}^t} + {d^t}{\bf{b}}">

### <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}_l} = {{\bf{x}}^t} - {d^t}{\bf{b}}">

### <img src="http://latex.codecogs.com/gif.latex?{{\bf{x}}^t} = {{\bf{x}}^{t - 1}} - {\delta ^t}{\bf{b}}sign\left( {f\left( {{{\bf{x}}_r}} \right) - f\left( {{{\bf{x}}_l}} \right)} \right)">

### <img src="http://latex.codecogs.com/gif.latex?{d^t} = {c_1}\sqrt {f\left( {{{\bf{x}}^t}} \right)}">

### <img src="http://latex.codecogs.com/gif.latex?{\delta ^t} = {c_2}{d^t}">

  <!-- $$
    \left\{ \begin{array}{l}
  {{\bf{x}}_r} = {{\bf{x}}^t} + {d^t}{\bf{b}}\\
  {{\bf{x}}_l} = {{\bf{x}}^t} - {d^t}{\bf{b}}\\
  {{\bf{x}}^t} = {{\bf{x}}^{t - 1}} - {\delta ^t}{\bf{b}}sign\left( {f\left( {{{\bf{x}}_r}} \right) - f\left( {{{\bf{x}}_l}} \right)} \right)
  \end{array} \right.
  $$ -->

where

- <img src="https://render.githubusercontent.com/render/math?math=c_1"> and <img src="https://render.githubusercontent.com/render/math?math=c_2"> are parameters to the BAS algorithm
- <img src="https://render.githubusercontent.com/render/math?math={\delta^t}"> is the step size of searching which accounts for the convergence speed following a decreasing function of t instead of an increasing function or a constant.
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

- 6 axes robot manipulator
- D-H Table
  |<img src="http://latex.codecogs.com/gif.latex?i">|<img src="http://latex.codecogs.com/gif.latex?{\theta}\quad(rad)">|<img src="http://latex.codecogs.com/gif.latex?d\quad(cm)">|<img src="http://latex.codecogs.com/gif.latex?a\quad(cm)">|<img src="http://latex.codecogs.com/gif.latex?\alpha\quad(rad)">|
  |---|---|---|---|---|
  |1|0| 34.5| 7.5| 1.570796|
  |2|1.570796 |0 |27 |0|
  |3|0 |0 |9 |1.570796|
  |4|0 |29.5 |0 |-1.570796|
  |5|0 |0 |0 |1.570796|
  |6|0 |10.2 |0 |0|
- Joint space limit
  - <img src="http://latex.codecogs.com/gif.latex?-170^\circ  \le {\theta _1} \le 170^\circ">
  - <img src="http://latex.codecogs.com/gif.latex?- 135^\circ  \le {\theta _2} \le 82.79^\circ">
  - <img src="http://latex.codecogs.com/gif.latex?- 74.88^\circ  \le {\theta _3} \le 104^\circ">
  - <img src="http://latex.codecogs.com/gif.latex?- 190^\circ  \le {\theta _4} \le 190^\circ">
  - <img src="http://latex.codecogs.com/gif.latex?- 118.88^\circ  \le {\theta _5} \le 118.88^\circ">
  - <img src="http://latex.codecogs.com/gif.latex?- 360^\circ  \le {\theta _6} \le 360">
- Testing Motion (cartesian position of the end effector)

  - [See txt file](https://github.com/chiehwun/2021-NCKU_ORA/blob/main/Final_Project/Code/position.txt)

- Parameters

  - PSO
    - <img src="http://latex.codecogs.com/gif.latex?{w} = 2.0" />
    - <img src="http://latex.codecogs.com/gif.latex?{c_1} = 0.5339" />
    - <img src="http://latex.codecogs.com/gif.latex?{c_2} = 1.0548" />
  - BAS
    - <img src="http://latex.codecogs.com/gif.latex?{c_1} = 0.25" />
    - <img src="http://latex.codecogs.com/gif.latex?{c_2} = 0.2" />

## Result

- PSO
  - Particle Number = 10
  - Time = 80 sec

<br>
<div align=center>
<img src="https://github.com/chiehwun/2021-NCKU_ORA/blob/main/Final_Project/pso/pso_error.png">
</div>
<br>

- BAS

  - Beetles Number = 10
  - Time = 104
  <br>
  <div align=center>
  <img src="https://github.com/chiehwun/2021-NCKU_ORA/blob/main/Final_Project/bas/bas(10)_error.png">
  </div>
  <br>

  > **Comment**
  >
  > 1. PSO is faster than BAS
  > 2. The error of PSO is smaller than BAS

## Reference

###### [1] https://en.wikipedia.org/wiki/Metaheuristic

###### [2] J. Kennedy and R. Eberhart, "Particle swarm optimization, " Proceedings of ICNN'95 - _International Conference on Neural Networks_, 1995, pp. 1942-1948 vol.4

###### [3] https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/

###### [4] X. Jiang, S. Li, "BAS: Beetle Antennae Search Algorithm for Optimization Problems, " in arXiv conference, 2017

###### [5] Y. Cheng, C. Li, S. Li, Z. Li, "Motion Planning of Redundant Manipulator With Variable Joint Velocity Limit Based on Beetle Antennae Search Algorithm, " in _IEEE Access_, vol. 8, pp. 138788-138799, 2020
