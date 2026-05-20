# EXAMPLE 5–8

![](image/06326514d09dffb061def8e30dd96cadf2fc85bd146688e9bfd791edb2b76b55.jpg)

<details>
<summary>text_image</summary>

k
m
b
x
</details>

Figure 5–30 Mechanical system.

Consider the mechanical system shown in Figure 5–30, where m=1 kg, b=3 N-secm, and k=2 Nm. Assume that at t=0 the mass m is pulled downward such that x(0)=0.1 m and (0)=0.05 msec. The displacement x(t) is measured from the equilibrium position before thex mass is pulled down. Obtain the motion of the mass subjected to the initial condition. (Assume no external forcing function.)

The system equation is

$$m \ddot {x} + b \dot {x} + k x = 0$$

with the initial conditions x(0)=0.1 m and (x is measured from the equilib-x  (0) = 0.05 msec. rium position.) The Laplace transform of the system equation gives

$$m \left[ s ^ {2} X (s) - s x (0) - \dot {x} (0) \right] + b [ s X (s) - x (0) ] + k X (s) = 0$$

or

$$(m s ^ {2} + b s + k) X (s) = m x (0) s + m \dot {x} (0) + b x (0)$$

Solving this last equation for X(s) and substituting the given numerical values, we obtain

$$
\begin{array}{l} X (s) = \frac {m x (0) s + m \dot {x} (0) + b x (0)}{m s ^ {2} + b s + k} \\ = \frac {0 . 1 s + 0 . 3 5}{s ^ {2} + 3 s + 2} \\ \end{array}
$$

This equation can be written as

$$X (s) = \frac {0 . 1 s ^ {2} + 0 . 3 5 s}{s ^ {2} + 3 s + 2} \frac {1}{s}$$

Hence the motion of the mass m may be obtained as the unit-step response of the following system:

$$G (s) = \frac {0 . 1 s ^ {2} + 0 . 3 5 s}{s ^ {2} + 3 s + 2}$$

MATLAB Program 5–14 will give a plot of the motion of the mass.The plot is shown in Figure 5–31.
