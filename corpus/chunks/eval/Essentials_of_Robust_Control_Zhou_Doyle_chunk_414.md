= \left[ \begin{array}{c c c} A & - L Z ^ {- 1} & B \\ \hline \left[ \begin{array}{c} - (I + D D ^ {*}) ^ {- \frac {1}{2}} C \\ (I + D ^ {*} D) ^ {- \frac {1}{2}} D ^ {*} C \end{array} \right] & \left[ \begin{array}{c} - (I + D D ^ {*}) ^ {- \frac {1}{2}} Z ^ {- 1} \\ (I + D ^ {*} D) ^ {- \frac {1}{2}} D ^ {*} Z ^ {- 1} \end{array} \right] & \left[ \begin{array}{c} 0 \\ I \end{array} \right] \\ Z C & I & Z D (I + D ^ {*} D) ^ {- \frac {1}{2}} \end{array} \right].
$$

Now the formulas in Chapter 14 can be applied to $\hat { G }$ to obtain a controller $\tilde { K }$ and then the K can be obtained from $K = - ( I + D ^ { * } D ) ^ { - { \frac { 1 } { 2 } } } \tilde { K } Z$ . We shall leave the detail to the reader. In the sequel, we shall consider the case $D = 0$ and $Z = I$ . In this case, we have $\gamma > 1$ and

$$X _ {\infty} (A - \frac {L C}{\gamma^ {2} - 1}) + (A - \frac {L C}{\gamma^ {2} - 1}) ^ {*} X _ {\infty} - X _ {\infty} (B B ^ {*} - \frac {L L ^ {*}}{\gamma^ {2} - 1}) X _ {\infty} + \frac {\gamma^ {2} C ^ {*} C}{\gamma^ {2} - 1} = 0Y _ {\infty} (A + L C) ^ {*} + (A + L C) Y _ {\infty} - Y _ {\infty} C ^ {*} C Y _ {\infty} = 0.$$

It is clear that $Y _ { \infty } = 0$ is the stabilizing solution. Hence by the formulas in Chapter 14 we have

$$
\left[ \begin{array}{l l} L _ {1 \infty} & L _ {2 \infty} \end{array} \right] = \left[ \begin{array}{l l} 0 & L \end{array} \right]
$$

and

$$Z _ {\infty} = I, \hat {D} _ {1 1} = 0, \hat {D} _ {1 2} = I, \hat {D} _ {2 1} = \frac {\sqrt {\gamma^ {2} - 1}}{\gamma} I.$$

The results are summarized in the following theorem.

Theorem 16.1 Let $D = 0$ and let L be such that $A + L C$ is stable. Then there exists a controller K such that

$$
\left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} <   \gamma
$$

$i f f \gamma > 1$ and there exists a stabilizing solution $X _ { \infty } \geq 0$ solving

$$X _ {\infty} (A - \frac {L C}{\gamma^ {2} - 1}) + (A - \frac {L C}{\gamma^ {2} - 1}) ^ {*} X _ {\infty} - X _ {\infty} (B B ^ {*} - \frac {L L ^ {*}}{\gamma^ {2} - 1}) X _ {\infty} + \frac {\gamma^ {2} C ^ {*} C}{\gamma^ {2} - 1} = 0.$$

Moreover, if the above conditions hold a central controller is given by

$$
K = \left[ \begin{array}{c c} A - B B ^ {*} X _ {\infty} + L C & L \\ \hline - B ^ {*} X _ {\infty} & 0 \end{array} \right].
$$

It is clear that the existence of a robust stabilizing controller depends on the choice of the stabilizing matrix $L { \mathrm { ( i . e . , } }$ the choice of the coprime factorization). Now let $Y \geq 0$ be the stabilizing solution to

$$A Y + Y A ^ {*} - Y C ^ {*} C Y + B B ^ {*} = 0$$
