# Process Model

Assume that the process dynamics are characterized by

$$x (t) = \frac {B _ {1} (q)}{A _ {1} (q)} u (t)$$

where $A_{1}(q)$ and $B_{1}(q)$ are polynomials in the forward shift operator without any common factors.

It is assumed that the action of the disturbances on the system can be described as filtered white noise. Since the system is linear, we can reduce all disturbances to an equivalent disturbance v at the system output. The output is thus given by

$$y (t) = x (t) + v (t)$$

where

$$v (t) = \frac {C _ {1} (q)}{A _ {2} (q)} e (t)$$

$C_{1}(q)$ and $A_{2}(q)$ are polynomials in the forward shift operator without any common factors, and $\{e(t)\}$ is a sequence of independent random variables (white noise) with zero mean and standard deviation $\sigma$ .

The process can now be reduced to the standard form

$$A (q) y (t) = B (q) u (t) + C (q) e (t) \tag {4.1}$$

where

$$A = A _ {1} A _ {2}B = B _ {1} A _ {2} \tag {4.2}C = C _ {1} A _ {1}$$

Because of the assumptions, the three polynomials have no common factor. The model (4.1) is thus a minimal representation. The polynomials are normalized such that both the A and C polynomials are monic, that is, the leading coefficients are unity. Finally, the C polynomial can be multiplied by an arbitrary power of q without changing the correlation structure of $C(q)e(t)$ . This is used to normalize C such that

$$\deg C = \deg A = n$$

The A and B polynomials may have zeros inside or outside the unit disc. It is assumed that the zeros of the C polynomial are inside the unit disc. By spectral factorization the polynomial $C(q)$ can be changed so that all its zeros are inside the unit disc or on the unit circle. An example shows how this is done.
