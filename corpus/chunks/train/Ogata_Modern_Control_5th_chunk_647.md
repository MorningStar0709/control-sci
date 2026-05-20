$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & - a _ {n} \\ 1 & 0 & \dots & 0 & - a _ {n - 1} \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ 0 & 0 & \dots & 1 & - a _ {1} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} b _ {n} - a _ {n} b _ {0} \\ b _ {n - 1} - a _ {n - 1} b _ {0} \\ \cdot \\ \cdot \\ \cdot \\ b _ {1} - a _ {1} b _ {0} \end{array} \right] u \tag {9-5}

y = \left[ \begin{array}{l l l l l} 0 & 0 & \dots & 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n - 1} \\ x _ {n} \end{array} \right] + b _ {0} u \tag {9-6}
$$

Note that the n\*n state matrix of the state equation given by Equation (9–5) is the transpose of that of the state equation defined by Equation (9–3).

Diagonal Canonical Form. Consider the transfer-function system defined by Equation (9–2). Here we consider the case where the denominator polynomial involves only distinct roots. For the distinct-roots case, Equation (9–2) can be written as

$$
\begin{array}{l} \frac {Y (s)}{U (s)} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{(s + p _ {1}) (s + p _ {2}) \cdots (s + p _ {n})} \\ = b _ {0} + \frac {c _ {1}}{s + p _ {1}} + \frac {c _ {2}}{s + p _ {2}} + \dots + \frac {c _ {n}}{s + p _ {n}} \tag {9-7} \\ \end{array}
$$

The diagonal canonical form of the state-space representation of this system is given by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ . \\ . \\ . \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c c} - p _ {1} & & & & & 0 \\ & - p _ {2} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & - p _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ . \\ . \\ . \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 1 \\ . \\ . \\ . \\ 1 \end{array} \right] u \tag {9-8}

y = \left[ \begin{array}{l l l l} c _ {1} & c _ {2} & \dots & c _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + b _ {0} u \tag {9-9}
$$
