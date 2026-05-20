# 5.4.1 Analytical Solution to the Riccati Equation

This subsection is based on $[89, 138]$ . The solution of the matrix difference Riccati equation is critical for linear quadratic regulator system. Thus, traditionally, the solution to the DRE (5.3.20) is obtained by iteration in a recursive manner using the final condition (5.3.14). Alternatively, one can obtain analytical solution to the DRE.

Let us rewrite the Hamiltonian system (5.2.22) arising in the time-invariant LQR system as (omitting the optimal notation (\*) for clarity)

$$
\left[ \begin{array}{l} \mathbf {x} (k) \\ \boldsymbol {\lambda} (k) \end{array} \right] = \mathbf {H} \left[ \begin{array}{l} \mathbf {x} (k + 1) \\ \boldsymbol {\lambda} (k + 1) \end{array} \right]. \tag {5.4.12}
$$

Here, the Hamiltonian matrix $\mathbf{H}$ is

$$
\mathbf {H} = \left[ \begin{array}{l l} \mathbf {H} _ {1 1} & \mathbf {H} _ {1 2} \\ \mathbf {H} _ {2 1} & \mathbf {H} _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} ^ {- 1} & \mathbf {A} ^ {- 1} \mathbf {E} \\ \mathbf {Q A} ^ {- 1} & \mathbf {A} ^ {\prime} + \mathbf {Q A} ^ {- 1} \mathbf {E} \end{array} \right] \tag {5.4.13}
$$

![](image/d55f70932bf8b84cc9ff772a4addb1ccfcd73b564b575b07099dda6239f7a95f.jpg)

<details>
<summary>line</summary>

| k | x₁(k) | x₂(k) |
| --- | --- | --- |
| 0 | 5.0 | 0.0 |
| 1 | 2.9 | -0.3 |
| 2 | 1.1 | -0.6 |
| 3 | 0.3 | -0.4 |
| 4 | 0.0 | -0.1 |
| 5 | 0.0 | 0.0 |
| 6 | 0.0 | 0.0 |
| 7 | 0.0 | 0.0 |
| 8 | 0.0 | 0.0 |
| 9 | 0.0 | 0.0 |
| 10 | 0.0 | 0.0 |
</details>

Figure 5.7 Implementation of Optimal Control for Example 5.4 where,

$$\mathbf {E} = \mathbf {B R} ^ {- 1} \mathbf {B} ^ {\prime}.$$

Let us note that

$$\mathbf {H} _ {1 1} \mathbf {H} _ {2 2} - \mathbf {H} _ {1 2} \mathbf {H} _ {2 1} = \mathbf {I}. \tag {5.4.14}$$

The boundary conditions for (5.4.12) are reproduced here from (5.3.1) and (5.3.5) as

$$\mathbf {x} (k = k _ {0}) = \mathbf {x} _ {0}; \quad \boldsymbol {\lambda} (k = k _ {f}) = \mathbf {P} (k = k _ {f}) \mathbf {x} (k _ {f}). \tag {5.4.15}$$

Also, in trying to obtain the difference Riccati equation, we assumed a transformation (5.3.6) between the state and costate as

$$\boldsymbol {\lambda} (k) = \mathbf {P} (k) \mathbf {x} (k); \quad \forall k \leq k _ {f}. \tag {5.4.16}$$
