in which ${ \hat { x } } ( T - N )$ is the optimal estimate for the unconstrained full information problem. Next we consider using ${ \hat { x } } ( T - N | T - 2 )$ in place of $\hat { x } ( T - N ) : = \hat { x } ( T - N | T - 1 )$ . We might guess that the proper weight for this prior estimate would be the smoothed covariance $P ( T - N | T - 2 )$ instead of $P ^ { - } ( T - N ) : = P ( T - N | T - 1 )$ , and that guess is correct, but not complete. Notice that the smoothed prior $\hat { x } ( T - N | T - 2 )$ is influenced by the measurements ${ \bf y } _ { 0 : T - 2 }$ . But the sum of stage costs in the MHE problem at time $T$ depends on measurements $\mathbf { y } _ { T } .$ −N:T−1, so we have to adjust the prior weighting so we do not double count the data $\mathbf { y } _ { T - N : T - 2 }$ . The correct prior weighting for the smoothing update has been derived by Rao, Rawlings, and Lee (2001), which we summarize next. The following notation is useful; for any square matrix R and integer $k \geq 1$ , define $\mathrm { d i a g } _ { k } ( R )$ to be the following

![](image/35d1f6468eadcbd2d46945d17d62163c32328febbd095aaf5c11d263392e93c2.jpg)

<details>
<summary>line</summary>

| k | y(k) |
| --- | --- |
| T - 2N | ~0.5 |
| T - N | ~1.0 |
| T | >1.0 |
</details>

Figure 4.3: Smoothing update.

$$
\operatorname{diag} _ {k} (R) := \underbrace {\left[ \begin{array}{c c c c} R & & & \\ & R & & \\ & & \ddots & \\ & & & R \end{array} \right]} _ {k \text {times}} \qquad \mathcal {O} _ {k} = \left[ \begin{array}{c c c c c} 0 & & & & \\ & C & & \\ & C A & C & & \\ & \vdots & \vdots & \ddots & \\ & C A ^ {k - 2} & C A ^ {k - 3} & \cdots & C \end{array} \right]
W _ {k} = \mathrm{diag} _ {k} (R) + \mathcal {O} _ {k} (\mathrm{diag} _ {k} (Q)) \mathcal {O} _ {k} ^ {\prime}
$$

We require the smoothed covariance $P ( T - N | T - 2 )$ , which we can obtain from the following recursion (Rauch, Tung, and Striebel, 1965;

Bryson and Ho, 1975)

$$P (k \mid T) = P (k) +P (k) A ^ {\prime} \left(P ^ {-} (k + 1)\right) ^ {- 1} \left(P (k + 1 | T) - P ^ {-} (k + 1)\right) \left(P ^ {-} (k + 1)\right) ^ {- 1} A P (k)$$

We iterate this equation backwards N−1 times starting from the known value $P ( T - 1 | T - 2 ) : = P ^ { - } ( T - 1 )$ to obtain $P ( T - N | T - 2 )$ . The smoothing arrival cost is then given by

$$
\begin{array}{l} \tilde {Z} _ {T - N} (z) = \hat {V} _ {T - 1} ^ {0} + (1 / 2) | z - \hat {x} (T - N | T - 2) | _ {(P (T - N | T - 2)) ^ {- 1}} ^ {2} \\ - (1 / 2) \left| \mathbf {y} _ {T - N: T - 2} - \mathcal {O} _ {N - 1} z \right| _ {(W _ {N - 1}) ^ {- 1}} ^ {2} \quad T > N \\ \end{array}
$$
