By equating the coefficients of the like powers of s on both sides of this last equation, we can determine the values of $k _ { e 1 } , k _ { e 2 }$ , and $k _ { e 3 }$ . This approach is convenient if $n = 1$ , 2, or 3, where n is the dimension of the state vector x. (Although this approach can be used when $n = 4 , 5 , 6 , \ldots$ , the computations involved may become very tedious.)

Another approach to the determination of the state observer gain matrix $\mathbf { K } _ { e }$ is to use Ackermann’s formula. This approach is presented in the following.

Ackermann’s Formula. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-62}y = \mathbf {C x} \tag {10-63}$$

In Section 10–2 we derived Ackermann’s formula for pole placement for the system defined by Equation (10–62).The result was given by Equation (10–18), rewritten thus:

$$
\mathbf {K} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] ^ {- 1} \phi (\mathbf {A})
$$

For the dual of the system defined by Equations (10–62) and (10–63),

$$\dot {\mathbf {z}} = \mathbf {A} ^ {*} \mathbf {z} + \mathbf {C} ^ {*} vn = \mathbf {B} ^ {*} \mathbf {z}$$

the preceding Ackermann’s formula for pole placement is modified to

$$
\mathbf {K} = \left[ \begin{array}{l l l l l} 0 & 0 & \dots & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right] ^ {- 1} \phi (\mathbf {A} ^ {*}) \tag {10-64}
$$

As stated earlier, the state observer gain matrix $\mathbf { K } _ { e }$ is given by $\mathbf { K } ^ { \ast }$ , where K is given by Equation (10–64). Thus,

$$
\mathbf {K} _ {e} = \mathbf {K} ^ {*} = \phi (\mathbf {A} ^ {*}) ^ {*} \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ . \\ . \\ . \\ \mathbf {C A} ^ {n - 2} \\ \mathbf {C A} ^ {n - 1} \end{array} \right] ^ {- 1} \left[ \begin{array}{l} 0 \\ 0 \\ . \\ . \\ . \\ 0 \\ 1 \end{array} \right] = \phi (\mathbf {A}) \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ . \\ . \\ . \\ \mathbf {C A} ^ {n - 2} \\ \mathbf {C A} ^ {n - 1} \end{array} \right] ^ {- 1} \left[ \begin{array}{l} 0 \\ 0 \\ . \\ . \\ . \\ 0 \\ 0 \\ 1 \end{array} \right] \tag {10-65}
$$

where $\phi ( s )$ is the desired characteristic polynomial for the state observer, or
