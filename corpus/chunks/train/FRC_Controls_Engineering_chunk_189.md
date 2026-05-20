# 7.3 Linear system discretization

We’re going to discretize the following continuous time state-space model

$$\dot {\mathbf {x}} = \mathbf {A} _ {c} \mathbf {x} + \mathbf {B} _ {c} \mathbf {u} + \mathbf {w}\mathbf {y} = \mathbf {C} _ {c} \mathbf {x} + \mathbf {D} _ {c} \mathbf {u} + \mathbf {v}$$

where w is the process noise, v is the measurement noise, and both are zero-mean white noise sources with covariances of $\mathbf { Q } _ { c }$ and $\mathbf { R } _ { c }$ respectively. w and v are defined as normally distributed random variables.

$$\mathbf {w} \sim N (0, \mathbf {Q} _ {c})\mathbf {v} \sim N (0, \mathbf {R} _ {c})$$

Discretization is done using a zero-order hold. That is, the input is only updated at discrete intervals and it’s held constant between samples.
