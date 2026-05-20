# Example 8.3 Calculate the $L_{2}$ norm of

$$
G (s) = \frac {1}{s ^ {2} + 3 s + 2} \left[ \begin{array}{c c} s + 3 & - (s + 2) \\ - 2 & s + 2 \end{array} \right].
$$

Solution We compute

$$
\begin{array}{l} \operatorname{tr} G ^ {T} (- s) G (s) = \frac {(s + 3) (- s + 3) + 4 + (s + 2) (s + 2) - (- s + 2) (s + 2)}{(s + 1) (s + 2) (- s + 1) (- s + 2)} \\ = \frac {- 3 s ^ {2} + 2 1}{(s + 1) (s + 2) (- s + 1) (- s + 2)}. \\ \end{array}
$$

If we integrate about a contour enclosing the LHP (positive angle direction), the integral of Equation 8.27 is the sum of the residues at s = -1 and s = -2:

$$\| G \| _ {2} ^ {2} = \frac {1 8}{(1) (2) (3)} + \frac {9}{(- 1) (3) (4)} = \frac {9}{4}.$$

Therefore, $\| G\| _2^2 = 3 / 2$

A different type of norm is the induced norm, which applies to operators and is essentially a type of maximum gain. For a matrix, the induced Euclidean norm is

$$
\begin{array}{l} \| A \| _ {2 i} = \max _ {\| \mathbf {d} \| _ {2} = 1} \| A \mathbf {d} \| _ {2} \\ = \overline {{{\sigma}}} (A) \tag {8.28} \\ \end{array}
$$

as we have seen.

To obtain the induced norm for an LTI system, consider first a stable, strictly proper SISO system. If the input $u(\cdot) \in \ell_2$ (see Equation 8.22), the output $y(\cdot) \in \ell_2$ . By Parseval's theorem,

$$\| y \| _ {2} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | G (j \omega) | ^ {2} | u (j \omega) | ^ {2} d \omega . \tag {8.29}$$

Clearly,

$$\| y \| _ {2} ^ {2} \leq \sup _ {\omega} | G (j \omega) | ^ {2} \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | u (j \omega) | ^ {2} d \omega$$

or

$$\| y \| _ {2} ^ {2} \leq \sup _ {\omega} | G (j \omega) | ^ {2} \| u \| _ {2} ^ {2}. \tag {8.30}$$

We argue that the RHS of Equation 8.30 can be approached arbitrarily closely, for a fixed value of $\| u\| _2$ that is chosen to be 1 with no loss of generality. Suppose $|u(j\omega)|^2$ approaches an impulse of area $2\pi$ in the frequency domain at $\omega = \omega_0$ . Then the integral of Equation 8.29 approaches $|G(j\omega_0)|^2$ . If $|G(j\omega)|$ has a maximum at some finite value of $\omega$ , we may choose $\omega_0$ to be that frequency. If not, then $|G(j\omega)|$ must approach a supremum as $\omega \to \infty$ ; we can make $\omega_0$ as large as we like, and $|G(j\omega_0)|$ will be as close to the supremum as we wish. The RHS of Equation 8.30 can be approached arbitrarily closely, and

$$\sup _ {\| u \| _ {2} = 1} \| y \| _ {2} = \sup _ {\omega} | G (j \omega) |. \tag {8.31}$$

This norm is also the infinity norm of G, given by
