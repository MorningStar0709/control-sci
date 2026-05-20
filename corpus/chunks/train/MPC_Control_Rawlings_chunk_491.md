in which $x _ { i } , i \ = \ 1 , \ldots s$ are the samples, $\boldsymbol { \psi } _ { i }$ are the weights. As an example, the top of Figure 4.7 displays a normally distributed scalar random variable represented by a sampled density with five samples. The sampled density is a series of impulses at the sample locations $x _ { i }$ . In this example, the weights $w _ { i }$ are the values of $p ( \boldsymbol { x } _ { i } )$ , normalized to sum to unity. It may seem strange to represent a well-behaved function like $p ( x )$ with such a “rough” function like $p _ { s } ( x )$ , but we will see the advantages shortly. Sometimes we may wish to study convergence of a sampled density to the original density as the number of samples becomes large. To define convergence of this representation of the probability distribution, we refer to the corresponding cumulative distribution rather than the density. From integration, the sampled cumulative distribution is

$$P _ {s} (x) = \sum_ {i \in \mathbb {I} _ {x}} w _ {i} \quad \mathbb {I} _ {x} = \{i | x _ {i} \leq x \}$$

The bottom of Figure 4.7 shows the corresponding cumulative sampled distribution for the sampled density with five samples. The cumulative sampled distribution is a staircase function with steps of size $w _ { i }$ at the sample locations $x _ { i }$ . We can then measure convergence of $P _ { s } ( x )$ to $P ( x )$ as $s  \infty$ in any convenient function norm. We delay further discussion of convergence until Section 4.7.2 in which we present some of the methods for choosing the samples and the weights.

In the sequel, we mostly drop the subscript s on sampled densities and cumulative distributions when it is clear from context that we are referring to this type of representation of a probability distribution. We can conveniently calculate the expectation of any function of a random variable having a sampled density by direct integration to obtain

$$
\begin{array}{l} \mathcal {E} (f (\xi)) = \int p _ {s} (x) f (x) d x \\ = \int \sum_ {i} w _ {i} \delta (x - x _ {i}) f (x) d x \\ = \sum_ {i} w _ {i} f (x _ {i}) \\ \end{array}
$$

For example, we often wish to evaluate the mean of the sampled density, which is

$$\mathcal {E} (\xi) = \sum_ {i} w _ {i} x _ {i}$$

The convenience of integrating the sampled density is one of its main attractive features. If we create a new function (not necessarily a density) by multiplication of $p ( x )$ by another function $g ( x )$

$$\overline {{p}} (x) = g (x) p (x)$$

we can easily obtain the sampled function ${ \overline { { p } } } .$ . We simply adjust the

weights and leave the samples where they are

$$
\begin{array}{l} \overline {{p}} (x) = g (x) p (x) \\ = \sum_ {i} g (x) w _ {i} \delta \left(x - x _ {i}\right) \\ = \sum_ {i} w _ {i} g (x _ {i}) \delta (x - x _ {i}) \\ \overline {{p}} (x) = \sum_ {i} \overline {{w}} _ {i} \delta (x - x _ {i}) \quad \overline {{w}} _ {i} = w _ {i} g (x _ {i}) \tag {4.36} \\ \end{array}
$$
