# How to Compute $\Phi$ and $\Gamma$

The calculations required to sample a continuous-time system are the evaluation of a matrix exponential and the integration of a matrix exponential. These can be done in many different ways, for instance, by using the following:

- Numerical calculation in MATLAB $^{\textregistered}$ or MATRIX $_{X}^{\textregistered}$   
- Series expansion of the matrix exponential   
- The Laplace transform—the Laplace transform of $\exp(At)$ is $(sI - A)^{-1}$

- Cayley-Hamilton's theorem (see Appendix B)   
- Transformation to diagonal or Jordan forms

\- Symbolic computer algebra, using programs such as Maple® and Mathematica®.

Calculations by hand are feasible for low-order systems, $n \leq 2$ , and for high-order systems with special structures. One way to simplify the computations is to compute

$$\Psi = \int_ {0} ^ {h} e ^ {A s} d s = I h + \frac {A h ^ {2}}{2 !} + \frac {A ^ {2} h ^ {3}}{3 !} + \dots + \frac {A ^ {i} h ^ {i + 1}}{(i + 1) !} + \dots$$

The matrices $\Phi$ and $\Gamma$ are given by

$$
\begin{array}{l} \Phi = I + A \Psi \\ \Gamma = \Psi B \\ \end{array}
$$

Computer evaluation can be done using several different numerical algorithms in MATLAB $^{\textregistered}$ or MATRIX $_{X}^{\textregistered}$ .
