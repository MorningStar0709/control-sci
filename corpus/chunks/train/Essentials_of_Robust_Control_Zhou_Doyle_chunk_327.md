$$
Y = \mathrm{Ric} \left[ \begin{array}{c c} (A - B D ^ {*} \tilde {R} ^ {- 1} C) ^ {*} & - C ^ {*} \tilde {R} ^ {- 1} C \\ - B R ^ {- 1} B ^ {*} & - (A - B D ^ {*} \tilde {R} ^ {- 1} C) \end{array} \right] \geq 0.
$$

(c) Show that the controllability Gramian P and the observability Gramian $Q$ of $\left[ \begin{array} { l } { M } \\ { N } \end{array} \right]$ are given by

$$P = (I + Y X) ^ {- 1} Y, \quad Q = X$$

while the controllability Gramian $\tilde { P }$ and observability Gramian $\tilde { Q } ~ \mathrm { o f } ~ \biggl [ ~ \tilde { M } ~ \tilde { N } ~ \biggr ]$ are given by

$$\tilde {P} = Y, \quad \tilde {Q} = (I + X Y) ^ {- 1} X.$$

Problem 12.9 Let $G ( s ) = \left[ { \frac { A \mid B } { C \mid D } } \right]$ Find $M _ { 1 }$ and $M _ { 2 }$ such that $M _ { 1 } ^ { - 1 } , M _ { 2 } ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ and

$$M _ {1} M _ {1} ^ {\sim} = I + G G ^ {\sim}, \quad M _ {2} ^ {\sim} M _ {2} = I + G ^ {\sim} G.$$

Problem 12.10 Let $A \in \mathbb { R } ^ { m \times m }$ , $B \in \mathbb { R } ^ { n \times n }$ , $C \in \mathbb { R } ^ { m \times n }$ , and consider the Sylvester equation

$$A X + X B = C$$

for an unknown matrix $\ b X \in \mathbb { R } ^ { m \times n }$ . Let

$$
M = \left[ \begin{array}{c c} B & 0 \\ C & - A \end{array} \right], N = \left[ \begin{array}{c c} B & 0 \\ 0 & - A \end{array} \right].
$$

1. Let the columns of ${ \left[ \begin{array} { l } { U } \\ { V } \end{array} \right] } \in \mathbb { C } ^ { n + m \times n }$ be the eigenvectors of M associated with the eigenvalues of B and suppose U is nonsingular. Show that

$$X = V U ^ {- 1}$$

solves the Sylvester equation. Moreover, every solution of the Sylvester equation can be written in the above form.

2. Show that the Sylvester equation has a solution if and only if M and N are similar. (See Lancaster and Tismenetsky [1985, page 423].)

Problem 12.11 Let $A \in \mathbb { R } ^ { n \times n }$ . Show that

$$P (t) = \int_ {0} ^ {t} e ^ {A ^ {*} \tau} Q e ^ {A \tau} d \tau$$

satisfies

$$\dot {P} (t) = A ^ {*} P (t) + P (t) A + Q, \quad P (0) = 0.$$

Problem 12.12 A more general case of the above problem is when the given matrices are time varying and the initial condition is not zero. Let $A ( t ) , Q ( t ) , P _ { 0 } \in \mathbb { R } ^ { n \times n }$ . Show that

$$P (t) = \Phi^ {T} (t, t _ {0}) P _ {0} \Phi (t, t _ {0}) + \int_ {t _ {0}} ^ {t} \Phi^ {T} (t, \tau) Q (\tau) \Phi (t, \tau) d \tau$$

satisfies

$$\dot {P} (t) = A ^ {*} P (t) + P (t) A + Q (t), \quad P (t _ {0}) = P _ {0}$$

where $\Phi ( t , \tau )$ is the state transition matrix for the system ${ \dot { x } } = A ( t ) x$ .

Problem 12.13 Let $A \in \mathbb { R } ^ { n \times n } , R = R ^ { * } , Q = Q ^ { * }$ . Define
