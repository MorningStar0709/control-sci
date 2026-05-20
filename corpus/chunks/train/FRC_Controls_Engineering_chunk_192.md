<table><tr><td>Method</td><td>Conversion to  $\mathbf{A}_{d}$ </td></tr><tr><td>Zero-order hold</td><td> $e^{\mathbf{A}_{c}T}$ </td></tr><tr><td>Bilinear</td><td> $\left( \mathbf{I} + \frac{1}{2}\mathbf{A}_{c}T \right) \left( \mathbf{I} - \frac{1}{2}\mathbf{A}_{c}T \right)^{-1}$ </td></tr><tr><td>Backward Euler</td><td> $(\mathbf{I} - \mathbf{A}_{c}T)^{-1}$ </td></tr><tr><td>Forward Euler</td><td> $\mathbf{I} + \mathbf{A}_{c}T$ </td></tr></table>

Table 7.2: Discretization methods (matrix case). The zero-order hold discretization method is exact.

<table><tr><td>Method</td><td>Taylor series expansion</td></tr><tr><td>Zero-order hold</td><td> $\mathbf{I} + \mathbf{A}_c T + \frac{1}{2} \mathbf{A}_c^2 T^2 + \frac{1}{6} \mathbf{A}_c^3 T^3 + \ldots$ </td></tr><tr><td>Bilinear</td><td> $\mathbf{I} + \mathbf{A}_c T + \frac{1}{2} \mathbf{A}_c^2 T^2 + \frac{1}{4} \mathbf{A}_c^3 T^3 + \ldots$ </td></tr><tr><td>Backward Euler</td><td> $\mathbf{I} + \mathbf{A}_c T + \mathbf{A}_c^2 T^2 + \mathbf{A}_c^3 T^3 + \ldots$ </td></tr><tr><td>Forward Euler</td><td> $\mathbf{I} + \mathbf{A}_c T$ </td></tr></table>

Table 7.3: Taylor series expansions of discretization methods (matrix case). The zeroorder hold discretization method is exact.

uses an exponential.

$$
\begin{array}{l} \dot {x} = a x \\ \frac {d x}{d t} = a x (t) \\ d x = a x (t) d t \\ \frac {1}{x (t)} d x = a d t \\ \int_ {0} ^ {t} \frac {1}{x (t)} d x = \int_ {0} ^ {t} a d t \\ \ln (x (t)) | _ {0} ^ {t} = a t | _ {0} ^ {t} \\ \ln (x (t)) - \ln (x (0)) = a t - a \cdot 0 \\ \ln (x (t)) - \ln (x _ {0}) = a t \\ \ln \left(\frac {x (t)}{x _ {0}}\right) = a t \\ \end{array}

\begin{array}{l} \frac {x (t)}{x _ {0}} = e ^ {a t} \\ x (t) = e ^ {a t} x _ {0} \\ \end{array}
$$

This solution generalizes via the matrix exponential to the set of differential equations $\dot { \mathbf { x } } = \mathbf { A } \mathbf { x } + \mathbf { B } \mathbf { u }$ we use to describe systems.[4]

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} _ {0} + \mathbf {A} ^ {- 1} (e ^ {\mathbf {A} t} - \mathbf {I}) \mathbf {B u}$$

where $\mathbf { x } _ { \mathrm { 0 } }$ contains the initial conditions and u is the constant input from time 0 to t. If the initial state is the current system state, then we can describe the system’s state over time as

$$\mathbf {x} _ {k + 1} = e ^ {\mathbf {A} T} \mathbf {x} _ {k} + \mathbf {A} ^ {- 1} (e ^ {\mathbf {A} T} - \mathbf {I}) \mathbf {B} \mathbf {u} _ {k}$$

or more compactly,

$$\mathbf {x} _ {k + 1} = \mathbf {A} _ {d} \mathbf {x} _ {k} + \mathbf {B} _ {d} \mathbf {u} _ {k}$$

where T is the time between samples $\mathbf { x } _ { k }$ and $\mathbf { x } _ { k + 1 }$ . Theorem 7.3.1 has more efficient ways to compute $\mathbf { A } _ { d }$ and $\mathbf { B } _ { d }$ .
