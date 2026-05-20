# Numerical Solution

Even in the simplest cases there is no analytic solution to the Bellman equation (Eq. 7.17). It is therefore necessary to resort to numerical solution. One iteration of Eq. (7.17) involves

- Discretization of the loss $V$ in the variables of the hyperstate,   
- Evaluation of the integral in Eq. (7.18) using a quadrature formula, and   
- Minimization over $u(t - 1)$ for each combination of the discretized hyperstate.

Both V and u are functions of the hyperstate, so the storage requirements increase rapidly when the order of the system increases. Assume that the dimension of the hyperstate is 2 and that each variable is discretized into ten steps. Thus the loss and control tables contain 100 values each. Let the hyperstate have dimension 6, and let each variable be discretized in ten steps. The dimension of the loss and control tables is then $10^{6}$ each. This means that only very simple problems have been solved numerically because of the “curse of dimensionality.”
