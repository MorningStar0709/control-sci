# 9–2 STATE-SPACE REPRESENTATIONS OF TRANSFER-FUNCTION SYSTEMS

Many techniques are available for obtaining state-space representations of transfer-function systems. In Chapter 2 we presented a few such methods. This section presents state-space representations in the controllable, observable, diagonal, or Jordan canonical forms. (Methods for obtaining such state-space representations from transfer functions are discussed in detail in Problems A–9–1 through A–9–4.)

State-Space Representations in Canonical Forms. Consider a system defined by

$$y ^ {(n)} + a _ {1} ^ {(n - 1)} y + \dots + a _ {n - 1} \dot {y} + a _ {n} y = b _ {0} ^ {(n)} u + b _ {1} ^ {(n - 1)} u + \dots + b _ {n - 1} \dot {u} + b _ {n} u \tag {9-1}$$

where u is the input and y is the output. This equation can also be written as

$$\frac {Y (s)}{U (s)} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} \tag {9-2}$$

In what follows we shall present state-space representations of the system defined by Equation (9–1) or (9–2) in controllable canonical form, observable canonical form, and diagonal (or Jordan) canonical form.

Controllable Canonical Form. The following state-space representation is called a controllable canonical form:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \dot {x} _ {n - 1} \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & - a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n - 1} \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ \cdot \\ \cdot \\ \cdot \\ 0 \\ 1 \end{array} \right] u \tag {9-3}

y = \left[ b _ {n} - a _ {n} b _ {0} \mid b _ {n - 1} - a _ {n - 1} b _ {0} \mid \dots \mid b _ {1} - a _ {1} b _ {0} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + b _ {0} u \tag {9-4}
$$

The controllable canonical form is important in discussing the pole-placement approach to control systems design.

Observable Canonical Form. The following state-space representation is called an observable canonical form:
