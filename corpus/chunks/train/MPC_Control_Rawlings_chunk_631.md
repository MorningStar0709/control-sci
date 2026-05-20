# 5.6.2 State Estimator

Several state estimators for nonlinear systems are described in Chapter 4. For each t, let I(t) denote the information available to the state estimator at time t: for a full information estimator

$$\mathcal {I} (t) := \left\{\left(y (j), u (j)\right) \mid j \in \mathbb {I} _ {- \infty : t} \right\}$$

whereas for a moving horizon estimator

$$\mathcal {I} (t) := \left\{\left(y (j), u (j)\right) \mid j \in \mathbb {I} _ {t - T: t} \right\}$$

where T is the horizon. For each $t , j$ let $\hat { x } ( t | j )$ denote the estimate of $x ( t )$ give data $\mathcal { I } ( j )$ ; for simplicity, we use x(t) ˆ to denote $\hat { x } ( t | t - 1 )$ . We make the strong assumption that we have available an estimator satisfying the following difference equation

$$\hat {x} (t + 1) = f (\hat {x} (t), u (t)) + \delta$$

where $\delta \in \mathbb { \Delta }$ and ∆ is a compact subset of $\mathbb { R } ^ { n }$ . Since

$$\hat {x} (t + 1) = f (\hat {x} (t | t), u (t)) + w (t) = f (\hat {x} (t), u (t)) + \delta (t)$$

where

$$\delta (t) := \left[ f (\hat {x} (t | t), u (t)) - f (\hat {x} (t), u (t)) \right] + w (t)$$

the form of the evolution equation for ${ \hat { x } } ( t )$ is acceptable; the assumption that ∆ is constant is conservative. However controlling a random system with a time-varying bound on the disturbance would be considerably more complicated.

Our second assumption is the the state estimation error $\tilde { x } ( t ) : =$ ${ \boldsymbol x } ( t ) - \hat { { \boldsymbol x } } ( t )$ lies in a compact set $\mathbb { \Sigma } _ { x }$ . This is also a conservative assumption, made for simplicity.

Before proceeding to propose a tube-based controller, we examine briefly nominal MPC.
