# Example 5.2

Consider the minimization of the performance index (PI) [120]

$$J (k _ {0}) = \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} u ^ {2} (k), \tag {5.2.24}$$

subject to the boundary conditions

$$x (k _ {0} = 0) = 1, \quad x (k _ {f} = 1 0) = 0 \tag {5.2.25}$$

for a simple scalar system

$$x (k + 1) = x (k) + u (k). \tag {5.2.26}$$

Solution: Let us first identify the various matrices by comparing the present state (5.2.26) and the PI (5.2.24) with the corresponding general formulation of the state (5.2.1) and the PI (5.2.3),

respectively, to get

$$\mathbf {A} (k) = 1; \quad \mathbf {B} (k) = 1; \quad \mathbf {F} (k _ {f}) = 0; \quad \mathbf {Q} (k) = 0; \quad \mathbf {R} (k) = 1. \tag {5.2.27}$$

Now let us use the procedure given in Table 5.1.

\- Step 1: Form the Pontryagin $\mathcal{H}$ function as

$$\mathcal {H} (x (k), u (k), \lambda (k + 1)) = \frac {1}{2} u ^ {2} (k) + \lambda (k + 1) [ x (k) + u (k) ]. \tag {5.2.28}$$

\- Step 2: Minimizing $\mathcal{H}$ of (5.2.28) w.r.t. $u(k)$

$$\frac {\partial \mathcal {H}}{\partial u (k)} = 0 \longrightarrow u ^ {*} (k) + \lambda^ {*} (k + 1) = 0 \longrightarrow u ^ {*} (k) = - \lambda^ {*} (k + 1). \tag {5.2.29}$$

\- Step 3: Using the control relation (5.2.29) and the Hamiltonian (5.2.28), form the optimal $\mathcal{H}^*$ function

$$\mathcal {H} ^ {*} (x ^ {*} (k), \lambda^ {*} (k + 1)) = x ^ {*} (k) \lambda^ {*} (k + 1) - \frac {1}{2} \lambda^ {* 2} (k + 1). \tag {5.2.30}$$

\- Step 4: Obtain the set of 2 state and costate difference equations

$$x ^ {*} (k + 1) = \frac {\partial \mathcal {H} ^ {*}}{\partial \lambda^ {*} (k + 1)} \longrightarrow x ^ {*} (k + 1) = x ^ {*} (k) - \lambda^ {*} (k + 1) \tag {5.2.31}$$

and

$$\lambda^ {*} (k) = \frac {\partial \mathcal {H} ^ {*}}{\partial x ^ {*} (k)} \longrightarrow \lambda^ {*} (k) = \lambda^ {*} (k + 1). \tag {5.2.32}$$

Solving these 2 equations (5.2.31) and (5.2.32) (by first eliminating $\lambda(k)$ and solving for $x(k)$ ) along with the boundary conditions (5.2.25), we get the optimal solutions as

$$x ^ {*} (k) = 1 - 0. 1 k; \quad \lambda^ {*} (k + 1) = 0. 1. \tag {5.2.33}$$

\- Step 5: Using the previous state and costate solutions, the optimal control $u^{*}(k)$ is obtained from (5.2.29) as

$$u ^ {*} (k) = - 0. 1. \tag {5.2.34}$$
