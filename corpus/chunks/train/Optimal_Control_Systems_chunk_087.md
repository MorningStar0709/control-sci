# 2.4 The Second Variation

In the study of extrema of functionals, we have so far considered only the necessary condition for a functional to have a relative or weak extremum, i.e., the condition that the first variation vanish leading to the classic Euler-Lagrange equation. To establish the nature of optimum (maximum or minimum), it is required to examine the second variation. In the relation (2.3.7) for the increment consider the terms corresponding to the second variation [120],

$$
\begin{array}{l} \delta^ {2} J = \int_ {t _ {0}} ^ {t _ {f}} \frac {1}{2 !} \left[ \left(\frac {\partial^ {2} V}{\partial x ^ {2}}\right) _ {*} (\delta x (t)) ^ {2} + \left(\frac {\partial^ {2} V}{\partial \dot {x} ^ {2}}\right) _ {*} (\delta \dot {x} (t)) ^ {2} \right. \\ \left. + 2 \left(\frac {\partial^ {2} V}{\partial x \partial \dot {x}}\right) _ {*} \delta x (t) \delta \dot {x} (t) \right] d t. \tag {2.4.1} \\ \end{array}
$$

Consider the last term in the previous equation and rewrite it in terms of $\delta x(t)$ only using integration by parts ( $\int udv = uv - \int vdu$ where, $u = \frac{\partial^2V}{\partial x\partial\dot{x}}\delta x(t)$ and $v = \delta x(t)$ ). Then using $\delta x(t_0) = \delta x(t_f) = 0$ for fixed-end conditions, we get

$$
\begin{array}{l} \delta^ {2} J = \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \left\{\left(\frac {\partial^ {2} V}{\partial x ^ {2}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial^ {2} V}{\partial x \partial \dot {x}}\right) _ {*} \right\} (\delta x (t)) ^ {2} \right. \\ \left. + \left(\frac {\partial^ {2} V}{\partial \dot {x} ^ {2}}\right) _ {*} (\delta \dot {x} (t)) ^ {2} \right] d t. \tag {2.4.2} \\ \end{array}
$$

According to Theorem 2.1, the fundamental theorem of the calculus of variations, the sufficient condition for a minimum is $\delta^2 J > 0$ . This, for arbitrary values of $\delta x(t)$ and $\delta \dot{x}(t)$ , means that

$$\left(\frac {\partial^ {2} V}{\partial x ^ {2}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial^ {2} V}{\partial x \partial \dot {x}}\right) _ {*} > 0, \tag {2.4.3}\left(\frac {\partial^ {2} V}{\partial \dot {x} ^ {2}}\right) _ {*} > 0. \tag {2.4.4}$$

For maximum, the signs of the previous conditions are reversed. Alternatively, we can rewrite the second variation (2.4.1) in matrix form as
