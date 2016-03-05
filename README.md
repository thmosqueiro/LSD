Learning Sistemas Dinamicos
=====

This is a small piece of python code to help the study of dynamical
systems in two dimensions. LSD will let you test several initial
conditions by clicking on where you want the dynamical system to
start. The idea is to be able to study different kinds of attractors
and, by changing the system's parameters, visualize simple
bifurcations. A possible extension to 3D systems is almost
straightforward and I plan to implement it in the near future.

It was inspired by lectures from [Prof. Reynaldo
Pinto](http://neurobiofisica.ifsc.usp.br/) & Prof. [Leonardo
Maia](http://www.ifsc.usp.br/~lpmaia/) at IFSC (USP). The course
material can be found
[here](http://www.ifsc.usp.br/~reynaldo/curso_caos/). It uses a linear
multistep methods to solve the differential equations. To visualize
the evolution of the dynamical system, I'm simply using matplotlib
with animations.


How to use
---

To use it, simply run 
```
# python LSD.py
```
It will open a blank plot. Click and watch the animation.

![Example](https://raw.githubusercontent.com/thmosqueiro/LSD/master/example.png)

If you're feeling lost type
```
# python LSD.py -h
```


How to install
---

LSD is no fancy piece of software: it's simply a small python script
to handle easy visualization of 2-D dynamical systems. All you need to
do is to download LSD.py and run it.

Currently, it only depends on numpy, matplotlib and scipy. If you're
on Ubuntu,
```
# sudo apt-get install -y python-numpy python-matplotlib python-scipy
```
On Fedora,
```
# su -c 'dnf install -y python-numpy python-matplotlib python-scipy
```
If you're using something else, it should be pretty easy to figure out
what to do, or else just hit me with a question.

License?
---

Do whatever you want, don't sue me.
