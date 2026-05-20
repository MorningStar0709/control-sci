# THEOREM 5.3 Lyapunov's stability theorem: Time-varying systems

Let $x = 0$ be an equilibrium point for Eq. (5.25) and $D = \{x \in R^n | \| x\| < r\}$ . Let $V$ be a continuously differentiable function such that

$$\alpha_ {1} (\| x \|) \leq V (x, t) \leq \alpha_ {2} (\| x \|) \tag {5.26}\frac {d V}{d t} = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (x, t) \leq - \alpha_ {3} (\| x \|)$$

for $\forall t \geq 0$ , where $\alpha_{1}, \alpha_{2}$ , and $\alpha_{3}$ are class $K$ functions. Then $x = 0$ is uniformly asymptotically stable.

Proof: A proof can be found in Khalil (1992).

Remark 1. The derivative of $V$ along the trajectories of Eq. (5.25) is now given by

$$\frac {d V}{d t} = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (x, t)$$

Remark 2. A function $V(x,t)$ satisfying the left inequality of (5.26) is said to be positive definite. A function satisfying the right inequality of (5.26) is said to be decrescent.

Remark 3. To show stability for time-variable systems, it is necessary to bound the function $V(x,t)$ by a function that doesn't depend on $t$ .

When using Lyapunov theory on adaptive control problems, we often find that dV/dt only is negative semidefinite. This implies that additional conditions must be imposed on the system. The following lemma gives a useful result.
