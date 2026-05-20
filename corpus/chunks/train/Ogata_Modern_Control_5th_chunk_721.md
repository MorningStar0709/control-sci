The same system may be represented by the following state-space equation, which is in the observable canonical form:

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{l l} 0 & - 0. 4 \\ 1 & - 1. 3 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0. 8 \\ 1 \end{array} \right] u \tag {9-122}

y = \left[ \begin{array}{l l} 0 & 1 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] \tag {9-123}
$$

Show that the state-space representation given by Equations (9–120) and (9–121) gives a system that is state controllable, but not observable. Show, on the other hand, that the state-space representation defined by Equations (9–122) and (9–123) gives a system that is not completely state controllable, but is observable. Explain what causes the apparent difference in the controllability and observability of the same system.

Solution. Consider the system defined by Equations (9–120) and (9–121). The rank of the controllability matrix

$$
\left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 1 & - 1. 3 \end{array} \right]
$$

is 2. Hence, the system is completely state controllable. The rank of the observability matrix

$$
\left[ \begin{array}{c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} 0. 8 & - 0. 4 \\ 1 & - 0. 5 \end{array} \right]
$$

is 1. Hence the system is not observable.

Next consider the system defined by Equations (9–122) and (9–123). The rank of the controllability matrix

$$
\left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 0. 8 & - 0. 4 \\ 1 & - 0. 5 \end{array} \right]
$$

is 1. Hence, the system is not completely state controllable. The rank of the observability matrix

$$
\left[ \begin{array}{c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 1 & - 1. 3 \end{array} \right]
$$

is 2. Hence, the system is observable.

The apparent difference in the controllability and observability of the same system is caused by the fact that the original system has a pole-zero cancellation in the transfer function. Referring to Equation (2–29), for D=0 we have

$$G (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B}$$

If we use Equations (9–120) and (9–121), then
