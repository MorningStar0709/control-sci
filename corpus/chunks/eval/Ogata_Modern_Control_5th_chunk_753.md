$$
\left[ \begin{array}{l} \dot {\mathbf {x}} (t) - \dot {\mathbf {x}} (\infty) \\ \dot {\xi} (t) - \dot {\xi} (\infty) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} (t) - \mathbf {x} (\infty) \\ \xi (t) - \xi (\infty) \end{array} \right] + \left[ \begin{array}{c} \mathbf {B} \\ 0 \end{array} \right] [ u (t) - u (\infty) ] \tag {10-37}
$$

Define

$$
\begin{array}{l} \mathbf {x} (t) - \mathbf {x} (\infty) = \mathbf {x} _ {e} (t) \\ \xi (t) - \xi (\infty) = \xi_ {e} (t) \\ u (t) - u (\infty) = u _ {e} (t) \\ \end{array}
$$

Then Equation (10–37) can be written as

$$
\left[ \begin{array}{l} \dot {\mathbf {x}} _ {e} (t) \\ \dot {\boldsymbol {\xi}} _ {e} (t) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} _ {e} (t) \\ \boldsymbol {\xi} _ {e} (t) \end{array} \right] + \left[ \begin{array}{c} \mathbf {B} \\ 0 \end{array} \right] u _ {e} (t) \tag {10-38}
$$

where

$$u _ {e} (t) = - \mathbf {K x} _ {e} (t) + k _ {I} \xi_ {e} (t) \tag {10-39}$$

Define a new (n+1)th-order error vector $\mathbf { e } ( t )$ by

$$
\mathbf {e} (t) = \left[ \begin{array}{c} \mathbf {x} _ {e} (t) \\ \xi_ {e} (t) \end{array} \right] = (n + 1) \text {-vector}
$$

Then Equation (10–38) becomes

$$\dot {\mathbf {e}} = \hat {\mathbf {A}} \mathbf {e} + \hat {\mathbf {B}} u _ {e} \tag {10-40}$$

where

$$
\hat {\mathbf {A}} = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right], \qquad \hat {\mathbf {B}} = \left[ \begin{array}{c} \mathbf {B} \\ 0 \end{array} \right]
$$

and Equation (10–39) becomes

$$u _ {e} = - \hat {\mathbf {K}} \mathbf {e} \tag {10-41}$$

where

$$
\hat {\mathbf {K}} = \left[ \begin{array}{c c} \mathbf {K} & - k _ {I} \end{array} \right]
$$

The state error equation can be obtained by substituting Equation (10–41) into Equation (10–40):

$$\dot {\mathbf {e}} = (\hat {\mathbf {A}} - \hat {\mathbf {B}} \hat {\mathbf {K}}) \mathbf {e} \tag {10-42}$$
