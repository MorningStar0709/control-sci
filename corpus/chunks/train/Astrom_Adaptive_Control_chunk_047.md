# Process Descriptions

In this book the processes will mainly be described by linear single-input, single-output systems. In continuous time the process can be in state space form:

$$\frac {d x}{d t} = A x + B u \tag {1.9}y = C x$$

or in transfer function form:

$$G _ {p} (s) = \frac {B (s)}{A (s)} = \frac {b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \cdots b _ {m}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots a _ {n}} \tag {1.10}$$

where $s$ is the Laplace transform variable. Notice that $A, B,$ and $C$ are used for matrices as well as polynomials. In normal cases this will not cause any misunderstanding. In ambiguous cases the argument will be used in the polynomials.

In discrete time the process can be described in state space form:

$$x (t + 1) = \Phi x (t) + \Gamma u (t)y (t) = C x (t)$$

where the sampling interval is taken as the time unit. The discrete time system can also be represented by the pulse transfer function

$$H _ {p} (z) = \frac {B (z)}{A (z)} = \frac {b _ {0} z ^ {m} + b _ {1} z ^ {m - 1} + \cdots b _ {m}}{z ^ {n} + a _ {1} z ^ {n - 1} + \cdots a _ {n}} \tag {1.11}$$

where $z$ is the $z$ -transform variable.

The parameters, $b_{0}, b_{1}, \ldots, b_{m}, a_{1}, \ldots, a_{n}$ of systems (1.10) and (1.11) as well as the orders m, n are often assumed to be unknown or partly unknown.
