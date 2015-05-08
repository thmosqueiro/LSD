Learning Sistemas Dinamicos
=====

Inspired by lectures from Prof. Reynaldo Pinto at IFSC (USP), this
small script enables you to easily try out bidimensional dynamical
systems. The idea is to be able to study different kinds of attractors
and, by changing the system's parameters, visualize simple
bifurcations. A possible extension to 3D systems is almost
straightforward and I plan to implement it in the near future.

It uses a linear multistep methods to solve the differential
equations. To visualize the evolution of the dynamical system, I'm
simply using matplotlib with animations.


Using
=====

To use it, simply run 

# python LSD.py

It will open a blank plot. Click and watch the animation.

![Example](https://raw.githubusercontent.com/thmosqueiro/LSD/master/example.png)
