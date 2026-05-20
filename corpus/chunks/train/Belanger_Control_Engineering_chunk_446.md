$$
\frac {d}{d t} \left[ \begin{array}{c} \Delta \widehat {\mathbf {x}} \\ - - \\ \widehat {\mathbf {u}} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} A & - B \\ - - & - - \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} \Delta \widehat {\mathbf {x}} \\ - - \\ \widehat {\mathbf {u}} ^ {*} \end{array} \right] + \left[ \begin{array}{c} B \\ - - \\ 0 \end{array} \right] \mathbf {u} + \left[ \begin{array}{c} G _ {1} \\ - - \\ G _ {2} \end{array} \right] (\Delta \mathbf {y} - C \Delta \widehat {\mathbf {x}})
\mathbf {u} = \widehat {\mathbf {u}} ^ {*} + \Delta \mathbf {u} = \widehat {\mathbf {u}} ^ {*} - K \Delta \widehat {\mathbf {x}}
$$

where K is a state feedback gain calculated for the linearized system. Insertion of the control law for u yields

$$\frac {d}{d t} \Delta \widehat {\mathbf {x}} = A \Delta \widehat {\mathbf {x}} - B \widehat {\mathbf {u}} ^ {*} + B (\widehat {\mathbf {u}} ^ {*} - K \Delta \widehat {\mathbf {x}}) + G _ {1} (\Delta \mathbf {y} - C \Delta \widehat {\mathbf {x}})$$

or

$$\frac {d}{d t} \Delta \widehat {\mathbf {x}} = (A - B K - G _ {1} C) \Delta \widehat {\mathbf {x}} + G _ {1} \Delta \mathbf {y} \tag {7.98}$$

and

$$\frac {d}{d t} \widehat {\mathbf {u}} ^ {*} = - G _ {2} C \Delta \widehat {\mathbf {x}} + G _ {2} \Delta \mathbf {y} \tag {7.99}$$

with the control given by

$$\mathbf {u} = \widehat {\mathbf {u}} ^ {*} - K \Delta \widehat {\mathbf {x}}. \tag {7.100}$$

In matrix form, the controller equations are

$$
\begin{array}{l} \frac {d}{d t} \left[ \begin{array}{c} \Delta \widehat {\mathbf {x}} \\ - \\ \widehat {\mathbf {u}} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} A - B K - G _ {1} C & 0 \\ - G _ {2} C & 0 \end{array} \right] \left[ \begin{array}{c} \Delta \widehat {\mathbf {x}} \\ - \\ \widehat {\mathbf {u}} ^ {*} \end{array} \right] + \left[ \begin{array}{c} G _ {1} \\ - \\ G _ {2} \end{array} \right] \Delta \mathbf {y} \\ \mathbf {u} = \left[ \begin{array}{c c c c} & - K & & I \end{array} \right] \left[ \begin{array}{c} \Delta \widehat {\mathbf {x}} \\ - - \\ \widehat {\mathbf {u}} ^ {*} \end{array} \right]. \tag {7.101} \\ \end{array}
$$

The controller “A matrix” is block triangular, so its eigenvalues are those of the diagonal blocks, the $n \times n$ matrix $A - BK - G_{1}C$ and the $r \times r$ zero matrix. Because of the latter, the controller has r integrations, so the system is of Type 1.

The procedure is summarized as follows:

1. Design a state feedback control law for the incremental linear system.   
2. Design an observer (full- or reduced-order) for the system, augmented by the equation for the unknown steady-state input, as in Equations 7.96 and 7.97.
