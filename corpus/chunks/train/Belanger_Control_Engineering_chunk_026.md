# 2.2 STATE EQUATIONS

We begin with the simple example of Figure 2.1. A mass $M$ is moving on a horizontal plane under the influence of an external force, $F$ , against a friction force, $D(v)$ , where $v$ is the velocity. From Newton's second law,

$$M \frac {d v}{d t} = F - D (v)\frac {d v}{d t} = \frac {F}{M} - \frac {D (v)}{M}. \tag {2.1}$$

Also,

$$\frac {d x}{d t} = v. \tag {2.2}$$

Equations 2.1 and 2.2 describe the motion of the mass. Note that these two equations have very different origins: Equation 2.1 comes from the physics of the problem, whereas Equation 2.2 simply expresses the definition of velocity.

Equation 2.1 is a conservation law and expresses the rate of change of momentum in terms of force. Such rate equations are quite common in physics because of the many conservation principles, e.g., mass and energy. Rate equations are generally first-order differential equations, as are many other equations that, like Equation 2.2, express definitions. It follows that a large class of models can be expressed as sets of first-order differential equations, as follows:

$$
\dot {x} _ {1} = f _ {1} (x _ {1}, x _ {2}, \dots , x _ {n}, u _ {1}, u _ {2}, \dots , u _ {r}, t)\dot {x} _ {2} = f _ {2} (x _ {1}, x _ {2}, \dots , x _ {n}, u _ {1}, u _ {2}, \dots , u _ {r}, t)
\begin{array}{c c} \vdots & \ddots \\ \vdots & \ddots \end{array}
\dot {x} _ {n} = f _ {n} (x _ {1}, x _ {2}, \dots , x _ {n}, u _ {1}, u _ {2}, \dots , u _ {r}, t) \tag {2.3}y _ {1} = h _ {1} (x _ {1}, x _ {2}, \dots , x _ {n}, u _ {1}, u _ {2}, \dots , u _ {r}, t)
\begin{array}{c c} \vdots & \vdots \\ \vdots & \vdots \end{array}
y _ {m} = h _ {m} (x _ {1}, x _ {2}, \dots , x _ {n}, u _ {1}, u _ {2}, \dots , u _ {r}, t). \tag {2.4}
$$

![](image/972b8938c99b2323182eccecf4563b8536d109770c008af4af3a5ee3cc4328b5.jpg)

<details>
<summary>text_image</summary>

F → M ← D(v)
x
</details>

Figure 2.1 Mass moving on a plane

Here, $u_{1}$ , $u_{2}$ , $\ldots$ , $u_{r}$ are the r inputs, and $y_{1}$ , $y_{2}$ , $\ldots$ , $y_{m}$ are the m outputs. The variables $x_{1}$ , $x_{2}$ , $\ldots$ , $x_{n}$ are called state variables. Equations 2.3, the state equations, describe the dynamical behavior of the system. Equations 2.4, the output equations, are algebraic expressions for the outputs in terms of the state variables, the inputs, and time.

Equations 2.1 and 2.2 are in state form. If we define $x$ and $v$ as state variables and $F$ as the input, then

$$x _ {1} = xx _ {2} = vu = F$$

and we write
