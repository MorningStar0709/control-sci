# 3.1 Problem Formulation

We discuss the plant and the quadratic performance index with particular reference to physical significance. This helps us to obtain some elegant mathematical conditions on the choice of various matrices in the quadratic cost functional. Thus, we will be dealing with an optimization problem from the engineering perspective.

Consider a linear, time-varying (LTV) system

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {3.1.1}\mathbf {y} (t) = \mathbf {C} (t) \mathbf {x} (t) \tag {3.1.2}$$

with a cost functional (CF) or performance index (PI)

$$
\begin{array}{l} J (\mathbf {u} (t)) = J (\mathbf {x} \left(t _ {0}\right), \mathbf {u} (t), t _ {0}) \\ = \frac {1}{2} \left[ \mathbf {z} \left(t _ {f}\right) - \mathbf {y} \left(t _ {f}\right) \right] ^ {\prime} \mathbf {F} \left(t _ {f}\right) \left[ \mathbf {z} \left(t _ {f}\right) - \mathbf {y} \left(t _ {f}\right) \right] \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ [ \mathbf {z} (t) - \mathbf {y} (t) ] ^ {\prime} \mathbf {Q} (t) [ \mathbf {z} (t) - \mathbf {y} (t) ] + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \tag {3.1.3} \\ \end{array}
$$
