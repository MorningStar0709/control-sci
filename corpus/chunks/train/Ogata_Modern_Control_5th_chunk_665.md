$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u
$$

where u(t) is the unit-step function occurring at t=0, or

$$u (t) = 1 (t)$$

For this system,

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

The state-transition matrix $\mathbf { \Phi } \mathbf { d } \mathbf { p } ( t ) = e ^ { \mathbf { A } t }$ was obtained in Example 9–5 as

$$
\boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t} = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right]
$$

The response to the unit-step input is then obtained as

$$
\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} \left[ \begin{array}{c c} 2 e ^ {- (t - \tau)} - e ^ {- 2 (t - \tau)} & e ^ {- (t - \tau)} - e ^ {- 2 (t - \tau)} \\ - 2 e ^ {- (t - \tau)} + 2 e ^ {- 2 (t - \tau)} & - e ^ {- (t - \tau)} + 2 e ^ {- 2 (t - \tau)} \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] [ 1 ] d \tau
$$

or

$$
\left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right] \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] + \left[ \begin{array}{c} \frac {1}{2} - e ^ {- t} + \frac {1}{2} e ^ {- 2 t} \\ e ^ {- t} - e ^ {- 2 t} \end{array} \right]
$$

If the initial state is zero, or x(0)=0, then x(t) can be simplified to

$$
\left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] = \left[ \begin{array}{c} \frac {1}{2} - e ^ {- t} + \frac {1}{2} e ^ {- 2 t} \\ e ^ {- t} - e ^ {- 2 t} \end{array} \right]
$$
