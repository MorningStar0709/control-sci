# 5.3.1 Closed-Loop Optimal Control: Matrix Difference Riccati Equation

In order to obtain closed-loop optimal configuration, we need to try to express the costate function $\boldsymbol{\lambda}^{*}(k+1)$ in the optimal control (5.3.2) in terms of the state function $\mathbf{x}^{*}(k)$ . The final condition (5.3.5) prompts us to express

$$\boldsymbol {\lambda} ^ {*} (k) = \mathbf {P} (k) \mathbf {x} ^ {*} (k) \tag {5.3.6}$$

where, $\mathbf{P}(k)$ is yet to be determined. This linear transformation is called the Riccati transformation, and is of fundamental importance in the solution of the problem. Using the transformation (5.3.6) in the state and costate equations (5.3.3) and (5.3.4), we have

$$\mathbf {P} (k) \mathbf {x} ^ {*} (k) = \mathbf {Q} (k) \mathbf {x} ^ {*} (k) + \mathbf {A} ^ {\prime} (k) \mathbf {P} (k + 1) \mathbf {x} ^ {*} (k + 1) \tag {5.3.7}$$

and

$$\mathbf {x} ^ {*} (k + 1) = \mathbf {A} (k) \mathbf {x} ^ {*} (k) - \mathbf {E} (k) \mathbf {P} (k + 1) \mathbf {x} ^ {*} (k + 1). \tag {5.3.8}$$

Solving for $\mathbf{x}^{*}(k + 1)$ from (5.3.8)

$$\mathbf {x} ^ {*} (k + 1) = [ \mathbf {I} + \mathbf {E} (k) \mathbf {P} (k + 1) ] ^ {- 1} \mathbf {A} (k) \mathbf {x} ^ {*} (k). \tag {5.3.9}$$

Substituting (5.3.9) in (5.3.7) yields

$$\mathbf {P} (k) \mathbf {x} ^ {*} (k) = \mathbf {Q} (k) \mathbf {x} ^ {*} (k) + \mathbf {A} ^ {\prime} (k) \mathbf {P} (k + 1) [ \mathbf {I} + \mathbf {E} (k) \mathbf {P} (k + 1) ] ^ {- 1} \mathbf {A} (k) \mathbf {x} ^ {*} (k). \tag {5.3.10}$$

Since, this relation (5.3.10) must hold for all values of $\mathbf{x}^*(k)$ , we have

$$\boxed {\mathbf {P} (k) = \mathbf {A} ^ {\prime} (k) \mathbf {P} (k + 1) [ \mathbf {I} + \mathbf {E} (k) \mathbf {P} (k + 1) ] ^ {- 1} \mathbf {A} (k) + \mathbf {Q} (k).} \tag {5.3.11}$$

This relation (5.3.11) is called the matrix difference Riccati equation (DRE). Alternatively, we can express (5.3.11) as

$$\mathbf {P} (k) = \mathbf {A} ^ {\prime} (k) \left[ \mathbf {P} ^ {- 1} (k + 1) + \mathbf {E} (k) \right] ^ {- 1} \mathbf {A} (k) + \mathbf {Q} (k) \tag {5.3.12}$$

where, we assume that the inversion of $\mathbf{P}(k)$ exists for all $k \neq k_{f}$ . The final condition for solving the matrix DRE (5.3.11) or (5.3.12) is obtained from (5.3.5) and (5.3.6) as

$$\boldsymbol {\lambda} (k _ {f}) = \mathbf {F} (k _ {f}) \mathbf {x} (k _ {f}) = \mathbf {P} (k _ {f}) \mathbf {x} (k _ {f}), \tag {5.3.13}$$

which gives
