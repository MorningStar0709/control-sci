# 3.2.6 LQR System for General Performance Index

In this subsection, we address the state regulator system with a more general performance index than given by $(3.2.2)$ . Consider a linear, time-varying plant described by

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t), \tag {3.2.48}$$

with a cost functional

$$
\begin{array}{l} J (\mathbf {u}) = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + 2 \mathbf {x} ^ {\prime} (t) \mathbf {S u} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \\ = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {u} ^ {\prime} (t) \right] \left[ \begin{array}{l l} \mathbf {Q} (t) & \mathbf {S} (t) \\ \mathbf {S} ^ {\prime} (t) & \mathbf {R} (t) \end{array} \right] \left[ \begin{array}{l} \mathbf {x} (t) \\ \mathbf {u} (t) \end{array} \right] d t, \tag {3.2.49} \\ \end{array}
$$

where, the various vectors and matrices are defined in earlier sections and the $nxr$ matrix $\mathbf{S}(t)$ is only a positive definite matrix.

Using the identical procedure as for the LQR system, we get the matrix differential Riccati equation as

$$
\begin{array}{l} \dot {\mathbf {P}} (t) = - \mathbf {P} (t) \mathbf {A} (t) - \mathbf {A} ^ {\prime} (t) \mathbf {P} (t) - \mathbf {Q} (t) \\ + \left[ \mathbf {P} (t) \mathbf {B} (t) + \mathbf {S} (t) \right] \mathbf {R} ^ {- 1} (t) [ \mathbf {B} ^ {\prime} (t) \mathbf {P} (t) + \mathbf {S} ^ {\prime} (t) ] \tag {3.2.50} \\ \end{array}
$$

with the final condition on $\mathbf{P}(t)$ as

$$\mathbf {P} (t _ {f}) = \mathbf {F} (t _ {f}). \tag {3.2.51}$$

The optimal control is then given by

$$\mathbf {u} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \left[ \mathbf {S} ^ {\prime} (t) + \mathbf {P} (t) \right] \mathbf {x} (t). \tag {3.2.52}$$

Obviously, when $\mathbf{S}(t)$ is made zero in the previous analysis, we get the previous results shown in Table 3.1.
