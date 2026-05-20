$$\gg \delta_ {\mathbf {g}} (\mathbf {P} _ {1}, \mathbf {P} _ {2}) = \operatorname{gap} (\mathbf {P} _ {1}, \mathbf {P} _ {2}, \text { tol })$$

Next, note that $b _ { \mathrm { o b t } } ( P _ { 1 } ) = 1 / \sqrt { 2 }$ and the optimal controller achieving $b _ { \mathrm { o b t } } ( P _ { 1 } )$ is $K _ { \mathrm { o b t } } =$ 0. There must be a plant $P$ with $\delta _ { \nu } ( P _ { 1 } , P ) = b _ { \mathrm { o b t } } ( P _ { 1 } ) = 1 / \sqrt { 2 }$ that can not be stabilized by $K _ { \mathrm { o b t } } = 0 ;$ ; that is, there must be an unstable plant $P$ such that $\delta _ { \nu } ( P _ { 1 } , P ) = b _ { \mathrm { o b t } } ( P _ { 1 } ) =$ $1 / { \sqrt { 2 } }$ . A such $P$ can be found using Corollary 17.2:

$$
\{P: \delta_ {g} (P _ {1}, P) \leq b _ {\mathrm{obt}} (P _ {1}) \}
= \left\{P: P = \frac {N _ {1} + \Delta_ {N}}{M _ {1} + \Delta_ {M}}, \Delta_ {N}, \Delta_ {M} \in \mathcal {H} _ {\infty}, \left\| \left[ \begin{array}{c} \Delta_ {N} \\ \Delta_ {M} \end{array} \right] \right\| _ {\infty} \leq b _ {\mathrm{obt}} (P _ {1}) \right\}.
$$

that is, there must be $\Delta _ { N } , \ \Delta _ { M } \in \mathcal { H } _ { \infty } , \ \left\| \left[ \begin{array} { l } { \Delta _ { N } } \\ { \Delta _ { M } } \end{array} \right] \right\| _ { \infty } = b _ { \mathrm { o b t } } ( P _ { 1 } )$ such that

$$P = \frac {N _ {1} + \Delta_ {N}}{M _ {1} + \Delta_ {M}}$$

is unstable. Let

$$\Delta_ {N} = 0, \quad \Delta_ {M} = \frac {1}{\sqrt {2}} \frac {s - 1}{s + 1}.$$

Then

$$P = \frac {N _ {1} + \Delta_ {N}}{M _ {1} + \Delta_ {M}} = \frac {s - 1}{2 s}, \quad \delta_ {\nu} (P _ {1}, P) = b _ {\mathrm{obt}} (P _ {1}) = 1 / \sqrt {2}.$$

Example 17.2 We shall now consider the following question: Given an uncertain plant

$$P (s) = \frac {k}{s - 1}, \quad k \in [ k _ {1}, k _ {2} ],$$

(a) Find the best nominal design model $P _ { 0 } = \frac { k _ { 0 } } { s - 1 }$ in the sense

$$\inf _ {k _ {0} \in [ k _ {1}, k _ {2} ]} \sup _ {k \in [ k _ {1}, k _ {2} ]} \delta_ {g} (P, P _ {0}).$$

(b) Let $k _ { 1 }$ be fixed and $k _ { 2 }$ be variable. Find the $k _ { 0 }$ so that the largest family of the plant $P$ can be guaranteed to be stabilized a priori by any controller satisfying $b _ { P _ { 0 } , K } = b _ { \mathrm { o b t } } ( P _ { 0 } )$ .

For simplicity, suppose $k _ { 1 } \geq 1$ . It can be shown that $\begin{array} { r } { \delta _ { g } ( P , P _ { 0 } ) = \frac { | k _ { 0 } - k | } { k _ { 0 } + k } } \end{array}$ . Then the optimal $k _ { 0 }$ for question (a) satisfies

$$\frac {k _ {0} - k _ {1}}{k _ {0} + k _ {1}} = \frac {k _ {2} - k _ {0}}{k _ {2} + k _ {0}};$$

that is, $k _ { 0 } = \sqrt { k _ { 1 } k _ { 2 } }$ and
