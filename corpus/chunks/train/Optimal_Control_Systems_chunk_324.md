# 6.2 Pontryagin Minimum Principle

In the above,

1. if the optimal state $\mathbf{x}^{*}(t)$ equations are satisfied, it results in the state relation (6.1.6),   
2. if the costate $\lambda^{*}(t)$ is selected so that the coefficient of the dependent variation $\delta \mathbf{x}(t)$ in the integrand is identically zero, it results in the costate condition (6.1.7), and   
3. the boundary condition is selected such that it results in the auxiliary boundary condition (6.1.8).

When the previous items are satisfied, then the first variation (6.2.6) becomes

$$\delta J (\mathbf {u} ^ {*} (t), \delta \mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f}} \left[ \frac {\partial \mathcal {H}}{\partial \mathbf {u}} \right] ^ {\prime} \delta \mathbf {u} (t) d t. \tag {6.2.7}$$

The integrand in the previous relation is the first order approximation to change in the Hamiltonian H due to a change in $\mathbf{u}(t)$ alone. This means that by definition

$$
\begin{array}{l} \left[ \frac {\partial \mathcal {H}}{\partial \mathbf {u}} \left(\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t\right) \right] ^ {\prime} \delta \mathbf {u} (t) \equiv \\ \mathcal {H} \left(\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t) + \delta \mathbf {u} (t), \boldsymbol {\lambda} ^ {*} (t), t\right) - \mathcal {H} \left(\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t\right). \tag {6.2.8} \\ \end{array}
$$

Then, using (6.2.8) in the first variation (6.2.7), we have

$$
\begin{array}{l} \delta J (\mathbf {u} ^ {*} (t), \delta \mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f}} [ \mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t) + \delta \mathbf {u} (t), \boldsymbol {\lambda} ^ {*} (t), t) \\ - \left. \mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t) \right] d t. \tag {6.2.9} \\ \end{array}
$$

Now, using the above, the necessary condition (6.2.5) becomes

$$\int_ {t _ {0}} ^ {t _ {f}} \left[ \mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t) + \delta \mathbf {u} (t), \boldsymbol {\lambda} ^ {*} (t), t) - \mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), t) \right] d t \geq 0 \tag {6.2.10}$$

for all admissible $\delta \mathbf{u}(t)$ less than a small value. The relation (6.2.10) becomes
