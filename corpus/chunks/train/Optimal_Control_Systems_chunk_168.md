$$
\begin{array}{l} J _ {2} = 2 J = \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t, \tag {3.2.38} \\ \end{array}
$$

get the corresponding matrix differential Riccati equation for $J_{2}$ as

$$
\begin{array}{l} \frac {\dot {\mathbf {P}} _ {2} (t)}{2} = - \frac {\mathbf {P} _ {2} (t)}{2} \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \frac {\mathbf {P} _ {2} (t)}{2} - \mathbf {Q} (t) \\ + \frac {\mathbf {P} _ {2} (t)}{2} \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \frac {\mathbf {P} _ {2} (t)}{2} \tag {3.2.39} \\ \end{array}
$$

with final condition

$$\frac {\mathbf {P} _ {2} (t = t _ {f})}{2} = \mathbf {F} (t _ {f}). \tag {3.2.40}$$

Comparing the previous DRE for $J_{2}$ with the corresponding DRE (3.2.34) for $J$ , we can easily see that $\mathbf{P}_2(t) = 2\mathbf{P}(t)$ and hence the optimal control becomes

$$
\begin{array}{l} \mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \frac {\mathbf {P} _ {2} (t)}{2} \mathbf {x} ^ {*} (t) = - \frac {\mathbf {K} _ {2} (t)}{2} \mathbf {x} ^ {*} (t) \\ = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) \mathbf {x} ^ {*} (t) = - \mathbf {K} (t) \mathbf {x} ^ {*} (t). \tag {3.2.41} \\ \end{array}
$$

Thus, using $J_{2}$ without the $\frac{1}{2}$ in the performance index, we get the same optimal control (3.2.41) for the original plant (3.2.31), but the only difference being that the Riccati coefficient matrix $\mathbf{P}_{2}(t)$ is twice that of $\mathbf{P}(t)$ and $J_{2}$ is twice that of $J(\text{for example, see [3, 42]})$ .

However, we will retain the $\frac{1}{2}$ in J throughout the book due to the obvious simplifications in obtaining the optimal control, state and costate equations (3.2.4), (3.2.6) and (3.2.7), respectively. Precisely, the factor $\frac{1}{2}$ in the PI (3.2.2) and hence in the Hamiltonian (3.2.3) gets eliminated while taking partial derivatives of the Hamiltonian w.r.t. the control, state and costate functions.
