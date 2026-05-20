$$
| s \mathbf {I} - \mathbf {A} | = \left| \begin{array}{c c} s - 1 & - 1 \\ 4 & s + 3 \end{array} \right| = (s - 1) (s + 3) + 4
= s ^ {2} + 2 s + 1 = s ^ {2} + a _ {1} s + a _ {2}
$$

we have

$$a _ {1} = 2, \quad a _ {2} = 1$$

Define

$$\mathbf {T} = \mathbf {M W}$$

where

$$
\mathbf {M} = \left[ \begin{array}{c c} 0 & 2 \\ 2 & - 6 \end{array} \right], \qquad \mathbf {W} = \left[ \begin{array}{c c} 2 & 1 \\ 1 & 0 \end{array} \right]
$$

Then

$$
\mathbf {T} = \left[ \begin{array}{c c} 0 & 2 \\ 2 & - 6 \end{array} \right] \left[ \begin{array}{c c} 2 & 1 \\ 1 & 0 \end{array} \right] = \left[ \begin{array}{c c} 2 & 0 \\ - 2 & 2 \end{array} \right]
$$

and

$$
\mathbf {T} ^ {- 1} = \left[ \begin{array}{c c} 0. 5 & 0 \\ 0. 5 & 0. 5 \end{array} \right]
$$

Define

$$\mathbf {x} = \mathbf {T} \hat {\mathbf {x}}$$

Then the state equation becomes

$$\dot {\hat {\mathbf {x}}} = \mathbf {T} ^ {- 1} \mathbf {A} \mathbf {T} \hat {\mathbf {x}} + \mathbf {T} ^ {- 1} \mathbf {B} u$$

Since

$$
\mathbf {T} ^ {- 1} \mathbf {A T} = \left[ \begin{array}{c c} 0. 5 & 0 \\ 0. 5 & 0. 5 \end{array} \right] \left[ \begin{array}{c c} 1 & 1 \\ - 4 & - 3 \end{array} \right] \left[ \begin{array}{c c} 2 & 0 \\ - 2 & 2 \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - 2 \end{array} \right]
$$

and

$$
\mathbf {T} ^ {- 1} \mathbf {B} = \left[ \begin{array}{c c} 0. 5 & 0 \\ 0. 5 & 0. 5 \end{array} \right] \left[ \begin{array}{c} 0 \\ 2 \end{array} \right] = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

we have

$$
\left[ \begin{array}{c} \dot {\hat {x}} _ {1} \\ \dot {\hat {x}} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - 2 \end{array} \right] \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u
$$

which is in the controllable canonical form.

A–10–5. Consider a system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 2 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c} 1 & 0 \end{array} \right]
$$

The characteristic equation of the system is

$$
| s \mathbf {I} - \mathbf {A} | = \left| \begin{array}{c c} s & - 1 \\ 2 & s + 3 \end{array} \right| = s ^ {2} + 3 s + 2 = (s + 1) (s + 2) = 0
$$

The eigenvalues of matrix A are –1 and –2.
