# Solution:

We consider as usual the simplified notation $x = x ( t ) , u = u ( t )$ and $p = p ( t )$ . We first calculate the Hamiltonian as

$$H (t, x, u, p, p _ {0}) = \langle p, f (t, x, u) \rangle + p _ {0} L (t, x, u) \tag {233}$$

We assume the following: we can consider $p _ { 0 } = - 1$ , given that this problem is in R: imposing it different than −1 would not change the result (which can be proved i.e. by finding out the condition for optimality: when we set the gradient to 0, being p and $p _ { 0 }$ both scalars, we could just eliminate $p _ { 0 }$ by including it in the value of the new $p : = p _ { n e w } . )$ We will consider this assumption also for the other scalar problems.

The Hamiltonian in this case then becomes:

$$H (t, x, u, p) = p (a x + b u) - \frac {1}{2} u ^ {2} \tag {234}$$

By applying Pontryagin’s maximum principle, we can find $u ^ { * } ( t )$ by maximizing the Hamiltonian:

$$u ^ {*} (t) = \underset {u \in \mathbb {R}} {\operatorname{argmax}} \left[ p (a x + b u) - \frac {1}{2} u ^ {2} \right] \tag {235}$$

Which given that the problem is concave, we can find by setting the first derivative equal to zero:

$$\frac {\partial H}{\partial u} = p b - u = 0 \tag {236}\Longrightarrow u ^ {*} (t) = p ^ {*} (t) b \tag {237}$$

Then, we may find the optimal $p ^ { * }$ by satisfying the following equation:

$$\dot {p} ^ {*} = - H _ {x} (t, x ^ {*}, u ^ {*}, t ^ {*}) = - \frac {\partial}{\partial x} \left[ p (a x + b u) - \frac {1}{2} u ^ {2} \right] = - p a \tag {238}$$

Solving this simple ODE yields

$$p ^ {*} (t) = c _ {1} e ^ {- a t} \tag {239}$$

In order to satisfy the boundary condition, we can get the value of $c _ { 1 }$ :

$$p ^ {*} (T) = - K _ {x} \left(T, x ^ {*} (T)\right) = - \frac {\partial}{\partial x} \left[ \frac {1}{2} q \cdot x (T) ^ {2} \right] = - q x ^ {*} (T) \tag {240}\Longrightarrow p ^ {*} (T) = c _ {1} e ^ {- a T} = - q x (T) \tag {241}\Longrightarrow c _ {1} = - q x (T) e ^ {a T} \tag {243}$$

By substituting $c _ { 1 }$ into the previous expression, we can get the value for the optimal p as

$$p ^ {*} (t) = - q x ^ {*} (T) e ^ {a (T - t)} \tag {244}$$

In which the optimal final point $x ^ { * } ( T )$ can be obtained by solving the differential equation related to the state. Finally, we get the expression for the optimal control:

$$u ^ {*} (t) = - b q x ^ {*} (T) e ^ {a (T - t)} \tag {245}$$
