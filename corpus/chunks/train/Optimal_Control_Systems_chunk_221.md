# Example 4.2

Consider the same Example 4.1 with a different PI as

$$J = \int_ {t _ {0}} ^ {t _ {f}} \left[ [ 2 t - x _ {1} (t) ] ^ {2} + 0. 0 2 u ^ {2} (t) \right] d t \tag {4.1.49}$$

where, $t_{f}$ is specified and $\mathbf{x}(t_{f})$ is free. Find the optimal control in order that the state $x_{1}(t)$ track a ramp function $z_{1}(t)=2t$ and without much expenditure of control energy. Plot all the variables (Riccati coefficients, optimal states and control) for initial conditions $\mathbf{x}(0)=[-1\quad0]^{\prime}$ .

Solution: The performance index (4.1.49) indicates that the state $x_{1}(t)$ is to be kept close to the reference input $z_{1}(t)=2t$ and since there is no condition on state $x_{2}(t)$ , one can choose arbitrarily as $z_{2}(t)=0$ . Now, in our present case, with $\mathbf{e}(t)=\mathbf{z}(t)-\mathbf{C}\mathbf{x}(t)$ , we have $e_{1}(t)=z_{1}(t)-x_{1}(t)$ , $e_{2}(t)=z_{2}(t)-x_{2}(t)$ and C=I.

![](image/316d23f5972c912b3db28c2ad0ef948e432ea2e010fe3af4e8a46b873dc234d8.jpg)

<details>
<summary>line</summary>

| t | p₁₁(t) | p₁₂(t) | p₂₂(t) |
| --- | --- | --- | --- |
| 0 | 1.0 | 0.2 | 0.0 |
| 20 | 1.0 | 0.2 | 0.0 |
</details>

Figure 4.2 Riccati Coefficients for Example 4.1

Next, let us identify the various matrices in the present tracking system by comparing the state (4.1.38) and the PI (4.1.39) of the present problem (note the absence of the factor 1/2 in PI) with the corresponding state (4.1.29) and the PI (4.1.30), respectively, of the general formulation of the problem, we get

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right]; \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]; \quad \mathbf {C} = \mathbf {I}; \quad \mathbf {z} (t) = \left[ \begin{array}{c} 2 t \\ 0 \end{array} \right];

\mathbf {Q} = \left[ \begin{array}{l l} 2 & 0 \\ 0 & 0 \end{array} \right] \quad \mathbf {R} = r = 0. 0 4. \tag {4.1.50}
$$

Let $\mathbf{P}(t)$ be the 2x2 symmetric matrix and $\mathbf{g}(t)$ be the 2x1 vector as

$$
\mathbf {P} (t) = \left[ \begin{array}{l l} p _ {1 1} (t) & p _ {1 2} (t) \\ p _ {1 2} (t) & p _ {2 2} (t) \end{array} \right]; \quad \mathbf {g} (t) = \left[ \begin{array}{l} g _ {1} (t) \\ g _ {2} (t) \end{array} \right]. \tag {4.1.51}
$$

Then, the optimal control given by (4.1.31) becomes

$$u ^ {*} (t) = - 2 5 0 \left[ p _ {1 2} x _ {1} ^ {*} (t) + p _ {2 2} x _ {2} ^ {*} (t) - g _ {2} (t) \right] \tag {4.1.52}$$
