# Exercise 2.3: Destabilization with state constraints

Consider a state feedback regulation problem with the origin as the setpoint (Muske and Rawlings, 1993). Let the system be

$$
A = \left[ \begin{array}{c c} 4 / 3 & - 2 / 3 \\ 1 & 0 \end{array} \right] \quad B = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \quad C = [ - 2 / 3 1 ]
$$

and the controller objective function tuning matrices be

$$Q = I \quad R = I \quad N = 5$$

(a) Plot the unconstrained regulator performance starting from initial condition $x ( 0 ) = { \bigg [ } 3 \quad 3 { \bigg ] } ^ { \prime }$ .

(b) Add the output constraint $y ( k ) \ \leq \ 0 . 5$ . Plot the response of the constrained regulator (both input and output). Is this regulator stabilizing? Can you modify the tuning parameters Q, R to affect stability as in Section 1.3.4?

(c) Change the output constraint to $y ( k ) \le 1 + \epsilon , \epsilon > 0$ . Plot the closed-loop response for a variety of . Are any of these regulators destabilizing?

(d) Set the output constraint back to $y ( k ) \leq 0 . 5$ and add the terminal constraint $x ( N ) = 0 .$ . What is the solution to the regulator problem in this case? Increase the horizon N. Does this problem eventually go away?
