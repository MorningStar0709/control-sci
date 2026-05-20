# 5.2 STABILITY CONDITIONS CONCERNING POLE-ZERO CANCELLATIONS

The first conditions are necessary conditions that forbid certain pole-zero cancellations between $F$ and $P$ . Let $F(s)$ and $P(s)$ be written as ratios of polynomials, i.e., as

$$F (s) = \frac {N _ {F} (s)}{D _ {F} (s)}P (s) = \frac {N _ {P} (s)}{D _ {P} (s)}. \tag {5.1}$$

It is assumed that the pairs $(N_{F}, D_{F})$ and $(N_{P}, D_{P})$ are coprime, i.e., have no common factors. This is assured, in particular, if $F(s)$ and $P(s)$ are transfer functions of minimal realizations.

The loop gain is

$$L (s) = F (s) P (s) = \frac {N _ {L} (s)}{D _ {L} (s)} = \frac {N _ {F} (s)}{D _ {F} (s)} \frac {N _ {P} (s)}{D _ {P} (s)}. \tag {5.2}$$

In the writing of Equation 5.2, it is assumed that common factors between $N_F$ and $D_P$ (or $N_P$ and $D_F$ ) are cancelled, so that $N_L$ and $D_L$ are coprime. Thus, it is not true, in general, that $N_L = N_F N_P$ and $D_L = D_F D_P$ ; that holds only in the absence of cancellations.

For example, if $F$ and $P$ are given by

$$F (s) = \frac {- s - 1}{(s + 2) (s + 3)} \quad P (s) = \frac {(s + 3)}{(s + 1) (s - 1)}$$

then

$$L (s) = F (s) P (s) = \frac {1}{(s + 1) (s + 2)}.$$

Note that $N_{L}(s) = 1$ and $D_{L}(s) = (s + 1)(s + 2)$ are indeed coprime, and that $N_{L} \neq N_{F}N_{P}$ and $D_{L} \neq D_{F}D_{P}$ .

By Theorem 4.4 (Chapter 4), the necessary and sufficient conditions for internal stability, given minimal realizations of $F$ and $P$ , are that the transfer functions $S$ , $PS$ , and $P^{-1}T$ be stable. We write these as ratios of polynomials.

$$S (s) = \frac {1}{1 + L} = \frac {D _ {L}}{N _ {L} + D _ {L}} \tag {5.3}P (s) S (s) = \frac {N _ {P}}{D _ {P}} \frac {D _ {L}}{N _ {L} + D _ {L}} \tag {5.4}$$

and

$$T (s) = \frac {L}{1 + L} = \frac {N _ {L}}{N _ {L} + D _ {L}} \tag {S}P ^ {- 1} (s) T (s) = \frac {D _ {P}}{N _ {P}} \frac {N _ {L}}{N _ {L} + D _ {L}}. \tag {5.6}$$

There can be no pole-zero cancellation between $D_L$ and $N_L + D_L$ . To show this assume that there is, i.e., that $s_0$ is a root of both $D_L$ and $D_L + N_L$ . Then,

$$D _ {L} (s _ {0}) = 0$$

and

$$0 = N _ {L} (s _ {0}) + D _ {L} (s _ {0}) = N _ {L} (s _ {0}).$$

which implies that $N_{L}(s_{0}) = 0$ . Now, because $D_{L}$ and $N_{L}$ are coprime, they may not have a common root $s_{0}$ ; therefore, the existence of a pole-zero cancellation violates the assumption of coprimeness.
