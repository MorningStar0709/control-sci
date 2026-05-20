Remark 1. By introducing reciprocal polynomials, Eq. (12.45) can be written as

$$r P (z) P ^ {*} (z) = \rho A (z) A ^ {*} (z) + z ^ {d} B (z) B ^ {*} (z) \tag {12.46}$$

where $P^{*}(z) = z^{n}P(z^{-1})$ , and so on.

Remark 2. If $P(z)$ satisfies (12.45) so does $z^l P(z)$ , where $l$ is an arbitrary integer. To obtain a unique $P$ we can either specify the degree of $P$ or choose $P$ as the polynomial of lowest degree that satisfies (12.45). For a control problem it is natural to interpret $P(z)$ as the closed loop characteristic polynomial under state feedback. With this interpretation it is natural to require that $\deg P(z) = \deg A(z) = n$ . Notice that it is possible to find a $P$ of lower degree when $\rho = 0$ or when $A(0) = 0$ .

Conceptually the spectral-factorization problem can be solved by finding the zeros of the right-hand side of (12.45) and sorting them. There are also efficient recursive algorithms for solving the problem.
