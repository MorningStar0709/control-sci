# $\mathcal { H } _ { \infty } ^ { - }$ Space

$\mathcal { H } _ { \infty } ^ { - }$ is a (closed) subspace of $\mathcal { L } _ { \infty }$ with functions that are analytic and bounded in the open left-half plane. The $\mathcal { H } _ { \infty } ^ { - }$ norm is defined as

$$\| F \| _ {\infty} := \sup _ {\operatorname{Re} (s) < 0} \overline {{\sigma}} \left[ F (s) \right] = \sup _ {\omega \in \mathbb {R}} \overline {{\sigma}} \left[ F (j \omega) \right].$$

The real rational subspace of $\mathcal { H } _ { \infty } ^ { - }$ is denoted by $\mathcal { R H } _ { \infty } ^ { - }$ , which consists of all proper, real rational, antistable transfer matrices $( \mathrm { i . e . }$ ., functions with all poles in the open right-half plane).

Let $G ( s ) \in { \mathcal { L } } _ { \infty }$ be a $p \times q$ transfer matrix. Then a multiplication operator is defined as

$$M _ {G}: \mathcal {L} _ {2} \longmapsto \mathcal {L} _ {2}M _ {G} f := G f.$$

In writing the preceding mapping, we have assumed that $f$ has a compatible dimension. A more accurate description of the foregoing operator should be

$$M _ {G}: \mathcal {L} _ {2} ^ {q} \longmapsto \mathcal {L} _ {2} ^ {p}.$$

That ${ \mathrm { i s } } , f$ is a q-dimensional vector function with each component in $\mathcal { L } _ { 2 }$ . However, we shall suppress all dimensions in this book and assume that all objects have compatible dimensions.

A useful fact about the multiplication operator is that the norm of a matrix G in $\mathcal { L } _ { \infty }$ equals the norm of the corresponding multiplication operator.

Theorem 4.3 Let $G \in { \mathcal { L } } _ { \infty }$ be a $p \times q$ transfer matrix. Then $\| M _ { G } \| = \| G \| _ { \infty }$

Remark 4.1 It is also true that this operator norm equals the norm of the operator restricted to $\mathcal { H } _ { 2 } \ ( \mathrm { o r } \ \mathcal { H } _ { 2 } ^ { \perp } )$ ; that is,

$$\left\| M _ {G} \right\| = \left\| M _ {G} \mid_ {\mathcal {H} _ {2}} \right\| := \sup \left\{\left\| G f \right\| _ {2}: f \in \mathcal {H} _ {2}, \| f \| _ {2} \leq 1 \right\}.$$

This will be clear in the proof where an $f \in \mathcal { H } _ { 2 }$ is constructed.

![](image/34a256b7dabd69c3c3458c7c5fe7b5b0e1f3474712d8b13616440eab000a3baa.jpg)

Proof. By definition, we have

$$\left\| M _ {G} \right\| = \sup \left\{\left\| G f \right\| _ {2}: f \in \mathcal {L} _ {2}, \| f \| _ {2} \leq 1 \right\}.$$

First we see that $\| G \| _ { \infty }$ is an upper bound for the operator norm:
