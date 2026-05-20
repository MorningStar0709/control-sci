# 8.5 NORMS

The Euclidean, or $\ell_2$ , norm of a vector $\mathbf{x}$ has been defined as

$$\| \mathbf {x} \| _ {2} = \left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2}\right) ^ {1 / 2} = (\mathbf {x} ^ {T} \mathbf {x}) ^ {1 / 2}. \tag {8.21}$$

For a vector signal $\mathbf{x}(t)$ , the $\ell_2$ norm is

$$\| \mathbf {x} \| _ {2} = \left[ \int_ {- \infty} ^ {\infty} \mathbf {x} ^ {T} (t) \mathbf {x} (t) d t \right] ^ {1 / 2}. \tag {8.22}$$

This norm is the square root of the sum of the energy in each component of the vector.

For power signals, we may use the root-mean-square (rms) value

$$r m s (\mathbf {x}) = \left(\lim _ {T \rightarrow \infty} \frac {1}{2 T} \int_ {- T} ^ {T} \mathbf {x} ^ {T} (t) \mathbf {x} (t) d t\right) ^ {1 / 2}. \tag {8.23}$$

For an $m \times r$ matrix, we can define the Frobenius norm,

$$\| A \| _ {2} = \left(\sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {r} A _ {i j} ^ {2}\right) ^ {1 / 2}. \tag {8.24}$$

It can be shown that

$$\| A \| _ {2} ^ {2} = \operatorname{tr} (A ^ {T} A) = \operatorname{tr} (A A ^ {T}) \tag {8.25}$$

where "tr" refers to the trace, i.e., the sum of the diagonal elements.

Linear, time-invariant systems are generalizations of matrices; a matrix operates on a vector to produce another vector, and an LTI system operates on a signal to produce another signal. By analogy to the Frobenius norm, we define the $L_{2}$ norm for an $m \times r$ transfer function $G(s)$ as

$$\| G \| _ {2} = \left(\frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \operatorname{tr} [ G ^ {T} (- j \omega) G (j \omega) ] d \omega\right) ^ {1 / 2}. \tag {8.26}$$

It is easy to show that $\| G\| _2$ exists [2] if, and only if, each element of $G(s)$ is strictly proper and has no poles on the imaginary axis. In that case, we write $G\in L_2$ . Under those conditions, the norm can be evaluated as an integral in the complex plane:

$$
\begin{array}{l} \| G \| _ {2} ^ {2} = \frac {1}{2 \pi j} \int_ {- j ^ {\infty}} ^ {j ^ {\infty}} \operatorname{tr} \left[ G ^ {T} (- s) G (s) \right] d s \\ = \frac {1}{2 \pi j} \oint \operatorname{tr} \left[ G ^ {T} (- s) G (s) \right] d s \tag {8.27} \\ \end{array}
$$

where the last integral is taken over a contour that runs up the j-axis and around an infinite semicircle in either half plane. Since $G(s)$ is strictly proper, it is easily shown that the integrand vanishes over the semicircle, so that the residue theorem can be used.

If $G \in L_2$ and, in addition, $G$ is stable, then we say that $G \in H^2$ ; $H^2$ is the so-called Hardy space defined with the 2-norm.
