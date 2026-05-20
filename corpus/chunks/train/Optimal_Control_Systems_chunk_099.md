\- Step 3: First Variation: Then using the Taylor series expansion and retaining linear terms only, the first variation of the functional $J_{a}$ becomes

$$
\begin{array}{l} \delta J _ {a} = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial \mathcal {L}}{\partial x _ {1}}\right) _ {*} \delta x _ {1} (t) + \left(\frac {\partial \mathcal {L}}{\partial x _ {2}}\right) _ {*} \delta x _ {2} (t) \right. \\ \left. + \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} \delta \dot {x} _ {1} (t) + \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {2}}\right) _ {*} \delta \dot {x} _ {2} (t) \right] d t. \tag {2.6.7} \\ \end{array}
$$

As before in the section on CoV, we rewrite the terms containing $\delta\dot{x}_{1}(t)$ and $\delta\dot{x}_{2}(t)$ in terms of those containing $\delta x_{1}(t)$ and $\delta x_{2}(t)$

only (using integration by parts, $\int udv = uv - \int vdu$ ). Thus

$$
\begin{array}{l} \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial \mathcal {L}}{\partial x _ {1}}\right) _ {*} \delta \dot {x} _ {1} (t) d t = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} \frac {d}{d t} (\delta x _ {1} (t)) d t \\ = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} d (\delta x _ {1} (t)) \\ = \left. \left[ \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} \delta x _ {1} (t) \right] \right| _ {t _ {0}} ^ {t _ {f}} \\ - \int_ {t _ {0}} ^ {t _ {f}} \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}\right) _ {*} \delta x _ {1} (t) d t. \tag {2.6.8} \\ \end{array}
$$

Using the above, we have the first variation (2.6.7) as
