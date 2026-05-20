$$
\frac {1}{b _ {P , K} (\omega)} := \overline {{\sigma}} \left(\left[ \begin{array}{c} I \\ K (j \omega) \end{array} \right] (I + P (j \omega) K (j \omega)) ^ {- 1} \left[ \begin{array}{c c} I & P (j \omega) \end{array} \right]\right)
$$

and

$$\psi (P _ {1} (j \omega), P _ {2} (j \omega)) = \overline {{\sigma}} \left(\Psi (P _ {1} (j \omega), P _ {2} (j \omega))\right).$$

The following theorem states that robust stability can be checked using the frequencyby-frequency test.

Theorem 17.8 Suppose $( P _ { 0 } , K )$ is stable and $\delta _ { \nu } ( P _ { 0 } , P _ { 1 } ) < 1$ . Then $( P _ { 1 } , K )$ is stable if

$$b _ {P _ {0}, K} (\omega) > \psi (P _ {0} (j \omega), P _ {1} (j \omega)), \quad \forall \omega .$$

Moreover,

$$\arcsin b _ {P _ {1}, K} (\omega) \geq \arcsin b _ {P _ {0}, K} (\omega) - \arcsin \psi (P _ {0} (j \omega), P _ {1} (j \omega)), \quad \forall \omega$$

and

$$\arcsin b _ {P _ {1}, K} \geq \arcsin b _ {P _ {0}, K} - \arcsin \delta_ {\nu} (P _ {0}, P _ {1}).$$

Proof. Let $P _ { 1 } = \tilde { M } _ { 1 } ^ { - 1 } \tilde { N } _ { 1 } , P _ { 0 } = N _ { 0 } M _ { 0 } ^ { - 1 } = \tilde { M } _ { 0 } ^ { - 1 } \tilde { N } _ { 0 }$ and $K = U V ^ { - 1 }$ be normalized coprime factorizations, respectively. Then

$$
\frac {1}{b _ {P _ {1} , K} (\omega)} = \overline {{\sigma}} \left(\left[ \begin{array}{l} V \\ U \end{array} \right] (\tilde {M} _ {1} V + \tilde {N} _ {1} U) ^ {- 1} \left[ \begin{array}{l l} \tilde {M} _ {1} & \tilde {N} _ {1} \end{array} \right]\right) = \overline {{\sigma}} \left((\tilde {M} _ {1} V + \tilde {N} _ {1} U) ^ {- 1}\right).
$$

That is,

$$
b _ {P _ {1}, K} (\omega) = \underline {{\sigma}} (\tilde {M} _ {1} V + \tilde {N} _ {1} U) = \underline {{\sigma}} \left(\left[ \begin{array}{c c} \tilde {M} _ {1} & \tilde {N} _ {1} \end{array} \right] \left[ \begin{array}{c} V \\ U \end{array} \right]\right).
$$

Similarly,

$$
b _ {P _ {0}, K} (\omega) = \underline {{\sigma}} (\tilde {M} _ {0} V + \tilde {N} _ {0} U) = \underline {{\sigma}} \left(\left[ \begin{array}{c c} \tilde {M} _ {0} & \tilde {N} _ {0} \end{array} \right] \left[ \begin{array}{c} V \\ U \end{array} \right]\right).
$$

Note that

$$
\psi (P _ {0} (j \omega), P _ {1} (j \omega)) = \overline {{\sigma}} \left(\left[ \begin{array}{c c} \tilde {M} _ {1} & \tilde {N} _ {1} \end{array} \right] \left[ \begin{array}{c} N _ {0} \\ - M _ {0} \end{array} \right]\right)
