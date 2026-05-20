# 2.5.1 Direct Method

Now we generalize the preceding method of elimination using differential calculus. Consider the extrema of a function $f(x_{1}, x_{2})$ with two interdependent variables $x_{1}$ and $x_{2}$ , subject to the condition

$$g (x _ {1}, x _ {2}) = 0. \tag {2.5.16}$$

As a necessary condition for extrema, we have

$$d f = \frac {\partial f}{\partial x _ {1}} d x _ {1} + \frac {\partial f}{\partial x _ {2}} d x _ {2} = 0. \tag {2.5.17}$$

However, since $dx_{1}$ and $dx_{2}$ are not arbitrary, but related by the condition

$$d g = \frac {\partial g}{\partial x _ {1}} d x _ {1} + \frac {\partial g}{\partial x _ {2}} d x _ {2} = 0, \tag {2.5.18}$$

it is not possible to conclude as in the case of extremization of functions without conditions that

$$\frac {\partial f}{\partial x _ {1}} = 0 \quad \text { and } \quad \frac {\partial f}{\partial x _ {2}} = 0 \tag {2.5.19}$$

in the necessary condition (2.5.17). This is easily seen, since if the set of extrema conditions (2.5.19) is solved for optimal values $x_1^*$ and $x_2^*$ , there is no guarantee that these optimal values, would, in general satisfy the given condition (2.5.16).

In order to find optimal values that satisfy both the condition (2.5.16) and that of the extrema conditions (2.5.17), we arbitrarily choose one of the variables, say $x_{1}$ , as the independent variable. Then $x_{2}$ becomes a dependent variable as per the condition (2.5.16). Now, assuming that $\partial g/\partial x_{2} \neq 0$ , (2.5.18) becomes

$$d x _ {2} = - \left\{\frac {\partial g / \partial x _ {1}}{\partial g / \partial x _ {2}} \right\} d x _ {1} \tag {2.5.20}$$

and using (2.5.20) in the necessary condition (2.5.17), we have

$$d f = \left[ \frac {\partial f}{\partial x _ {1}} - \frac {\partial f}{\partial x _ {2}} \left\{\frac {\partial g / \partial x _ {1}}{\partial g / \partial x _ {2}} \right\} \right] d x _ {1} = 0. \tag {2.5.21}$$

As we have chosen $dx_{1}$ to be the independent, we now can consider it to be arbitrary, and conclude that in order to satisfy (2.5.21), we have the coefficient of $dx_{1}$ to be zero. That is

$$\left(\frac {\partial f}{\partial x _ {1}}\right) \left(\frac {\partial g}{\partial x _ {2}}\right) - \left(\frac {\partial f}{\partial x _ {2}}\right) \left(\frac {\partial g}{\partial x _ {1}}\right) = 0. \tag {2.5.22}$$

Now, the relation (2.5.22) and the condition (2.5.16) are solved simultaneously for the optimal solutions $x_1^*$ and $x_2^*$ . Equation (2.5.22) can be rewritten as

$$
\left| \begin{array}{c c} \frac {\partial f}{\partial x _ {1}} & \frac {\partial f}{\partial x _ {2}} \\ \frac {\partial g}{\partial x _ {1}} & \frac {\partial g}{\partial x _ {2}} \end{array} \right| = 0. \tag {2.5.23}
$$

This is also, as we know, the Jacobian of $f$ and $g$ w.r.t. $x_{1}$ and $x_{2}$ . This method of elimination of the dependent variables is quite tedious for higher order problems.
