$$
\left[ \begin{array}{c} \hat {\dot {x}} _ {1} \\ \hat {\dot {x}} _ {2} \\ \hat {\dot {x}} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \left[ \begin{array}{c} \hat {x} _ {1} \\ \hat {x} _ {2} \\ \hat {x} _ {3} \end{array} \right] + \left[ \begin{array}{c} \gamma_ {3} \\ \gamma_ {2} \\ \gamma_ {1} \end{array} \right] u
$$

where

$$
\left[ \begin{array}{c} \gamma_ {3} \\ \gamma_ {2} \\ \gamma_ {1} \end{array} \right] = \mathbf {Q} ^ {- 1} \mathbf {B}
$$

The transfer function $G ( s )$ for the system defined by Equations (10–155) and (10–156) is

$$G (s) = \mathbf {C Q} \left(s \mathbf {I} - \mathbf {Q} ^ {- 1} \mathbf {A Q}\right) ^ {- 1} \mathbf {Q} ^ {- 1} \mathbf {B} + D$$

Noting that

$$
\mathbf {C Q} = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right]
$$

we have

$$
G (s) = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} s & 0 & a _ {3} \\ - 1 & s & a _ {2} \\ 0 & - 1 & s + a _ {1} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} \gamma_ {3} \\ \gamma_ {2} \\ \gamma_ {1} \end{array} \right] + D
$$

Note that $D = b _ { 0 }$ . Since

$$
\left[ \begin{array}{c c c} s & 0 & a _ {3} \\ - 1 & s & a _ {2} \\ 0 & - 1 & s + a _ {1} \end{array} \right] ^ {- 1} = \frac {1}{s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + a _ {3}} \left[ \begin{array}{c c c} s ^ {2} + a _ {1} s + a _ {2} & - a _ {3} & - a _ {3} s \\ s + a _ {1} & s ^ {2} + a _ {1} s & - a _ {2} s - a _ {3} \\ 1 & s & s ^ {2} \end{array} \right]
$$

we have

$$
\begin{array}{l} G (s) = \frac {1}{s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + a _ {3}} \left[ \begin{array}{l l l} 1 & s & s ^ {2} \end{array} \right] \left[ \begin{array}{l} \gamma_ {3} \\ \gamma_ {2} \\ \gamma_ {1} \end{array} \right] + D \\ = \frac {\gamma_ {1} s ^ {2} + \gamma_ {2} s + \gamma_ {3}}{s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + a _ {3}} + b _ {0} \\ = \frac {b _ {0} s ^ {3} + \left(\gamma_ {1} + a _ {1} b _ {0}\right) s ^ {2} + \left(\gamma_ {2} + a _ {2} b _ {0}\right) s + \gamma_ {3} + a _ {3} b _ {0}}{s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + a _ {3}} \\ = \frac {b _ {0} s ^ {3} + b _ {1} s ^ {2} + b _ {2} s + b _ {3}}{s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + a _ {3}} \\ \end{array}
$$

Hence,

$$\gamma_ {1} = b _ {1} - a _ {1} b _ {0}, \quad \gamma_ {2} = b _ {2} - a _ {2} b _ {0}, \quad \gamma_ {3} = b _ {3} - a _ {3} b _ {0}$$

Thus, we have shown that

$$
\mathbf {Q} ^ {- 1} \mathbf {B} = \left[ \begin{array}{c} \gamma_ {3} \\ \gamma_ {2} \\ \gamma_ {1} \end{array} \right] = \left[ \begin{array}{c} b _ {3} - a _ {3} b _ {0} \\ b _ {2} - a _ {2} b _ {0} \\ b _ {1} - a _ {1} b _ {0} \end{array} \right]
$$
