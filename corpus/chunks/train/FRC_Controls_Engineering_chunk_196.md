# 7.5 Closed-loop controller

With the control law $\mathbf { u } _ { k } = \mathbf { K } ( \mathbf { r } _ { k } - \mathbf { x } _ { k } )$ , we can derive the closed-loop state-space equations. We’ll discuss where this control law comes from in subsection 7.7.

First is the state update equation. Substitute the control law into equation (7.10).

$$
\begin{array}{l} \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B K} (\mathbf {r} _ {k} - \mathbf {x} _ {k}) \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B K r} _ {k} - \mathbf {B K x} _ {k} \\ \mathbf {x} _ {k + 1} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} _ {k} + \mathbf {B K r} _ {k} \tag {7.12} \\ \end{array}
$$

Now for the output equation. Substitute the control law into equation (7.11).

$$
\begin{array}{l} \mathbf {y} _ {k} = \mathbf {C x} _ {k} + \mathbf {D} (\mathbf {K} (\mathbf {r} _ {k} - \mathbf {x} _ {k})) \\ \mathbf {y} _ {k} = \mathbf {C x} _ {k} + \mathbf {D K r} _ {k} - \mathbf {D K x} _ {k} \\ \mathbf {y} _ {k} = (\mathbf {C} - \mathbf {D K}) \mathbf {x} _ {k} + \mathbf {D K r} _ {k} \tag {7.13} \\ \end{array}
$$

Instead of commanding the system to a state using the vector $\mathbf { u } _ { k }$ directly, we can now specify a vector of desired states through $\mathbf { r } _ { k }$ and the controller will choose values of $\mathbf { u } _ { k }$ for us over time that drive the system toward the reference.

The eigenvalues of A − BK are the poles of the closed-loop system. Therefore, the rate of convergence and stability of the closed-loop system can be changed by moving the poles via the eigenvalues of A − BK. A and B are inherent to the system, but K can be chosen arbitrarily by the controller designer. For equation (7.12) to reach steady-state, the eigenvalues of A − BK must be in the left-half plane. There will be steady-state error if $\mathbf { A r } _ { k } \neq \mathbf { r } _ { k }$ .
