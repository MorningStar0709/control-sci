# 11.7 Problems

11.1 Consider the first-order system

$$\frac {d x}{d t} = - a x + b u$$

Assume that the loss function of (11.4) should be minimized with $Q_{1c} = 1$ and $Q_{2c} = \rho$ . Determine the corresponding discrete-time loss function (11.9).

11.2 Consider the continuous-time double integrator in Example A.1. Assume that the loss function of (11.4) should be minimized with

$$
Q _ {1 c} = \left( \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right) \quad \text { and } \quad Q _ {2 c} = 1
$$

Determine $Q_{1}$ , $Q_{12}$ , and $Q_{2}$ in the corresponding discrete-time loss function (11.9).

11.3 Given the system

$$x (k + 1) = a x (k) + b u (k)$$

with the loss function

$$J = \sum_ {k = 0} ^ {N} x ^ {2} (k)$$

Let the admissible control strategy be such that $u(k)$ is a function of $x(k)$ . Determine the strategy that minimizes the loss.

11.4 Consider the system in Problem 11.3. Determine the control strategy that minimizes the loss when the admissible control strategies are such that $u(k)$ is a function of $x(k - 1)$ .

11.5 The inventory model in Example A.5 is described by

$$
x (k + 1) = \left( \begin{array}{l l} 1 & 1 \\ 0 & 0 \end{array} \right) x (k) + \left( \begin{array}{l} 0 \\ 1 \end{array} \right) u (k)

y (k) = \left( \begin{array}{c c} 1 & 0 \end{array} \right) x (k)
$$

(a) Determine the steady-state LQ-controller when $Q_{1} = C^{T}C$ and $Q_{2} = \rho$ .   
(b) Determine the poles of the closed-loop system and investigate how they depend on the weight on the control signal, $\rho$ .   
(c) Simulate the system using the controller in (a). Assume that $x(0)^{T} = [1\ 1]$ and consider the output and the control signal for different values of $\rho$ .

11.6 Consider the two-tank system with the pulse-transfer operator given in Problem 2.10 (b). Use (11.35) and plot the root locus with respect to $\rho$ that shows the closed-loop poles when the system is controlled by the steady-state LQ-controller for the loss function

$$J = \sum_ {k = 0} ^ {\infty} \left(y (k) ^ {2} + \rho u (k) ^ {2}\right)$$

11.7 Show that a deadbeat control law, a control law such that the matrix $\Phi - \Gamma L$ has all its eigenvalues at the origin, can be obtained from the discrete-time optimization with $Q_{2} = 0$ , $Q_{1} = 0$ , and $Q_{0} = I$ .
