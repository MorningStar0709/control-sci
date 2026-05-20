It is desired to find the optimal control signal u such that the performance index

$$
J = \int_ {0} ^ {\infty} \left(\mathbf {x} ^ {T} \mathbf {Q x} + u ^ {2}\right) d t, \quad \mathbf {Q} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & \mu \end{array} \right]
$$

is minimized. Determine the optimal signal u(t).

B–10–21. Consider the inverted-pendulum system shown in Figure 10–59. It is desired to design a regulator system that will maintain the inverted pendulum in a vertical position in the presence of disturbances in terms of angle u and/or angular velocity ${ \dot { \theta } } .$ The regulator system is required. to return the cart to its reference position at the end of each control process. (There is no reference input to the cart.)

The state-space equation for the system is given by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 2 0. 6 0 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ - 0. 4 9 0 5 & 0 & 0 & 0 \end{array} \right]

\mathbf {B} = \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \\ 0. 5 \end{array} \right], \qquad \mathbf {x} = \left[ \begin{array}{c} \theta \\ \dot {\theta} \\ x \\ \dot {x} \end{array} \right]
$$

We shall use the state-feedback control scheme

$$u = - \mathbf {K x}$$

Using MATLAB, determine the state-feedback gain matrix $\mathbf { K } = \left[ k _ { 1 } k _ { 2 } k _ { 3 } k _ { 4 } \right]$ such that the following performance index J is minimized:

$$J = \int_ {0} ^ {\infty} (\mathbf {x} ^ {*} \mathbf {Q x} + u ^ {*} R u) d t$$

where

$$
\mathbf {Q} = \left[ \begin{array}{c c c c} 1 0 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right], \quad R = 1
$$

Then obtain the system response to the following initial condition:

$$
\left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \\ x _ {3} (0) \\ x _ {4} (0) \end{array} \right] = \left[ \begin{array}{c} 0. 1 \\ 0 \\ 0 \\ 0 \end{array} \right]
$$

Plot response curves u versus $t , { \dot { \theta } }$ versus t, x versus t, and x versus t.
