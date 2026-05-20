Now using (5.5.14) and (5.5.12) in the costate relation in (5.5.11), we have

$$
\begin{array}{l} \left[ - \mathbf {P} (k) + \mathbf {A} ^ {\prime} \mathbf {P} (k + 1) [ \mathbf {I} + \mathbf {E P} (k + 1) ] ^ {- 1} \mathbf {A} + \mathbf {V} \right] \mathbf {x} (k) + \\ \left[ \mathbf {g} (k) + \mathbf {A} ^ {\prime} \mathbf {P} (k + 1) [ \mathbf {I} + \mathbf {E P} (k + 1) ] ^ {- 1} \mathbf {E g} (k + 1) - \right. \\ \left. \mathbf {A} ^ {\prime} \mathbf {g} (k + 1) - \mathbf {W} \mathbf {z} (k) \right] = 0 \tag {5.5.15} \\ \end{array}
$$

This equation must hold for all values of the state $\mathbf{x}^{*}(k)$ which in turn leads to the fact that the coefficient of $\mathbf{x}(k)$ and the rest of the terms in (5.5.15) must individually vanish. That is

$$\boxed {\mathbf {P} (k) = \mathbf {A} ^ {\prime} \mathbf {P} (k + 1) [ \mathbf {I} + \mathbf {E P} (k + 1) ] ^ {- 1} \mathbf {A} + \mathbf {V}} \quad \text {or}\boxed {\mathbf {P} (k) = \mathbf {A} ^ {\prime} \left[ \mathbf {P} ^ {- 1} (k + 1) + \mathbf {E} \right] ^ {- 1} \mathbf {A} + \mathbf {V}} \tag {5.5.16}$$

and

$$\boxed {\mathbf {g} (k) = \mathbf {A} ^ {\prime} \left\{\mathbf {I} - \left[ \mathbf {P} ^ {- 1} (k + 1) + \mathbf {E} \right] ^ {- 1} \mathbf {E} \right\} \mathbf {g} (k + 1) + \mathbf {W z} (k)} \quad \text {or}\boxed {\mathbf {g} (k) = \left\{\mathbf {A} ^ {\prime} - \mathbf {A} ^ {\prime} \mathbf {P} (k + 1) [ \mathbf {I} + \mathbf {E P} (k + 1) ] ^ {- 1} \mathbf {E} \right\} \mathbf {g} (k + 1) + \mathbf {W} \mathbf {z} (k).} \tag {5.5.17}$$

To obtain the boundary conditions for (5.5.16) and (5.5.17), let us compare (5.5.9) and (5.5.12) to yield

$$\boxed {\mathbf {P} \left(k _ {f}\right) = \mathbf {C} ^ {\prime} \mathbf {F C}} \tag {5.5.18}\boxed {\mathbf {g} \left(k _ {f}\right) = \mathbf {C} ^ {\prime} \mathbf {F} \mathbf {z} \left(k _ {f}\right).} \tag {5.5.19}$$

Let us note that (5.5.16) is the nonlinear, matrix difference Riccati equation (DRE) to be solved backwards using the final condition (5.5.18), and the linear, vector difference equation (5.5.17) is solved backwards using the final condition (5.5.19).

\- Step 5: Closed-Loop Optimal Control: Once we obtain these solutions off-line, we are ready to use the transformation (5.5.12) in the control relation (5.5.10) to get the closed-loop optimal control as

$$\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} [ \mathbf {P} (k + 1) \mathbf {x} (k + 1) - \mathbf {g} (k + 1) ] \tag {5.5.20}$$
