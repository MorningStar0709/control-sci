Comparing the characteristic polynomial $\lvert s \mathbf { I } - \left( \mathbf { A } - \mathbf { K } ^ { * } \mathbf { C } \right) \rvert$ and the characteristic poly-@ nomial $\left| s \mathbf { I } - \left( \mathbf { A } - \mathbf { K } _ { e } \mathbf { C } \right) \right.$ for the observer system [refer to Equation (10–57)], we find @ that $\mathbf { K } _ { e }$ and $\mathbf { K } ^ { \ast }$ are related by

$$\mathbf {K} _ {e} = \mathbf {K} ^ {*}$$

Thus, using the matrix K determined by the pole-placement approach in the dual system, the observer gain matrix $\mathbf { K } _ { e }$ for the original system can be determined by using the relationship ${ \bf K } _ { e } = { \bf K } ^ { * }$ . (See Problem A–10–10 for the details.)

Necessary and Sufficient Condition for State Observation. As discussed, a necessary and sufficient condition for the determination of the observer gain matrix $\mathbf { K } _ { e }$ for the desired eigenvalues of $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C }$ is that the dual of the original system

$$\dot {\mathbf {z}} = \mathbf {A} ^ {*} \mathbf {z} + \mathbf {C} ^ {*} v$$

be completely state controllable. The complete state controllability condition for this dual system is that the rank of

$$
\left[ \begin{array}{c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right]
$$

be n. This is the condition for complete observability of the original system defined by Equations (10–55) and (10–56).This means that a necessary and sufficient condition for the observation of the state of the system defined by Equations (10–55) and (10–56) is that the system be completely observable.

Once we select the desired eigenvalues (or desired characteristic equation), the fullorder state observer can be designed, provided the plant is completely observable. The desired eigenvalues of the characteristic equation should be chosen so that the state observer responds at least two to five times faster than the closed-loop system considered. As stated earlier, the equation for the full-order state observer is

$$\tilde {\mathbf {x}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \tilde {\mathbf {x}} + \mathbf {B} u + \mathbf {K} _ {e} y \tag {10-60}$$
