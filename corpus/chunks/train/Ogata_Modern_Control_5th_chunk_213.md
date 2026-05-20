When step commands have left-hand arguments such as

$$[ y, x, t ] = \text { step } (\text { num }, \text { den }, t)[ y, x, t ] = \operatorname{step} (A, B, C, D, i u)[ \mathrm{y}, \mathrm{x}, \mathrm{t} ] = \operatorname{step} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{iu}, \mathrm{t}) \tag {5-36}$$

no plot is shown on the screen. Hence it is necessary to use a plot command to see the response curves. The matrices y and x contain the output and state response of the system, respectively, evaluated at the computation time points t. (y has as many columns as outputs and one row for each element in t. x has as many columns as states and one row for each element in t.)

Note in Equation (5–36) that the scalar iu is an index into the inputs of the system and specifies which input is to be used for the response, and t is the user-specified time. If the system involves multiple inputs and multiple outputs, the step command, such as given by Equation (5–36), produces a series of step-response plots, one for each input and output combination of

$$
\begin{array}{l} \dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} \\ \mathbf {y} = \mathbf {C x} + \mathbf {D u} \\ \end{array}
$$

(For details, see Example 5–3.)

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & - 1 \\ 6. 5 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \\ \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right] \\ \end{array}
$$

Obtain the unit-step response curves.

Although it is not necessary to obtain the transfer-matrix expression for the system to obtain the unit-step response curves with MATLAB, we shall derive such an expression for reference. For the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

the transfer matrix G(s) is a matrix that relates Y(s) and U(s) as follows:

$$\mathbf {Y} (s) = \mathbf {G} (s) \mathbf {U} (s)$$
