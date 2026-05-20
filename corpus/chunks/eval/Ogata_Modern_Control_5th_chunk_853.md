$$
\begin{array}{l} \left[ \begin{array}{c c} \mathbf {A M} & \mathbf {B} \\ - \mathbf {C M} & 0 \end{array} \right] = \left[ \begin{array}{c c c c c c} \mathbf {A} [ \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} ] & \mathbf {B} \\ - \mathbf {C} [ \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} ] & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c c c c} \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} & \dots & \mathbf {A} ^ {n} \mathbf {B} & \mathbf {B} \\ - \mathbf {C B} & - \mathbf {C A B} & \dots & - \mathbf {C A} ^ {n - 1} \mathbf {B} & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c c c} \hat {\mathbf {A}} \hat {\mathbf {B}} & \hat {\mathbf {A}} ^ {2} \hat {\mathbf {B}} & \dots & \hat {\mathbf {A}} ^ {n} \hat {\mathbf {B}} & \hat {\mathbf {B}} \end{array} \right] \\ \end{array}
$$

we find that the rank of

$$
\left[ \begin{array}{c c c c c c} \hat {\mathbf {B}} & \hat {\mathbf {A}} \hat {\mathbf {B}} & \hat {\mathbf {A}} ^ {2} \hat {\mathbf {B}} & \dots & \hat {\mathbf {A}} ^ {n} \hat {\mathbf {B}} \end{array} \right]
$$

is $n + 1$ . Thus, the system defined by Equation (10–168) is completely state controllable.

A–10–13. Consider the system shown in Figure 10–49. Using the pole-placement-with-observer approach, design a regulator system such that the system will maintain the zero position $\left( y _ { 1 } = 0 { \mathrm { a n d } } y _ { 2 } = 0 \right)$ in the presence of disturbances. Choose the desired closed-loop poles for the pole-placement part to be

$$s = - 2 + j 2 \sqrt {3}, \quad s = - 2 - j 2 \sqrt {3}, \quad s = - 1 0, \quad s = - 1 0$$

and the desired poles for the minimum-order observer to be

$$s = - 1 5, \quad s = - 1 6$$

First, determine the state feedback gain matrix K and observer gain matrix $\mathbf { K } _ { e }$ . Then, obtain the response of the system to an arbitrary initial condition—for example,

$$y _ {1} (0) = 0. 1, \quad y _ {2} (0) = 0, \quad \dot {y} _ {1} (0) = 0, \quad \dot {y} _ {2} (0) = 0e _ {1} (0) = 0. 1, \quad e _ {2} (0) = 0. 0 5$$

where $e _ { 1 }$ and $e _ { 2 }$ are defined by

$$e _ {1} = y _ {1} - \widetilde {y} _ {1}e _ {2} = y _ {2} - \widetilde {y} _ {2}$$

Assume that $m _ { 1 } = 1 \mathrm { k g } , m _ { 2 } = 2 \mathrm { k g } , k = 3 6 \mathrm { N } / \mathrm { m } , \mathrm { a n d } b = 0 . 6 \mathrm { N } \mathrm { - s } / \mathrm { m } .$

Solution. The equations for the system are

$$m _ {1} \ddot {y} _ {1} = k (y _ {2} - y _ {1}) + b (\dot {y} _ {2} - \dot {y} _ {1}) + um _ {2} \ddot {y} _ {2} = k (y _ {1} - y _ {2}) + b (\dot {y} _ {1} - \dot {y} _ {2})$$
