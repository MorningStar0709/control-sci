- Step 1: Augmented Performance Index   
- Step 2: Lagrangian   
- Step 3: Euler-Lagrange Equation   
- Step 4: Hamiltonian   
- Step 5: Open-Loop Optimal Control   
- Step 6: State and Costate System

Now these steps are described in detail.

\- Step 1: Augmented Performance Index: First, we formulate an augmented cost functional by adjoining the original cost functional (5.2.3) with the condition or plant relation (5.2.1) using Lagrange multiplier (later to be called as costate function) $\lambda(k+1)$ as

$$
\begin{array}{l} J _ {a} = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f}) \mathbf {F} (k _ {f}) \mathbf {x} (k _ {f}) \\ + \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ \mathbf {x} ^ {\prime} (k) \mathbf {Q} (k) \mathbf {x} (k) + \mathbf {u} ^ {\prime} (k) \mathbf {R} (k) \mathbf {u} (k) \right] \\ + \boldsymbol {\lambda} (k + 1) [ \mathbf {A} (k) \mathbf {x} (k) + \mathbf {B} (k) \mathbf {u} (k) - \mathbf {x} (k + 1) ]. \tag {5.2.4} \\ \end{array}
$$

Minimization of the augmented cost functional (5.2.4) is the same as that of the original cost functional (5.2.3), since $J = J_{a}$ . The reason for associating the stage $(k + 1)$ with the Lagrange multiplier $\lambda(k + 1)$ is mainly the simplicity of the final result as will be apparent later.

\- Step 2: Lagrangian: Let us now define a new function called Lagrangian as

$$
\begin{array}{l} \mathcal {L} (\mathbf {x} (k), \mathbf {u} (k), \mathbf {x} (k + 1), \boldsymbol {\lambda} (k + 1)) \\ = \frac {1}{2} \mathbf {x} ^ {\prime} (k) \mathbf {Q} (k) \mathbf {x} (k) + \frac {1}{2} \mathbf {u} ^ {\prime} (k) \mathbf {R} (k) \mathbf {u} (k) \\ + \lambda^ {\prime} (k + 1) [ \mathbf {A} (k) \mathbf {x} (k) + \mathbf {B} (k) \mathbf {u} (k) - \mathbf {x} (k + 1) ]. \tag {5.2.5} \\ \end{array}
$$

\- Step 3: Euler-Lagrange Equations: We now apply the Euler-Lagrange (EL) equation (5.1.21) to this new function $\mathcal{L}$ with respect to the variables $\mathbf{x}(k)$ , $\mathbf{u}(k)$ , and $\boldsymbol{\lambda}(k+1)$ . Thus, we get
