# 7.3.2 Problem Formulation and Statement

Consider a body with a unit mass undergoing translational motion

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = u (t), \quad | u (t) | \leq 1 \tag {7.3.1} \\ \end{array}
$$

where, $x_{1}(t)$ is the position, $x_{2}(t)$ is the velocity, and $u(t)$ is the thrust force. Let us assume that the thrust (i.e., the control) is proportional to $\phi(t)$ , the rate of fuel consumption. Then, the total fuel consumed becomes

$$J = \int_ {t _ {0}} ^ {t _ {f}} \phi (t) d t. \tag {7.3.2}$$

Let us further assume that

1. the mass of fuel consumed is small compared with the total mass of the body,   
2. the rate of fuel, $\phi(t)$ is proportional to the magnitude of the thrust, $u(t)$ , and   
3. the final time $t_f$ is free or fixed.

Then from (7.3.2), the performance index can be formulated as

$$J (u) = \int_ {t _ {0}} ^ {t _ {f}} | u (t) | d t. \tag {7.3.3}$$

The fuel-optimal control problem may be stated as follows: Find the control $u(t)$ which forces the system (7.3.1) from any initial state $(x_{1}(0), x_{2}(0) = x_{10}, x_{20})$ to the origin in a certain unspecified final time $t_{f}$ while minimizing the fuel consumption (7.3.3).

Note that in case the final time $t_f$ is fixed then that final time $t_f$ must be greater than the minimum time $t_f^*$ required to drive the system from $(x_{10}, x_{20})$ to the origin.
