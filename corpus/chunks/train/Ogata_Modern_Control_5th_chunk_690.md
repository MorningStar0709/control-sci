# EXAMPLE PROBLEMS AND SOLUTIONS

A–9–1. Consider the transfer function system defined by Equation (9–2), rewritten

$$\frac {Y (s)}{U (s)} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} \tag {9-68}$$

Derive the following controllable canonical form of the state-space representation for this transfer-function system:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \dot {x} _ {n - 1} \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n - 1} \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ \cdot \\ \cdot \\ \cdot \\ 0 \\ 1 \end{array} \right] u \tag {9-69}

y = \left[ b _ {n} - a _ {n} b _ {0} \mid b _ {n - 1} - a _ {n - 1} b _ {0} \mid \dots \mid b _ {1} - a _ {1} b _ {0} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + b _ {0} u \tag {9-70}
$$

Solution. Equation (9–68) can be written as

$$\frac {Y (s)}{U (s)} = b _ {0} + \frac {\left(b _ {1} - a _ {1} b _ {0}\right) s ^ {n - 1} + \cdots + \left(b _ {n - 1} - a _ {n - 1} b _ {0}\right) s + \left(b _ {n} - a _ {n} b _ {0}\right)}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}}$$

which can be modified to

$$Y (s) = b _ {0} U (s) + \hat {Y} (s) \tag {9-71}$$

where

$$\hat {Y} (s) = \frac {(b _ {1} - a _ {1} b _ {0}) s ^ {n - 1} + \cdots + (b _ {n - 1} - a _ {n - 1} b _ {0}) s + (b _ {n} - a _ {n} b _ {0})}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} U (s)$$

Let us rewrite this last equation in the following form:

$$
\begin{array}{l} \frac {\hat {Y} (s)}{\left(b _ {1} - a _ {1} b _ {0}\right) s ^ {n - 1} + \cdots + \left(b _ {n - 1} - a _ {n - 1} b _ {0}\right) s + \left(b _ {n} - a _ {n} b _ {0}\right)} \\ = \frac {U (s)}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} = Q (s) \\ \end{array}
$$

From this last equation, the following two equations may be obtained:

$$s ^ {n} Q (s) = - a _ {1} s ^ {n - 1} Q (s) - \dots - a _ {n - 1} s Q (s) - a _ {n} Q (s) + U (s) \tag {9-72}\hat {Y} (s) = \bigl (b _ {1} - a _ {1} b _ {0} \bigr) s ^ {n - 1} Q (s) + \dots + \bigl (b _ {n - 1} - a _ {n - 1} b _ {0} \bigr) s Q (s)+ \left(b _ {n} - a _ {n} b _ {0}\right) Q (s) \tag {9-73}$$

Now define state variables as follows:
