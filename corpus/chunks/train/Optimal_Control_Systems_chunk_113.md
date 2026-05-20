$$
\begin{array}{l} \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \delta \dot {\mathbf {x}} (t) d t = \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \frac {d}{d t} (\delta \mathbf {x} (t)) d t \\ = \left. \left[ \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \delta \mathbf {x} (t) \right] \right| _ {t _ {0}} ^ {t _ {f}} \\ - \int_ {t _ {0}} ^ {t _ {f}} \left[ \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} \right] ^ {\prime} \delta \mathbf {x} (t) d t. \tag {2.7.17} \\ \end{array}
$$

Also note that since $\mathbf{x}(t_0)$ is specified, $\delta \mathbf{x}(t_0) = 0$ . Thus, using (2.7.17) the first variation $\delta J$ in (2.7.16) becomes

$$
\begin{array}{l} \delta J = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial \mathcal {L}}{\partial \mathbf {x}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} \right] ^ {\prime} \delta \mathbf {x} (t) d t \\ + \int_ {t _ {0}} ^ {t _ {f}} \left(\frac {\partial \mathcal {L}}{\partial \mathbf {u}}\right) _ {*} ^ {\prime} \delta \mathbf {u} (t) d t \\ + \left. \mathcal {L} \right| _ {t _ {f}} \delta t _ {f} + \left[ \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} ^ {\prime} \delta \mathbf {x} (t) \right] \Bigg | _ {t _ {f}}. \tag {2.7.18} \\ \end{array}
$$

\- Step 6: Condition for Extrema: For extrema of the functional $J$ , the first variation $\delta J$ should vanish according to the fundamental theorem (Theorem 2.1) of the CoV. Also, in a typical control system such as (2.7.1), we note that $\delta \mathbf{u}(t)$ is the independent control variation and $\delta \mathbf{x}(t)$ is the dependent state variation. First, we choose $\lambda(t) = \lambda^{*}(t)$ which is at our disposal and hence $\mathcal{L}^*$ such that the coefficient of the dependent variation $\delta \mathbf{x}(t)$ in (2.7.18) be zero. Then, we have the Euler-Lagrange equation

$$\left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\mathbf {x}}}\right) _ {*} = 0 \tag {2.7.19}$$
