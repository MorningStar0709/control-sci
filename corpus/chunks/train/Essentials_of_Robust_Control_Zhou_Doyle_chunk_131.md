Evidently, from these equations, the transfer matrix from v to u is

$$
M (s) = \left[ \begin{array}{c c} A + B F & B \\ \hline F & I \end{array} \right]
$$

and that from v to y is

$$
N (s) = \left[ \begin{array}{c c} A + B F & B \\ \hline C + D F & D \end{array} \right]
$$

Therefore,

$$u = M v, y = N v$$

so that $y = N M ^ { - 1 } u ;$ that is, $P = N M ^ { - 1 }$ .

![](image/90f4615d7042fa04bb2b70da8c4d7c944a696106325985e9a66a194aed6b1761.jpg)

We shall now see how coprime factorizations can be used to obtain alternative characterizations of internal stability conditions. Consider again the standard stability analysis diagram in Figure 5.2. We begin with any rcf’s and lcf’s of $P$ and $\hat { K }$ :

$$P = N M ^ {- 1} = \tilde {M} ^ {- 1} \tilde {N} \tag {5.10}\hat {K} = U V ^ {- 1} = \tilde {V} ^ {- 1} \tilde {U}. \tag {5.11}$$

Lemma 5.7 Consider the system in Figure 5.2. The following conditions are equivalent:

1. The feedback system is internally stable.   
$\left[ \begin{array} { l l } { M } & { U } \\ { N } & { V } \end{array} \right]$ is invertible in $\mathcal { R H } _ { \infty }$   
3. $\left[ \begin{array} { c c } { { \tilde { V } } } & { { - \tilde { U } } } \\ { { - \tilde { N } } } & { { \tilde { M } } } \end{array} \right]$ is invertible in $\mathcal { R H } _ { \infty }$ .   
4. $\tilde { M } V - \tilde { N } U$ is invertible in $\mathcal { R } \mathcal { H } _ { \infty }$ .   
5. $\tilde { V } M - \tilde { U } N$ is invertible in $\mathcal { R } \mathcal { H } _ { \infty }$ .

Proof. Note that the system is internally stable if

$$
\left[ \begin{array}{c c} I & - \hat {K} \\ - P & I \end{array} \right] ^ {- 1} \in \mathcal {R H} _ {\infty}
$$

or, equivalently,

$$
\left[ \begin{array}{c c} I & \hat {K} \\ P & I \end{array} \right] ^ {- 1} \in \mathcal {R H} _ {\infty} \tag {5.12}
$$

Now

$$
\left[ \begin{array}{c c} I & \hat {K} \\ P & I \end{array} \right] = \left[ \begin{array}{c c} I & U V ^ {- 1} \\ N M ^ {- 1} & I \end{array} \right] = \left[ \begin{array}{c c} M & U \\ N & V \end{array} \right] \left[ \begin{array}{c c} M ^ {- 1} & 0 \\ 0 & V ^ {- 1} \end{array} \right]
$$

so that

$$
\left[ \begin{array}{c c} I & \hat {K} \\ P & I \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} M & 0 \\ 0 & V \end{array} \right] \left[ \begin{array}{c c} M & U \\ N & V \end{array} \right] ^ {- 1}
$$

Since the matrices

$$
\left[ \begin{array}{c c} M & 0 \\ 0 & V \end{array} \right], \left[ \begin{array}{c c} M & U \\ N & V \end{array} \right]
$$

are right coprime (this fact is left as an exercise for the reader), equation (5.12) holds iff
