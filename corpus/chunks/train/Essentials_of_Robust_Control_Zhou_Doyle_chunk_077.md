# 3.3 Observers and Observer-Based Controllers

It is clear that if a system is controllable and the system states are available for feedback, then the system closed-loop poles can be assigned arbitrarily through a constant feedback. However, in most practical applications, the system states are not completely accessible and all the designer knows are the output y and input u. Hence, the estimation of the system states from the given output information y and input u is often necessary to realize some specific design objectives. In this section, we consider such an estimation problem and the application of this state estimation in feedback control.

Consider a plant modeled by equations (3.1) and (3.2). An observer is a dynamical system with input $( u , y )$ and output (say, ˆx), that asymptotically estimates the state x, that is, ${ \hat { x } } ( t ) - x ( t )  0$ as $t \to \infty$ for all initial states and for every input.

Theorem 3.5 An observer exists iff $( C , A )$ is detectable. Further, $i f \ ( C , A )$ is detectable, then a full-order Luenberger observer is given by

$$\dot {q} = A q + B u + L (C q + D u - y) \tag {3.3}\hat {x} = q, \tag {3.4}$$

where L is any matrix such that $A + L C$ is stable.

Recall that, for a dynamical system described by the equations (3.1) and (3.2), if (A, B) is controllable and state x is available for feedback, then there is a state feedback $u = F x$ such that the closed-loop poles of the system can be arbitrarily assigned. Similarly, if $( C , A )$ is observable, then the system observer poles can be arbitrarily placed so that the state estimator ˆx can be made to approach x arbitrarily fast. Now let us consider what will happen if the system states are not available for feedback so that the estimated state has to be used. Hence, the controller has the following dynamics:

$$\dot {\hat {x}} = (A + L C) \hat {x} + B u + L D u - L yu = F \hat {x}.$$

Then the total system state equations are given by

$$
\left[ \begin{array}{c} \dot {x} \\ \dot {\hat {x}} \end{array} \right] = \left[ \begin{array}{c c} A & B F \\ - L C & A + B F + L C \end{array} \right] \left[ \begin{array}{c} x \\ \hat {x} \end{array} \right].
$$

Let $e : = x - { \hat { x } } ;$ ; then the system equation becomes

$$
\left[ \begin{array}{c} \dot {e} \\ \dot {\hat {x}} \end{array} \right] = \left[ \begin{array}{c c} A + L C & 0 \\ - L C & A + B F \end{array} \right] \left[ \begin{array}{c} e \\ \hat {x} \end{array} \right]
$$
