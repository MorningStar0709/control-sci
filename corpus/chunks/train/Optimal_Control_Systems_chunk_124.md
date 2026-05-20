# Example 2.12

Given a second order (double integrator) system as

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = u (t) \tag {2.7.46}$$

and the performance index as

$$J = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} u ^ {2} (t) d t \tag {2.7.47}$$

find the optimal control and optimal state, given the boundary (initial and final) conditions as

$$\mathbf {x} (0) = [ 1 \quad 2 ] ^ {\prime}; \quad \mathbf {x} (2) = [ 1 \quad 0 ] ^ {\prime}. \tag {2.7.48}$$

Assume that the control and state are unconstrained.

Solution: We follow the step-by-step procedure given in Table 2.1. First, by comparing the present plant (2.7.46) and the PI (2.7.47) with the general formulation of the plant (2.7.1) and the PI (2.7.2), we identify

$$V (\mathbf {x} (t), \mathbf {u} (t), t) = V (u (t)) = \frac {1}{2} u ^ {2} (t)\mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) = [ f _ {1}, f _ {2} ] ^ {\prime}, \tag {2.7.49}$$

where, $f_{1} = x_{2}(t)$ , $f_{2} = u(t)$ .

\- Step 1: Form the Hamiltonian function as

$$
\begin{array}{l} \mathcal {H} = \mathcal {H} (x _ {1} (t), x _ {2} (t), u (t), \lambda_ {1} (t), \lambda_ {2} (t)) \\ = V (u (t)) + \lambda^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t)) \\ = \frac {1}{2} u ^ {2} (t) + \lambda_ {1} (t) x _ {2} (t) + \lambda_ {2} (t) u (t). \tag {2.7.50} \\ \end{array}
$$

\- Step 2: Find $u^{*}(t)$ from

$$\frac {\partial \mathcal {H}}{\partial u} = 0 \longrightarrow u ^ {*} (t) + \lambda_ {2} ^ {*} (t) = 0 \longrightarrow u ^ {*} (t) = - \lambda_ {2} ^ {*} (t). \tag {2.7.51}$$

\- Step 3: Using the results of Step 2 in Step 1, find the optimal $\mathcal{H}^*$ as

$$
\begin{array}{l} \mathcal {H} ^ {*} (x _ {1} ^ {*} (t), x _ {2} ^ {*} (t), \lambda_ {1} ^ {*} (t), \lambda_ {2} ^ {*} (t)) = \frac {1}{2} \lambda_ {2} ^ {* ^ {2}} (t) + \lambda_ {1} ^ {*} (t) x _ {2} ^ {*} (t) - \lambda_ {2} ^ {* ^ {2}} (t) \\ = \lambda_ {1} ^ {*} (t) x _ {2} ^ {*} (t) - \frac {1}{2} \lambda_ {2} ^ {* 2} (t). \tag {2.7.52} \\ \end{array}
$$

\- Step 4: Obtain the state and costate equations from
