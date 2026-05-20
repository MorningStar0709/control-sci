$$
\begin{array}{l} e ^ {A t} \mathbf {v} _ {i} = \mathbf {v} _ {i} + s _ {i} \mathbf {v} _ {i} t + \frac {1}{2 !} s _ {i} ^ {2} \mathbf {v} _ {i} t ^ {2} + \dots + \frac {1}{k !} s _ {i} ^ {k} \mathbf {v} _ {i} t ^ {k} + \dots \\ = \left(1 + s _ {i} t + \frac {1}{2 !} s _ {i} ^ {2} t ^ {2} + \dots + \frac {1}{k !} s _ {i} ^ {k} t ^ {k} + \dots\right) \mathbf {v} _ {i} \\ = e ^ {s _ {i} t} \mathbf {v} _ {i} \tag {3.13} \\ \end{array}
$$

so that $\mathbf{v}_i$ is an eigenvector of the matrix $e^{At}$ , with eigenvalue $e^{s_i t}$ .

The significance of this mathematical fact is this: the zero-input response to an initial state $x_{0} = v_{i}$ is $\mathbf{x}(t) = e^{s_{i}t} \mathbf{v}_{i}$ . Only the mode $s_{i}$ is excited. The solution $\mathbf{x}(t)$ is a vector whose direction, defined by $v_{i}$ , is constant in time, and whose magnitude is $|e^{s_{i}t}|$ times that of $x_{0}$ . The eigenvectors are called the modal vectors.

![](image/dad60f69276b4653d0ee858814cf6e68142b1425fedfa0b6af924fee64494f7d.jpg)
