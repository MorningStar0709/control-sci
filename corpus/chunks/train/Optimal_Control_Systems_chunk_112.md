# 2.7 Variational Approach to Optimal Control Systems

Using mean-value theorem and Taylor series, and retaining the linear terms only, we have

$$
\begin{array}{l} \int_ {t _ {f}} ^ {t _ {f} + \delta t _ {f}} \mathcal {L} ^ {\delta} d t = \left. \mathcal {L} ^ {\delta} \right| _ {t _ {f}} \delta t _ {f} \\ \approx \left\{\mathcal {L} + \left(\frac {\partial \mathcal {L}}{\partial \mathbf {x}}\right) _ {*} ^ {\prime} \delta \mathbf {x} (t) + \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \delta \dot {\mathbf {x}} (t) \right. \\ \left. + \left(\frac {\partial \mathcal {L}}{\partial \mathbf {u}}\right) _ {*} ^ {\prime} \delta \mathbf {u} (t) \right\} \Bigg | _ {t _ {f}} \delta t _ {f} \\ \approx \mathcal {L} | _ {t _ {f}} \delta t _ {f}. \tag {2.7.15} \\ \end{array}
$$

\- Step 5: First Variation: Defining increment $\Delta J$ , using Taylor series expansion, extracting the first variation $\delta J$ by retaining only the first order terms, we get the first variation as

$$
\begin{array}{l} \Delta J = J _ {a} (\mathbf {u} (t)) - J _ {a} \left(\mathbf {u} ^ {*} (t)\right) \\ = \int_ {t _ {0}} ^ {t _ {f}} (\mathcal {L} ^ {\delta} - \mathcal {L}) d t + \left. \mathcal {L} \right| _ {t _ {f}} \delta t _ {f} \\ \delta J = \int_ {t _ {0}} ^ {t _ {f}} \left\{\left(\frac {\partial \mathcal {L}}{\partial \mathbf {x}}\right) _ {*} ^ {\prime} \delta \mathbf {x} (t) + \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \delta \dot {\mathbf {x}} (t) + \left(\frac {\partial \mathcal {L}}{\partial \mathbf {u}}\right) _ {*} ^ {\prime} \delta \mathbf {u} (t) \right\} d t \\ + \left. \mathcal {L} \right| _ {t _ {f}} \delta t _ {f}. \tag {2.7.16} \\ \end{array}
$$

Considering the $\delta\dot{\mathbf{x}}(t)$ term in the first variation (2.7.16) and integrating by parts (using $\int udv = uv - \int vdu$ ),
