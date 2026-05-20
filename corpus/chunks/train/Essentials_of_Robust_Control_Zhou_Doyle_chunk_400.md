It is easy to see that $\tilde { R } _ { 1 2 }$ and $\tilde { R } _ { 2 1 }$ are both minimum phase and invertible and hence have full column and full row rank, respectively, for all $\omega \in \mathbb { R } \cup \infty$ . Consequently, by invoking Lemma 15.1, we conclude that if $\tilde { R }$ is a contraction and $\| \Delta \| _ { \infty } < 1$ , then $\left\| \mathcal { F } _ { \ell } ( \tilde { R } , \Delta ) \right\| _ { \infty } < 1$ . This guarantees the existence of a $Q$ such that $\| Q \| _ { \infty } < \gamma \ \mathrm { o r }$ , equivalently, the existence of a $\hat { K }$ such that $\left\| \mathcal { F } _ { \ell } ( G , \hat { K } ) \right\| _ { \infty } < \gamma$ . This observation leads to the following theorem.

Theorem 15.2 Suppose $W _ { 1 }$ and $W _ { 2 }$ are stable, minimum phase and invertible transfer matrices such that $\tilde { R }$ is a contraction. Let $K _ { 0 }$ be a stabilizing controller such that $\| \mathcal { F } _ { \ell } ( G , K _ { 0 } ) \| _ { \infty } < \gamma$ . Then $\hat { K }$ is also a stabilizing controller such that $\left\| \mathcal { F } _ { \ell } ( G , \hat { K } ) \right\| _ { \infty } < \gamma$ $i f$

$$\| \Delta \| _ {\infty} = \left\| W _ {2} ^ {- 1} (\hat {K} - K _ {0}) W _ {1} ^ {- 1} \right\| _ {\infty} < 1.$$

Since $\tilde { R }$ can always be made contractive for sufficiently small $W _ { 1 }$ and $W _ { 2 }$ , there are infinite many $W _ { 1 }$ and $W _ { 2 }$ that satisfy the conditions in the theorem. It is obvious that to make $\left. \bar { W } _ { 2 } ^ { - 1 } ( \hat { K } - K _ { 0 } ) W _ { 1 } ^ { - 1 } \right. _ { \infty } < 1$ for some $\hat { K }$ , one would like to select the “largest” ∞ $W _ { 1 }$ and $W _ { 2 }$ such that $\tilde { R }$ is a contraction.

Lemma 15.3 Assume that $\| R _ { 2 2 } \| _ { \infty } < \gamma$ and define

$$
L = \left[ \begin{array}{c c} L _ {1} & L _ {2} \\ L _ {2} ^ {\sim} & L _ {3} \end{array} \right] = \mathcal {F} _ {\ell} (\left[ \begin{array}{c c c c} 0 & - R _ {1 1} & 0 & R _ {1 2} \\ - R _ {1 1} ^ {\sim} & 0 & R _ {2 1} ^ {\sim} & 0 \\ \hdashline 0 & R _ {2 1} & 0 & - R _ {2 2} \\ R _ {1 2} ^ {\sim} & 0 & - R _ {2 2} ^ {\sim} & 0 \end{array} \right], \gamma^ {- 1} I).
$$

Then $\tilde { R }$ is a contraction if $W _ { 1 }$ and $W _ { 2 }$ satisfy

$$
\left[ \begin{array}{c c} (W _ {1} ^ {\sim} W _ {1}) ^ {- 1} & 0 \\ 0 & (W _ {2} W _ {2} ^ {\sim}) ^ {- 1} \end{array} \right] \geq \left[ \begin{array}{c c} L _ {1} & L _ {2} \\ L _ {2} ^ {\sim} & L _ {3} \end{array} \right].
$$

Proof. See Goddard and Glover [1993].
