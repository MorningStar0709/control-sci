In the design of the state observer, it is desirable to determine several observer gain matrices $\mathbf { K } _ { e }$ based on several different desired characteristic equations. For each of the several different matrices $\mathbf { K } _ { e }$ , simulation tests must be run to evaluate the resulting system performance. Then we select the best $\mathbf { K } _ { e }$ from the viewpoint of overall system performance. In many practical cases, the selection of the best matrix $\mathbf { K } _ { e }$ boils down to a compromise between speedy response and sensitivity to disturbances and noises.

EXAMPLE 10–6 Consider the system

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}y = \mathbf {C x}$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 2 0. 6 \\ 1 & 0 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c} 0 & 1 \end{array} \right]
$$

We use the observed state feedback such that

$$u = - \mathbf {K} \widetilde {\mathbf {x}}$$

Design a full-order state observer, assuming that the system configuration is identical to that shown in Figure 10–11. Assume that the desired eigenvalues of the observer matrix are

$$\mu_ {1} = - 1 0, \quad \mu_ {2} = - 1 0$$

The design of the state observer reduces to the determination of an appropriate observer gain matrix $\mathbf { K } _ { e }$ .

Let us examine the observability matrix. The rank of

$$
\left[ \begin{array}{c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right]
$$

is 2. Hence, the system is completely observable and the determination of the desired observer gain matrix is possible. We shall solve this problem by three methods.

Method 1: We shall determine the observer gain matrix by use of Equation (10–61). The given system is already in the observable canonical form. Hence, the transformation matrix ${ \bf Q } = ( { \bf W } { \bf N } ^ { * } ) ^ { - 1 }$ is I. Since the characteristic equation of the given system is

$$
| s \mathbf {I} - \mathbf {A} | = \left| \begin{array}{c c} s & - 2 0. 6 \\ - 1 & s \end{array} \right| = s ^ {2} - 2 0. 6 = s ^ {2} + a _ {1} s + a _ {2} = 0
$$

we have

$$a _ {1} = 0, \quad a _ {2} = - 2 0. 6$$

The desired characteristic equation is

$$(s + 1 0) ^ {2} = s ^ {2} + 2 0 s + 1 0 0 = s ^ {2} + \alpha_ {1} s + \alpha_ {2} = 0$$

Hence,

$$\alpha_ {1} = 2 0, \quad \alpha_ {2} = 1 0 0$$
