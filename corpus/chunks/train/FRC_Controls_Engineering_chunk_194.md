# Theorem 7.3.1 — Linear system zero-order hold.

$$\mathbf {A} _ {d} = e ^ {\mathbf {A} _ {c} T} \tag {7.4}\mathbf {B} _ {d} = \int_ {0} ^ {T} e ^ {\mathbf {A} _ {c} \tau} d \tau \mathbf {B} _ {c} = \mathbf {A} _ {c} ^ {- 1} (\mathbf {A} _ {d} - \mathbf {I}) \mathbf {B} _ {c} \tag {7.5}\mathbf {C} _ {d} = \mathbf {C} _ {c} \tag {7.6}\mathbf {D} _ {d} = \mathbf {D} _ {c} \tag {7.7}\mathbf {Q} _ {d} = \int_ {\tau = 0} ^ {T} e ^ {\mathbf {A} _ {c} \tau} \mathbf {Q} _ {c} e ^ {\mathbf {A} _ {c} ^ {\top} \tau} d \tau \tag {7.8}\mathbf {R} _ {d} = \frac {1}{T} \mathbf {R} _ {c} \tag {7.9}$$

where subscripts c and d denote matrices for the continuous or discrete systems respectively, $T$ is the sample period of the discrete system, and $e ^ { \mathbf { A } _ { c } T }$ is the matrix exponential of $\mathbf { A } _ { c } T$ .

See appendix D.1 for derivations.

$\mathbf { A } _ { d }$ and $\mathbf { B } _ { d }$ can be computed in one step as

$$
e ^ {\left[ \begin{array}{c c} \mathbf {A} _ {c c} & \mathbf {B} _ {c c} \\ \mathbf {0} & \mathbf {0} \end{array} \right] ^ {T}} = \left[ \begin{array}{c c} \mathbf {A} _ {d c c} & \mathbf {B} _ {d c c} \\ \mathbf {0} & \mathbf {I} \end{array} \right]
$$

and $\mathbf { Q } _ { d }$ can be computed as

$$
\Phi = e ^ {\left[ \begin{array}{c c} - \mathbf {A} _ {c c} & \mathbf {Q} _ {c c} \\ \mathbf {0} & \mathbf {A} _ {c c} ^ {\top} \end{array} \right] ^ {T}} = \left[ \begin{array}{c c} - \mathbf {A} _ {d c c} & \mathbf {A} _ {d c c} ^ {- 1} \mathbf {Q} _ {d c c} \\ \mathbf {0} & \mathbf {A} _ {d c c} ^ {\top} \end{array} \right]
$$

where $\mathbf { Q } _ { d } = \Phi _ { 2 , 2 } ^ { \mathsf { T } } \Phi _ { 1 , 2 } . \mathsf {  { [ 5 ] } }$

To see why $\mathbf { R } _ { c }$ is being divided by T , consider the discrete white noise sequence $\mathbf { v } _ { k }$ and the (non-physically realizable) continuous white noise process v. Whereas $\mathbf { R } _ { d , k } =$ $E [ \mathbf { v } _ { k } \mathbf { v } _ { k } ^ { \mathsf { T } } ]$ is a covariance matrix, ${ \bf R } _ { c } ( t )$ defined by $E [ { \bf v } ( t ) { \bf v } ^ { \top } ( \tau ) ] = { \bf R } _ { c } ( t ) \delta ( t - \tau )$ is a spectral density matrix (the Dirac function $\delta ( t - \tau )$ has units of $1 / \mathrm { s e c } )$ . The covariance matrix ${ \bf R } _ { c } ( t ) \delta ( t - \tau )$ has infinite-valued elements. The discrete white noise sequence can be made to approximate the continuous white noise process by shrinking the pulse lengths (T ) and increasing their amplitude, such that $\mathbf { R } _ { d } \to { \frac { 1 } { T } } \mathbf { R } _ { c }$ .

That is, in the limit as $T  0$ , the discrete noise sequence tends to one of infinitevalued pulses of zero duration such that the area under the “impulse” autocorrelation function is $\mathbf { R } _ { d } T$ . This is equal to the area $\mathbf { R } _ { c }$ under the continuous white noise impulse autocorrelation function.
