# 9–3 TRANSFORMATION OF SYSTEM MODELS WITH MATLAB

In this section we shall consider the transformation of the system model from transfer function to state space, and vice versa. We shall begin our discussion with the transformation from transfer function to state space.

Let us write the closed-loop transfer function as

$$\frac {Y (s)}{U (s)} = \frac {\text { numerator polynomial in } s}{\text { denominator polynomial in } s} = \frac {\text { num }}{\text { den }}$$

Once we have this transfer-function expression, the MATLAB command

$$[ A, B, C, D ] = \text { tf2ss(num,den) }$$

will give a state-space representation. It is important to note that the state-space representation for any system is not unique. There are many (indeed, infinitely many) statespace representations for the same system.The MATLAB command gives one possible such state-space representation.

State-Space Formulation of Transfer-Function Systems. Consider the transfer-function system

$$\frac {Y (s)}{U (s)} = \frac {1 0 s + 1 0}{s ^ {3} + 6 s ^ {2} + 5 s + 1 0} \tag {9-22}$$

There are many (again, infinitely many) possible state-space representations for this system. One possible state-space representation is

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 0 & - 5 & - 6 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 0 \\ - 5 0 \end{array} \right] u

y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + [ 0 ] u
$$

Another possible state-space representation (among infinitely many alternatives) is

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{r r r} - 6 & - 5 & - 1 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right] u \tag {9-23}

y = \left[ \begin{array}{l l l} 0 & 1 0 & 1 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + [ 0 ] u \tag {9-24}
$$

MATLAB transforms the transfer function given by Equation (9–22) into the state-space representation given by Equations (9–23) and (9–24). For the example system considered here, MATLAB Program 9–1 will produce matrices A, B, C, and D.
