The foregoing also applies to complex frequencies, the difference being that it is impossible to have a complex vector as an initial state. It is known that, for real matrices, both eigenvalues and eigenvectors occur in complex conjugate pairs. A real initial state, $x_{0}$ , is formed from pairs of complex conjugate eigenvectors $v_{i}$ and $v_{i}^{*}$ corresponding to complex conjugate modes $s_{i}$ and $s_{i}^{*}$ , as follows:

$$\mathbf {x} _ {0} = \alpha \mathbf {v} _ {i} + \alpha^ {*} \mathbf {v} _ {i} ^ {*} = 2 R e (\alpha \mathbf {v} _ {i}) \tag {3.14}$$

with $\alpha$ a complex constant. By zero-input linearity, the response is

$$
\begin{array}{l} \mathbf {x} (t) = e ^ {A t} \alpha \mathbf {v} _ {i} + e ^ {A t} \alpha^ {*} \mathbf {v} _ {i} ^ {*} \\ = \alpha e ^ {s _ {i} t} \mathbf {v} _ {i} + \alpha^ {*} e ^ {s _ {i} ^ {*} t} \mathbf {v} _ {i} ^ {*} \\ = 2 R e \left(\alpha e ^ {s _ {i} t} \mathbf {v} _ {i}\right). \tag {3.15} \\ \end{array}
$$

For $s_{i} = \sigma_{i} + j\omega_{i}$ , $e^{s_{i}t}$ yields sinusoids of frequency $\omega_{i}$ , multiplied by the exponential $e^{\sigma_{i}t}$ . Since $\mathbf{v}_{i} = Re(\mathbf{v}_{i}) + jIm(\mathbf{v}_{i})$ , $\mathbf{x}(t)$ is a linear combination of the real and imaginary parts; $\mathbf{x}(t)$ does not move along one vector but lies in the plane described by the two vectors $Re(\mathbf{v}_{i})$ and $Im(\mathbf{v}_{i})$ .
