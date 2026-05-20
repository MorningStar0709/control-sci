Closed-Loop Transfer Function. For the system shown in Figure 2–4, the output $C ( s )$ and input $R ( s )$ are related as follows: since

$$
\begin{array}{l} C (s) = G (s) E (s) \\ E (s) = R (s) - B (s) \\ = R (s) - H (s) C (s) \\ \end{array}
$$

eliminating E(s) from these equations gives

$$C (s) = G (s) \left[ R (s) - H (s) C (s) \right]$$

or

$$\frac {C (s)}{R (s)} = \frac {G (s)}{1 + G (s) H (s)} \tag {2-3}$$

The transfer function relating $C ( s )$ to $R ( s )$ is called the closed-loop transfer function. It relates the closed-loop system dynamics to the dynamics of the feedforward elements and feedback elements.

From Equation (2–3), C(s) is given by

$$C (s) = \frac {G (s)}{1 + G (s) H (s)} R (s)$$

Thus the output of the closed-loop system clearly depends on both the closed-loop transfer function and the nature of the input.

Obtaining Cascaded, Parallel, and Feedback (Closed-Loop) Transfer Functions with MATLAB. In control-systems analysis, we frequently need to calculate the cascaded transfer functions, parallel-connected transfer functions, and feedback-connected (closed-loop) transfer functions. MATLAB has convenient commands to obtain the cascaded, parallel, and feedback (closed-loop) transfer functions.

Suppose that there are two components $G _ { 1 } ( s )$ and $G _ { 2 } ( s )$ connected differently as shown in Figure 2–5 (a), (b), and (c), where

$$G _ {1} (s) = \frac {\text { num1 }}{\text { den1 }}, \quad G _ {2} (s) = \frac {\text { num2 }}{\text { den2 }}$$

To obtain the transfer functions of the cascaded system, parallel system, or feedback (closed-loop) system, the following commands may be used:

$$[ \text { num }, \text { den } ] = \text { series } (\text { num1 }, \text { den1 }, \text { num2 }, \text { den2 })[ \text { num }, \text { den } ] = \text { parallel } (\text { num1 }, \text { den1 }, \text { num2 }, \text { den2 })[ \text {num}, \text {den} ] = \text {feedback} (\text {num1}, \text {den1}, \text {num2}, \text {den2})$$

As an example, consider the case where

$$G _ {1} (s) = \frac {1 0}{s ^ {2} + 2 s + 1 0} = \frac {\text { num1 }}{\text { den1 }}, \quad G _ {2} (s) = \frac {5}{s + 5} = \frac {\text { num2 }}{\text { den2 }}$$

MATLAB Program 2–1 gives $C ( s ) / R ( s ) = \mathrm { n u m } /$ den for each arrangement of $G _ { 1 } ( s )$ and $G _ { 2 } ( s )$ . Note that the command

$\mathsf { p r i n t s y s } ( \mathsf { n u m } , \mathsf { d e n } )$

displays the numden Cthat is, the transfer function $C ( s ) / R ( s ) \bar { }$ D of the system considered.
