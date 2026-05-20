# Theorem 7.7.1 — Linear-quadratic regulator.

$$\mathbf {u} _ {k} ^ {*} = \underset {\mathbf {u} _ {k}} {\arg \min} \sum_ {k = 0} ^ {\infty} \left(\mathbf {x} _ {k} ^ {\top} \mathbf {Q x} _ {k} + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k}\right)\text { subject to } \mathbf {x} _ {k + 1} = \mathbf {A} \mathbf {x} _ {k} + \mathbf {B} \mathbf {u} _ {k} \tag {7.14}$$

If the system is controllable, the optimal control policy $\mathbf { u } _ { k } ^ { * }$ that drives all the states to zero is − $\mathbf { \nabla } \cdot \mathbf { K } \mathbf { x } _ { k }$ . To converge to nonzero states, a reference vector $\mathbf { r } _ { k }$ can be added to the state $\mathbf { x } _ { k }$ .

$$\mathbf {u} _ {k} = \mathbf {K} (\mathbf {r} _ {k} - \mathbf {x} _ {k}) \tag {7.15}$$

This means that optimal control can be achieved with simply a set of proportional gains on all the states. To use the control law, we need knowledge of the full state of the system. That means we either have to measure all our states directly or estimate those we do not measure.

See appendix B.1 for how K is calculated. If the result is finite, the controller is guaranteed to be stable and robust with a gain margin of infinity and a phase margin of 60 degrees (see appendix B.2). However, using a state estimator forfeits the robustness guarantees.[8]

![](image/4c16f0cc091cb3927c9db91b277eb7e79dd1d4d0ee6d5b88540a0a7986c275ff.jpg)

LQR design’s Q and R matrices don’t need discretization, but the K calculated for continuous time and discrete time systems will be different. The discrete time gains approach the continuous time gains as the sample period tends to zero.
