$$
\begin{array}{l} \left[ \begin{array}{c} \dot {\hat {x}} _ {1} \\ \dot {\hat {x}} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c c} 1 & 1 \\ - 4 & - 3 \end{array} \right] \left[ \begin{array}{c c} - 1 & 0 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] + \left[ \begin{array}{c c} - 1 & 0 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c} 0 \\ 2 \end{array} \right] u \\ = \left[ \begin{array}{l l} 0 & - 1 \\ 1 & - 2 \end{array} \right] \left[ \begin{array}{l} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 2 \end{array} \right] u \tag {10-157} \\ \end{array}
$$

The output equation becomes

$$y = \mathbf {C Q} \hat {\mathbf {x}}$$

or

$$
y = \left[ \begin{array}{l l} 1 & 1 \end{array} \right] \left[ \begin{array}{c c} - 1 & 0 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{l} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \end{array} \right] \left[ \begin{array}{l} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] \tag {10-158}
$$

Equations (10–157) and (10–158) are in the observable canonical form.

A–10–10. For the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

consider the problem of designing a state observer such that the desired eigenvalues for the observer gain matrix are $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ .

Show that the observer gain matrix given by Equation (10–61), rewritten as

$$
\mathbf {K} _ {e} = (\mathbf {W N} ^ {*}) ^ {- 1} \left[ \begin{array}{c} \alpha_ {n} - a _ {n} \\ \alpha_ {n - 1} - a _ {n - 1} \\ \cdot \\ \cdot \\ \cdot \\ \alpha_ {1} - a _ {1} \end{array} \right] \tag {10-159}
$$

can be obtained from Equation (10–13) by considering the dual problem. That is, the matrix Ke can be determined by considering the pole-placement problem for the dual system, obtaining the state-feedback gain matrix K, and taking its conjugate transpose, or ${ \bf K } _ { e } = { \bf K } ^ { * }$ .

Solution. The dual of the given system is

$$\dot {\mathbf {z}} = \mathbf {A} ^ {*} \mathbf {z} + \mathbf {C} ^ {*} v \tag {10-160}n = \mathbf {B} ^ {*} \mathbf {z}$$

Using the state-feedback control

$$v = - \mathbf {K} \mathbf {z}$$

Equation (10–160) becomes

$$\dot {\mathbf {z}} = (\mathbf {A} ^ {*} - \mathbf {C} ^ {*} \mathbf {K}) \mathbf {z}$$

Equation (10–13), which is rewritten here, is
