$$
\begin{array}{l} \mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B} \boldsymbol {\tau} \mathbf {v} d \tau \\ = e ^ {\mathbf {A} t} \mathbf {x} (0) + e ^ {\mathbf {A} t} \int_ {0} ^ {t} e ^ {- \mathbf {A} \tau} \tau d \tau \mathbf {B v} \\ = e ^ {\mathbf {A} t} \mathbf {x} (0) + e ^ {\mathbf {A} t} \left(\frac {\mathbf {I}}{2} t ^ {2} - \frac {2 \mathbf {A}}{3 !} t ^ {3} + \frac {3 \mathbf {A} ^ {2}}{4 !} t ^ {4} - \frac {4 \mathbf {A} ^ {3}}{5 !} t ^ {5} + \dots\right) \mathbf {B v} \\ \end{array}
$$

If A is nonsingular, then this last equation can be simplified to give

$$
\begin{array}{l} \mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + (\mathbf {A} ^ {- 2}) \left(e ^ {\mathbf {A} t} - \mathbf {I} - \mathbf {A} t\right) \mathbf {B v} \\ = e ^ {\mathbf {A} t} \mathbf {x} (0) + \left[ \mathbf {A} ^ {- 2} \left(e ^ {\mathbf {A} t} - \mathbf {I}\right) - \mathbf {A} ^ {- 1} t \right] \mathbf {B v} \tag {9-97} \\ \end{array}
$$

A–9–7. Obtain the response y(t) of the following system:

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {1} \end{array} \right] = \left[ \begin{array}{c c} - 1 & - 0. 5 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0. 5 \\ 0 \end{array} \right] u, \qquad \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \end{array} \right] \\ y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] \\ \end{array}
$$

where u(t) is the unit-step input occurring at $t = 0 ,$ , or

$$u (t) = 1 (t)$$

Solution. For this system

$$
\mathbf {A} = \left[ \begin{array}{c c} - 1 & - 0. 5 \\ 1 & 0 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0. 5 \\ 0 \end{array} \right]
$$

The state transition matrix $\mathbf { { \Phi } } \mathbf { d } \mathbf { p } ( t ) = e ^ { \mathbf { A } t }$ can be obtained as follows:

$$\boldsymbol {\Phi} (t) = e ^ {\mathbf {A} t} = \mathscr {L} ^ {- 1} \left[ (s \mathbf {I} - \mathbf {A}) ^ {- 1} \right]$$

Since
