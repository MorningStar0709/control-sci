$$
\begin{array}{l} y = h (\chi) + \nu \quad \eta = h (\chi) \\ y = h (\hat {x}) + \hat {v} \quad \hat {y} = h (\hat {x}) \\ \end{array}
$$

We begin with a reasonably general definition of the full information estimator that produces an estimator that is stable, which we also shall define subsequently. The full information objective function is

$$V _ {T} (\chi (0), \boldsymbol {\omega}) = \ell_ {x} \big (\chi (0) - \overline {{x}} _ {0} \big) + \sum_ {i = 0} ^ {T - 1} \ell_ {i} (\boldsymbol {\omega} (i), \nu (i)) \tag {4.2}$$

subject to

$$\chi^ {+} = f (\chi , \omega) \quad y = h (\chi) + \nu$$

in which T is the current time, $y ( i )$ is the measurement at time i, and $\overline { { x } } _ { 0 }$ is the prior information on the initial state.1 Because $\nu = y - h ( \chi )$ is the error in fitting the measurement y, $\ell _ { i } ( \omega , \nu )$ costs the model disturbance and the fitting error. These are the two error sources we reconcile in all state estimation problems.

The full information estimator is then defined as the solution to

$$\min _ {\chi (0), \boldsymbol {\omega}} V _ {T} (\chi (0), \boldsymbol {\omega}) \tag {4.3}$$

We denote the solution as $\hat { x } ( 0 | T ) , \hat { w } ( i | T ) , 0 \leq i \leq T - 1 , T \geq 1$ , and the optimal cost as $V _ { T } ^ { 0 }$ . We also use ${ \hat { x } } ( T ) : = { \hat { x } } ( T | T )$ to simplify the notation. The optimal solution and cost also depend on the measurement sequence $\mathbf { y } ,$ and the prior $\overline { { x } } _ { 0 }$ , but this dependency is made explicit only when necessary. The choice of stage costs $\ell _ { x } ( \cdot )$ and $\ell _ { i } ( \cdot )$ is made after we define the class of disturbances affecting the system.

The next order of business is to decide what class of systems to consider if the goal is to obtain a stable state estimator. A standard choice in most nonlinear estimation literature is to assume system observability. The drawback with this choice is that it is overly restrictive for even linear systems. As discussed in Chapter 1, for linear systems we require only detectability for stable estimation (Exercise 1.33). We therefore start instead with an assumption of detectability that is appropriate for nonlinear systems. First we require the definition of i-IOSS (Sontag and Wang, 1997)
