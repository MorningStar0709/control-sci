# 4.7 Particle Filtering

lated to the left by $\sqrt { 1 0 } )$ . Exercise 4.20 discusses this example further. -

Unbiasedness of sampled densities. A sampled density is unbiased if it possesses the following property

$$\mathcal {E} _ {\mathrm{sa}} \left(P _ {s} (x; s)\right) = P (x) \quad 1 \leq s, - \infty < x < \infty$$

in which the expectation is taken over the probability density of $P _ { s }$ considered as a random variable as discussed previously. As we discuss subsequently, some sampling procedures are unbiased for all s, while others are only asymptotically unbiased as s becomes large. A convenient test for unbiasedness is the following

$$\mathcal {E} _ {\mathrm{sa}} \left(\int p _ {s} (x) g (x) d x\right) = \int p (x) g (x) d x \quad \text { for all } g (\cdot) \tag {4.43}$$

In other words, the expectation over the sampling process of integrals of any function g with the sampled density should be equal to the integral of g with the exact density. If the sampling process has the probability given by (4.38), we can verify (4.43) as follows

$$
\begin{array}{l} \mathcal {E} _ {\mathrm{sa}} \left(\int p _ {s} (x) g (x) d x\right) = \mathcal {E} _ {\mathrm{sa}} \left(\sum_ {i} w _ {i} g \left(x _ {i}\right)\right) \\ = \int p _ {\mathrm{sa}} \left(x _ {1}, \dots , x _ {s}\right) \sum_ {i} w _ {i} g \left(x _ {i}\right) d x _ {1} \dots d x _ {s} \\ = \int p _ {\mathrm{sa}} (x _ {1}) \cdot \cdot \cdot p _ {\mathrm{sa}} (x _ {s}) \sum_ {i} w _ {i} g (x _ {i}) d x _ {1} \cdot \cdot \cdot d x _ {s} \\ = \int p (x _ {1}) \dots p (x _ {s}) \sum_ {i} w _ {i} g (x _ {i}) d x _ {1} \dots d x _ {s} \\ = \frac {1}{s} \sum_ {i} \int p (x _ {i}) g (x _ {i}) d x _ {i} \prod_ {j \neq i} \int p (x _ {j}) d x _ {j} \\ = \frac {1}{s} \sum_ {i} \int p (x _ {i}) g (x _ {i}) d x _ {i} \\ \end{array}
\mathcal {E} _ {\mathrm{sa}} \left(\int p _ {s} (x) g (x) d x\right) = \int p (x) g (x) d x
$$
