# Example 3.9 The inverse of the controllability matrix

Consider the third-order system

$$
x (k + 1) = \left( \begin{array}{c c c} - a _ {1} & - a _ {2} & - a _ {3} \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right) x (k) + \left( \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right) u (k)
$$

which is in controllable form. The controllability matrix is

$$
W _ {c} = \left( \begin{array}{l l l} \Gamma & \Phi \Gamma & \Phi^ {2} \Gamma \end{array} \right) = \left( \begin{array}{c c c} 1 & - a _ {1} & a _ {1} ^ {2} - a _ {2} \\ 0 & 1 & - a _ {1} \\ 0 & 0 & 1 \end{array} \right)
$$

The inverse is given by

$$
W _ {c} ^ {- 1} = \left( \begin{array}{c c c} 1 & a _ {1} & a _ {2} \\ 0 & 1 & a _ {1} \\ 0 & 0 & 1 \end{array} \right)
$$

The example can be generalized to the nth-order case, where

$$
W _ {c} ^ {- 1} = \left( \begin{array}{c c c c c c} 1 & a _ {1} & a _ {2} & \dots & a _ {n - 2} & a _ {n - 1} \\ 0 & 1 & a _ {1} & \dots & a _ {n - 3} & a _ {n - 2} \\ \vdots & \vdots & \vdots & \dots & \ddots & \vdots \\ 0 & 0 & 0 & \dots & 1 & a _ {1} \\ 0 & 0 & 0 & \dots & 0 & 1 \end{array} \right)
$$
