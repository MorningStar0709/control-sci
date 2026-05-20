$$
s \mathbf {I} - \mathbf {A} = \left[ \begin{array}{c c} s & 0 \\ 0 & s \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] = \left[ \begin{array}{c c} s & - 1 \\ 2 & s + 3 \end{array} \right]
$$

the inverse of $\left( s \mathbf { I } - \mathbf { A } \right)$ is given by

$$
\begin{array}{l} (s \mathbf {I} - \mathbf {A}) ^ {- 1} = \frac {1}{(s + 1) (s + 2)} \left[ \begin{array}{c c} s + 3 & 1 \\ - 2 & s \end{array} \right] \\ = \left[ \begin{array}{c c} \frac {s + 3}{(s + 1) (s + 2)} & \frac {1}{(s + 1) (s + 2)} \\ \frac {- 2}{(s + 1) (s + 2)} & \frac {s}{(s + 1) (s + 2)} \end{array} \right] \\ \end{array}
$$

Hence,

$$
\begin{array}{l} \boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t} = \mathcal {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right] \\ = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right] \\ \end{array}
$$

Noting that $\Phi ^ { - 1 } ( t ) = \Phi ( - t )$ we obtain the inverse of the state-transition matrix as follows:,

$$
\mathbf {\Phi} ^ {- 1} (t) = e ^ {- \mathbf {A} t} = \left[ \begin{array}{c c} 2 e ^ {t} - e ^ {2 t} & e ^ {t} - e ^ {2 t} \\ - 2 e ^ {t} + 2 e ^ {2 t} & - e ^ {t} + 2 e ^ {2 t} \end{array} \right]
$$

Solution of Nonhomogeneous State Equations. We shall begin by considering the scalar case

$$\dot {x} = a x + b u \tag {9-39}$$

Let us rewrite Equation (9–39) as

$$\dot {x} - a x = b u$$

Multiplying both sides of this equation by $e ^ { - a t }$ , we obtain

$$e ^ {- a t} [ \dot {x} (t) - a x (t) ] = \frac {d}{d t} [ e ^ {- a t} x (t) ] = e ^ {- a t} b u (t)$$

Integrating this equation between 0 and t gives

$$e ^ {- a t} x (t) - x (0) = \int_ {0} ^ {t} e ^ {- a \tau} b u (\tau) d \tau$$

or

$$x (t) = e ^ {a t} x (0) + e ^ {a t} \int_ {0} ^ {t} e ^ {- a \tau} b u (\tau) d \tau$$

The first term on the right-hand side is the response to the initial condition and the second term is the response to the input $u ( t )$ .

Let us now consider the nonhomogeneous state equation described by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} \tag {9-40}$$

where x = n-vector

$$\mathbf {u} = r \text {-vector}$$

A = n \* n constant matrix

B = n \* r constant matrix

By writing Equation (9–40) as

$$\dot {\mathbf {x}} (t) - \mathbf {A x} (t) = \mathbf {B u} (t)$$

and premultiplying both sides of this equation by $e ^ { - \mathbf { A } t }$ , we obtain

$$e ^ {- \mathbf {A} t} [ \dot {\mathbf {x}} (t) - \mathbf {A x} (t) ] = \frac {d}{d t} [ e ^ {- \mathbf {A} t} \mathbf {x} (t) ] = e ^ {- \mathbf {A} t} \mathbf {B u} (t)$$
