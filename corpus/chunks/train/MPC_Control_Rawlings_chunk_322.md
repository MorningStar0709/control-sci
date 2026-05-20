# Exercise 2.14: An MPC stability result

Given the following nonlinear model and objective function

$$
\begin{array}{l} x ^ {+} = f (x, u), \quad 0 = f (0, 0) \\ x (0) = x \\ V _ {N} (x, \mathbf {u}) = \sum_ {k = 0} ^ {N - 1} \ell (x (k), u (k)) \\ \end{array}
$$

Consider the terminal constraint MPC regulator

$$\min _ {\mathbf {u}} V _ {N} (x, \mathbf {u})$$

subject to

$$x ^ {+} = f (x, u) \quad x (0) = x \quad x (N) = 0$$

and denote the first move in the optimal control sequence as $u ^ { 0 } ( x )$ . Given the closedloop system

$$x ^ {+} = f (x, u ^ {0} (x))$$

(a) Prove that the origin is asymptotically stable for the closed-loop system. State the cost function assumption and controllability assumption required so that the control problem is feasible for some set of defined initial conditions.   
(b) What assumptions about the cost function $\ell ( x , u )$ are required to strengthen the controller so that the origin is exponentially stable for the closed-loop system? How does the controllability assumption change for this case?
