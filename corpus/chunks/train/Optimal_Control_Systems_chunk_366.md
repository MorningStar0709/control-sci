# Example 6.4

Find the closed-loop optimal control for the first-order system

$$\dot {x} (t) = - 2 x (t) + u (t) \tag {6.5.22}$$

with the performance index

$$J = \int_ {0} ^ {\infty} [ x ^ {2} (t) + u ^ {2} (t) ] d t. \tag {6.5.23}$$

Hint: Assume that $J^{*} = fx^{2}(t)$ .

Solution: First of all, let us identify the various functions as

$$V (x (t), u (t)) = x ^ {2} (t) + u ^ {2} (t),f (x (t), u (t)) = - 2 x (t) + u (t). \tag {6.5.24}$$

We now follow the step-by-step procedure given in Table 6.4.

\- Step 1: Form the $\mathcal{H}$ function as

$$
\begin{array}{l} \mathcal {H} (x (t), u (t), J _ {x} ^ {*}) = V (x (t), u (t)) + J _ {x} ^ {*} f (x (t), u (t)) \\ = x ^ {2} (t) + u ^ {2} (t) + 2 f x (t) [ - 2 x (t) + u (t) ] \\ = x ^ {2} (t) + u ^ {2} (t) - 4 f x ^ {2} (t) + 2 f x (t) u (t) \tag {6.5.25} \\ \end{array}
$$

where, we used $J^{*} = fx^{2}(t)$ and $J_{x}^{*} = 2fx(t)$ . Here, we use a slightly different approach by using the value of $J_{x}^{*}$ in the beginning itself.

\- Step 2: Minimize $\mathcal{H}$ w.r.t. $u$ to obtain optimal control $u^{*}(t)$ as

$$\frac {\partial \mathcal {H}}{\partial u} = 2 u ^ {*} (t) + 2 f x ^ {*} (t) = 0 \longrightarrow u ^ {*} (t) = - f x ^ {*} (t). \tag {6.5.26}$$

Step 3: Using the result of Step 2 in Step 1, find the optimal H as

$$\mathcal {H} ^ {*} (x ^ {*} (t), J _ {x} ^ {*}, t) = x ^ {* ^ {2}} (t) - 4 f x ^ {* ^ {2}} (t) - f ^ {2} x ^ {* ^ {2}} (t). \tag {6.5.27}$$

\- Step 4: Solve the HJB equation

$$\mathcal {H} ^ {*} (x ^ {*} (t), J _ {x} ^ {*}) + J _ {t} ^ {*} = 0 \longrightarrowx ^ {* ^ {2}} (t) - 4 f x ^ {* ^ {2}} (t) - f ^ {2} x ^ {* ^ {2}} (t) = 0. \tag {6.5.28}$$

Note that $J_{t} = 0$ in the previous HJB equation. For any $x^{*}(t)$ , the previous equation becomes

$$f ^ {2} + 4 f - 1 = 0 \rightarrow f = - 2 \pm \sqrt {5}. \tag {6.5.29}$$

Taking the positive value of $f$ in (6.5.29), we get

$$J ^ {*} = f x ^ {* ^ {2}} (t) = (- 2 + \sqrt {5}) x ^ {* ^ {2}} (t). \tag {6.5.30}$$

Note that $(6.5.29)$ is the scalar version of the matrix ARE $(3.5.15)$ for the infinite-time interval regulator system.

\- Step 5: Using the value of $f$ from Step 4, in Step 2, we get the optimal control as

$$u ^ {*} (t) = - f x ^ {*} (t) = - (\sqrt {5} - 2) x ^ {*} (t). \tag {6.5.31}$$
