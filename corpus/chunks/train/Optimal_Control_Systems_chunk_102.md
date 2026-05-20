Thus, the introduction of the Lagrange multiplier $\lambda(t)$ has enabled us to treat the variables $x_{1}(t)$ and $x_{2}(t)$ as though they were independent, in spite of the fact that they are related by the condition (2.6.2). The solution of the two, second-order differential equations (2.6.16) and (2.6.17) and the condition relation (2.6.2) or (2.6.18) along with the boundary conditions (2.6.3) give the optimal solutions $x_{1}^{*}(t)$ , $x_{2}^{*}(t)$ , and $\lambda^{*}(t)$ .

Now, we generalize the preceding procedure for an nth order system. Consider the extremization of a functional

$$J = \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) d t \tag {2.6.19}$$

where, $\mathbf{x}(t)$ is an $n$ th order state vector, subject to the plant equation (condition)

$$g _ {i} (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) = 0; \quad i = 1, 2, \dots , m \tag {2.6.20}$$

and boundary conditions, $\mathbf{x}(0)$ and $\mathbf{x}(t_f)$ . We form an augmented functional

$$J _ {a} = \int_ {t _ {0}} ^ {t _ {f}} \mathcal {L} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \boldsymbol {\lambda} (t), t) d t \tag {2.6.21}$$

where, the Lagrangian $\mathcal{L}$ is given by

$$\mathcal {L} (\mathbf {x} (t), \dot {\mathbf {x}} (t), \boldsymbol {\lambda} (t), t) = V (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) + \boldsymbol {\lambda} ^ {\prime} (t) g _ {i} (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) \tag {2.6.22}$$

and the Lagrange multiplier $\lambda(t) = [\lambda_1(t), \lambda_2(t), \ldots, \lambda_m(t)]'$ . We now apply the Euler-Lagrange equation on $J_a$ to yield

$$\left(\frac {\partial \mathcal {L}}{\partial \mathbf {x}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} = 0, \tag {2.6.23}\left(\frac {\partial \mathcal {L}}{\partial \boldsymbol {\lambda}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\boldsymbol {\lambda}}}\right) _ {*} = 0 \longrightarrow g _ {i} (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) = 0. \tag {2.6.24}$$

Note that from (2.6.22), the Lagrangian $\mathcal{L}$ is independent of $\dot{\lambda}(t)$ and hence the Euler-Lagrange equation (2.6.24) is nothing but the given relation regarding the plant or the system (2.6.20). Thus, we solve the Euler-Lagrange equation (2.6.23) along with the given boundary conditions. Let us now illustrate the preceding method by a simple example.
