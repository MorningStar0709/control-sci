Now let P be a proper real rational matrix. A right coprime factorization $( r c f )$ of $P$ is a factorization $P = N M ^ { - 1 }$ , where N and M are right coprime over $\mathcal { R H } _ { \infty }$ . Similarly, a left coprime factorization $( l c f )$ has the form $P = \tilde { M } ^ { - 1 } \tilde { N }$ , where $\tilde { N }$ and M˜ are left-coprime over $\mathcal { R } \mathcal { H } _ { \infty }$ . A matrix $P ( s ) \in \mathcal { R } _ { p } ( s )$ is said to have double coprime factorization if there exist a right coprime factorization $P = N M ^ { - 1 }$ , a left coprime factorization $P = \tilde { M } ^ { - 1 } \tilde { N }$ , and $X _ { r } , Y _ { r } , X _ { l } , Y _ { l } \in \mathcal { R H } _ { \infty }$ such that

$$
\left[ \begin{array}{c c} X _ {r} & Y _ {r} \\ - \tilde {N} & \tilde {M} \end{array} \right] \left[ \begin{array}{c c} M & - Y _ {l} \\ N & X _ {l} \end{array} \right] = I. \tag {5.7}
$$

Of course, implicit in these definitions is the requirement that both M and $\tilde { M }$ be square and nonsingular.

Theorem 5.6 Suppose $P ( s )$ is a proper real rational matrix and

$$
P = \left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right]
$$

is a stabilizable and detectable realization. Let F and L be such that $A + B F$ and $A + L C$ are both stable, and define

$$
\left[ \begin{array}{c c} M & - Y _ {l} \\ N & X _ {l} \end{array} \right] = \left[ \begin{array}{c c c} A + B F & B & - L \\ \hline F & I & 0 \\ C + D F & D & I \end{array} \right] \tag {5.8}

\left[ \begin{array}{c c} X _ {r} & Y _ {r} \\ - \tilde {N} & \tilde {M} \end{array} \right] = \left[ \begin{array}{c c c} A + L C & - (B + L D) & L \\ \hline F & I & 0 \\ C & - D & I \end{array} \right]. \tag {5.9}
$$

Then $P = N M ^ { - 1 } = \tilde { M } ^ { - 1 } \tilde { N }$ are rcf and lcf, respectively, and, furthermore, equation (5.7) is satisfied.

Proof. The theorem follows by verifying equation (5.7).

![](image/ee28fd2b600ab007b28cb210397149afa61bff12ef6d4c0c916d231a1d3688cc.jpg)

Remark 5.2 Note that if P is stable, then we can take $X _ { r } = X _ { l } = I , Y _ { r } = Y _ { l } = 0$ , $N = \tilde { N } = P , M = \tilde { M } = I .$ . ✸

Remark 5.3 The coprime factorization of a transfer matrix can be given a feedbackcontrol interpretation. For example, right coprime factorization comes out naturally from changing the control variable by a state feedback. Consider the state-space equations for a plant P :

$$\dot {x} = A x + B uy = C x + D u.$$

Next, introduce a state feedback and change the variable

$$v := u - F x$$

where F is such that $A + B F$ is stable. Then we get

$$\dot {x} = (A + B F) x + B vu = F x + vy = (C + D F) x + D v.$$
