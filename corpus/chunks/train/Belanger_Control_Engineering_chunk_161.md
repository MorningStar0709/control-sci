# ■ Theorem 3.8

A single-input, single-output LTI system is input-output stable if, and only if, its transfer function has all its poles in the open left-half plane.

Proof: First, let us demonstrate sufficiency. If $p_1, p_2, \ldots, p_K$ are the poles of the transfer function, the impulse response is a sum of terms of the form $t^k e^{p_i t}$ . If $Re(p_i) < 0$ for $i = 1, 2, \ldots, K$ , then $h(t)$ decreases exponentially and is absolutely integrable, so the system is input-output stable.

To show necessity, assume that at least one pole has a nonnegative real part. Let $p_{1}$ be the pole with the largest (i.e., “most positive”) real part. For t sufficiently large, the terms $t^{k}e^{p_{1}t}$ will dominate the others in $h(t)$ ; i.e.,

$$h (t) \approx a t ^ {k} e ^ {p _ {1} t}$$

for large t. Since the integral of $t^{k}|e^{p_{1}t}|$ diverges if $Rep_{1} \geq 0$ , the integral of $h(t)$ blows up and the system is not input–output stable. ■

In the case of multi-input, multi-output systems, the necessary and sufficient condition is that all individual elements of the matrix transfer function have all their poles in the open left-half plane.

The two types of stability are related. If an LTI system is internally stable, it is also input-output stable, because all transfer function poles are eigenvalues of the A matrix: if all eigenvalues of A are in the open left-half plane, so are the poles.

The converse is not always true: if all transfer function poles lie in the open left-half plane, it does not follow that all eigenvalues of A do. The A matrix could have unstable hidden modes that do not appear in the transfer function.

This leads to the concepts of detectability and stabilizability, defined as follows.
