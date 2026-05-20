$$
\begin{array}{l} \mathbf {x} ^ {*} \mathbf {P} \mathbf {x} = \mathbf {x} ^ {*} \int_ {0} ^ {\infty} e ^ {\mathbf {A} ^ {*} t} \mathbf {Q} e ^ {\mathbf {A} t} d t \mathbf {x} \\ = \int_ {0} ^ {\infty} (e ^ {\mathbf {A} t} \mathbf {x}) ^ {*} \mathbf {Q} (e ^ {\mathbf {A} t} \mathbf {x}) d t > 0, \quad \text {   for   } \mathbf {x} \neq \mathbf {0} \\ = 0, \quad \text {   for   } \mathbf {x} = \mathbf {0} \\ \end{array}
$$

Hence, P is positive definite. This completes the proof.

A–10–16. Consider the control system described by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-173}$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

Assuming the linear control law

$$u = - \mathbf {K} \mathbf {x} = - k _ {1} x _ {1} - k _ {2} x _ {2} \tag {10-174}$$

determine the constants $k _ { 1 }$ and $k _ { 2 }$ so that the following performance index is minimized:

$$J = \int_ {0} ^ {\infty} \mathbf {x} ^ {T} \mathbf {x} d t$$

Consider only the case where the initial condition is

$$
\mathbf {x} (0) = \left[ \begin{array}{c} c \\ 0 \end{array} \right]
$$

Choose the undamped natural frequency to be 2 radsec.

Solution. Substituting Equation (10–174) into Equation (10–173), we obtain

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \mathbf {x}$$

or

$$
\begin{array}{l} \left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \left[ - k _ {1} x _ {1} - k _ {2} x _ {2} \right] \\ = \left[ \begin{array}{c c} 0 & 1 \\ - k _ {1} & - k _ {2} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] \tag {10-175} \\ \end{array}
$$

Thus,

$$
\mathbf {A} - \mathbf {B K} = \left[ \begin{array}{c c} 0 & 1 \\ - k _ {1} & - k _ {2} \end{array} \right]
$$

Elimination of $x _ { 2 }$ from Equation (10–175) yields

$$\ddot {x} _ {1} + k _ {2} \dot {x} _ {1} + k _ {1} x _ {1} = 0$$

Since the undamped natural frequency is specified as 2 radsec, we obtain

$$k _ {1} = 4$$

Therefore,

$$
\mathbf {A} - \mathbf {B K} = \left[ \begin{array}{c c} 0 & 1 \\ - 4 & - k _ {2} \end{array} \right]
$$

is a stable matrix ifA - BK $k _ { 2 } > 0$ . Our problem now is to determine the value of $k _ { 2 }$ so that the performance index
