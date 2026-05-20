where, the nxn matrix $\mathbf{M}(t)$ is yet to be determined. Note the difference between the transformations (4.3.12) and (4.3.13). Now as before in the case of free-end-point system, by simple manipulation of the state and costate system (4.3.11) and (4.3.13) (that is, eliminating $\mathbf{x}^* (t)$ ), we obtain

$$\dot {\mathbf {x}} ^ {*} (t) = \dot {\mathbf {M}} (t) \boldsymbol {\lambda} ^ {*} (t) + \mathbf {M} (t) \dot {\boldsymbol {\lambda}} ^ {*} (t) \longrightarrow\left[ \dot {\mathbf {M}} (t) - \mathbf {A} (t) \mathbf {M} (t) - \mathbf {M} (t) \mathbf {A} ^ {\prime} (t) - \mathbf {M} (t) \mathbf {Q} (t) \mathbf {M} (t) + \right.\left. \mathbf {B} (t) \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} (t) \right] \boldsymbol {\lambda} ^ {*} (t) = 0. \tag {4.3.14}$$

Now, if the previous equation should be valid for all $t \in [t_0, t_f]$ , and for any arbitrary $\lambda^*(t)$ , we then have

$$\dot {\mathbf {M}} (t) = \mathbf {A} (t) \mathbf {M} (t) + \mathbf {M} (t) \mathbf {A} ^ {\prime} (t) + \mathbf {M} (t) \mathbf {Q} (t) \mathbf {M} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} (t). \tag {4.3.15}$$

Let us call this the inverse matrix differential Riccati equation (DRE) just to distinguish from the normal DRE (3.2.34).

\- Step 5: Boundary Conditions: Now the boundary condition for (4.3.15) is obtained as follows. Here, we have different cases to be discussed.

1. $\mathbf{x}(t_f) = 0$ and $\mathbf{x}(t_0) \neq 0$ : We know from the given boundary conditions (4.3.5) that $\mathbf{x}(t_f) = 0$ and using this in (4.3.13), we get

$$\mathbf {x} (t _ {f}) = 0 = \mathbf {M} (t _ {f}) \boldsymbol {\lambda} (t _ {f}). \tag {4.3.16}$$

For arbitrary $\lambda(t_f)$ , (4.3.16) becomes

$$\boxed {\mathbf {M} \left(t _ {f}\right) = 0.} \tag {4.3.17}$$

2. $\mathbf{x}(t_f) \neq 0$ and $\mathbf{x}(t_0) = 0$ : Here, at $t = t_0$ , (4.3.13) becomes

$$\mathbf {x} (t _ {0}) = 0 = \mathbf {M} (t _ {0}) \boldsymbol {\lambda} (t _ {0}) \tag {4.3.18}$$

and for arbitrary $\lambda(t_0)$ , (4.3.18) becomes

$$\mathbf {M} (t _ {0}) = 0. \tag {4.3.19}$$

Thus, we solve the inverse matrix DRE (4.3.15) backward using the final condition (4.3.17) or forward using the initial condition(4.3.19).

The optimal control (4.3.8) with the transformation (4.3.13) becomes

$$\boxed {\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {M} ^ {- 1} (t) \mathbf {x} ^ {*} (t).} \tag {4.3.20}$$
