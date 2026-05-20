# Exercise 7.7: Is QP constraint qualification relevant to MPC?

Continuity properties of the MPC control law are often used to establish robustness properties of MPC such as robust asymptotic stability. In early work on continuity properties of linear model MPC, Scokaert, Rawlings, and Meadows (1997) used results on continuity of QPs with respect to parameters to establish MPC stability under perturbations. For example, Hager (1979) considered the following quadratic program

$$\min _ {u} (1 / 2) u ^ {\prime} H u + h ^ {\prime} u + c$$

subject to

$$D u \leq d$$

and established that the QP solution $u ^ { 0 }$ and cost $V ^ { 0 }$ are Lipschitz continuous in the data of the QP, namely the parameters H, h, D, d. To establish this result Hager (1979) made the following assumptions.

• The solution is unique for all H, h, D, d in a chosen set of interest.

• The rows of D corresponding to the constraints active at the solution are linearly independent. The assumption of linear independence of active constraints is a form of constraint qualification.

(a) First we show that some form of constraint qualification is required to establish continuity of the QP solution with respect to matrix D. Consider the following QP example that does not satisfy Hager’s constraint qualification assumption.

$$
H = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \qquad D = \left[ \begin{array}{c c} 1 & 1 \\ - 1 & - 1 \end{array} \right] \qquad d = \left[ \begin{array}{c} 1 \\ - 1 \end{array} \right] \qquad h = \left[ \begin{array}{c} - 1 \\ - 1 \end{array} \right] \qquad c = 1
$$

Find the solution $u ^ { 0 }$ for this problem.

Next perturb the D matrix to

$$
D = \left[ \begin{array}{c c} 1 & 1 \\ - 1 + \epsilon & - 1 \end{array} \right]
$$

in which $\epsilon > 0$ is a small perturbation. Find the solution to the perturbed problem. Are $V ^ { 0 }$ and $u ^ { 0 }$ continuous in parameter D for this QP? Draw a sketch of the feasible region and cost contours for the original and perturbed problems. What happens to the feasible set when D is perturbed?

(b) Next consider MPC control of the following system with state inequality constraint and no input constraints

$$
A = \left[ \begin{array}{c c} - 1 / 4 & 1 \\ - 1 & 1 / 2 \end{array} \right] \qquad B = \left[ \begin{array}{c c} 1 & 1 \\ - 1 & - 1 \end{array} \right] \qquad x (k) \leq \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] \quad k \in \mathbb {I} _ {0: N}
$$
