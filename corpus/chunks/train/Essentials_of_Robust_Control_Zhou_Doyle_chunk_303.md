and where $A _ { a }$ is stable, such that K has the form

$$
K = \left[ \begin{array}{c c} A _ {e} + B _ {e} F _ {e} + L _ {e} C _ {e} & - L _ {e} \\ \hline F _ {e} & 0 \end{array} \right] \tag {11.4}
$$

where $A _ { e } + B _ { e } F _ { e }$ and $A _ { e } + L _ { e } C _ { e }$ are stable.

Proof. K is representable as in Figure 11.3 for some Q in $\mathcal { R H } _ { \infty }$ . For K to be strictly proper, Q must be strictly proper. Take a minimal realization of Q:

$$
Q = \left[ \begin{array}{c c} A _ {a} & B _ {a} \\ \hline C _ {a} & 0 \end{array} \right].
$$

Since $Q \in \mathcal { R } \mathcal { H } _ { \infty } , A _ { a }$ is stable. Let x and $x _ { a }$ denote state vectors for J and $Q ,$ respectively, and write the equations for the system in Figure 11.3:

$$\dot {x} = (A + B _ {2} F + L C _ {2}) x - L y + B _ {2} u _ {1}u = F x + u _ {1}y _ {1} = - C _ {2} x + y\dot {x} _ {a} = A _ {a} x _ {a} + B _ {a} y _ {1}u _ {1} = C _ {a} x _ {a}$$

These equations yield

$${\dot {x} _ {e}} = {(A _ {e} + B _ {e} F _ {e} + L _ {e} C _ {e}) x _ {e} - L _ {e} y}u = F _ {e} x _ {e}$$

where

$$
x _ {e} := \left[ \begin{array}{c} x \\ x _ {a} \end{array} \right], F _ {e} := \left[ \begin{array}{c c} F & C _ {a} \end{array} \right], L _ {e} := \left[ \begin{array}{c} L \\ - B _ {a} \end{array} \right]
$$

and where $A _ { e } , B _ { e } , C _ { e }$ are as in equation (11.3).

![](image/708956a67c4cc8644c20854646b47aa7a384642cd594b46c6043bfdcc894c804.jpg)

Example 11.1 Consider a standard feedback system shown in Figure 5.1 with $P = \frac { 1 } { s - 1 }$ We shall find all stabilizing controllers for P such that the steady-state errors with respect to the step input and sin 2t are both zero. It is easy to see that the controller must provide poles at 0 and $\pm 2 j$ . Now let the set of stabilizing controllers for a modified plant $\frac { ( s + 1 ) ^ { 3 } } { ( s - 1 ) s ( s ^ { 2 } + 2 ^ { 2 } ) }$ be $K _ { m }$ . Then the desired set of controllers is given by

$$K = \frac {(s + 1) ^ {3}}{s (s ^ {2} + 2 ^ {2})} K _ {m}.$$
