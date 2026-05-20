# 9.2.2 Separation principle

The separation principle for linear stochastic systems states that the optimal controller and optimal observer for the stochastic system can be designed independently, and the combination of a stable controller and a stable observer is itself stable.

This means that designing the optimal feedback controller for the stochastic system can be decomposed into designing the optimal state observer, then feeding that into the optimal controller for the deterministic system.

Consider the following state-space model.

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k}\mathbf {y} _ {k} = \mathbf {C x} _ {k} + \mathbf {D u} _ {k}$$

We’ll use the following controller for state feedback.

$$\mathbf {u} _ {k} = - \mathbf {K} \hat {\mathbf {x}} _ {k}$$

With the estimation error defined as ${ \bf e } _ { k } = { \bf x } _ { k } - \hat { \bf x } _ { k }$ , we get the observer dynamics derived in equation (9.8).

$$\mathbf {e} _ {k + 1} = (\mathbf {A} - \mathbf {L C}) \mathbf {e} _ {k}$$

Also, after rearranging the error equation to be $\hat { \mathbf { x } } _ { k } = \mathbf { x } _ { k } - \mathbf { e } _ { k }$ , the controller can be rewritten as

$$\mathbf {u} _ {k} = - \mathbf {K} (\mathbf {x} _ {k} - \mathbf {e} _ {k})$$

Substitute this into the model.

$$
\begin{array}{l} \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} \\ \mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} - \mathbf {B K} (\mathbf {x} _ {k} - \mathbf {e} _ {k}) \\ \mathbf {x} _ {k + 1} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} _ {k} + \mathbf {B K e} _ {k} \\ \end{array}
$$

Now, we can write the closed-loop dynamics as

$$
\left[ \begin{array}{c} \mathbf {x} _ {k + 1} \\ \mathbf {e} _ {k + 1} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B K} \\ \mathbf {0} & \mathbf {A} - \mathbf {L C} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {e} _ {k} \end{array} \right]
$$

Since the closed-loop system matrix is triangular, the eigenvalues are those of A−BK and A − LC. Therefore, the stability of the feedback controller and observer are independent.
