We call a set of vectors $\{ u _ { 1 } , u _ { 2 } , \ldots , u _ { k } \}$ an orthonormal basis for a subspace $S \in \mathbb { F } ^ { n }$ if the vectors form a basis of S and are orthonormal. It is always possible to extend such a basis to a full orthonormal basis $\left\{ u _ { 1 } , u _ { 2 } , \ldots , u _ { n } \right\}$ for $\mathbb { F } ^ { n }$ . Note that in this case

$$S ^ {\perp} = \mathrm{span} \{u _ {k + 1}, \ldots , u _ {n} \},$$

and $\{ u _ { k + 1 } , \ldots , u _ { n } \}$ is called an orthonormal completion of $\{ u _ { 1 } , u _ { 2 } , \ldots , u _ { k } \}$ .

Let $A \in \mathbb { F } ^ { m \times n }$ be a linear transformation from $\mathbb { F } ^ { n }$ to $\mathbb { F } ^ { m }$ ; that is,

$$A: \mathbb {F} ^ {n} \longmapsto \mathbb {F} ^ {m}.$$

Then the kernel or null space of the linear transformation A is defined by

$$\operatorname{Ker} A = N (A) := \{x \in \mathbb {F} ^ {n}: A x = 0 \},$$

and the image or range of A is

$$\operatorname{Im} A = R (A) := \left\{y \in \mathbb {F} ^ {m}: y = A x, x \in \mathbb {F} ^ {n} \right\}.$$

Let $a _ { i } , i = 1 , 2 , \ldots , n$ denote the columns of a matrix $A \in \mathbb { F } ^ { m \times n }$ ; then

$$\operatorname{Im} A = \operatorname{span} \left\{a _ {1}, a _ {2}, \dots , a _ {n} \right\}.$$

A square matrix $U \in F ^ { n \times n }$ whose columns form an orthonormal basis for $\mathbb { F } ^ { n }$ is called a unitary matrix (or orthogonal matrix $\operatorname { i f } \mathbb { F } = \mathbb { R } )$ , and it satisfies $U ^ { * } U = I = U U ^ { * }$ .

Now let $A = [ a _ { i j } ] \in \mathbb { C } ^ { n \times n }$ ; then the trace of A is defined as

$$\operatorname{trace} (A) := \sum_ {i = 1} ^ {n} a _ {i i}.$$

Illustrative MATLAB Commands:

basis of $\mathbf { K e r A } = \mathbf { n u l l } ( \mathbf { A } )$ ; basis of Im $\mathbf { A } = \mathbf { o r t h } ( \mathbf { A } )$ ; rank of $\mathbf { A } = \mathbf { r a n k } ( \mathbf { A } )$ ;
