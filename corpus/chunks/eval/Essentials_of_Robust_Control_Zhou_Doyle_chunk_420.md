$$
\left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} = \left\| M ^ {- 1} (I + K P) ^ {- 1} \left[ \begin{array}{c c} I & K \end{array} \right] \right\| _ {\infty}.
$$

Proof. This follows from Corollary 16.7 and the fact that

$$
\left\| M ^ {- 1} (I + K P) ^ {- 1} \left[ \begin{array}{c c} I & K \end{array} \right] \right\| _ {\infty} = \left\| \left[ \begin{array}{c} I \\ P \end{array} \right] (I + K P) ^ {- 1} \left[ \begin{array}{c c} I & K \end{array} \right] \right\| _ {\infty}.
$$

![](image/83de8b1d0373cd34a850039e80d5275942d1c10e5dac8cef00f2959a7f9dd36c.jpg)

This corollary says that any $\mathcal { H } _ { \infty }$ controller for the normalized left coprime factorization is also an $\mathcal { H } _ { \infty }$ controller for the normalized right coprime factorization. Hence one can work with either factorization.

For future reference, we shall define

$$
b _ {P, K} := \left\{ \begin{array}{l l} \left(\left\| \left[ \begin{array}{c} I \\ K \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} I & P \end{array} \right] \right\| _ {\infty}\right) ^ {- 1} & \text { if   } K \text {   stabilizes   } P \\ 0 & \text { otherwise } \end{array} \right.
$$

and

$$b _ {\text { opt }} := \sup _ {K} b _ {P, K}.$$

Then $b _ { P , K } = b _ { K , P }$ and

$$
b _ {\mathrm{opt}} = \sqrt {1 - \lambda_ {\max} (Y Q)} = \sqrt {1 - \left\| \left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] \right\| _ {H} ^ {2}}.
$$

The number $b _ { P , K }$ can be related to the classical gain and phase margins as shown in Vinnicombe [1993b].

Theorem 16.9 Let P be a SISO plant and K be a stabilizing controller. Then

$$\mathrm{gainmargin} \geq \frac {1 + b _ {P , K}}{1 - b _ {P , K}}$$

and

$$\text { phase margin } \geq 2 \arcsin (b _ {P, K}).$$

Proof. Note that for SISO system

$$b _ {P, K} \leq \frac {| 1 + P (j \omega) K (j \omega) |}{\sqrt {1 + | P (j \omega) | ^ {2}} \sqrt {1 + | K (j \omega) | ^ {2}}}, \quad \forall \omega .$$

So, at frequencies where $k : = - P ( j \omega ) K ( j \omega ) \in \mathbb { R } ^ { + }$ ,

$$b _ {P, K} \leq \frac {| 1 - k |}{\sqrt {(1 + | P | ^ {2}) (1 + \frac {k ^ {2}}{| P | ^ {2}})}} \leq \frac {| 1 - k |}{\sqrt {\underset {P} {\min} \left\{(1 + | P | ^ {2}) (1 + \frac {k ^ {2}}{| P | ^ {2}}) \right\}}} = \left| \frac {1 - k}{1 + k} \right|,$$

which implies that

$$k \leq \frac {1 - b _ {P , K}}{1 + b _ {P , K}}, \quad \text { or } \quad k \geq \frac {1 + b _ {P , K}}{1 - b _ {P , K}}$$

from which the gain margin result follows. Similarly, at frequencies where $P ( j \omega ) K ( j \omega ) =$ $- e ^ { j \theta }$ ,

$$b _ {P, K} \leq \frac {| 1 - e ^ {j \theta} |}{\sqrt {(1 + | P | ^ {2}) (1 + \frac {1}{| P | ^ {2}})}} \leq \frac {| 2 \sin \frac {\theta}{2} |}{\sqrt {\underset {P} {\min} \left\{(1 + | P | ^ {2}) (1 + \frac {1}{| P | ^ {2}}) \right\}}} = \frac {| 2 \sin \frac {\theta}{2} |}{2},$$

which implies $\theta \geq 2$ arcsin $b _ { P , K }$

For example, $b _ { P , K } = 1 / 2$ guarantees a gain margin of 3 and a phase margin of $6 0 ^ { \mathrm { o } }$ .
