# 3.2 Finite-Time Linear Quadratic Regulator

2. The initial condition $\mathbf{x}(t=t_{0})=\mathbf{x}_{0}$ is given. The terminal time $t_{f}$ is specified, and the final state $\mathbf{x}(t_{f})$ is not specified.

3. The terminal cost matrix $\mathbf{F}(t_{f})$ and the error weighted matrix $\mathbf{Q}(t)$ are nxn positive semidefinite matrices, respectively; and the control weighted matrix $\mathbf{R}(t)$ is an rxr positive definite matrix.

4. Finally, the fraction $\frac{1}{2}$ in the cost functional (3.2.2) is associated mainly to cancel a 2 that would have otherwise been carried on throughout the result, as seen later.

We follow the Pontryagin procedure described in Chapter 2 (Table 2.1) to obtain optimal solution and then propose the closed-loop configuration. First, let us list the various steps under which we present the method.

\- Step 1: Hamiltonian

\- Step 2: Optimal Control

\- Step 3: State and Costate System

\- Step 4: Closed-Loop Optimal Control

\- Step 5: Matrix Differential Riccati Equation

Now let us discuss the preceding steps in detail.

\- Step 1: Hamiltonian: Using the definition of the Hamiltonian given by (2.7.27) in Chapter 2 along with the performance index (3.2.2), formulate the Hamiltonian as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t)) = \frac {1}{2} \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \\ + \boldsymbol {\lambda} ^ {\prime} (t) [ \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) ] \tag {3.2.3} \\ \end{array}
$$

where, $\lambda(t)$ is the costate vector of $n$ th order.

\- Step 2: Optimal Control: Obtain the optimal control $\mathbf{u}^{*}(t)$ using the control relation (2.7.29) as

$$\frac {\partial \mathcal {H}}{\partial \mathbf {u}} = 0 \longrightarrow \mathbf {R} (t) \mathbf {u} ^ {*} (t) + \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) = 0 \tag {3.2.4}$$

leading to

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \tag {3.2.5}$$

where, we used
