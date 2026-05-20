# Example 2.14

Consider the same Example 2.12 with changed boundary conditions as

$$
\mathbf {x} (0) = \left[ \begin{array}{c c} 1 & 2 \end{array} \right] ^ {\prime}; \quad x _ {1} (2) = 0; \quad x _ {1} \left(t _ {f}\right) = 3; \quad x _ {2} \left(t _ {f}\right) \text {is free.} \tag {2.7.64}
$$

Find the optimal control and optimal state.

Solution: Following the procedure illustrated in Table 2.1 (Type (e)), we get the same optimal control, states and costates as given in (2.7.54) and (2.7.55) which are repeated here for convenience.

$$
\begin{array}{l} x _ {1} ^ {*} (t) = \frac {C _ {3}}{6} t ^ {3} - \frac {C _ {4}}{2} t ^ {2} + C _ {2} t + C _ {1}, \\ x _ {2} ^ {*} (t) = \frac {C _ {3}}{2} t ^ {2} - C _ {4} t + C _ {2}, \\ \lambda_ {1} ^ {*} (t) = C _ {3}, \\ \lambda_ {2} ^ {*} (t) = - C _ {3} t + C _ {4}, \\ u ^ {*} (t) = - \lambda_ {2} ^ {*} (t) = C _ {3} t - C _ {4}. \tag {2.7.65} \\ \end{array}
$$

The only difference is in solving for the constants $C_1$ to $C_4$ and the unknown $t_f$ . First of all, note that the performance index (2.7.47) does not contain the terminal cost function $S$ , that is, $S = 0$ . From the given boundary conditions (2.7.64), we have $t_f$ unspecified and hence $\delta t_f$ is free in the general boundary condition (2.7.32) leading to the specific final condition

$$\left(\mathcal {H} + \frac {\partial S}{\partial t}\right) _ {t _ {f}} = 0 \longrightarrow \lambda_ {1} (t _ {f}) x _ {2} (t _ {f}) - 0. 5 \lambda_ {2} ^ {2} (t _ {f}) = 0 \tag {2.7.66}$$

Also, since $x_{2}(t_{f})$ is free, $\delta x_{2_f}$ is arbitrary and hence the general boundary condition (2.7.32) becomes

$$\lambda_ {2} \left(t _ {f}\right) = \left(\frac {\partial S}{\partial x _ {2}}\right) = 0 \tag {2.7.67}$$

where $\mathcal{H}$ is given by (2.7.52). Combining (2.7.64), (2.7.66) and (2.7.67), we have the following 5 boundary conditions for the 5 unknowns (4 constants of integration $C_1$ to $C_4$ and 1 unknown $t_f$ ) as

$$x _ {1} (0) = 1; \quad x _ {2} (0) = 2; \quad x _ {1} \left(t _ {f}\right) = 3;\lambda_ {2} (t _ {f}) = 0; \quad \lambda_ {1} (t _ {f}) x _ {2} (t _ {f}) - 0. 5 \lambda_ {2} ^ {2} (t _ {f}) = 0. \tag {2.7.68}$$

Using these boundary conditions along with (2.7.65), the constants are found to be

$$C _ {1} = 1; \quad C _ {2} = 2; \quad C _ {3} = 4 / 9; \quad C _ {4} = 4 / 3; \quad t _ {f} = 3. \tag {2.7.69}$$

Finally, the optimal states, costates, and control are given from
