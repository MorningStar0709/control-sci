# ■ Theorem 8.1

Let $G(s)$ be strictly proper with a stabilizable and detectable realization $(A, B, C)$ . Then $\|G\|_{\infty} < 1$ if, and only if, H has no eigenvalues on the imaginary axis.

Proof: By Lemma 8.1, the poles of $[I - G^T(-s)G(s)]^{-1}$ must be eigenvalues of $H$ . Conversely, because of Lemma 8.2, all $j$ -axis eigenvalues of $H$ will appear as poles of $[I - G^T(-s)G(s)]^{-1}$ .

If: Suppose $\| G\|_{\infty} < 1$ . For all $\omega$ and complex vectors $\mathbf{v} \neq \mathbf{0}$ ,

$$
\begin{array}{l} \mathbf {v} ^ {T} [ I - G ^ {T} (- j \omega) G (j \omega) ] \mathbf {v} = \| \mathbf {v} \| ^ {2} - \mathbf {v} ^ {* T} G ^ {T} (- j \omega) G (j \omega) \mathbf {v} \\ \geq \{1 - \overline {{{\sigma}}} ^ {2} [ G (j \omega) ] \} \| \mathbf {v} \| ^ {2} \\ \geq (1 - \| G \| _ {\infty} ^ {2}) \| \mathbf {v} \| ^ {2} \\ > 0. \\ \end{array}
$$

This shows that $I - G^{T}(-j\omega)G(j\omega)$ is Hermitian for all $\omega$ ; hence, its determinant is strictly positive so that $[I - G^{T}(-s)G(s)]^{-1}$ has no poles at $s = j\omega$ , any $\omega$ .

Only if: Suppose $\| G\|_{\infty}\geq 1$ . Since $G$ is strictly proper, $G(j\omega)\to 0$ as $\omega \to \infty$ ; because of continuity, $\overline{\sigma}[G(j\omega)] = 1$ for some $\omega = \omega_0$ . We may then choose a $\mathbf{v}_0$ such that $\mathbf{v}_0^{*^T}G^T (-j\omega_0)G(j\omega_0)\mathbf{v}_0 = 1$ and, following the steps in the "if" part, show that $\det [I - G^T (-j\omega_0)G(j\omega_0)] = 0$ . In that case, $[I - G^T (-s)G(s)]^{-1}$ does have a pole at $s = j\omega_0$ , and that pole appears as an eigenvalue of $H$ .

In actual fact, we want a test of the statement $\| G\|_{\infty} < \gamma$ . This is achieved by testing $\| \gamma^{-1}G\|_{\infty} < 1$ ; to see this, note that

$$\| \gamma^ {- 1} G \| _ {\infty} = \gamma^ {- 1} \| G \| _ {\infty}$$

so that

$$\| \gamma^ {- 1} G \| _ {\infty} < 1 \Rightarrow \| G \| _ {\infty} < \gamma .$$

The realization for $\gamma^{-1}G$ is constructed simply by replacing $B$ with $\gamma^{-1}B$ in the matrix $H$ .

The calculation of $\|G\|_{\infty}$ is an iterative process, a search for that value of $\gamma$ such that the matrix $H(\gamma)=[_{-C^{T}C}{}^{\gamma^{-2}BB^{T}}]$ has one or more eigenvalues on the imaginary axis. The procedure can begin with an upper bound for $\gamma$ , and the search can commence from there. It helps to realize that H is a symplectic matrix—it has the property that its eigenvalues are symmetrically located with respect to the j-axis.
