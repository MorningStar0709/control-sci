$$\dot {x} _ {1} = x _ {2} \tag {5.53}\dot {x} _ {2} = \frac {- k _ {1} - k _ {2}}{m _ {1}} x _ {1} + \frac {- b _ {1} - b _ {2}}{m _ {1}} x _ {2} + \frac {k _ {2}}{m _ {1}} x _ {3} + \frac {b _ {2}}{m _ {1}} x _ {4} + \frac {k _ {1}}{m _ {1}} u _ {1} + \frac {b _ {1}}{m _ {1}} u _ {2} \tag {5.54}\dot {x} _ {3} = x _ {4} \tag {5.55}\dot {x} _ {4} = \frac {k _ {2}}{m _ {2}} x _ {1} + \frac {b _ {2}}{m _ {2}} x _ {2} - \frac {k _ {2}}{m _ {2}} x _ {3} - \frac {b _ {2}}{m _ {2}} x _ {4} \tag {5.56}$$

The complete state equation in matrix-vector format is the collection of Eqs. (5.53)– (5.56)

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - \left(k _ {1} + k _ {2}\right) / m _ {1} & - \left(b _ {1} + b _ {2}\right) / m _ {1} & k _ {2} / m _ {1} & b _ {2} / m _ {1} \\ 0 & 0 & 0 & 1 \\ k _ {2} / m _ {2} & b _ {2} / m _ {2} & - k _ {2} / m _ {2} & - b _ {2} / m _ {2} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ k _ {1} / m _ {1} & b _ {1} / m _ {1} \\ 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \tag {5.57}
$$

Recall that the two system outputs or measurements are specified as $y _ { 1 } = z _ { 2 }$ and $y _ { 2 } = \ddot { z } _ { 2 }$ . The first output equation is simply $y _ { 1 } = x _ { 3 }$ , and the second output equation is obtained from the fourth state equation (5.56), or the bottomrow terms in Eq. (5.57)

$$
\left[ \begin{array}{l} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ k _ {2} / m _ {2} & b _ {2} / m _ {2} & - k _ {2} / m _ {2} & - b _ {2} / m _ {2} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] + \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} u _ {1} \\ u _ {2} \end{array} \right] \tag {5.58}
$$
