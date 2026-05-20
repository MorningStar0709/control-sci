# 5.3 Internal Stability

Consider a system described by the standard block diagram in Figure 5.2 and assume that the system is well-posed.

Definition 5.2 The system of Figure 5.2 is said to be internally stable if the transfer matrix

$$
\left[ \begin{array}{c c} I & - \hat {K} \\ - P & I \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} (I - \hat {K} P) ^ {- 1} & \hat {K} (I - P \hat {K}) ^ {- 1} \\ P (I - \hat {K} P) ^ {- 1} & (I - P \hat {K}) ^ {- 1} \end{array} \right] \tag {5.4}

= \left[ \begin{array}{c c} I + \hat {K} (I - P \hat {K}) ^ {- 1} P & \hat {K} (I - P \hat {K}) ^ {- 1} \\ (I - P \hat {K}) ^ {- 1} P & (I - P \hat {K}) ^ {- 1} \end{array} \right]
$$

from $( w _ { 1 } , w _ { 2 } )$ to $( e _ { 1 } , e _ { 2 } )$ belongs to $\mathcal { R H } _ { \infty }$ .

Note that to check internal stability, it is necessary (and sufficient) to test whether each of the four transfer matrices in equation (5.4) is in $\mathcal { H } _ { \infty }$ . Stability cannot be concluded even if three of the four transfer matrices in equation (5.4) are in $\mathcal { H } _ { \infty }$ . For example, let an interconnected system transfer function be given by

$$P = \frac {s - 1}{s + 1}, \qquad \hat {K} = - \frac {1}{s - 1}.$$

Then it is easy to compute

$$
\left[ \begin{array}{c} e _ {1} \\ e _ {2} \end{array} \right] = \left[ \begin{array}{c c} \frac {s + 1}{s + 2} & - \frac {s + 1}{(s - 1) (s + 2)} \\ \frac {s - 1}{s + 2} & \frac {s + 1}{s + 2} \end{array} \right] \left[ \begin{array}{c} w _ {1} \\ w _ {2} \end{array} \right],
$$

which shows that the system is not internally stable although three of the four transfer functions are stable.

Remark 5.1 Internal stability is a basic requirement for a practical feedback system. This is because all interconnected systems may be unavoidably subject to some nonzero initial conditions and some (possibly small) errors, and it cannot be tolerated in practice that such errors at some locations will lead to unbounded signals at some other locations in the closed-loop system. Internal stability guarantees that all signals in a system are bounded provided that the injected signals (at any locations) are bounded. ✸

However, there are some special cases under which determining system stability is simple.

Corollary 5.2 Suppose $\hat { K } \in \mathcal { R } \mathcal { H } _ { \infty }$ . Then the system in Figure 5.2 is internally stable if and only if it is well-posed and $P ( I - \hat { K } P ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ .
