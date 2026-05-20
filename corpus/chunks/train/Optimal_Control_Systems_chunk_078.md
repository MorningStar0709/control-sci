To express the relation for the first variation (2.3.8) entirely in terms containing $\delta x(t)$ (since $\delta\dot{x}(t)$ is dependent on $\delta x(t)$ ), we integrate by parts the term involving $\delta\dot{x}(t)$ as (omitting the arguments in V for simplicity)

$$
\begin{array}{l} \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \delta \dot {x} (t) d t = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \frac {d}{d t} (\delta x (t)) d t \\ = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} d (\delta x (t)), \\ = \left[ \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \delta x (t) \right] _ {t _ {0}} ^ {t _ {f}} \\ - \int_ {t _ {0}} ^ {t _ {f}} \delta x (t) \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} d t. \tag {2.3.9} \\ \end{array}
$$

In the above, we used the well-known integration formula $\int udv = uv - \int vdu$ where $u = \partial V/\partial\dot{x}$ and $v = \delta x(t)$ . Using (2.3.9), the relation (2.3.8) for first variation becomes

$$
\begin{array}{l} \delta J \left(x ^ {*} (t), \delta x (t)\right) = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial V}{\partial x}\right) _ {*} \delta x (t) d t + \left[ \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \delta x (t) \right] _ {t _ {0}} ^ {t _ {f}} \\ - \int_ {t _ {0}} ^ {t _ {f}} \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \delta x (t) d t, \\ = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial V}{\partial x}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \right] \delta x (t) d t \\ + \left. \left[ \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \delta x (t) \right] \right| _ {t _ {0}} ^ {t _ {f}}. \tag {2.3.10} \\ \end{array}
$$

Using the relation (2.3.3) for boundary variations in (2.3.10), we get

$$\delta J \left(x ^ {*} (t), \delta x (t)\right) = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial V}{\partial x}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \right] \delta x (t) d t. \tag {2.3.11}$$

\- Step 4: Fundamental Theorem: We now apply the fundamental theorem of the calculus of variations (Theorem 2.1), i.e., the variation of $J$ must vanish for an optimum. That is, for the optimum $x^{*}(t)$ to exist, $\delta J(x^{*}(t), \delta x(t)) = 0$ . Thus the relation (2.3.11) becomes

$$\int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial V}{\partial x}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} \right] \delta x (t) d t = 0. \tag {2.3.12}$$

Note that the function $\delta x(t)$ must be zero at $t_0$ and $t_f$ , but for this, it is completely arbitrary.

\- Step 5: Fundamental Lemma: To simplify the condition obtained in the equation (2.3.12), let us take advantage of the following lemma called the fundamental lemma of the calculus of variations [47, 46, 79].
