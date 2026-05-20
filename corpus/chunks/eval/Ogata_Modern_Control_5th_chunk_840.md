It is desired to have eigenvalues at –3 and –5 by using a state-feedback control u=–Kx. Determine the necessary feedback gain matrix K and the control signal u.

Solution. The given system is completely state controllable, since the rank of

$$
\mathbf {M} = \left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] = \left[ \begin{array}{c c} 0 & 2 \\ 2 & - 6 \end{array} \right]
$$

is 2. Hence, arbitrary pole placement is possible.

Since the characteristic equation of the original system is

$$s ^ {2} + 3 s + 2 = s ^ {2} + a _ {1} s + a _ {2} = 0$$

we have

$$a _ {1} = 3, \quad a _ {2} = 2$$

The desired characteristic equation is

$$(s + 3) (s + 5) = s ^ {2} + 8 s + 1 5 = s ^ {2} + \alpha_ {1} s + \alpha_ {2} = 0$$

Hence,

$$\alpha_ {1} = 8, \quad \alpha_ {2} = 1 5$$

It is important to point out that the original state equation is not in the controllable canonical form, because matrix B is not

$$
\left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

Hence, the transformation matrix T must be determined.

$$
\mathbf {T} = \mathbf {M W} = \left[ \begin{array}{c c} \mathbf {B} & \mathbf {A B} \end{array} \right] \left[ \begin{array}{c c} a _ {1} & 1 \\ 1 & 0 \end{array} \right] = \left[ \begin{array}{c c} 0 & 2 \\ 2 & - 6 \end{array} \right] \left[ \begin{array}{c c} 3 & 1 \\ 1 & 0 \end{array} \right] = \left[ \begin{array}{c c} 2 & 0 \\ 0 & 2 \end{array} \right]
$$

Hence,

$$
\mathbf {T} ^ {- 1} = \left[ \begin{array}{c c} 0. 5 & 0 \\ 0 & 0. 5 \end{array} \right]
$$

Referring to Equation (10–13), the necessary feedback gain matrix is given by

$$
\begin{array}{l} \mathbf {K} = \left[ \alpha_ {2} - a _ {2} \mid \alpha_ {1} - a _ {1} \right] \mathbf {T} ^ {- 1} \\ = [ 1 5 - 2 \mid 8 - 3 ] \left[ \begin{array}{c c} 0. 5 & 0 \\ 0 & 0. 5 \end{array} \right] = [ 6. 5 \quad 2. 5 ] \\ \end{array}
$$

Thus, the control signal u becomes

$$
u = - \mathbf {K} \mathbf {x} = - [ 6. 5 \quad 2. 5 ] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

A–10–6. A regulator system has a plant

$$\frac {Y (s)}{U (s)} = \frac {1 0}{(s + 1) (s + 2) (s + 3)}$$

Define state variables as

$$x _ {1} = yx _ {2} = \dot {x} _ {1}x _ {3} = \dot {x} _ {2}$$

By use of the state-feedback control $u = - \mathbf { K } \mathbf { x } ,$ it is desired to place the closed-loop poles at

$$s = - 2 + j 2 \sqrt {3}, \quad s = - 2 - j 2 \sqrt {3}, \quad s = - 1 0$$

Obtain the necessary state-feedback gain matrix K with MATLAB.

Solution. The state-space equations for the system become
