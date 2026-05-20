# 8.4 STABILITY

We write

$$P (s) F (s) = L (s) = \frac {N (s)}{D (s)}.$$

where $N(s)$ is an $m \times m$ matrix of polynomials and $D(s)$ is a polynomial. It is assumed that, if $D(s_{0}) = 0$ , then $\det[N(s_{0})] \neq 0$ . This is the equivalent of the SISO condition that excludes pole-zero cancellations. Then, from Equation 8.2,

$$
\begin{array}{l} S (s) = \left(I + \frac {N (s)}{D (s)}\right) ^ {- 1} \\ = D (s) [ D (s) I + N (s) ] ^ {- 1} \\ = D (s) \frac {\operatorname{Adj} [ D (s) I + N (s) ]}{\det [ D (s) I + N (s) ]}. \\ \end{array}
$$

The characteristic equation is

$$\det \left(D (s) I + N (s)\right) = 0. \tag {8.17}$$

Using the fact that, for an $n \times n$ matrix $A$ and a scalar $k$ , $\det(kA) = k^n \det A$ , we write Equation 8.17 as

$$[ D (s) ] ^ {n} \det \left(I + \frac {N (s)}{D (s)}\right) = 0. \tag {8.18}$$

If $D(s_{0})=0$ , then $s_{0}$ is not a root of the characteristic equation; from Equation 8.17, that would require $\det N(s_{0})=0$ , which is excluded. Therefore, in Equation 8.18, the factor $[D(s)]^{n}$ must be cancelled out by the determinant, so the roots of the characteristic equation satisfy

$$\det \left(I + \frac {N (s)}{D (s)}\right) = \det [ I + L (s) ] = 0. \tag {8.19}$$

The Routh criterion may be applied to the characteristic equation, Equation 8.19, as in the SISO case. To use the Nyquist criterion in its usual form, we write

$$1 + \{\det [ I + L (s) ] - 1 \} = 0. \tag {8.20}$$

The Nyquist plot is that of $\det[I + L(j\omega)] - 1$ ; N is counted as in the SISO case, and P is the number of RHP poles of $L(s)$ , i.e., the number of RHP roots of $D(s)$ .

Example 8.2 A $2 \times 2$ plant has a matrix transfer function $P(s)$ equal to the loop gain $L(s)$ of Example 8.1. The controller is $F(s) = kI$ . Study the stability for $k = 0.1, 1$ , and 10.

Solution

$$
\begin{array}{l} \det [ I + L (s) ] = \det \left[ \begin{array}{c c} 1 + \frac {k}{s} & - \frac {. 5 k}{s + 1} \\ k & 1 + \frac {k}{s (s + 1)} \end{array} \right] \\ = 1 + \frac {k}{- s} + \frac {k}{s (s + 1)} + \frac {k ^ {2}}{s ^ {2} (s + 1)} + \frac {0 . 5 k ^ {2}}{s + 1} \\ = 1 + \frac {(- . 5 k ^ {2} + k) s ^ {2} + 2 k s + k ^ {2}}{s ^ {2} (s + 1)}. \\ \end{array}
$$

According to Equation 8.17, we should study the Nyquist locus for

$$\det [ I + L (s) ] - 1 = \frac {(- 0 . 5 k ^ {2} + k) s ^ {2} + 2 k s + k ^ {2}}{s ^ {2} (s + 1)}.$$
