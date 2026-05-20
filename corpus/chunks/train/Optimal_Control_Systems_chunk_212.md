$$\dot {\mathbf {g}} (t) = \left[ \mathbf {P} (t) \mathbf {E} (t) - \mathbf {A} ^ {\prime} (t) \right] \mathbf {g} (\mathbf {t}) - \mathbf {W} (\mathbf {t}) \mathbf {z} (\mathbf {t}). \tag {4.1.20}$$

Since $\mathbf{P}(t)$ is nxn symmetric matrix, and $\mathbf{g}(t)$ is of n vector, the equations (4.1.19) and (4.1.20) are a set of $n(n+1)/2 + n$ first-order differential equations. The boundary conditions are obtained from (4.1.15) as

$$\boldsymbol {\lambda} (t _ {f}) = \mathbf {P} (t _ {f}) \mathbf {x} (t _ {f}) - \mathbf {g} (t _ {f}), \tag {4.1.21}$$

which compared with the boundary condition (4.1.14) gives us for all $\mathbf{x}(t_f)$ and $\mathbf{z}(t_f)$ ,

$$\boxed {\mathbf {P} (t _ {f}) = \mathbf {C} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {C} (t _ {f}),} \tag {4.1.22}\boxed {\mathbf {g} (t _ {f}) = \mathbf {C} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {z} (t _ {f}).} \tag {4.1.23}$$

Thus, the matrix DRE (4.1.19) and the vector equation (4.1.20) are to be solved backward using the boundary conditions (4.1.22) and (4.1.23).

\- Step 5: Closed-Loop Optimal Control: The optimal control (4.1.7) is now given in terms of the state using the linear transformation (4.1.15)

$$
\begin{array}{l} \mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) [ \mathbf {P} (t) \mathbf {x} ^ {*} (t) - \mathbf {g} (t) ] \\ = - \mathbf {K} (t) \mathbf {x} ^ {*} (t) + \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {g} (t) \tag {4.1.24} \\ \end{array}
$$

where, $\mathbf{K}(t) = \mathbf{R}^{-1}(t)\mathbf{B}'(t)\mathbf{P}(t)$ , is the Kalman gain.

\- Step 6: Optimal State: Using this optimal control $\mathbf{u}^{*}(t)$ from (4.1.24) in the original plant (4.1.1), we have the optimal state obtained from

$$
\begin{array}{l} \dot {\mathbf {x}} ^ {*} (t) = \left[ \mathbf {A} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \right] \mathbf {x} ^ {*} (t) \\ + \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {g} (t) \\ = [ \mathbf {A} (t) - \mathbf {E} (t) \mathbf {P} (t) ] \mathbf {x} ^ {*} (t) + \mathbf {E} (t) \mathbf {g} (t). \tag {4.1.25} \\ \end{array}
$$

\- Step 7: Optimal Cost: The optimal cost $J^{*}(t)$ for any time $t$ can be obtained as (see [6])

$$J ^ {*} (t) = \frac {1}{2} \mathbf {x} ^ {* \prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) - \mathbf {x} ^ {* \prime} (t) \mathbf {g} (t) + \mathbf {h} (t) \tag {4.1.26}$$
