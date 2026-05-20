# 7.2.2 Problem Solution

Our problem solution consists of the list of the following steps with the details following.

- Step 1: Performance Index   
- Step 2: Hamiltonian   
- Step 3: Minimization of Hamiltonian   
- Step 4: Costate Solutions   
- Step 5: Time-Optimal Control Sequences   
- Step 6: State Trajectories   
- Step 7: Switch Curve   
- Step 8: Phase Plane Regions   
- Step 9: Control Law   
- Step 10: Minimum Time

\- Step 1: Performance Index: For minimum-time system, the performance index (7.1.16) is easily seen to be

$$J = \int_ {t _ {0}} ^ {t _ {f}} 1 d t = t _ {f} - t _ {0} \tag {7.2.5}$$

where, $t_0$ is fixed and $t_f$ is free.

\- Step 2: Hamiltonian: From the system (7.2.3) and the PI (7.2.5), form the Hamiltonian (7.1.17) as

$$\mathcal {H} (\mathbf {x} (t), \boldsymbol {\lambda} (t), u (t)) = 1 + \lambda_ {1} (t) x _ {2} (t) + \lambda_ {2} (t) u (t). \tag {7.2.6}$$

\- Step 3: Minimization of Hamiltonian: According to the Pontryagin Principle, we need to minimize the Hamiltonian as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), u ^ {*} (t)) \leq \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), u (t),) \\ = \min _ {| \mathbf {u} | \leq 1} \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), u (t)). \tag {7.2.7} \\ \end{array}
$$

Using the Hamiltonian (7.2.6) in the condition (7.2.7), we have

$$1 + \lambda_ {1} ^ {*} (t) x _ {2} ^ {*} (t) + \lambda_ {2} ^ {*} (t) u ^ {*} (t)\leq 1 + \lambda_ {1} ^ {*} (t) x _ {2} ^ {*} (t) + \lambda_ {2} ^ {*} (t) u (t) \tag {7.2.8}$$

which leads to

$$\lambda_ {2} ^ {*} (t) u ^ {*} (t) \leq \lambda_ {2} ^ {*} (t) u (t). \tag {7.2.9}$$

Using the result of the previous section, we have the optimal control (7.1.27) given in terms of the signum function as

$$u ^ {*} (t) = - s g n \{\lambda_ {2} ^ {*} (t) \}. \tag {7.2.10}$$

Now to know the nature of the optimal control, we need to solve for the costate function $\lambda_2^*(t)$ .

\- Step 4: Costate Solutions: The costate equations (7.1.19) along with the Hamiltonian (7.2.6) are

$$\dot {\lambda} _ {1} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {1} ^ {*}} = 0,\dot {\lambda} _ {2} ^ {*} (t) = - \frac {\partial \mathcal {H}}{\partial x _ {2} ^ {*}} = - \lambda_ {1} ^ {*} (t). \tag {7.2.11}$$

Solving the previous equations, we get the costates as

$$\lambda_ {1} ^ {*} (t) = \lambda_ {1} ^ {*} (0),\lambda_ {2} ^ {*} (t) = \lambda_ {2} ^ {*} (0) - \lambda_ {1} (0) t. \tag {7.2.12}$$
