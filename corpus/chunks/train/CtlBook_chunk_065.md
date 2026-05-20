# 2.5 Conversion to Transfer Function

EOMs are Linear Ordinary Dierential Equations, LODEs. As such, we can easily apply the Laplace Transform. Using the EOMs of Example 2.4,

$$M _ {1} X _ {1} (s) s ^ {2} + B X _ {1} (s) s - B X _ {2} (s) s + K X _ {1} (s) = F (s)M _ {2} X _ {2} (s) s ^ {2} + B X _ {2} (s) s - B X _ {1} (s) s = 0$$

Note that we have assumed zero initial conditions. What does this assumption mean? Mathematically it means

$$x _ {i} (t = 0) = 0, \quad \dot {x} _ {i} (t = 0) = 0, \quad \ddot {x} _ {i} (t = 0) = 0$$

and physically this corresponds to the system being at rest and having no kinetic or potential energy.

We will use the Laplace transform to solve for a Transfer Function. Transfer functions are ratios between the Laplace Transforms of two physical variables. Examples:

$$\frac {X _ {2} (s)}{F (s)}, \qquad \frac {X _ {1} (s)}{X _ {2} (s)} \qquad \text { etc. }$$

Often we need to analyze a system when we know its input (say X(s)) but do not know its output (say Y (s)). If we can obtain the transfer function

$$G (s) = \frac {Y (s)}{X (s)}$$

then we can get the Laplace transform of the output by

$$Y (s) = G (s) X (s)$$

The transfer function is obtained by algebraically manipulating the Laplace transform of one or more EOMs. Sometimes multiple EOMs have to be solved simultaneously to get the transfer function.
