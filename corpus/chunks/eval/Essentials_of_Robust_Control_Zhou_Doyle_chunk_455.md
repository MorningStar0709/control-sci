$$
\begin{array}{l} b _ {\mathrm{obt}} (P) := \left\{\inf _ {K \text {   stabilizing }} \left\| \left[ \begin{array}{c} I \\ K \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} I & P \end{array} \right] \right\| _ {\infty} \right\} ^ {- 1} \\ = \sqrt {1 - \lambda_ {\max} (Y Q)} = \sqrt {1 - \left\| \left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] \right\| _ {H} ^ {2}} \\ \end{array}
$$

and

$$
b _ {P, K} := \left\| \left[ \begin{array}{c} I \\ K \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} I & P \end{array} \right] \right\| _ {\infty} ^ {- 1} = \left\| \left[ \begin{array}{c} I \\ P \end{array} \right] (I + K P) ^ {- 1} \left[ \begin{array}{c c} I & K \end{array} \right] \right\| _ {\infty} ^ {- 1}.
$$

The following results were shown by Qiu and Davison [1992a].

Theorem 17.3 Suppose the feedback system with the pair $( P _ { 0 } , K _ { 0 } )$ is stable. Let $\mathcal { P } : =$ $\{ P : \ \delta _ { g } ( P , P _ { 0 } ) < r _ { 1 } \}$ and $\mathcal { K } : = \{ K : ~ \delta _ { g } ( K , K _ { 0 } ) < r _ { 2 } \}$ . Then

(a) The feedback system with the pair $( P , K )$ is also stable for all $P \in \mathcal { P }$ and $K \in \mathcal { K }$ if and only if

$$\arcsin b _ {P _ {0}, K _ {0}} \geq \arcsin r _ {1} + \arcsin r _ {2}.$$

(b) The worst possible performance resulting from these sets of plants and controllers is given by

$$\inf _ {P \in \mathcal {P}, K \in \mathcal {K}} \arcsin b _ {P, K} = \arcsin b _ {P _ {0}, K _ {0}} - \arcsin r _ {1} - \arcsin r _ {2}.$$

The sufficiency part of the theorem follows from Theorem 17.8 in the next section. Note that the theorem is still true if one of the uncertainty balls is taken as closed ball. In particular, one can take either $r _ { 1 } = 0$ or $r _ { 2 } = 0$ .

Example 17.1 Consider

$$P _ {1} = \frac {s - 1}{s + 1}, P _ {2} = \frac {2 s - 1}{s + 1}.$$

Then $P _ { 1 } = N _ { 1 } / M _ { 1 }$ and $P _ { 2 } = N _ { 2 } / M _ { 2 }$ with

$$N _ {1} = \frac {1}{\sqrt {2}} \frac {s - 1}{s + 1}, \quad M _ {1} = \frac {1}{\sqrt {2}}, \quad N _ {2} = \frac {2 s - 1}{\sqrt {5} s + \sqrt {2}}, \quad M _ {2} = \frac {s + 1}{\sqrt {5} s + \sqrt {2}}$$

are normalized coprime factorizations. It is easy to show that

$$\delta_ {g} (P _ {1}, P _ {2}) = 1 / 3 > \| \Psi (P _ {1}, P _ {2}) \| _ {\infty} = \sup _ {\omega} \frac {| \omega |}{\sqrt {1 0 \omega^ {2} + 4}} = \frac {1}{\sqrt {1 0}},$$

which implies that any controller $K$ that stabilizes $P _ { 1 }$ and achieves only $b _ { P _ { 1 } , K } > 1 / 3$ will actually stabilize $P _ { 2 }$ by Theorem 17.3. The following Matlab command can be used to compute the gap:
