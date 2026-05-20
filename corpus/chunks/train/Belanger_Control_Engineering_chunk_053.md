# Example 2.9 (Pendulum on a Cart)

For the inverted pendulum of Example 2.5, calculate the incremental system, with $x^{*} = \theta^{*} = 0$ .

Solution The equilibrium point is simply the vertical equilibrium, with all quantities equal to zero.

To find the incremental system, it is possible to calculate the Jacobian corresponding to Equations 2.40. An alternative way is to write the Lagrangian for small changes from equilibrium. The Lagrangian is written by throwing out terms of order higher than 2 in the variables. We use the fact that $\sin\theta\approx\theta$ and $\cos\theta\approx1-\frac{1}{2}\theta^{2}$ to write

$${\cal L} = \frac {1}{2} M (\dot {x}) ^ {2} + \frac {1}{2} m (\dot {x} + \ell \dot {\theta}) ^ {2} - V _ {0} - m g \ell (1 - \frac {1}{2} \theta^ {2}).$$

We write

$$
\begin{array}{l} \frac {\partial L}{\partial \dot {x}} = M \dot {x} + m (\dot {x} + \ell \dot {\theta}); \quad \frac {\partial L}{\partial x} = 0 \\ \frac {\partial L}{\partial \dot {\theta}} = m \ell (\dot {x} + \ell \dot {\theta}); \quad \frac {\partial L}{\partial \theta} = m g \ell \theta . \\ \end{array}
$$

Lagrange's equations are

$$
\begin{array}{l} (M + m) \ddot {x} + m \ell \ddot {\theta} = F \\ m \ell \ddot {x} + m \ell^ {2} \ddot {\theta} - m g \ell \theta = 0. \\ \end{array}
$$

Solving for $\ddot{x}$ and $\ddot{\theta}$ yields

$$
\begin{array}{l} \ddot {x} = \dot {v} = - \frac {m g}{M} \theta + \frac {F}{M} \\ \ddot {\theta} = \dot {\omega} = \frac {(M + m) g}{M \ell} \theta - \frac {F}{M \ell}. \\ \end{array}
$$

These, plus the two definitions $\dot{x} = v$ and $\dot{\theta} = \omega$ , are the incremental state equations (no $\Delta$ 's are required, because the variables are 0 at equilibrium).

This technique can be used to advantage in cases where the equilibrium point is easy to calculate and only the incremental equations are sought. Another, non-Lagrangian method is used in the following example. Basically, since the right-hand sides are linear in the state and control increments, we perturb the states and inputs one at a time to calculate the contribution of each.
