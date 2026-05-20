# Modified z-transform

The behavior between sampling points can be investigated using the modified z-transform. This is the ordinary z-transform, but a time delay mh, which is a fraction of the sampling period is introduced. The modified z-transform is defined as follows.

DEFINITION 2.2 THE MODIFIED z-TRANSFORM The modified z-transform of a continuous-time function is given by

$$\tilde {F} (z, m) = \sum_ {k = 0} ^ {\infty} z ^ {- k} f (k h - h + m h) \quad 0 \leq m \leq 1 \tag {2.34}$$

The inverse transform is given by

$$f (n h - h + m h) = \frac {1}{2 \pi i} \int_ {\Gamma} \tilde {F} (z, m) z ^ {n - 1} d z$$

where the contour $\Gamma$ encloses all singularities of the integrand.

The modified z-transform is useful for many purposes—for example, the inter-sample behavior can easily be investigated using these transforms. There are extensive tables of modified z-transforms and many theorems about their properties (see the References).
