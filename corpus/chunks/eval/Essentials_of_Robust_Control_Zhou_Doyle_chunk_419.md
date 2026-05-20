and assume $0 < \lambda \neq 1$ . Then $A > 0$ and

$$
\det (M ^ {*} M - \lambda I) = 0
\Leftrightarrow \quad \det (\left[ \begin{array}{c c} I & 0 \\ 0 & 0 \end{array} \right] T ^ {*} T \left[ \begin{array}{c c} I & 0 \\ 0 & 0 \end{array} \right] - \lambda T ^ {*} T) = 0

\Leftrightarrow \det {\left[ \begin{array}{c c} (1 - \lambda) A & - \lambda B \\ - \lambda B ^ {*} & - \lambda D \end{array} \right]} = 0
\Leftrightarrow \quad \det (- \lambda D - \frac {\lambda^ {2}}{1 - \lambda} B ^ {*} A ^ {- 1} B) = 0\Leftrightarrow \quad \det (\frac {1 - \lambda}{\lambda} D + B ^ {*} A ^ {- 1} B) = 0
\begin{array}{l} \Leftrightarrow \quad \det \left[ \begin{array}{c c} - \lambda A & - \lambda B \\ - \lambda B ^ {*} & (1 - \lambda) D \end{array} \right] = 0 \\ \Leftrightarrow \quad \det (N ^ {*} N - \lambda I) = 0. \\ \end{array}
$$

This implies that all nonzero eigenvalues of $M ^ { * } M$ and $N ^ { * } N$ that are not equal to 1 are equal; that is, $\sigma _ { i } ( M ) = \sigma _ { i } ( I - M )$ for all i such that $0 < \sigma _ { i } ( M ) \neq 1$ . ✷

Using this matrix fact, we have the following corollary.

Corollary 16.7 Let K and P be any compatibly dimensioned complex matrices. Then

$$
\left\| \left[ \begin{array}{c} I \\ K \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} I & P \end{array} \right] \right\| = \left\| \left[ \begin{array}{c} I \\ P \end{array} \right] (I + K P) ^ {- 1} \left[ \begin{array}{c c} I & K \end{array} \right] \right\|.
$$

Proof. Define

$$
M = \left[ \begin{array}{c} I \\ K \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} I & P \end{array} \right], N = \left[ \begin{array}{c} - P \\ I \end{array} \right] (I + K P) ^ {- 1} \left[ \begin{array}{c c} - K & I \end{array} \right].
$$

Then it is easy to verify that $M ^ { 2 } = M$ and $N = I - M$ . By Lemma 16.6, we have $\| M \| = \| N \|$ . The corollary follows by noting that

$$
\left[ \begin{array}{c} I \\ P \end{array} \right] (I + K P) ^ {- 1} \left[ \begin{array}{c c} I & K \end{array} \right] = \left[ \begin{array}{c c} 0 & I \\ - I & 0 \end{array} \right] N \left[ \begin{array}{c c} 0 & - I \\ I & 0 \end{array} \right].
$$

![](image/afc69c9977b20b08df39051c3362e0af5dc9842a644dd32048a7ce5e272f8102.jpg)

Corollary 16.8 Let $P = \tilde { M } ^ { - 1 } \tilde { N } = N M ^ { - 1 }$ be, respectively, the normalized left and right coprime factorizations. Then
