If the eigenvalues $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ of the matrix A are distinct, than $\Phi ( t )$ will contain the n exponentials

$$e ^ {\lambda_ {1} t}, e ^ {\lambda_ {2} t}, \dots , e ^ {\lambda_ {n} t}$$

In particular, if the matrix A is diagonal, then

$$
\boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t} = \left[ \begin{array}{c c c c c c} e ^ {\lambda_ {1} t} & & & & & 0 \\ & e ^ {\lambda_ {2} t} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & e ^ {\lambda_ {n} t} \end{array} \right] \quad (\mathbf {A}: \text { diagonal })
$$

If there is a multiplicity in the eigenvalues—for example, if the eigenvalues of A are

$$\lambda_ {1}, \lambda_ {1}, \lambda_ {1}, \lambda_ {4}, \lambda_ {5}, \dots , \lambda_ {n},$$

then $\Phi ( t )$ will contain, in addition to the exponentials $e ^ { \lambda _ { 1 } t } , e ^ { \lambda _ { 4 } t } , e ^ { \lambda _ { 5 } t } , \ldots , e ^ { \lambda _ { n } t }$ terms like, $t e ^ { \lambda _ { 1 } t }$ and $\dot { t } ^ { 2 } e ^ { \lambda _ { 1 } t }$ t.

Properties of State-Transition Matrices. We shall now summarize the important properties of the state-transition matrix $\Phi ( t )$ For the time-invariant system.

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}$$

for which

$$\boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t}$$

we have the following:

1. $\Phi ( 0 ) = e ^ { \mathbf { A } 0 } = \mathbf { I }$   
$2 . \Phi ( t ) = e ^ { \mathbf { A } t } = \left( e ^ { - \mathbf { A } t } \right) ^ { - 1 } = \left[ \Phi ( - t ) \right] ^ { - 1 } \mathrm { o r } \Phi ^ { - 1 } ( t ) = \Phi ( - t )$   
3. $\Phi \bigl ( t _ { 1 } + t _ { 2 } \bigr ) = e ^ { \mathbf { A } \left( t _ { 1 } + t _ { 2 } \right) } = e ^ { \mathbf { A } t _ { 1 } } e ^ { \mathbf { A } t _ { 2 } } = \Phi \bigl ( t _ { 1 } \bigr ) \Phi \bigl ( t _ { 2 } \bigr ) = \Phi \bigl ( t _ { 2 } \bigr ) \Phi \bigl ( t _ { 1 } \bigr )$   
4. $\bigl [ \Phi ( t ) \bigr ] ^ { n } = \Phi ( n t )$   
5. At2 - t1B At1 - t0B = At2 - t0B = At1 - t0B At2 - t1B

EXAMPLE 9–5 Obtain the state-transition matrix $\Phi ( t )$ of the following system:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

Obtain also the inverse of the state-transition matrix, $\Phi ^ { - 1 } ( t )$ .

For this system,

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right]
$$

The state-transition matrix $\Phi ( t )$ is given by

$$\boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t} = \mathscr {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right]$$

Since
