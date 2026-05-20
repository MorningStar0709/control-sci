# 10.2.1 Definitions of $\mu$

We shall motivate the definition of the structured singular value by asking the following question: Given a matrix $M \in \mathbb { C } ^ { p \times q }$ , what is the smallest perturbation matrix $\Delta \in \mathbb { C } ^ { q \times p }$ in the sense of $\overline { { \sigma } } ( \Delta )$ such that

$$\det (I - M \Delta) = 0?$$

That is, we are interested in finding

$$\alpha_ {\min} := \inf \left\{\overline {{\sigma}} (\Delta): \det (I - M \Delta) = 0, \Delta \in \mathbb {C} ^ {q \times p} \right\}.$$

It is easy to see that

$$\alpha_ {\min} = \inf \left\{\alpha : \det (I - \alpha M \Delta) = 0, \overline {{\sigma}} (\Delta) \leq 1, \Delta \in \mathbb {C} ^ {q \times p} \right\} = \frac {1}{\max _ {\overline {{\sigma}} (\Delta) \leq 1} \rho (M \Delta)}$$

and

$$\max _ {\overline {{\sigma}} (\Delta) \leq 1} \rho (M \Delta) = \overline {{\sigma}} (M).$$

Hence the smallest norm of a “destabilizing” perturbation matrix is $1 / \overline { { \sigma } } ( M )$ with a smallest “destabilizing” ∆:

$$\Delta_ {\mathrm{des}} = \frac {1}{\overline {{\sigma}} (M)} v _ {1} u _ {1} ^ {*}, \quad \det (I - M \Delta_ {\mathrm{des}}) = 0$$

where $M = \overline { { \sigma } } ( M ) u _ { 1 } v _ { 1 } ^ { * } + \sigma _ { 2 } u _ { 2 } v _ { 2 } ^ { * } + \cdot \cdot \cdot$ is a singular value decomposition.

So the reciprocal of the largest singular value of a matrix is a measure of the smallest “destabilizing” perturbation matrix. Hence it is instructive to introduce the following alternative definition for the largest singular value:

$$\overline {{\sigma}} (M) := \frac {1}{\inf \{\overline {{\sigma}} (\Delta) : \det (I - M \Delta) = 0 , \Delta \in \mathbb {C} ^ {q \times p} \}}.$$

Next we consider a similar problem but with ∆ structurally restricted. In particular, we consider the block diagonal matrix ∆. We shall consider two types of blocks: repeated scalar and $f u l l$ blocks. Let S and F represent the number of repeated scalar blocks and the number of full blocks, respectively. To bookkeep their dimensions, we introduce positive integers $r _ { 1 } , . . . , r _ { S } ; m _ { 1 } , . . . , m _ { F }$ . The ith repeated scalar block is $r _ { i } \times r _ { i } .$ , while the jth full block is $m _ { j } \times m _ { j }$ . With those integers given, we define $\pmb { \Delta } \subset \mathbb { C } ^ { n \times n }$ as
