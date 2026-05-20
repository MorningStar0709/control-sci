# The z-Transform

Section 2.7 introduces z-transforms as mappings from sequences to functions of a complex variable. A different z-transform whose domain is continuous functions can be defined as follows:

DEFINITION 7.1 THE z-TRANSFORM The z-transform of a continuous-time function is defined as

$$\tilde {F} (z) = \sum_ {k = 0} ^ {\infty} z ^ {- k} f (k h) \tag {7.32}$$

The inverse transform is given by

$$f (k h) = \frac {1}{2 \pi i} \oint_ {\Gamma} z ^ {k - 1} \tilde {F} (z) d z$$

where the contour of integration $\Gamma$ encloses all singularities of the integrand.

The z-transform of a continuous-time signal is thus obtained by sampling the signal and then applying the z-transform to the sampled sequence. Because the transform depends only on the values at the sampling instants, all time functions that agree at the sampling instants have the same transform.

Notice that the transform is inherently related to the clock, which defines the sampling instants. Also notice that the inverse transform defines the function at the sampling instants only.

These properties of the z-transform of a continuous-time function are easily misunderstood and have led to much confusion and many mistakes.
