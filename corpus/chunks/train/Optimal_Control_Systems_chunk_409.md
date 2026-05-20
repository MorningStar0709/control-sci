![](image/cf306c4f1ce93be63eb41011ae08f2f1a171d4390b2572e5a131d90244b9a87e.jpg)

<details>
<summary>line</summary>

| Time Point | Value |
| --- | --- |
| t0 | 0 |
| T1 | -1 |
| T2 | -1 |
| T3 | 0 |
| T4 | 0 |
| tf | -1 |
</details>

Figure 7.26 Singular Fuel-Optimal Control System

This means that the function $\mathbf{q}^*(t)$ is constant and hence all its time derivatives must vanish. By repeated differentiation of (7.4.15) and using (7.4.12), we have

$$(\mathbf {A b} _ {j}) ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) = 0,(\mathbf {A} ^ {2} \mathbf {b} _ {j}) ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) = 0,$$

• • • • • • • • • • •

$$\left(\mathbf {A} ^ {n - 1} \mathbf {b} _ {j}\right) ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) = 0,(\mathbf {A} ^ {n} \mathbf {b} _ {j}) ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) = 0, \tag {7.4.16}$$

for all $t \in [T_1, T_2]$ , where $j = 1, 2, \ldots, r$ . We can rewrite the previous set of equations as

$$[ \mathbf {A} \mathbf {G} _ {j} ] ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) = 0 \tag {7.4.17}$$

where,

$$\mathbf {G} _ {j} = [ \mathbf {b} _ {j}, \mathbf {A b} _ {j}, \dots , \mathbf {A} ^ {n - 1} \mathbf {b} _ {j} ]. \tag {7.4.18}$$

The condition (7.4.17) can further be rewritten as

$$\mathbf {G} _ {j} ^ {\prime} \mathbf {A} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) = 0 \forall t \in [ T _ {1}, T _ {2} ]. \tag {7.4.19}$$

But the condition (7.4.15) implies that $\boldsymbol{\lambda}^{*}(t) \neq 0$ . Then, for (7.4.19) to hold, it is necessary that the matrix $G_{j}^{\prime}A^{\prime}$ must be singular. This means that

$$\det \{\mathbf {G} _ {j} ^ {\prime} \mathbf {A} ^ {\prime} \} = \det \mathbf {A} \det \mathbf {G} _ {\mathbf {j}} = 0. \tag {7.4.20}$$

Thus, the sufficient condition for the system to be normal is that

$$\boxed {\det \{\mathbf {G} _ {j} ^ {\prime} \mathbf {A} ^ {\prime} \} \neq 0 \quad \forall \quad j = 1, 2, \dots , r.} \tag {7.4.21}$$

Thus, if the system $(7.4.1)$ is normal (that is also controllable), and if the matrix A is nonsingular, then the fuel-optimal system is normal.

\- Step 5: Bang-off-Bang Control Law: If the linear, time-invariant system (7.4.1) is normal and $\mathbf{x}^{*}(t)$ and $\lambda^{*}(t)$ are the state and costate trajectories, then the optimal control law $\mathbf{u}^{*}(t)$ given by (7.4.10) is repeated here as

$$\mathbf {u} ^ {*} (t) = - D E Z \left\{\mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \right\} \tag {7.4.22}$$
