$$
\left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \left[ \begin{array}{c c c} a _ {2} & a _ {1} & 1 \\ a _ {1} & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] = \left[ \begin{array}{c c c} - a _ {3} & 0 & 0 \\ 0 & a _ {1} & 1 \\ 0 & 1 & 0 \end{array} \right]
$$

The right-hand side of Equation (10–144) is

$$
\left[ \begin{array}{c c c} a _ {2} & a _ {1} & 1 \\ a _ {1} & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] = \left[ \begin{array}{c c c} - a _ {3} & 0 & 0 \\ 0 & a _ {1} & 1 \\ 0 & 1 & 0 \end{array} \right]
$$

Clearly, Equation (10–144) holds true. Thus, we have shown that

$$
\mathbf {T} ^ {- 1} \mathbf {A T} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right]
$$

Next, we shall show that

$$
\mathbf {T} ^ {- 1} \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] \tag {10-145}
$$

Note that Equation (10–145) can be written as

$$
\mathbf {B} = \mathbf {T} \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right] = \mathbf {M W} \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right]
$$

Noting that

$$
\mathbf {T} \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] = \left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A ^ {2} B} \end{array} \right] \left[ \begin{array}{c c c} a _ {2} & a _ {1} & 1 \\ a _ {1} & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] = \left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A ^ {2} B} \end{array} \right] \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right] = \mathbf {B}
$$

we have

$$
\mathbf {T} ^ {- 1} \mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right]
$$

The derivation shown here can be easily extended to the general case of any positive integer n.

A–10–4. Consider the state equation

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 1 & 1 \\ - 4 & - 3 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 2 \end{array} \right]
$$

The rank of the controllability matrix M,

$$
\mathbf {M} = \left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 0 & 2 \\ 2 & - 6 \end{array} \right]
$$

is 2. Thus, the system is completely state controllable. Transform the given state equation into the controllable canonical form.

Solution. Since
