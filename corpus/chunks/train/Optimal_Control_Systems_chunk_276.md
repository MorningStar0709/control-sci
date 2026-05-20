$$\boxed {\mathbf {P} \left(k _ {f}\right) = \mathbf {F} \left(k _ {f}\right).} \tag {5.3.14}$$

In the matrix DRE (5.3.11), the term $\mathbf{P}(k)$ is on the left hand side and $\mathbf{P}(k+1)$ is on the right hand side and hence it needs to be solved backwards starting from the final condition (5.3.14). Since $\mathbf{Q}(k)$ and $\mathbf{F}(k_{f})$ are assumed to be positive semidefinite, we can show that the Riccati matrix $\mathbf{P}(k)$ is positive definite. Now to obtain the closed-loop optimal control, we eliminate $\boldsymbol{\lambda}^{*}(k+1)$ from the control relation (5.3.2) and the state relation (5.3.4) and use the transformation (5.3.6). Thus, we get the relation for closed-loop, optimal control as

$$\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \mathbf {A} ^ {- T} (k) [ \mathbf {P} (k) - \mathbf {Q} (k) ] \mathbf {x} ^ {*} (k). \tag {5.3.15}$$

Here, $A^{-T}$ is the inverse of $A'$ and we assume that the inverse of $\mathbf{A}(k)$ exists. This relation (5.3.15) is the desired version for the closed-loop
