$$
\begin{array}{l} e ^ {\mathbf {A} t} = \frac {1}{2} (\mathbf {A} + 2 \mathbf {I} - \mathbf {A} e ^ {- 2 t}) \\ = \frac {1}{2} \left\{\left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right] + \left[ \begin{array}{c c} 2 & 0 \\ 0 & 2 \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 2 \end{array} \right] e ^ {- 2 t} \right\} \\ = \left[ \begin{array}{c c} 1 & \frac {1}{2} \big (1 - e ^ {- 2 t} \big) \\ 0 & e ^ {- 2 t} \end{array} \right] \\ \end{array}
$$

An alternative approach is to use Equation (9–48). We first determine $\alpha _ { 0 } ( t )$ and $\alpha _ { 1 } ( t )$ from

$$\alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {1} = e ^ {\lambda_ {1} t}\alpha_ {0} (t) + \alpha_ {1} (t) \lambda_ {2} = e ^ {\lambda_ {2} t}$$

Since $\lambda _ { 1 } = 0$ and $\lambda _ { 2 } = - 2 .$ , the last two equations become

$$\alpha_ {0} (t) = 1\alpha_ {0} (t) - 2 \alpha_ {1} (t) = e ^ {- 2 t}$$

Solving for $\alpha _ { 0 } ( t )$ and $\alpha _ { 1 } ( t )$ gives

$$\alpha_ {0} (t) = 1, \quad \alpha_ {1} (t) = \frac {1}{2} \left(1 - e ^ {- 2 t}\right)$$

Then $e ^ { \mathbf { A } t }$ can be written as

$$
e ^ {\mathbf {A} t} = \alpha_ {0} (t) \mathbf {I} + \alpha_ {1} (t) \mathbf {A} = \mathbf {I} + \frac {1}{2} \big (1 - e ^ {- 2 t} \big) \mathbf {A} = \left[ \begin{array}{c c} 1 & \frac {1}{2} \big (1 - e ^ {- 2 t} \big) \\ 0 & e ^ {- 2 t} \end{array} \right]
$$

Linear Independence of Vectors. The vectors $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { n }$ are said to be linearly independent if

$$c _ {1} \mathbf {x} _ {1} + c _ {2} \mathbf {x} _ {2} + \dots + c _ {n} \mathbf {x} _ {n} = \mathbf {0}$$

where $c _ { 1 } , c _ { 2 } , \ldots , c _ { n }$ are constants, implies that

$$c _ {1} = c _ {2} = \dots = c _ {n} = 0$$

Conversely, the vectors $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { n }$ are said to be linearly dependent if and only if $\mathbf { x } _ { i }$ can be expressed as a linear combination of $\mathbf { x } _ { j } \left( j = 1 , 2 , \ldots , n ; j \neq i \right)$ , or

$$\mathbf {x} _ {i} = \sum_ {\stackrel {j = 1} {j \neq i}} ^ {n} c _ {j} \mathbf {x} _ {j}$$

for some set of constants $c _ { j } .$ . This means that if $\mathbf { X } _ { i }$ can be expressed as a linear combination of the other vectors in the set, it is linearly dependent on them or it is not an independent member of the set.
