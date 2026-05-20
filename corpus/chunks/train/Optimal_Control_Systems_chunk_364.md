$$\frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {P} (t _ {f}) \mathbf {x} (t _ {f}) = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}), \tag {6.5.18}$$

we have the final condition for $\mathbf{P}(t)$ as

$$\boxed {\mathbf {P} (t _ {f}) = \mathbf {F} (t _ {f}).} \tag {6.5.19}$$

\- Step 5: Using (6.5.5) and (6.5.12), we have the closed-loop optimal control as

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t). \tag {6.5.20}$$

Some noteworthy features of this result follow.

1. The HJB partial differential equation (6.5.8) reduces to a nonlinear, matrix, differential equation (6.5.17).   
2. The matrix $\mathbf{P}(t)$ is determined by numerically integrating backward from $t_{f}$ to $t_{0}$ . We also note that since the nxn $\mathbf{P}(t)$ matrix is symmetric, one need to solve only $n(n+1)/2$ instead of nxn equations.   
3. The reason for assuming the solution of the form (6.5.11) is that we are able to obtain a closed-loop optimal control, which is linear, and time-varying w.r.t. the state.   
4. A necessary condition: The result that has been obtained is only the necessary condition for optimality in the sense that the minimum cost function $J^{*}(\mathbf{x}(t), t)$ must satisfy the HJB equation.
