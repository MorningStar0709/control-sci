Corollary 16.5 A controller solves the normalized $l e f t$ coprime factor robust stabilization problem if and only if it solves the following $\mathcal { H } _ { \infty }$ control problem:

$$
\left\| \left[ \begin{array}{c} I \\ K \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} I & P \end{array} \right] \right\| _ {\infty} <   \gamma
$$

and

$$
\begin{array}{l} \inf _ {K \text {stabilizing}} \left\| \left[ \begin{array}{l} I \\ K \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{l l} I & P \end{array} \right] \right\| _ {\infty} = \frac {1}{\sqrt {1 - \lambda_ {\max} (Y Q)}} \\ = \left(1 - \left\| \left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] \right\| _ {H} ^ {2}\right) ^ {- 1 / 2}. \\ \end{array}
$$

The solution Q can also be obtained in other ways. Let $X \geq 0$ be the stabilizing solution to

$$X A + A ^ {*} X - X B B ^ {*} X + C ^ {*} C = 0.$$

Then it is easy to verify that

$$Q = (I + X Y) ^ {- 1} X.$$

Hence

$$
\gamma_ {\mathrm{min}} = \frac {1}{\sqrt {1 - \lambda_ {\mathrm{max}} (Y Q)}} = \left(1 - \left\Vert \left[ \begin{array}{l l} \tilde {N} & \tilde {M} \end{array} \right] \right\Vert_ {H} ^ {2}\right) ^ {- 1 / 2} = \sqrt {1 + \lambda_ {\mathrm{max}} (X Y)}.
$$

Similar results can be obtained if one starts with a normalized right coprime factorization. In fact, a rather strong relation between the normalized left and right coprime factorization problems can be established using the following matrix fact.

Lemma 16.6 Let M be a square matrix such that $M ^ { 2 } = M$ . Then $\sigma _ { i } ( M ) = \sigma _ { i } ( I - M )$ for all i such that $0 < \sigma _ { i } ( M ) \neq 1$ .

Proof. We first show that the eigenvalues of M are either 0 or 1 and M is diagonalizable. In fact, assume that λ is an eigenvalue of M and x is a corresponding eigenvector. Then $\lambda x = M x = M M x = M ( M x ) = \lambda M x = \lambda ^ { 2 } x ;$ that is, $\lambda ( 1 - \lambda ) x = 0$ . This implies that either $\lambda = 0 ~ \mathrm { o r } ~ \lambda = 1$ . To show that M is diagonalizable, assume that $M = T J T ^ { - 1 }$ , where J is a Jordan canonical form. It follows immediately that J must be diagonal by the condition $M = M ^ { 2 }$ .

Next, assume that M is diagonalized by a nonsingular matrix T such that

$$
M = T \left[ \begin{array}{c c} I & 0 \\ 0 & 0 \end{array} \right] T ^ {- 1}.
$$

Then

$$
N := I - M = T \left[ \begin{array}{c c} 0 & 0 \\ 0 & I \end{array} \right] T ^ {- 1}.
$$

Define

$$
\left[ \begin{array}{c c} A & B \\ B ^ {*} & D \end{array} \right] := T ^ {*} T
$$
