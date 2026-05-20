$$\ddot {\theta} = 2 0. 6 0 1 \theta - u \tag {10-45}\ddot {x} = 0. 5 u - 0. 4 9 0 5 \theta \tag {10-46}$$

Let us define the state variables $x _ { 1 } , x _ { 2 } , x _ { 3 }$ , and $x _ { 4 }$ as

$$x _ {1} = \thetax _ {2} = \dot {\theta}x _ {3} = xx _ {4} = \dot {x}$$

Then, referring to Equations (10–45) and (10–46) and Figure 10–9 and considering the cart position x as the output of the system, we obtain the equations for the system as follows:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-47}y = \mathbf {C x} \tag {10-48}u = - \mathbf {K} \mathbf {x} + k _ {I} \xi \tag {10-49}\dot {\xi} = r - y = r - \mathbf {C x} \tag {10-50}$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 2 0. 6 0 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ - 0. 4 9 0 5 & 0 & 0 & 0 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \\ 0. 5 \end{array} \right], \qquad \mathbf {C} = [ 0 \quad 0 \quad 1 \quad 0 ]
$$

For the type 1 servo system, we have the state error equation as given by Equation (10–40):

$$\dot {\mathbf {e}} = \hat {\mathbf {A}} \mathbf {e} + \hat {\mathbf {B}} u _ {e} \tag {10-51}$$

where

$$
\hat {\mathbf {A}} = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 2 0. 6 0 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ - 0. 4 9 0 5 & 0 & 0 & 0 & 0 \\ 0 & 0 & - 1 & 0 & 0 \end{array} \right], \qquad \hat {\mathbf {B}} = \left[ \begin{array}{c} \mathbf {B} \\ 0 \end{array} \right] = \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \\ 0. 5 \\ 0 \end{array} \right]
$$

and the control signal is given by Equation (10–41):

$$u _ {e} = - \hat {\mathbf {K}} \mathbf {e}$$

where

$$
\hat {\mathbf {K}} = \left[ \begin{array}{c c} \mathbf {K} & - k _ {I} \end{array} \right] = \left[ \begin{array}{c c c c c} k _ {1} & k _ {2} & k _ {3} & k _ {4} & - k _ {I} \end{array} \right]
$$

To obtain a reasonable speed and damping in the response of the designed system (for example, the settling time of approximately 4 \~ 5 sec and the maximum overshoot of 15% \~ 16% in the step response of the cart), let us choose the desired closed-loop poles at $s = \mu _ { i }$ $( i = 1 , 2 , \bar { 3 , 4 , 5 ) }$ , where

$$\mu_ {1} = - 1 + j \sqrt {3}, \quad \mu_ {2} = - 1 - j \sqrt {3}, \quad \mu_ {3} = - 5, \quad \mu_ {4} = - 5, \quad \mu_ {5} = - 5$$

We shall determine the necessary state-feedback gain matrix by the use of MATLAB.

Before we proceed further, we must examine the rank of matrix P, where

$$
\mathbf {P} = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ - \mathbf {C} & 0 \end{array} \right]
$$
