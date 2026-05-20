$$
\begin{array}{l} g (1) - g (0) = \int_ {0} ^ {1} g ^ {\prime} (s) d s \\ = \int_ {0} ^ {1} D f (x + s (y - x)) (y - x) d s \\ \end{array}
$$

which completes the proof for $p = 1$ .

(b) Consider the function $g ( s ) = f ( x + s ( y - x ) )$ where $f : \mathbb { R } ^ { n }  \mathbb { R } .$ Then

$$\frac {d}{d s} \left[ g ^ {\prime} (s) (1 - s) + g (s) \right] = g ^ {\prime \prime} (s) (1 - s)$$

Integrating from 0 to 1 yields

$$g (1) - g (0) - g ^ {\prime} (0) = \int_ {0} ^ {1} (1 - s) g ^ {\prime \prime} (s) d s$$

But $g ^ { \prime \prime } ( s ) = ( y - x ) ^ { \prime } f _ { x x } ( x + s ( y - x ) ) ( y - x )$ so that the last equation yields

$$f (y) - f (x) = f _ {x} (x) (y - x) + \int_ {0} ^ {1} (1 - s) (y - x) ^ {\prime} f _ {x x} (x + s (y - x)) (y - x) d s$$

when $g ( s )$ is replaced by $f ( x + s ( y - x ) )$ .

Finally, we define directional derivatives which may exist even when a function fails to have a derivative. Let $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ . We define the directional derivative of f at a point $\boldsymbol { \hat { x } } \in \mathbb { R } ^ { n }$ in the direction $h \in \mathbb { R } ^ { n } ( h \neq$ 0) by

$$d f (\hat {x}; h) := \lim _ {t \searrow 0} \frac {f (\hat {x} + t h) - f (\hat {x})}{t}$$

if this limit exists (note that $t > 0$ is required). The directional derivative is positively homogeneous, i.e., $d f ( x ; \lambda h ) ~ = ~ \lambda d f ( x ; h )$ for all $\lambda > 0$ .

Not all the functions we discuss are differentiable everywhere. Examples include the max function $\psi ( \cdot )$ defined by $\psi ( x ) : = \mathrm { m a x } _ { i } \{ f ^ { i } ( x ) ~ |$ | $i \in I \}$ where each function $f ^ { i } : \mathbb { R } ^ { n }  \mathbb { R }$ is continuously differentiable everywhere. The function $\psi ( \cdot )$ is not differentiable at those x for which the active set $I ^ { 0 } ( x ) : = \{ i \in I | f ^ { i } ( x ) = \psi ( x ) \}$ has more than one element. The directional derivative $d ( x ; h )$ exists for all $x , h$ in $\mathbb { R } ^ { n }$ , however, and is given by

$$d \psi (x; h) = \max _ {i} \left\{d f _ {i} (x; h) \mid i \in I ^ {0} (x) \right\} = \max _ {i} \left\{\langle \nabla f _ {i} (x), h \rangle \mid i \in I ^ {0} (x) \right\}$$

When, as in this example, the directional derivative exists for all $x , h$ in $\mathbb { R } ^ { n }$ we can define a generalization, called the subgradient, of the conventional gradient. Suppose that $f : \mathbb { R } ^ { n }$ → R has a directional derivative for all $x , h$ in $\mathbb { R } ^ { n }$ . The $f ( \cdot )$ has a subgradient $\partial f ( \cdot )$ defined by

$$\partial \psi (x) := \{g \in \mathbb {R} ^ {n} \mid d f (x; h) \geq \langle g, h \rangle \forall h \in \mathbb {R} ^ {n} \}$$
