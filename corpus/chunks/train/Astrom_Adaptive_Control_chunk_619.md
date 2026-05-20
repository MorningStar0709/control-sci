# Stability and Robustness

In a variable-structure system we attempt to find a switching surface such that the closed-loop system behaves as desired. We now construct a variable-structure controller. For this purpose we assume that the system that we want to control is described by the nonlinear equation

$$\frac {d ^ {n} y}{d t ^ {n}} = f _ {1} \left(y, \frac {d y}{d t}, \dots , \frac {d ^ {n - 1} y}{d t ^ {n - 1}}\right) + g _ {1} \left(y, \frac {d y}{d t}, \dots , \frac {d ^ {n - 1} y}{d t ^ {n - 1}}\right) u$$

If we introduce the state

$$
x = \left( \begin{array}{c c c c} d ^ {n - 1} y & d ^ {n - 2} y \\ d t ^ {n - 1} & \overline {{d t ^ {n - 2}}} & \dots & \frac {d y}{d t} \end{array} y\right) ^ {T} \tag {10.6}
$$

the system can be written as

$$
\frac {d x}{d t} = \left( \begin{array}{c c c c c} 0 & 0 & \dots & 0 & 0 \\ \mathbf {1} & 0 & \dots & 0 & 0 \\ \vdots & & & \vdots \\ 0 & 0 & \dots & \mathbf {1} & 0 \end{array} \right) x + \left( \begin{array}{c} f _ {1} (x) + g _ {1} (x) u \\ 0 \\ \vdots \\ 0 \end{array} \right) \tag {10.7}
= f (x) + g (x) u
y = \left( \begin{array}{c c c c c} 0 & 0 & \dots & 0 & 1 \end{array} \right) x
$$

where $f(x)$ and $g(x)$ are vectors. The system is nonlinear but is affine in the control signal. Further, it is assumed that all the states can be measured and that the state vector has the special form given in Eq. (10.6). For simplicity it is assumed that the purpose of the control is to find a controller such that $x = 0$ is an asymptotically stable solution. The problem with constant reference signals is considered in Problem 10.14 at the end of the chapter.

There are three important questions that must be answered for VSS:

- Will the trajectories starting at any point hit the switching line?   
- Is there a sliding mode?   
- Is the sliding mode stable?

There are partial answers to these questions in the literature on VSS. For the special type of system defined by Eqs. (10.7) it is easy to derive a controller that makes the sliding mode stable.

Let the switching surface be

$$\sigma (x) = p _ {1} x _ {1} + p _ {2} x _ {2} + \dots + p _ {n} x _ {n} = p ^ {T} x = 0 \tag {10.8}$$

Using the definition of the state vector, we find that

$$\sigma (x) = p _ {1} y ^ {(n - 1)} + p _ {2} y ^ {(n - 2)} + \dots + p _ {n} y = 0$$

The dynamic behavior on the sliding surface can be specified by a proper choice of the numbers $p_{i}$ . The motion is determined by a differential equation of order n - 1. It will be stable if the polynomial

$$P (s) = p _ {1} s ^ {n - 1} + p _ {2} s ^ {n - 2} + \dots + p _ {n} \tag {10.9}$$

has all its roots in the left-half plane.
