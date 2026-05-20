# 2.1 Linear Subspaces

Let R denote the real scalar field and C the complex scalar field. For the interest of this chapter, let F be either R or C and let $\mathbb { F } ^ { n }$ be the vector space over F $( \mathrm { i . e . , } \mathbb { F } ^ { n }$ is either Rn or Cn). Now let $x _ { 1 } , x _ { 2 } , \ldots , x _ { k } \in \mathbb { F } ^ { n }$ . Then an element of the form $\alpha _ { 1 } x _ { 1 } + . . . + \alpha _ { k } x _ { k }$ with $\alpha _ { i } \in \mathbb { F }$ is a linear combination over F of $x _ { 1 } , \ldots , x _ { k }$ . The set of all linear combinations of $x _ { 1 } , x _ { 2 } , \ldots , x _ { k } \in \mathbb { F } ^ { n }$ is a subspace called the span of $x _ { 1 } , x _ { 2 } , \ldots , x _ { k }$ , denoted by

$$\mathrm{span} \{x _ {1}, x _ {2}, \ldots , x _ {k} \} := \{x = \alpha_ {1} x _ {1} + \ldots + \alpha_ {k} x _ {k}: \alpha_ {i} \in \mathbb {F} \}.$$

A set of vectors $x _ { 1 } , x _ { 2 } , \ldots , x _ { k } \in \mathbb { F } ^ { n }$ is said to be linearly dependent over F if there exists $\alpha _ { 1 } , \ldots , \alpha _ { k } \in \mathbb { F }$ not all zero such that $\alpha _ { 1 } x _ { 2 } + . . . + \alpha _ { k } x _ { k } = 0 ;$ otherwise the vectors are said to be linearly independent.

Let S be a subspace of $\mathbb { F } ^ { n }$ , then a set of vectors $\{ x _ { 1 } , x _ { 2 } , \dots , x _ { k } \} \in S$ is called a basis for S if $x _ { 1 } , x _ { 2 } , \ldots , x _ { k }$ are linearly independent and $S = \operatorname { s p a n } \{ x _ { 1 } , x _ { 2 } , . . . , x _ { k } \}$ . However, such a basis for a subspace S is not unique but all bases for S have the same number of elements. This number is called the dimension of S, denoted by dim(S).

A set of vectors $\{ x _ { 1 } , x _ { 2 } , \ldots , x _ { k } \}$ in $\mathbb { F } ^ { n }$ is mutually orthogonal if $x _ { i } ^ { * } x _ { j } = 0$ for all $i \neq j$ and orthonormal if $x _ { i } ^ { * } x _ { j } = \delta _ { i j }$ , where the superscript ∗ denotes complex conjugate transpose and $\delta _ { i j }$ is the Kronecker delta function with $\delta _ { i j } = 1$ for $i = j$ and $\delta _ { i j } = 0$ for $i \neq j$ . More generally, a collection of subspaces $S _ { 1 } , S _ { 2 } , \ldots , S _ { k }$ of $\mathbb { F } ^ { n }$ is mutually orthogonal if $x ^ { * } y = 0$ whenever $x \in S _ { i }$ and $y \in S _ { j }$ for $i \neq j$ .

The orthogonal complement of a subspace $S \subset \mathbb { F } ^ { n }$ is defined by

$$S ^ {\perp} := \{y \in \mathbb {F} ^ {n}: y ^ {*} x = 0 \text { for all } x \in S \}.$$
