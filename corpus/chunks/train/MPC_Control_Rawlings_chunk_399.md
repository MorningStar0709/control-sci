Hence an upper bound for $\phi _ { \infty }$ may be obtained by determining $\phi _ { N } , \mathrm { i . e . }$ , by solving a linear program. The constant $( 1 - \alpha ) ^ { - 1 }$ may be made as close as desired to 1 by choosing α suitably small. The set Z defined by

$$\mathbb {Z} := \{z \in \mathbb {R} ^ {n} | c ^ {\prime} z \leq d - (1 - \alpha) ^ {- 1} \phi_ {N} \} \subseteq \hat {\mathbb {Z}}$$

is a suitable constraint set for the robust controller. If there are several state constraints

$$y _ {j} := c _ {j} ^ {\prime} x \leq d _ {j} \forall j \in \mathcal {J}$$

and K and N are chosen as previously to satisfy $A _ { K } ^ { N } w \ \in \ \alpha \mathbb { W }$ for all $w ~ \in ~ \mathbb { W }$ and some $\alpha \in \mathsf { \Gamma } ( 0 , 1 )$ , then a suitable constraint set for the controller is the set

$$\mathbb {Z} := \{z \in \mathbb {R} ^ {n} \mid c _ {j} ^ {\prime} z \leq d _ {j} - (1 - \alpha) ^ {- 1} \phi_ {N} ^ {j}, \forall j \in \mathcal {J} \} \subseteq \hat {\mathbb {Z}}$$

in which, for each $j \in \mathcal I$ ,

$$\phi_ {N} ^ {j} := \max _ {\{w _ {i} \}} \left\{c _ {j} ^ {\prime} e \mid e \in S _ {K} (i) \right\} = \max _ {\{w _ {i} \}} \left\{c _ {j} ^ {\prime} \sum_ {i = 0} ^ {N - 1} A _ {K} ^ {i} w _ {i} \mid w _ {i} \in \mathbb {W} \right\}$$

A similar procedure may be used to obtain a suitable constraint set $\mathbb { V } \subseteq \hat { \mathbb { V } } = \mathbb { U } \ominus K S _ { K } ( \infty )$ . Suppose U is described by

$$\mathbb {U} := \{u \in \mathbb {R} ^ {m} \mid a _ {j} ^ {\prime} u \leq b _ {j} \forall j \in \mathcal {I} \}$$

If K and N are chosen as above, then a suitable constraint set V for the nominal system is

$$\mathbb {V} := \{\nu \in \mathbb {R} ^ {m} \mid a _ {j} ^ {\prime} \nu \leq b _ {j} - (1 - \alpha) ^ {- 1} \theta_ {N} ^ {j}, j \in \mathcal {I} \}$$

in which, for each $j \in \mathcal I$ ,

$$\theta_ {N} ^ {j} := \max _ {\{w _ {i} \}} \left\{a _ {j} ^ {\prime} K e \mid e \in S _ {K} (i) \right\} = \max _ {\{w _ {i} \}} \left\{a _ {j} ^ {\prime} K \sum_ {i = 0} ^ {N - 1} A _ {K} ^ {i} w _ {i} \mid w _ {i} \in \mathbb {W} \right\}$$
