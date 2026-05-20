Solving for the optimal state

$$x ^ {*} (t) = \frac {u ^ {*} (t)}{- a} \left[ \frac {u ^ {*} (t)}{\lambda^ {*} (t)} + 1 \right]. \tag {7.5.48}$$

Let us now discuss two situations.

1. Saturated Region: (i) At time $t = t_a$ (Figure 7.41(a)), $\lambda^*(t_a) = 2, u^*(t_a) = -1$ , then the optimal state (7.5.48) becomes

$$x ^ {*} (t _ {a}) = \frac {1}{2 a}, \quad \text { and since } \quad a < 0, x ^ {*} (t _ {a}) < 0. \tag {7.5.49}$$

Next, for time $t \in [t_a, t_f]$ , $u^*(t) = -1$ and $\lambda^*(t) > 2$ and the relation (7.5.48) reveals that $x^*(t) < x^*(t_a)$ . Combining this with (7.5.49), we have

$$x ^ {*} (t) < x ^ {*} (t _ {a}) < 0 \tag {7.5.50}$$

(ii) At time $t = t_c$ , (Figure 7.41(c)), $\lambda^*(t_c) = -2$ , $u^*(t_c) = +1$ , then the optimal state (7.5.48) becomes

$$x ^ {*} (t _ {c}) = - \frac {1}{2 a}, \quad \text { and since } \quad a < 0, x ^ {*} (t _ {c}) > 0. \tag {7.5.51}$$

Next, for time $t \in [t_c, t_f]$ , $u^*(t) = +1$ and $\lambda^*(t) < -2$ and the relation (7.5.48) reveals that $x^*(t) > x^*(t_c)$ . Combining this with (7.5.51), we have

$$x ^ {*} (t) > x ^ {*} \left(t _ {c}\right) > 0. \tag {7.5.52}$$

2. Unsaturated Region: During the unsaturated region,

$$\left| \lambda^ {*} (t) \right| \leq 1 \text {and} u ^ {*} (t) = - \frac {1}{2} \lambda^ {*} (t) \tag {7.5.53}$$

and using this, the Hamiltonian condition (7.5.47) becomes

$$u ^ {* 2} (t) + \lambda^ {*} (t) [ a x ^ {*} (t) + u ^ {*} (t) ] = 0\frac {1}{4} \lambda^ {* 2} (t) + a \lambda^ {*} (t) x ^ {*} (t) - \frac {1}{2} \lambda^ {* (2)} (t) = 0 \longrightarrow\lambda^ {*} (t) \left[ \frac {1}{4} \lambda^ {*} (t) - a x ^ {*} (t) \right] = 0 \tag {7.5.54}$$

solution of which becomes

$$\lambda^ {*} (t) = 0 \quad \text {or} \quad \lambda^ {*} (t) = 4 a x ^ {*} (t). \tag {7.5.55}$$

Here, $\lambda^{*}(t) = 0$ is not admissible because then the optimal control (7.5.44) becomes zero. For $\lambda^{*}(t) = 4ax^{*}(t)$ , the optimal control (7.5.44) becomes

$$u ^ {*} (t) = - 2 a x ^ {*} (t), \quad a < 0. \tag {7.5.56}$$

The previous relation also means that

$$\text { If } x ^ {*} (t) > 0, \text { then } u ^ {*} (t) = + 1\text { If } x ^ {*} (t) < 0, \text { then } u ^ {*} (t) = - 1\text { If } x ^ {*} (t) = 0, \text { then } u ^ {*} (t) = 0. \tag {7.5.57}$$

Control Law: Combining the previous relations for unsaturated region and for the saturated region, we finally get the control law for the entire region as
