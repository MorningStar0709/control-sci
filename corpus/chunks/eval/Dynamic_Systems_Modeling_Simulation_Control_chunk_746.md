# Example C.1

Let us demonstrate the construction of an extremely simple Simulink model by beginning with a system that consists of a single linear I/O equation:

$$2 \ddot {y} + 6 \dot {y} + 3 0 y = 4 \dot {u} (t) + u (t) \tag {C.1}$$

with initial conditions y(0) = 0 and ẏ (0) = 0. The input is a step function, $u ( t ) = 0 . 2 U ( t )$ . Because this system has zero initial conditions, we may use a transfer function to represent the system dynamics:

$$\frac {Y (s)}{U (s)} = \frac {4 s + 1}{2 s ^ {2} + 6 s + 3 0} \tag {C.2}$$

The reader should recall that we can use transfer functions only in the cases where the dynamic system has zero initial conditions. Our first step is to choose an I/O block that represents the system dynamics. Highlighting the Continuous library in the Simulink Library Browser will present the standard model options for dynamic systems: transfer function, SSR, and the integrator block. Left-click and hold the Transfer Fcn block and “drag and drop” this icon to the blank Simulink template. Note that the Transfer Fcn block has a single input port and a single output port. Double clicking the Transfer Fcn block opens a dialog box which allows the user to set the desired numerator and denominator coefficients of the transfer function. Figure C.2 shows the dialog box with the numerator and denominator coefficients set as vectors in descending powers of s in order to match the transfer function in Eq. (C.2). Clicking OK will close the dialog box and display the numerical coefficients in the transfer function block.
