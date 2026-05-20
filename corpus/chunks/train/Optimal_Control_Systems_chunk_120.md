# 2.7.3 Sufficient Condition

In order to determine the nature of optimization, i.e., whether it is minimum or maximum, we need to consider the second variation and examine its sign. In other words, we have to find a sufficient condition for extremum. Using (2.7.14), (2.7.28) and (2.7.37), we have the second variation in (2.7.16) and using the relation (2.7.28), we get

$$
\begin{array}{l} \delta^ {2} J = \int_ {t _ {0}} ^ {t _ {f}} \left[ \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} ^ {2}} (\delta \mathbf {x} (t)) ^ {2} + \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}} (\delta \mathbf {u} (t)) ^ {2} + 2 \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} \partial \mathbf {x}} (\delta \mathbf {u} (t) \delta \mathbf {x} (t)) \right] _ {*} d t \\ = \int_ {t _ {0}} ^ {t _ {f}} \left[ \begin{array}{l l} \delta \mathbf {x} ^ {\prime} (t) & \delta \mathbf {u} ^ {\prime} (t) \end{array} \right] \left[ \begin{array}{c c} \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} ^ {2}} & \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} \partial \mathbf {u}} \\ \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} \partial \mathbf {u}} & \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}} \end{array} \right] _ {*} \left[ \begin{array}{l} \delta \mathbf {x} (t) \\ \delta \mathbf {u} (t) \end{array} \right] d t \\ = \int_ {t _ {0}} ^ {t _ {f}} \left[ \begin{array}{l l} \delta \mathbf {x} ^ {\prime} (t) & \delta \mathbf {u} ^ {\prime} (t) \end{array} \right] \Pi \left[ \begin{array}{l} \delta \mathbf {x} (t) \\ \delta \mathbf {u} (t) \end{array} \right] d t. \tag {2.7.40} \\ \end{array}
$$

For the minimum, the second variation $\delta^2 J$ must be positive. This means that the matrix $\Pi$ in (2.7.40)

$$
\Pi = \left[ \begin{array}{l l} \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} ^ {2}} & \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} \partial \mathbf {u}} \\ \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {x} \partial \mathbf {u}} & \frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}} \end{array} \right] _ {*} \tag {2.7.41}
$$

must be positive definite. But the important condition is that the second partial derivative of $H^{*}$ w.r.t. $\mathbf{u}(t)$ must be positive. That is

$$\boxed {\left(\frac {\partial^ {2} \mathcal {H}}{\partial \mathbf {u} ^ {2}}\right) _ {*} > 0} \tag {2.7.42}$$

and for the maximum, the sign of (2.7.42) is reversed.
