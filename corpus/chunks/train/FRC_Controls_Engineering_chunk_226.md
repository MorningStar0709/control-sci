# 8.4.1 Feedback linearization for reference tracking

Feedback linearization lets us erase the nonlinear dynamics of a system so we can apply our own (usually linear) dynamics for reference tracking. To do this, we will perform a similar procedure as in subsection 7.8.1 and solve for u given the reference dynamics in r˙ .

$$\dot {\mathbf {r}} = f (\mathbf {x}) + \mathbf {B u}\mathbf {B} \mathbf {u} = \dot {\mathbf {r}} - f (\mathbf {x})\mathbf {u} = \mathbf {B} ^ {+} (\dot {\mathbf {r}} - f (\mathbf {x})) \tag {8.3}$$

R To use equation (8.3) in a discrete controller, one can approximate r˙ with rk+1−rk where T is the time period between the two references. $\frac { \mathbf { r } _ { k + 1 } - \mathbf { r } _ { k } } { T }$ T
