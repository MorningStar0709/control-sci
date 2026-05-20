# 2–2 TRANSFER FUNCTION AND IMPULSE-RESPONSE FUNCTION

In control theory, functions called transfer functions are commonly used to characterize the input-output relationships of components or systems that can be described by linear, time-invariant, differential equations. We begin by defining the transfer function and follow with a derivation of the transfer function of a differential equation system. Then we discuss the impulse-response function.

Transfer Function. The transfer function of a linear, time-invariant, differential equation system is defined as the ratio of the Laplace transform of the output (response function) to the Laplace transform of the input (driving function) under the assumption that all initial conditions are zero.

Consider the linear time-invariant system defined by the following differential equation:

$$
\begin{array}{l} a _ {0} ^ {(n)} y + a _ {1} ^ {(n - 1)} y + \dots + a _ {n - 1} \dot {y} + a _ {n} y \\ = b _ {0} ^ {(m)} x + b _ {1} ^ {(m - 1)} x + \dots + b _ {m - 1} \dot {x} + b _ {m} x \quad (n \geq m) \\ \end{array}
$$

where y is the output of the system and x is the input. The transfer function of this system is the ratio of the Laplace transformed output to the Laplace transformed input when all initial conditions are zero, or

$$
\begin{array}{l} \text { Transfer   function } = G (s) = \frac {\mathcal {L} [ \text { output } ]}{\mathcal {L} [ \text { input } ]} \Bigg | _ {\text { zero   initial   conditions }} \\ = \frac {Y (s)}{X (s)} = \frac {b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \cdots + b _ {m - 1} s + b _ {m}}{a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} \\ \end{array}
$$

By using the concept of transfer function, it is possible to represent system dynamics by algebraic equations in s. If the highest power of s in the denominator of the transfer function is equal to n, the system is called an nth-order system.

Comments on Transfer Function. The applicability of the concept of the transfer function is limited to linear, time-invariant, differential equation systems. The transfer function approach, however, is extensively used in the analysis and design of such systems. In what follows, we shall list important comments concerning the transfer function. (Note that a system referred to in the list is one described by a linear, time-invariant, differential equation.)
