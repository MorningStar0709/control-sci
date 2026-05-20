$$
\begin{array}{l} \Delta J (x ^ {*} (t), \delta x (t)) \triangleq J (x ^ {*} (t) + \delta x (t), \dot {x} ^ {*} (t) + \delta \dot {x} (t), t) \\ - J (x ^ {*} (t), \dot {x} ^ {*} (t), t) \\ = \int_ {t _ {0}} ^ {t _ {f}} V (x ^ {*} (t) + \delta x (t), \dot {x} ^ {*} (t) + \delta \dot {x} (t), t) d t \\ - \int_ {t _ {0}} ^ {t _ {f}} V (x ^ {*} (t), \dot {x} ^ {*} (t), t) d t. \tag {2.3.4} \\ \end{array}
$$

which by combining the integrals can be written as

$$
\begin{array}{l} \Delta J (x ^ {*} (t), \delta x (t)) = \int_ {t _ {0}} ^ {t _ {f}} [ V (x ^ {*} (t) + \delta x (t), \dot {x} ^ {*} (t) + \delta \dot {x} (t), t) \\ \left. - V \left(x ^ {*} (t), \dot {x} ^ {*} (t), t\right) \right] d t. \tag {2.3.5} \\ \end{array}
$$

where,

$$\dot {x} (t) = \frac {d x (t)}{d t} \quad \text { and } \quad \delta \dot {x} (t) = \frac {d}{d t} \left\{\delta x (t) \right\} \tag {2.3.6}$$

Expanding V in the increment (2.3.5) in a Taylor series about the point $x^{*}(t)$ and $\dot{x}^{*}(t)$ , the increment $\Delta J$ becomes (note the

cancelation of $V(x^{*}(t), \dot{x}^{*}(t), t))$

$$
\begin{array}{l} \Delta J = \Delta J (x ^ {*} (t), \delta x (t)) \\ = \int_ {t _ {0}} ^ {t _ {f}} \left[ \frac {\partial V \left(x ^ {*} (t) , \dot {x} ^ {*} (t) , t\right)}{\partial x} \delta x (t) + \frac {\partial V \left(x ^ {*} (t) , \dot {x} ^ {*} (t) , t\right)}{\partial \dot {x}} \delta \dot {x} (t) \right. \\ + \frac {1}{2 !} \left\{\frac {\partial^ {2} V (\dots)}{\partial x ^ {2}} (\delta x (t)) ^ {2} + \frac {\partial^ {2} V (\dots)}{\partial \dot {x} ^ {2}} (\delta \dot {x} (t)) ^ {2} + \right. \\ \left. + 2 \frac {\partial^ {2} V (\dots)}{\partial x \partial \dot {x}} \delta x (t) \delta \dot {x} (t) \right\} + \dots ] d t. \tag {2.3.7} \\ \end{array}
$$

Here, the partial derivatives are w.r.t. $x(t)$ and $\dot{x}(t)$ at the optimal condition (\*) and \* is omitted for simplicity.

\- Step 3: First Variation: Now, we obtain the variation by retaining the terms that are linear in $\delta x(t)$ and $\delta \dot{x}(t)$ as

$$
\begin{array}{l} \delta J \left(x ^ {*} (t), \delta x (t)\right) = \int_ {t _ {0}} ^ {t _ {f}} \left[ \frac {\partial V \left(x ^ {*} (t) , \dot {x} ^ {*} (t) , t\right)}{\partial x} \delta x (t) \right. \\ \left. + \frac {\partial V \left(x ^ {*} (t) , \dot {x} ^ {*} (t) , t\right)}{\partial \dot {x}} \delta \dot {x} (t) \right] d t. \tag {2.3.8} \\ \end{array}
$$
