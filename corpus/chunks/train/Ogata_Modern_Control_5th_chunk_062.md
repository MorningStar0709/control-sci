# 2–6 TRANSFORMATION OF MATHEMATICAL MODELS WITH MATLAB

MATLAB is quite useful to transform the system model from transfer function to state space, and vice versa. We shall begin our discussion with transformation from transfer function to state space.

Let us write the closed-loop transfer function as

$$\frac {Y (s)}{U (s)} = \frac {\text { numerator polynomial in } s}{\text { denominator polynomial in } s} = \frac {\text { num }}{\text { den }}$$

Once we have this transfer-function expression, the MATLAB command

$$[ A, B, C, D ] = \text { tf2ss(num,den) }$$

will give a state-space representation. It is important to note that the state-space representation for any system is not unique. There are many (infinitely many) state-space representations for the same system. The MATLAB command gives one possible such state-space representation.

Transformation from Transfer Function to State Space Representation. Consider the transfer-function system

$$
\begin{array}{l} \frac {Y (s)}{U (s)} = \frac {s}{(s + 1 0) \left(s ^ {2} + 4 s + 1 6\right)} \\ = \frac {s}{s ^ {3} + 1 4 s ^ {2} + 5 6 s + 1 6 0} \tag {2-39} \\ \end{array}
$$

There are many (infinitely many) possible state-space representations for this system. One possible state-space representation is

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 6 0 & - 5 6 & - 1 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \\ - 1 4 \end{array} \right] u

y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + [ 0 ] u
$$

Another possible state-space representation (among infinitely many alternatives) is

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} - 1 4 & - 5 6 & - 1 6 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right] u \tag {2-40}

y = \left[ \begin{array}{l l l} 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + [ 0 ] u \tag {2-41}
$$
