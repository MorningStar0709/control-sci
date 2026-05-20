Dual Problem. The problem of designing a full-order observer becomes that of determining the observer gain matrix $\mathbf { K } _ { e }$ such that the error dynamics defined by Equation (10–59) are asymptotically stable with sufficient speed of response. (The asymptotic stability and the speed of response of the error dynamics are determined by the eigenvalues of matrix $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C } . )$ Hence, the design of the full-order observer becomes that of determining an appropriate $\mathbf { K } _ { e }$ such that ${ \bf A } - { \bf K } _ { e }$ C has desired eigenvalues.Thus, the problem here becomes the same as the pole-placement problem we discussed in Section 10–2. In fact, the two problems are mathematically the same. This property is called duality.

Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

In designing the full-order state observer, we may solve the dual problem, that is, solve the pole-placement problem for the dual system

$$\dot {\mathbf {z}} = \mathbf {A} ^ {*} \mathbf {z} + \mathbf {C} ^ {*} vn = \mathbf {B} ^ {*} \mathbf {z}$$

assuming the control signal v to be

$$v = - \mathbf {K} \mathbf {z}$$

If the dual system is completely state controllable, then the state feedback gain matrix K can be determined such that matrix $\mathbf { A } ^ { * } - \mathbf { C } ^ { * } \mathbf { K }$ will yield a set of the desired eigenvalues.

If $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ are the desired eigenvalues of the state observer matrix, then by taking the same $\mu _ { i } \mathrm { { s } }$ as the desired eigenvalues of the state-feedback gain matrix of the dual system, we obtain

$$\left| s \mathbf {I} - (\mathbf {A} ^ {*} - \mathbf {C} ^ {*} \mathbf {K}) \right| = (s - \mu_ {1}) (s - \mu_ {2}) \dots (s - \mu_ {n})$$

Noting that the eigenvalues of $\mathbf { A } ^ { * } - \mathbf { C } ^ { * } \mathbf { K }$ and those of $\mathbf { A } - \mathbf { K } ^ { * } \mathbf { C }$ are the same, we have

$$\left| s \mathbf {I} - \left(\mathbf {A} ^ {*} - \mathbf {C} ^ {*} \mathbf {K}\right) \right| = \left| s \mathbf {I} - \left(\mathbf {A} - \mathbf {K} ^ {*} \mathbf {C}\right) \right|$$
