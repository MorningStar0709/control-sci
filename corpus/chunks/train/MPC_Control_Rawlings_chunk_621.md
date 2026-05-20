# 5.5.2 Control

The estimation problem has a solution similar to previous solutions. The control problem is more difficult. As before, we control the estimator state, making allowance for state estimation error. The estimator state $\hat { \phi }$ satisfies the difference equation

$$\hat {\phi} ^ {+} = \tilde {A} \hat {\phi} + \tilde {B} u + \delta$$

where the disturbance δ is defined by

$$\delta := L \tilde {y} = L (\tilde {C} \tilde {\phi} + \nu)$$

The disturbance $\delta = ( \delta _ { x } , \delta _ { d } )$ lies in the C−set ∆ defined by

$$\mathbb {A} := L (\tilde {C} \Phi \oplus \mathbb {N})$$

where the set Φ is defined in Section 5.5.1. The system $\hat { \phi } ^ { + } = \stackrel { \sim } { A } \hat { \phi } + \stackrel { \sim } { B } u + \delta$ is not stabilizable, however, so we examine the subsystems with states $\hat { x }$ and $\hat { d }$

$$
\begin{array}{l} \hat {x} ^ {+} = A \hat {x} + B _ {d} \hat {d} + B u + \delta_ {x} \\ \hat {d} ^ {+} = \hat {d} + \delta_ {d} \\ \end{array}
$$

where the disturbances $\delta _ { x }$ and $\delta _ { d }$ are components of $\delta ( \delta = ( \delta _ { x } , \delta _ { d } ) )$ and are defined by

$$\delta_ {x} := L _ {x} \tilde {\mathcal {Y}} = L _ {x} (\tilde {C} \tilde {\phi} + \nu) \qquad \delta_ {d} := L _ {d} \tilde {\mathcal {Y}} = L _ {d} (\tilde {C} \tilde {\phi} + \nu)$$

The matrices $L _ { x }$ and $L _ { d }$ are the corresponding components of L. The disturbance $\delta _ { x }$ and $\delta _ { d }$ lie in the $C - \mathbf { s e t s } \ \mathbb { \Delta } _ { x }$ and $\mathbb { \Delta } _ { d }$ defined by

$$
\mathbb {A} _ {x} := \left[ \begin{array}{c c} I _ {n} & 0 \end{array} \right] \mathbb {A} = L _ {x} [ \tilde {C} \Phi \oplus \mathbb {N} ] \qquad \mathbb {A} _ {d} := \left[ \begin{array}{c c} 0 & I _ {p} \end{array} \right] \mathbb {A} = L _ {d} [ \tilde {C} \Phi \oplus \mathbb {N} ]
$$

We assume that (A, B) is a stabilizable pair so the tube methodology may be employed to control $\hat { x }$ . The system $\hat { d } ^ { + } = \hat { d } + \delta _ { d }$ is uncontrollable. The central trajectory is therefore described by

$$
\begin{array}{l} z ^ {+} = A z + B _ {d} \hat {d} + B v \\ \hat {d} ^ {+} = \hat {d} \\ \end{array}
$$

We obtain $\nu = \bar { \kappa } _ { N } ( z , \hat { d } , \bar { r } )$ by solving a nominal optimal control problem defined later and set $u = \nu + K e , e : = \hat { x } - z$ where K is chosen so that $\rho ( A _ { K } ) < 1 , A _ { K } : = A + B K$ ; this is possible since $( A , B )$ is assumed to be stabilizable. It follows that $e : = { \hat { x } } - z$ satisfies the difference equation
