Note that what we have derived here can be easily extended to the case when n is any positive integer.

A–10–9. Consider a system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 1 & 1 \\ - 4 & - 3 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 2 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c} 1 & 1 \end{array} \right]
$$

The rank of the observability matrix N,

$$
\mathbf {N} = \left[ \begin{array}{c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} 1 & - 3 \\ 1 & - 2 \end{array} \right]
$$

is 2. Hence, the system is completely observable. Transform the system equations into the observable canonical form.

Solution. Since

$$\left| s \mathbf {I} - \mathbf {A} \right| = s ^ {2} + 2 s + 1 = s ^ {2} + a _ {1} s + a _ {2}$$

we have

$$a _ {1} = 2, \quad a _ {2} = 1$$

Define

$$\mathbf {Q} = (\mathbf {W N} ^ {*}) ^ {- 1}$$

where

$$
\mathbf {N} = \left[ \begin{array}{c c} 1 & - 3 \\ 1 & - 2 \end{array} \right], \qquad \mathbf {W} = \left[ \begin{array}{c c} a _ {1} & 1 \\ 1 & 0 \end{array} \right] = \left[ \begin{array}{c c} 2 & 1 \\ 1 & 0 \end{array} \right]
$$

Then

$$
\mathbf {Q} = \left\{\left[ \begin{array}{c c} 2 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c c} 1 & 1 \\ - 3 & - 2 \end{array} \right] \right\} ^ {- 1} = \left[ \begin{array}{c c} - 1 & 0 \\ 1 & 1 \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} - 1 & 0 \\ 1 & 1 \end{array} \right]
$$

and

$$
\mathbf {Q} ^ {- 1} = \left[ \begin{array}{c c} - 1 & 0 \\ 1 & 1 \end{array} \right]
$$

Define

$$\mathbf {x} = \mathbf {Q} \hat {\mathbf {x}}$$

Then the state equation becomes

$$\dot {\hat {\mathbf {x}}} = \mathbf {Q} ^ {- 1} \mathbf {A} \mathbf {Q} \hat {\mathbf {x}} + \mathbf {Q} ^ {- 1} \mathbf {B} u$$

or
