# 4.9 Problems

4.1 A general second-order discrete-time system can be written as

$$
x (k + 1) = \left( \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right) x (k) + \left( \begin{array}{l} b _ {1} \\ b _ {2} \end{array} \right) u (k)

y (k) = \left( \begin{array}{c c} c _ {1} & c _ {2} \end{array} \right) x (k)
$$

Determine a state-feedback controller of the form

$$u (k) = - L x (k)$$

such that the characteristic equation of the closed-loop system is

$$z ^ {2} + p _ {1} z + p _ {2} = 0$$

Use the result to verify the deadbeat controller for the double integrator given in Example 4.5.

4.2 Given the system

$$
x (k + 1) = \left( \begin{array}{l l} 1. 0 & 0. 1 \\ 0. 5 & 0. 1 \end{array} \right) x (k) + \left( \begin{array}{l} 1 \\ 0 \end{array} \right) u (k)

y (k) = \left( \begin{array}{c c} 1 & 1 \end{array} \right) x (k)
$$

Determine a linear state-feedback controller

$$u (k) = - L x (k)$$

such that the closed-loop poles are in 0.1 and 0.25.

4.3 Determine the deadbeat controller for the normalized motor in Example A.2. Assume that $x(0) = [1 - 1]^{T}$ . Determine the sample interval such that the control signal is less than one in magnitude. It can be assumed that the maximum value of $u(k)$ is at k = 0.

4.4 Consider the continuous system.

$$
\frac {d x}{d t} = \left( \begin{array}{c c} - 3 & 1 \\ 0 & - 2 \end{array} \right) x + \binom{0}{1} u

y = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x
$$

Sampling the system with h = 0.2 gives

$$
x (k + 1) = \left( \begin{array}{c c} 0. 5 5 & 0. 1 2 \\ 0 & 0. 6 7 \end{array} \right) x (k) + \binom {0. 0 1} {0. 1 6} u (k)
$$

(a) Determine a state-feedback control law such that the closed-loop characteristic polynomial is

$$z ^ {2} - 0. 6 3 z + 0. 2 1$$

(b) Determine the corresponding continuous-time characteristic polynomial and discuss the choice of the sampling period.   
(c) Simulate the closed-loop system when $x(0) = [10]^T$ .

4.5 The system

$$
x (k + 1) = \left( \begin{array}{l l} 0. 7 8 & 0 \\ 0. 2 2 & 1 \end{array} \right) x (k) + \left( \begin{array}{l} 0. 2 2 \\ 0. 0 3 \end{array} \right) u (k)

y (k) = \left( \begin{array}{c c} 0 & 1 \end{array} \right) x (k)
$$

represents the normalized motor for the sampling interval h = 0.25. Determine observers for the state based on the output by using each of the following.

(a) Direct calculation using (4.25).   
(b) A dynamic system that gives $\hat{x}(k + 1|k)$ using (4.28).   
(c) The reduced-order observer.
