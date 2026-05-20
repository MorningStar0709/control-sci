# Example 4.1

A second order plant

$$\dot {x} _ {1} (t) = x _ {2} (t),\dot {x} _ {2} (t) = - 2 x _ {1} (t) - 3 x _ {2} (t) + u (t)\mathbf {y} (t) = \mathbf {x} (t) \tag {4.1.38}$$

is to be controlled to minimize the performance index

$$
\begin{array}{l} J = \left[ 1 - x _ {1} (t _ {f}) \right] ^ {2} \\ + \int_ {t _ {0}} ^ {t _ {f}} \left[ \left[ 1 - x _ {1} (t) \right] ^ {2} + 0. 0 0 2 u ^ {2} (t) \right] d t. \tag {4.1.39} \\ \end{array}
$$

The final time $t_{f}$ is specified at 20, the final state $\mathbf{x}(t_{f})$ is free and the admissible controls and states are unbounded. It is required to keep the state $x_{1}(t)$ close to 1. Obtain the feedback control law and plot all the time histories of Riccati coefficients, g vector components, optimal states and control.

Solution: The performance index indicates that the state $x_{1}(t)$ is to be kept close to the reference input $z_{1}(t)=1$ and since there is no condition on state $x_{2}(t)$ , one can choose arbitrarily as $z_{2}(t)=0$ . Now, in our present case, with $\mathbf{e}(t)=\mathbf{z}(t)-\mathbf{C}\mathbf{x}(t)$ , we have $e_{1}(t)=z_{1}(t)-x_{1}(t)$ , $e_{2}(t)=z_{2}(t)-x_{2}(t)$ and C=I.

Next, let us identify the various matrices in the present tracking system by comparing the state (4.1.38) and the PI (4.1.39) of the present system (note the absence of the factor 1/2 in PI) with the corresponding state (4.1.29) and the PI (4.1.30), respectively, of the general formulation of the problem, we get

$$
\mathbf {A} = \left[ \begin{array}{l l} 0 & 1 \\ - 2 & - 3 \end{array} \right]; \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right]; \quad \mathbf {C} = \mathbf {I}; \quad \mathbf {z} (t) = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right];

\mathbf {Q} = \left[ \begin{array}{l l} 2 & 0 \\ 0 & 0 \end{array} \right] = \mathbf {F} (t _ {f}); \quad \mathbf {R} = r = 0. 0 0 4. \tag {4.1.40}
$$

Let $\mathbf{P}(t)$ be the 2x2 symmetric matrix and $\mathbf{g}(t)$ be the 2x1 vector as

$$
\mathbf {P} (t) = \left[ \begin{array}{l l} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right]; \quad \mathbf {g} (t) = \left[ \begin{array}{l} g _ {1} (t) \\ g _ {2} (t) \end{array} \right]. \tag {4.1.41}
$$

Then, the optimal control given by (4.1.31) becomes

$$u ^ {*} (t) = - 2 5 0 \left[ p _ {1 2} x _ {1} ^ {*} (t) + p _ {2 2} x _ {2} ^ {*} (t) - g _ {2} (t) \right] \tag {4.1.42}$$
