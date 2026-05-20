2.9(a)</td></tr><tr><td colspan="3">(b).
Free-final time and fixed-final state system, Fig.
2.9(b)</td></tr><tr><td colspan="3">(c).
Fixed-final time and free-final state system, Fig.
2.9(c)</td></tr><tr><td colspan="3">(d).
Free-final time and dependent free-final state system, Fig.
2.9(d).</td></tr><tr><td colspan="3">(e).
Free-final time and independent free-final state system</td></tr><tr><td>Type</td><td>Substitutions</td><td>Boundary Conditions</td></tr><tr><td>(a)</td><td> $\delta t_f = 0, \delta \mathbf{x}_f = 0$ </td><td> $\mathbf{x}(t_0) = \mathbf{x}_0, \mathbf{x}(t_f) = \mathbf{x}_f$ </td></tr><tr><td>(b)</td><td> $\delta t_f \neq 0, \delta \mathbf{x}_f = 0$ </td><td> $\mathbf{x}(t_0) = \mathbf{x}_0, \mathbf{x}(t_f) = \mathbf{x}_f, \left[ \mathcal{H}^* + \frac{\partial S}{\partial t} \right]_{t_f} = 0$ </td></tr><tr><td>(c)</td><td> $\delta t_f = 0, \delta \mathbf{x}_f \neq 0$ </td><td> $\mathbf{x}(t_0) = \mathbf{x}_0, \boldsymbol{\lambda}^*(t_f) = \left( \frac{\partial S}{\partial \mathbf{x}} \right)_{*t_f}$ </td></tr><tr><td>(d)</td><td> $\delta \mathbf{x}_f = \dot{\boldsymbol{\theta}}(t_f) \delta t_f$ </td><td> $\mathbf{x}(t_0) = \mathbf{x}_0, \mathbf{x}(t_f) = \boldsymbol{\theta}(t_f)$  $\left[ \mathcal{H}^* + \frac{\partial S}{\partial t} + \left\{ \left( \frac{\partial S}{\partial \mathbf{x}} \right)_* - \boldsymbol{\lambda}^*(t) \right\}' \dot{\boldsymbol{\theta}}(t) \right]_{t_f} = 0$ </td></tr><tr><td>(e)</td><td> $\delta t_f \neq 0$  $\delta \mathbf{x}_f \neq 0$ </td><td> $\delta \mathbf{x}(t_0) = \mathbf{x}_0$  $\left[ \mathcal{H}^* + \frac{\partial S}{\partial t} \right]_{t_f} = 0, \left[ \left( \frac{\partial S}{\partial \mathbf{x}} \right)_* - \boldsymbol{\lambda}^*(t) \right]_{t_f} = 0$ </td></tr></table>

Here, $\mathbf{x}(t)$ and $\mathbf{u}(t)$ are $n-$ and $r-$ dimensional state and control vectors respectively. Let us note that $\mathbf{u}(t)$ is unconstrained. The entire procedure (called Pontryagin Principle) is now summarized in Table 2.1.

Note: From Table 2.1 we note that the only difference in the procedure between the free-final point system without the final cost function (Lagrange problem) and free-final point system with final cost function (Bolza problem) is in the application of the general boundary condition.

To illustrate the Pontryagin method described previously, consider the following simple examples describing a second order system. Specifically, we selected a double integral plant whose analytical solutions for the optimal condition can be obtained and the same verified by using MATLAB $^{©}$ .

First we consider the fixed-final time and fixed-final state problem (Figure 2.9(a), Table 2.1, Type (a)).
