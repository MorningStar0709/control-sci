# 3.1 Descriptions of Linear Dynamical Systems

Let a finite dimensional linear time invariant (FDLTI) dynamical system be described by the following linear constant coefficient differential equations:

$$\dot {x} = A x + B u, \quad x (t _ {0}) = x _ {0} \tag {3.1}y = C x + D u, \tag {3.2}$$

where $\ b { x } ( t ) \in \mathbb { R } ^ { n }$ is called the system state, $x ( t _ { 0 } )$ is called the initial condition of the system, $u ( t ) \in \mathbb { R } ^ { m }$ is called the system input, and $\ b { y } ( t ) \in \mathbb { R } ^ { p }$ is the system output. The $A , B , C ,$ and D are appropriately dimensioned real constant matrices. A dynamical system with single-input $( m = 1 )$ and single-output $( p = 1 )$ is called a SISO (singleinput and single-output) system; otherwise it is called a MIMO (multiple-input and multiple-output) system. The corresponding transfer matrix from u to y is defined as

$$Y (s) = G (s) U (s),$$

where $U ( s )$ and $Y ( s )$ are the Laplace transforms of $u ( t )$ and y(t) with zero initial condition $( x ( 0 ) = 0 )$ . Hence, we have

$$G (s) = C (s I - A) ^ {- 1} B + D.$$

Note that the system equations (3.1) and (3.2) can be written in a more compact matrix form:

$$
{\left[ \begin{array}{l} \dot {x} \\ y \end{array} \right]} = {\left[ \begin{array}{l l} A & B \\ C & D \end{array} \right]} {\left[ \begin{array}{l} x \\ u \end{array} \right]}.
$$

To expedite calculations involving transfer matrices, we shall use the following notation:

$$
\left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right] := C (s I - A) ^ {- 1} B + D.
$$

In Matlab the system can also be written in the packed form using the command

$\gg { \bf G } { = } \mathrm { { \bf p c k } } ( { \bf A } , { \bf B } , { \bf C } , { \bf D } )$ % pack the realization in partitioned form   
seesys(G) % display G in partitioned format   
$\gg [ \mathbf { A } , \mathbf { B } , \mathbf { C } , \mathbf { D } ] { = } \mathbf { u n p c k } ( \mathbf { G } )$ % unpack the system matrix

Note that

$$
\left[ \begin{array}{c c} A & B \\ C & D \end{array} \right]
$$

is a real block matrix, not a transfer function.
