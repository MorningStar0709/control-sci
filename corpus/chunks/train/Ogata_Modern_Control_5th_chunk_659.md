converges absolutely for all finite t. (Hence, computer calculations for evaluating the elements of $e ^ { \mathbf { A } t }$ by using the series expansion can be easily carried out.)

Because of the convergence of the infinite series $\textstyle \sum _ { k = 0 } ^ { \infty } \mathbf { A } ^ { k } t ^ { k } / k !$ the series can be, differentiated term by term to give

$$
\begin{array}{l} \frac {d}{d t} e ^ {\mathbf {A} t} = \mathbf {A} + \mathbf {A} ^ {2} t + \frac {\mathbf {A} ^ {3} t ^ {2}}{2 !} + \dots + \frac {\mathbf {A} ^ {k} t ^ {k - 1}}{(k - 1) !} + \dots \\ = \mathbf {A} \left[ \mathbf {I} + \mathbf {A} t + \frac {\mathbf {A} ^ {2} t ^ {2}}{2 !} + \dots + \frac {\mathbf {A} ^ {k - 1} t ^ {k - 1}}{(k - 1) !} + \dots \right] = \mathbf {A} e ^ {\mathbf {A} t} \\ = \left[ \mathbf {I} + \mathbf {A} t + \frac {\mathbf {A} ^ {2} t ^ {2}}{2 !} + \dots + \frac {\mathbf {A} ^ {k - 1} t ^ {k - 1}}{(k - 1) !} + \dots \right] \mathbf {A} = e ^ {\mathbf {A} t} \mathbf {A} \\ \end{array}
$$

The matrix exponential has the property that

$$e ^ {\mathbf {A} (t + s)} = e ^ {\mathbf {A} t} e ^ {\mathbf {A} s}$$

This can be proved as follows:

$$
\begin{array}{l} e ^ {\mathbf {A} t} e ^ {\mathbf {A} s} = \left(\sum_ {k = 0} ^ {\infty} \frac {\mathbf {A} ^ {k} t ^ {k}}{k !}\right) \left(\sum_ {k = 0} ^ {\infty} \frac {\mathbf {A} ^ {k} s ^ {k}}{k !}\right) \\ = \sum_ {k = 0} ^ {\infty} \mathbf {A} ^ {k} \left(\sum_ {i = 0} ^ {\infty} \frac {t ^ {i} s ^ {k - i}}{i ! (k - i) !}\right) \\ = \sum_ {k = 0} ^ {\infty} \mathbf {A} ^ {k} \frac {(t + s) ^ {k}}{k !} \\ = e ^ {\mathbf {A} (t + s)} \\ \end{array}
$$

In particular, if s=–t, then

$$e ^ {\mathbf {A} t} e ^ {- \mathbf {A} t} = e ^ {- \mathbf {A} t} e ^ {\mathbf {A} t} = e ^ {\mathbf {A} (t - t)} = \mathbf {I}$$

Thus, the inverse of $e ^ { \mathbf { A } t }$ is $e ^ { - \mathbf { A } t }$ Since the inverse of. $e ^ { \mathbf { A } t }$ always exists, $e ^ { \mathbf { A } t }$ is nonsingular. It is very important to remember that

$$
\begin{array}{l} e ^ {(\mathbf {A} + \mathbf {B}) t} = e ^ {\mathbf {A} t} e ^ {\mathbf {B} t}, \quad \text { if } \mathbf {A B} = \mathbf {B A} \\ e ^ {(\mathbf {A} + \mathbf {B}) t} \neq e ^ {\mathbf {A} t} e ^ {\mathbf {B} t}, \quad \text { if } \mathbf {A B} \neq \mathbf {B A} \\ \end{array}
$$

To prove this, note that
