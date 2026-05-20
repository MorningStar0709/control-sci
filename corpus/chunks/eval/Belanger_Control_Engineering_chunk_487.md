$$\| G \| _ {\infty} = \lim _ {p \rightarrow \infty} \left(\frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} | G (j \omega) | ^ {p} d \omega\right) ^ {1 / p}. \tag {8.32}$$

The $\infty$ -norm of $G(s)$ exists if, and only if, $G$ is proper with no poles on the $j$ -axis. In that case, we write $G \in L^{\infty}$ . If, in addition, $G$ is stable, then we say $G \in H^{\infty}$ , the Hardy space with the infinity norm.

For multivariable systems,

$$
\begin{array}{l} \| \mathbf {y} \| _ {2} ^ {2} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \| G (j \omega) \mathbf {u} (j \omega) \| _ {2} ^ {2} d \omega \\ \leq \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \overline {{{\sigma}}} [ G (j \omega) ] \| \mathbf {u} (j \omega) \| ^ {2} d \omega \tag {8.33} \\ \leq \sup _ {\omega} \left[ \overline {{\sigma}} [ G (j \omega) ] \right] ^ {2} \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \| \mathbf {u} (j \omega) \| ^ {2} d \omega \\ \end{array}
$$

or

$$\| \mathbf {y} \| _ {2} ^ {2} \leq \left[ \sup _ {\omega} \overline {{{\sigma}}} [ G (j \omega) ] \right] ^ {2} \| \mathbf {u} \| _ {2} ^ {2}. \tag {8.34}$$

Note that $\|\mathbf{u}(j\omega)\|_{2}$ in the integrand refers to the 2-norm of the vector $\mathbf{u}(j\omega)$ , whereas in Equation 8.34 $\|u\|_{2}$ refers to the 2-norm of the signal.

Here again, the RHS of Equation 8.34 can be approached arbitrarily closely, by proper choice of $\mathbf{u}(j\omega)$ . Essentially, we pick $\mathbf{u}(j\omega)$ to be the eigenvector of $G^{*}(j\omega)G(j\omega)$ corresponding to the largest eigenvalue, and we concentrate the spectrum of $\mathbf{u}(j\omega)$ at the frequency where $\overline{\sigma}$ is the largest (or at some frequency that is arbitrarily large, if $\overline{\sigma}$ has no maximum but a supremum). Therefore,

$$\sup _ {\| \mathbf {u} \| _ {2} = 1} \| \mathbf {y} \| _ {2} = \sup _ {\omega} [ G (j \omega) ] \tag {8.35}$$

and we define

$$\| G \| _ {\infty} = \sup _ {\omega} \overline {{{\sigma}}} [ G (j \omega) ]. \tag {8.36}$$
