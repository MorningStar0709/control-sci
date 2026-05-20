# Formal Proof

After the informal discussion we will now give a formal proof of the statements. For this purpose we will first prove a preliminary result.

LEMMA 12.2 Let the polynomial $P(z)$ be a solution to the spectral factorization problem (12.46) and let $A(z)$ be monic. Assume that the polynomials $A(z)$ and $B(z)$ do not have common roots outside the unit disc or on the unit circle; then there exists a unique solution to the equations

$$
\begin{array}{l} A ^ {*} (z) X (z) + r P (z) S ^ {*} (z) = B (z) C ^ {*} (z) \\ z ^ {d} B ^ {*} (z) X (z) - r P (z) R ^ {*} (z) = - \rho A (z) C ^ {*} (z) \tag {12.49} \\ \end{array}
$$

with $\deg X(z) < n$ , $\deg R^{*}(z) \leq n$ and $\deg S^{*}(z) < n$ , where $n = \deg A(z)$ .

Proof. First, assume that polynomial $P(z)$ has distinct zeros $z_{i}$ . Since $P(z)$ is stable we have $|z_{i}| < 1$ . The values $A^{*}(z_{i})$ and $B^{*}(z_{i})$ cannot vanish simultaneously because this would contradict the assumption that $A(z)$ and $B(z)$ do not have common unstable factors. Evaluating (12.49) for $z = z_{i}$ we get

$$A ^ {*} (z _ {i}) X (z _ {i}) = B (z _ {i}) C ^ {*} (z _ {i})z _ {i} ^ {d} B ^ {*} (z _ {i}) X (z _ {i}) = - \rho A (z _ {i}) C ^ {*} (z _ {i}) \tag {12.50}$$

If both $A^{*}(z_{i})$ and $B^{*}(z_{i})$ are different from zero, both equations give the same result, since it follows from (12.46) that

$$\frac {B (z _ {i})}{A ^ {*} (z _ {i})} = - \frac {\rho A (z _ {i})}{z _ {i} ^ {d} B ^ {*} (z _ {i})}$$

If $A^{*}(z_{i}) = 0$ and $B^{*}(z_{i}) \neq 0$ it follows from (12.46) that $B(z_{i}) = 0$ . Since $A(z)$ is monic it also follows that $A^{*}(0) = 1$ . This implies that $|z_{i}| \neq 0$ . The equation

$$A ^ {*} (z _ {i}) X (z _ {i}) = B (z _ {i}) C ^ {*} (z _ {i})$$

is trivially satisfied and the solution to (12.50) is

$$X (z _ {i}) = - \frac {\rho A (z _ {i}) C ^ {*} (z _ {i})}{z _ {i} ^ {d} B ^ {*} (z _ {i})}$$

A similar argument shows that $X(z_{i})$ is unique also when $B^{*}(z_{i}) = 0$ and $A(z_{i}) \neq 0$ . We can thus determine $\deg P$ values $X(z_{i})$ . Using Lagrange's interpolation formula the polynomial $X(z)$ of degree $\deg P - 1$ which satisfies (12.50) is thus unique.

It follows from the construction of the polynomial $X(z)$ that the polynomial $A^{*}(z)X(z) - B(z)C^{*}(z)$ vanishes for the zeros $z_{i}$ of $P(z)$ . This implies that it is divisible by $P(z)$ . The quotient

$$S ^ {*} (z) = \frac {A ^ {*} (z) X (z) - B (z) C ^ {*} (z)}{r P (z)}$$

is thus a polynomial. It has degree
