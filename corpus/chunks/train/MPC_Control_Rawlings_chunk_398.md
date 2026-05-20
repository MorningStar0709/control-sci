is a suitable constraint for the nominal system, i.e., $z \in { \hat { \mathbb { Z } } }$ implies $c ^ { \prime } x \ = \ c ^ { \prime } z + c ^ { \prime } e \ \leq \ d$ or $x \in \mathbb { X }$ for all $e \ \in \ S _ { K } ( \infty )$ . To obtain ${ \hat { \mathbb { Z } } } ,$ we need to compute $\phi _ { \infty }$ . But computing $\phi _ { \infty }$ requires solving an infinite dimensional optimization problem, which is impractical. We can obtain an inner approximation to ${ \hat { \mathbb { Z } } } ,$ which is all we need to implement robust MPC, by computing an upper bound to $\phi _ { \infty }$ . We now show how this may be done (Rakovi´c, Kerrigan, Kouramas, and Mayne, 2003). We require the following assumption.

Assumption 3.16 (Compact convex disturbance set). The compact convex set W contains the origin in its interior.

For each $i \in \mathbb { I } _ { \geq 0 }$ , let $\phi _ { i }$ be defined as follows

$$\phi_ {i} := \max _ {e} \{c ^ {\prime} e \mid e \in S _ {K} (i) \}$$

It can be shown that

$$\phi_ {N} = \max _ {\{w _ {i} \}} \left\{c ^ {\prime} \sum_ {i = 0} ^ {N - 1} A _ {K} ^ {i} w _ {i} \mid w _ {i} \in \mathbb {W} \right\}$$

and that

$$\phi_ {\infty} = \max _ {\{w _ {i} \}} \left\{c ^ {\prime} \sum_ {i = 0} ^ {\infty} A _ {K} ^ {i} w _ {i} \mid w _ {i} \in \mathbb {W} \right\}$$

Suppose now we choose the feedback matrix K and the horizon N so that

$$A _ {K} ^ {N} \boldsymbol {w} \in \alpha \mathbb {W} \forall \boldsymbol {w} \in \mathbb {W}$$

where $\alpha \in ( 0 , 1 )$ . Because $A _ { K }$ is stable and W contains the origin in its interior, this choice is always possible. It follows from the definitions of $\phi _ { \infty }$ and $\phi _ { N }$ that

$$
\begin{array}{l} \phi_ {\infty} = \phi_ {N} + \max _ {\{w _ {i} \}} \left\{c ^ {\prime} \sum_ {i = N} ^ {\infty} A _ {K} ^ {i} w _ {i} \mid w _ {i} \in \mathbb {W} \right\} \\ = \phi_ {N} + \max _ {\{w _ {i} \}} \left\{c ^ {\prime} \left(A _ {K} ^ {N} w _ {0} + A _ {K} A _ {K} ^ {N} w _ {1} + A _ {K} ^ {2} A _ {K} ^ {N} w _ {2} + \dots\right) \mid w _ {i} \in \mathbb {W} \right\} \\ \leq \phi_ {N} + \max _ {\{w _ {i} \}} \left\{c ^ {\prime} \left(\alpha w _ {0} + A _ {K} \alpha w _ {1} + A _ {K} ^ {2} \alpha w _ {2} + \dots\right) \mid w _ {i} \in \mathbb {W} \right\} \\ \end{array}
$$

where the last line follows from the fact that $A _ { K } ^ { N } w \in \alpha W$ if $w \in \mathbb { W }$ . It follows that

$$\phi_ {\infty} \leq \phi_ {N} + \alpha \phi_ {\infty}$$

or

$$\phi_ {\infty} \leq (1 - \alpha) ^ {- 1} \phi_ {N}$$
