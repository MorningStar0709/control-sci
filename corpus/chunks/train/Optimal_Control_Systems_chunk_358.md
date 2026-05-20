# Example 6.3

Given a first-order system

$$\dot {x} (t) = - 2 x (t) + u (t) \tag {6.4.17}$$

and the performance index (PI)

$$J = \frac {1}{2} x ^ {2} (t _ {f}) + \frac {1}{2} \int_ {0} ^ {t _ {f}} [ x ^ {2} (t) + u ^ {2} (t) ] d t \tag {6.4.18}$$

find the optimal control.

Solution: First of all, comparing the present plant (6.4.17) and the PI (6.4.18) with the general formulation of the plant (6.4.1) and the PI (6.4.2), respectively, we see that

$$V (\mathbf {x} (t), \mathbf {u} (t), t) = \frac {1}{2} u ^ {2} (t) + \frac {1}{2} x ^ {2} (t); S (\mathbf {x} (t _ {f}), t _ {f}) = \frac {1}{2} x ^ {2} (t _ {f})f (\mathbf {x} (t), \mathbf {u} (t), t) = - 2 x (t) + u (t). \tag {6.4.19}$$

Now we use the procedure summarized in Table 6.4.

\- Step 1: The Hamiltonian (6.4.7) is

$$
\begin{array}{l} \mathcal {H} \left[ \mathbf {x} ^ {*} (t), J _ {\mathbf {x}}, \mathbf {u} ^ {*} (t), t \right] = V (\mathbf {x} (t), \mathbf {u} (t), t) + J _ {\mathbf {x}} \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \\ = \frac {1}{2} u ^ {2} (t) + \frac {1}{2} x ^ {2} (t) + J _ {\mathbf {x}} (- 2 x (t) + u (t)). \tag {6.4.20} \\ \end{array}
$$

\- Step 2: For an unconstrained control, a necessary condition for optimization is

$$\frac {\partial \mathcal {H}}{\partial u} = 0 \longrightarrow u (t) + J _ {x} = 0 \tag {6.4.21}$$

and solving

$$u ^ {*} (t) = - J _ {x}. \tag {6.4.22}$$

\- Step 3: Using the optimal control (6.4.22) and (6.4.20), form the optimal $\mathcal{H}$ function as

$$
\begin{array}{l} \mathcal {H} = \frac {1}{2} (- J _ {x}) ^ {2} + \frac {1}{2} x ^ {2} (t) + J _ {x} (- 2 x (t) - J _ {x}) \\ = - \frac {1}{2} J _ {x} ^ {2} + \frac {1}{2} x ^ {2} (t) - 2 x (t) J _ {x}. \tag {6.4.23} \\ \end{array}
$$

Now using the previous relations, the H-J-B equation (6.4.16) becomes

$$J _ {t} - \frac {1}{2} J _ {x} ^ {2} + \frac {1}{2} x ^ {2} (t) - 2 x (t) J _ {x} = 0 \tag {6.4.24}$$

with boundary condition (6.4.10) as

$$J (x (t _ {f}), t _ {f}) = S (x (t _ {f}), t _ {f}) = \frac {1}{2} x ^ {2} (t _ {f}). \tag {6.4.25}$$

\- Step 4: One way to solve the HJB equation (6.4.24) with the boundary condition (6.4.25) is to assume a solution and check if it satisfies the equation. In this simple case, since we want the optimal control (6.4.22) in terms of the states and the PI is a quadratic function of states and controls, we can guess the solution as

$$J (x (t)) = \frac {1}{2} p (t) x ^ {2} (t), \tag {6.4.26}$$

where, $p(t)$ , the unknown function to be determined, has the boundary condition as
