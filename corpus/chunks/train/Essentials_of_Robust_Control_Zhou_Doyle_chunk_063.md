# Proof.

(i) By definition

$$
\begin{array}{l} \underline {{\sigma}} (A + \Delta) := \min _ {\| x \| = 1} \| (A + \Delta) x \| \geq \min _ {\| x \| = 1} \left\{\| A x \| - \| \Delta x \| \right\} \\ \geq \min _ {\| x \| = 1} \| A x \| - \max _ {\| x \| = 1} \| \Delta x \| \\ = \underline {{\sigma}} (A) - \overline {{\sigma}} (\Delta). \\ \end{array}
$$

Hence $- { \overline { { \sigma } } } ( \Delta ) \leq { \underline { { \sigma } } } ( A + \Delta ) - { \underline { { \sigma } } } ( A )$ . The other inequality $\underline { { \sigma } } ( A + \Delta ) - \underline { { \sigma } } ( A ) \leq \overline { { \sigma } } ( \Delta )$ follows by replacing A by $A + \Delta$ and $\Delta$ by $- \Delta$ in the preceding proof.

(ii) This follows by noting that

$$
\begin{array}{l} \underline {{\sigma}} (A \Delta) := \min _ {\| x \| = 1} \| A \Delta x \| \\ = \sqrt {\min _ {\| x \| = 1} x ^ {*} \Delta^ {*} A ^ {*} A \Delta x} \\ \geq \underline {{\sigma}} (A) \min _ {\| x \| = 1} \| \Delta x \| = \underline {{\sigma}} (A) \underline {{\sigma}} (\Delta). \\ \end{array}
$$

(iii) Let the singular value decomposition of A be $A = U \Sigma V ^ { * }$ ; then $A ^ { - 1 } = V \Sigma ^ { - 1 } U ^ { * }$ . Hence $\overline { { \sigma } } ( A ^ { \widetilde { - 1 } } ) = \overline { { \sigma } } ( \Sigma ^ { - 1 } ) = 1 / \underline { { \sigma } } ( \Sigma ) = 1 / \underline { { \sigma } } ( A )$ .

✷

Note that (ii) may not be true if A and $\Delta$ are not square matrices. For example, consider $A = { \left[ \begin{array} { l } { 1 } \\ { 2 } \end{array} \right] }$ and $\Delta = { \left[ \begin{array} { l l } { 3 } & { 4 } \end{array} \right] }$ ; then $\underline { { \sigma } } ( A \Delta ) = 0$ but $\underline { { \sigma } } ( A ) = \sqrt { 5 }$ and $\underline { { \sigma } } ( \Delta ) = 5$ .

Some useful properties of SVD are collected in the following lemma.

Lemma 2.6 Let $A \in \mathbb { F } ^ { m \times n }$ and

$$\sigma_ {1} \geq \sigma_ {2} \geq \dots \geq \sigma_ {r} > \sigma_ {r + 1} = \dots = 0, r \leq \min \{m, n \}.$$

Then

1. $\operatorname { r a n k } ( A ) = r ;$   
2. $\operatorname { K e r } A = \operatorname { s p a n } \{ v _ { r + 1 } , . . . , v _ { n } \}$ and $( \operatorname { K e r } A ) ^ { \perp } = \operatorname { s p a n } \{ v _ { 1 } , \dots , v _ { r } \}$ ;   
3. Im $A = \operatorname { s p a n } \{ u _ { 1 } , \ldots , u _ { r } \}$ and $( \mathrm { I m } A ) ^ { \perp } = \operatorname { s p a n } \{ u _ { r + 1 } , \dots , u _ { m } \}$ ;   
4. $A \in \mathbb { F } ^ { m \times n }$ has a dyadic expansion:

$$A = \sum_ {i = 1} ^ {r} \sigma_ {i} u _ {i} v _ {i} ^ {*} = U _ {r} \Sigma_ {r} V _ {r} ^ {*},$$
