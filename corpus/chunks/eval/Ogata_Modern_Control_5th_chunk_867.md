A–10–17. Consider the same inverted-pendulum system as discussed in Example 10–5.The system is shown in Figure 10–8, where $M = 2 \mathrm { k g } , m = 0 . 1$ kg, and $l = 0 . 5$ m. The block diagram for the system is shown in Figure 10–9. The system equations are given by

$$
\begin{array}{l} \dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \\ y = \mathbf {C x} \\ u = - \mathbf {K} \mathbf {x} + k _ {I} \xi \\ \dot {\xi} = r - y = r - \mathbf {C x} \\ \end{array}
$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 2 0. 6 0 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ - 0. 4 9 0 5 & 0 & 0 & 0 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \\ 0. 5 \end{array} \right], \qquad \mathbf {C} = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \end{array} \right]
$$

Referring to Equation (10–51), the error equation for the system is given by

$$\dot {\mathbf {e}} = \hat {\mathbf {A}} \mathbf {e} + \hat {\mathbf {B}} u _ {e}$$

where

$$
\hat {\mathbf {A}} = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 2 0. 6 0 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ - 0. 4 9 0 5 & 0 & 0 & 0 & 0 \\ 0 & 0 & - 1 & 0 & 0 \end{array} \right], \quad \hat {\mathbf {B}} = \left[ \begin{array}{c} \mathbf {B} \\ 0 \end{array} \right] = \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \\ 0. 5 \\ 0 \end{array} \right]
$$

and the control signal is given by Equation (10–41):

$$u _ {e} = - \hat {\mathbf {K}} \mathbf {e}$$

where

$$
\begin{array}{l} \hat {\mathbf {K}} = \left[ \begin{array}{c c} \mathbf {K} & - k _ {I} \end{array} \right] = \left[ \begin{array}{c c c c c} k _ {1} & k _ {2} & k _ {3} & k _ {4} & - k _ {I} \end{array} \right] \\ \mathbf {e} = \left[ \begin{array}{c} \mathbf {x} _ {e} \\ \xi_ {e} \end{array} \right] = \left[ \begin{array}{c} \mathbf {x} (t) - \mathbf {x} (\infty) \\ \xi (t) - \xi (\infty) \end{array} \right] \\ \mathbf {x} = \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] = \left[ \begin{array}{l} \theta \\ \dot {\theta} \\ x \\ \dot {x} \end{array} \right] \\ \end{array}
$$

Using MATLAB, determine the state feedback gain matrix $\hat { \bf K }$ such that the following performance index J is minimized:

$$J = \int_ {0} ^ {\infty} (\mathbf {e} ^ {*} \mathbf {Q e} + u ^ {*} R u) d t$$

where

$$
\mathbf {Q} = \left[ \begin{array}{c c c c c} 1 0 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{array} \right], \qquad R = 0. 0 1
$$

Obtain the unit-step response of the system designed.

Solution. A MATLAB program to determine $\hat { \bf K }$ is given in MATLAB Program 10–34.The result is

$$k _ {1} = - 1 8 8. 0 7 9 9, \qquad k _ {2} = - 3 7. 0 7 3 8, \qquad k _ {3} = - 2 6. 6 7 6 7, \qquad k _ {4} = - 3 0. 5 8 2 4, \qquad k _ {I} = - 1 0. 0 0 0 0$$
