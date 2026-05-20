# Spectral Factorization

The LQ-problem is solved in Sec. 11.4 using the state-space approach, which led to a steady-state Riccati equation. It follows from the Riccati equation that

$$r P (z) P \left(z ^ {- 1}\right) = \rho A (z) A \left(z ^ {- 1}\right) + B (z) B \left(z ^ {- 1}\right) \tag {12.45}$$

where the monic polynomial $P(z)$ is the characteristic polynomial of the closed-loop system. [see Eq. (11.40)]. The closed-loop characteristic polynomial can be obtained by solving a steady-state Riccati equation. An alternative is to find a polynomial $P(z)$ that satisfies (12.45) directly. A feedback that gives the desired closed-loop poles can then be determined by pole placement. The problem of finding a polynomial $P(z)$ that satisfies (12.45) is called spectral factorization.

First, consider a polynomial of the form

$$F (z) = f _ {0} z ^ {2 n} + f _ {1} z ^ {2 n - 1} + \dots + f _ {n - 1} z ^ {n + 1} + f _ {n} z ^ {n} + f _ {n - 1} z ^ {n - 1} + \dots + f _ {1} z + f _ {0}$$

Such a polynomial is self-reciprocal because

$$F ^ {*} (z) = z ^ {2 n} F \left(z ^ {- 1}\right) = F (z)$$

It then follows that if $z = a$ is a zero of $F(z)$ , then $z = 1 / a$ is also a zero. Moreover, if the coefficients $f_i$ are real, then $z = \bar{a}$ and $z = 1 / \bar{a}$ are also zeros, where $\bar{a}$ is the complex conjugate of $a$ . The following result can now be established.

LEMMA 12.1 Let the real polynomials $A(z)$ and $B(z)$ be relatively prime with $\deg A(z) > \deg B(z)$ . Then there exists a unique polynomial $P(z)$ with $\deg P(z) = \deg A(z) = n$ and all its zeros inside the unit disc or on the unit circle such that (12.45) holds. If $\rho > 0$ , then $P(z)$ has no zeros on the unit circle.

Proof. A self-reciprocal polynomial is obtained if the right-hand side of (12.45) is multiplied by $z^{n}$ . The zeros of the right-hand side are thus mirror images with respect to the unit circle. Because the coefficients are real, the zeros are also symmetric with respect to the real axis. The right-hand side of (12.45) cannot have zeros on the unit circle because if $z = e^{iw}$ is such a zero, then

$$\rho A (e ^ {i \omega}) A (e ^ {- i \omega}) + B (e ^ {i \omega}) B (e ^ {- i \omega}) = \rho | A (e ^ {i \omega}) | ^ {2} + | B (e ^ {i \omega}) | ^ {2} = 0$$

As $\rho > 0$ , this implies that $z = \exp(i\omega)$ is a zero of both $A(z)$ and $B(z)$ , which contradicts the assumption that $A(z)$ and $B(z)$ are relatively prime. The condition $\deg P(z) = n$ ensures a unique $P(z)$ .
