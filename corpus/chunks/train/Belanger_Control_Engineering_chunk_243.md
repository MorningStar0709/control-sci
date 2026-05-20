Since unstable roots of $N_L + D_L$ cannot be cancelled out by the numerator $D_L$ , it follows that $S(s)$ will be stable if, and only if, the polynomial $D_L(s) + N_L(s)$ has all its roots in the open LHP. Note that this polynomial is the characteristic polynomial of the closed-loop system.

Next, consider $PS$ . Because $S$ is stable, the denominator factor $N_L(s) + D_L(s)$ has only LHP roots. For stability of $PS$ , it follows that the unstable roots of $D_P$ , if any, must be cancelled out by the numerator; i.e., the unstable roots of $D_P$ must be roots of either $N_P$ or $D_L$ . Since $N_P$ and $D_P$ are coprime, they have no common roots. Therefore, the unstable roots of $D_P$ must also be roots of $D_L$ . As Equation 5.2 shows, the roots of $D_P$ will be roots of $D_L$ unless they are cancelled by $N_F$ . It follows that, if $S(s)$ is stable, a necessary and sufficient condition for stability of $PS$ is that $N_F(s)$ and $D_P(s)$ have no common root in the closed RHP.

The same reasoning applied to $P^{-1}T$ leads to the conclusion that, given $S(s)$ stable, the transfer function $P^{-1}(s)T(s)$ is stable if, and only if, $N_{P}(s)$ and $D_{F}(s)$ have no common roots in the closed RHP.

To summarize, the following conditions are necessary and sufficient for internal stability, given minimality of the realizations for $F$ and $P$ :

1. There are no cancellations by $F(s)$ of closed RHP poles or zeros of $P(s)$ .

2. The polynomial $D_L(s) + N_L(s)$ has all its roots in the open LHP.

The special case $F(s) = k$ , called pure-gain control, will be used presently as a vehicle for the study of stability. It satisfies the first condition automatically, of course, since it has neither poles nor zeros. Stability is established by checking the second condition.
