Equation 7.84 is somewhat inconvenient, because it requires differentiation of $\mathbf{x}_m$ . In practice, that is to be avoided if, for example, $\mathbf{x}_m$ is actually somewhat noisy. The problem is circumvented by defining $\psi = \widehat{\mathbf{x}}_u - G\mathbf{x}_m$ . We use $\widehat{\mathbf{x}}_u = \psi + G\mathbf{x}_m$ in Equation 7.84, and obtain

$$
\begin{array}{l} \dot {\psi} + G \dot {\mathbf {x}} _ {m} = A _ {u u} \psi + A _ {u u} G \mathbf {x} _ {m} + A _ {u m} \mathbf {x} _ {m} + B _ {u} \mathbf {u} + G \dot {\mathbf {x}} _ {m} \\ - G A _ {m m} \mathbf {x} _ {m} - G B _ {m} \mathbf {u} - G A _ {m u} \boldsymbol {\psi} - G A _ {m u} G \mathbf {x} _ {m} \\ \end{array}
$$

or, collecting terms,

$$
\begin{array}{l} \dot {\psi} = (A _ {u u} - G A _ {m u}) \psi + (A _ {u u} G + A _ {u m} - G A _ {m m} - G A _ {m u} G) \mathbf {x} _ {m} \\ + (B _ {u} - G B _ {m}) \mathbf {u}. \tag {7.85} \\ \end{array}
$$

The end product $\widehat{\mathbf{x}}_u$ is obtained from

$$\widehat {\mathbf {x}} _ {u} = \psi + G \mathbf {x} _ {m}. \tag {7.86}$$
