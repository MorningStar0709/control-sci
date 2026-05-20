# 6.5 Nonlinear Distributed MPC

In the nonlinear case, the usual model comes from physical principles and conservation laws of mass, energy and momentum. The state has a physical meaning and the measured outputs usually are a subset of the state. We assume the model is of the form

$$
\begin{array}{l} \frac {d x _ {1}}{d t} = f _ {1} \left(x _ {1}, x _ {2}, u _ {1}, u _ {2}\right) \\ y _ {1} = C _ {1} x _ {1} \\ \frac {d x _ {2}}{d t} = f _ {2} \left(x _ {1}, x _ {2}, u _ {1}, u _ {2}\right) \\ y _ {2} = C _ {2} x _ {2} \\ \end{array}
$$

in which $C _ { 1 } , C _ { 2 }$ are matrices of zeros and ones selecting the part of the state that is measured in subsystems one and two. We generally cannot avoid state $x _ { 2 }$ dependence in the differential equation for $x _ { 1 }$ . But often it is only a small subset of the entire state $x _ { 2 }$ that appears in $f _ { 1 }$ , and vice versa. The reason in chemical process systems is that the two subsystems are generally coupled through a small set of process streams transferring mass and energy between the systems. These connecting streams isolate the coupling between the two systems and reduce the influence to a small part of the entire state required to describe each system.

Given these physical system models of the subsystems, the overall plant model is

$$
\begin{array}{l} \frac {d x}{d t} = f (x, u) \\ y = C x \\ \end{array}
$$

in which

$$
x = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] \qquad u = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \qquad f = \left[ \begin{array}{c} f _ {1} \\ f _ {2} \end{array} \right] \qquad y = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] \qquad C = \left[ \begin{array}{c c} C _ {1} & \\ & C _ {2} \end{array} \right]
$$

Nonconvexity. The basic difficulty in both the theory and application of nonlinear MPC is the nonconvexity in the control objective function caused by the nonlinear dynamic model. This difficulty applies even to centralized nonlinear MPC as discussed in Section 2.8, and motivates the development of suboptimal MPC. In the distributed case, nonconvexity causes even greater difficulties. As an illustration, consider the simple two-player, nonconvex game depicted in Figure 6.7. The cost function is

$$
\begin{array}{l} V (u _ {1}, u _ {2}) = e ^ {- 2 u _ {1}} - 2 e ^ {- u _ {1}} + e ^ {- 2 u _ {2}} - 2 e ^ {- u _ {2}} \\ + a \exp (- \beta ((u _ {1} + 0. 2) ^ {2} + (u _ {2} + 0. 2) ^ {2})) \\ \end{array}
$$
