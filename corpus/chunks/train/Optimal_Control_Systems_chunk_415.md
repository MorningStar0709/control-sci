# 7.5.2 Problem Solution

We present the solution to this energy-optimal system under the following steps. But first let us list the various steps involved.

- Step 1: Hamiltonian   
- Step 2: State and Costate Equations   
- Step 3: Optimal Condition   
- Step 4: Optimal Control   
- Step 5: Implementation

\- Step 1: Hamiltonian: Let us formulate the Hamiltonian for the system (7.5.2) and the PI (7.5.3) as

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t)) = \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {A x} (t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {B u} (t) \tag {7.5.6}$$

where, $\lambda(t)$ is the costate variable.

\- Step 2: State and Costate Equations: Let us assume optimal values $\mathbf{u}^{*}(t)$ , $\mathbf{x}^{*}(t)$ , and $\boldsymbol{\lambda}^{*}(t)$ . Then, the state $\mathbf{x}^{*}(t)$ and the costate $\boldsymbol{\lambda}^{*}(t)$ optimal values are given in terms of the Hamiltonian as

$$
\begin{array}{l} \dot {\mathbf {x}} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}}\right) _ {*} = \mathbf {A} (t) \mathbf {x} ^ {*} (t) + \mathbf {B} (t) \mathbf {u} ^ {*} (t) \\ \dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} = - \mathbf {A} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \tag {7.5.7} \\ \end{array}
$$

with the boundary conditions

$$\mathbf {x} (t _ {0}) = \mathbf {x} (t _ {0}); \quad \mathbf {x} (t _ {f}) = \mathbf {0} \tag {7.5.8}$$

where, we again note that $t_f$ is either fixed or free.

\- Step 3: Optimal Condition: Now using Pontryagin Principle, we invoke the condition for optimal control in terms of the Hamiltonian, that is,

$$
\begin{array}{l} \mathcal {H} \left(\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} ^ {*} (t)\right) \leq \mathcal {H} \left(\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} (t)\right) \\ = \min _ {| \mathbf {u} (t) | \leq 1} \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} (t)). \tag {7.5.9} \\ \end{array}
$$

Using (7.5.6) in (7.5.9), we have
