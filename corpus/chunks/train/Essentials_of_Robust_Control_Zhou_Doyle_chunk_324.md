# 12.4 Problems

Problem 12.1 Assume that $G ( s ) : = \left\lceil { \frac { A \left\lceil B \right\rceil } { C \left\lceil D \right\rceil } } \right\rceil \in { \mathcal { R L } } _ { \infty }$ is a stabilizable and detectable realization and $\gamma > \| G ( s ) \| _ { \infty }$ . Show that there exists a transfer matrix $M \in$ $\mathcal { R L } _ { \infty }$ such that $M ^ { \sim } M = \gamma ^ { 2 } I - G ^ { \sim } G$ and $M ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ . A particular realization of M is

$$
M (s) = \left[ \begin{array}{c c} A & B \\ \hline - R ^ {1 / 2} F & R ^ {1 / 2} \end{array} \right]
$$

where

$$
R = \gamma^ {2} I - D ^ {*} DF = R ^ {- 1} (B ^ {*} X + D ^ {*} C)
\begin{array}{r l r} {X} & {=} & {\mathrm{Ric} \left[ \begin{array}{c c} {A + B R ^ {- 1} D ^ {*} C} & {B R ^ {- 1} B ^ {*}} \\ {- C ^ {*} (I + D R ^ {- 1} D ^ {*}) C} & {- (A + B R ^ {- 1} D ^ {*} C) ^ {*}} \end{array} \right]} \end{array}
$$

and $X \geq 0$ if A is stable.

Problem 12.2 Let $G ( s ) ~ = ~ [ { \frac { A | ~ B ~ ] } { C | ~ D ~ ] } }$ be a stabilizable and detectable realization. C

Suppose $G ^ { \sim } ( j \omega ) G ( j \omega ) > 0$ for all ω or $\left[ \begin{array} { l l } { A - j \omega } & { B } \\ { C } & { D } \end{array} \right]$ has full-column rank for all ω.

$$
X = \operatorname{Ric} \left[ \begin{array}{c c} A - B R ^ {- 1} D ^ {*} C & - B R ^ {- 1} B ^ {*} \\ - C ^ {*} (I - D R ^ {- 1} D ^ {*}) C & - (A - B R ^ {- 1} D ^ {*} C) ^ {*} \end{array} \right]
$$

with $R : = D ^ { \ast } D > 0$ . Show

$$W ^ {\sim} W = G ^ {\sim} G$$

where $W ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ and

$$
W = \left[ \begin{array}{c c} A & B \\ \hline R ^ {- 1 / 2} (D ^ {*} C + B ^ {*} X) & R ^ {1 / 2} \end{array} \right].
$$

Problem 12.3 A square $( m \times m )$ matrix function $G ( s ) \in \mathcal { R } \mathcal { H } _ { \infty }$ is said to be positive real (PR) if $G ( j \omega ) + G ^ { * } ( j \omega ) \geq 0$ for all finite $\omega ;$ and $G ( s )$ is said to be strictly positive real (SPR) if $G ( j \omega ) + G ^ { * } ( j \omega ) > 0$ for all $\omega \in \mathbb { R }$ . Let $\left[ { \frac { A \left. B \right. } { C \left. D \right. } } \right]$ be a state-space realization of $G ( s )$ with A stable (not necessarily a minimal realization). Suppose there exist $X \geq 0 , Q$ , and W such that

$$X A + A ^ {*} X = - Q ^ {*} Q \tag {12.20}B ^ {*} X + W ^ {*} Q = C \tag {12.21}D + D ^ {*} = W ^ {*} W, \tag {12.22}$$

Show that G(s) is positive real and

$$G (s) + G ^ {\sim} (s) = M ^ {\sim} (s) M (s)$$

with $M ( s ) = [ { \frac { A \lfloor B \rfloor } { Q \rfloor W } } ]$ Furthermore, if $M ( j \omega )$ has full-column rank for all $\omega \in \mathbb { R }$ , then $G ( s )$ is strictly positive real.
