# 17.4 Extended Loop-Shaping Design

Let P be a family of parametric uncertainty systems and let $P _ { 0 } \in \mathcal { P }$ be a nominal design model. We are interested in finding a controller so that we have the largest possible robust stability margin; that is,

$$\sup _ {K} \inf _ {P \in \mathcal {P}} b _ {P, K}.$$

Note that by Theorem 17.8, for any $P _ { 1 } \in \mathcal { P }$ , we have

$$\arcsin b _ {P _ {1}, K} (\omega) \geq \arcsin b _ {P _ {0}, K} (\omega) - \arcsin \psi (P _ {0} (j \omega), P _ {1} (j \omega)), \quad \forall \omega .$$

Now suppose we need in $\mathrm { i f } _ { P \in \mathcal { P } } b _ { P , K } > \alpha$ . Then it is sufficient to have

$$\arcsin b _ {P _ {0}, K} (\omega) - \arcsin \psi (P _ {0} (j \omega), P _ {1} (j \omega)) > \arcsin \alpha , \forall \omega , P _ {1} \in \mathcal {P};$$

that is,

$$b _ {P _ {0}, K} (\omega) > \sin \left(\arcsin \psi (P _ {0} (j \omega), P _ {1} (j \omega)) + \arcsin \alpha\right), \quad \forall \omega , \quad P _ {1} \in \mathcal {P}.$$

Let $W ( s ) \in \mathcal { H } _ { \infty }$ be such that

$$| W (j \omega) | \geq \sin (\arcsin \psi (P _ {0} (j \omega), P _ {1} (j \omega)) + \arcsin \alpha), \quad \forall \omega , \quad P _ {1} \in \mathcal {P}.$$

Then it is sufficient to guarantee

$$\frac {| W (j \omega) |}{b _ {P _ {0} , K} (\omega)} < 1.$$

Let $P _ { 0 } = \tilde { M } _ { 0 } ^ { - 1 } \tilde { N } _ { 0 }$ be a normalized left coprime factorization and note that

$$
\frac {1}{b _ {P _ {0} , K} (\omega)} := \overline {{\sigma}} \left(\left[ \begin{array}{c} I \\ K (j \omega) \end{array} \right] (I + P _ {0} (j \omega) K (j \omega)) ^ {- 1} \tilde {M} _ {0} ^ {- 1} (j \omega)\right).
$$

Then it is sufficient to find a controller so that

$$
\left\| \left[ \begin{array}{c} I \\ K \end{array} \right] (I + P _ {0} K) ^ {- 1} \tilde {M} _ {0} ^ {- 1} W \right\| _ {\infty} <   1.
$$

The process can be iterated to find the largest possible α.

Combining the preceding robust stabilization idea and the $\mathcal { H } _ { \infty }$ loop-shaping in Chapter 16, one can devise an extended loop-shaping design procedure as follows. (A more advanced loop-shaping procedure can be found in Vinnicombe [1993b].)
