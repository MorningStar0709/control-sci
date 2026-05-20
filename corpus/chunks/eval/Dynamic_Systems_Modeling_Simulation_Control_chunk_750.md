# Example C.2

Consider a second-order system governed by the linear I/O equation

$$2 \ddot {z} + 8 \dot {z} + 4 0 z = 1. 4 u (t) \tag {C.3}$$

The system’s initial conditions are z(0) = −0.02 and $\dot { z } ( 0 ) = 0 . 1$ , and the input is a sinusoidal function, $u ( t ) =$ 0.8 sin 12t. Because this system has nonzero initial conditions, we cannot use a transfer function for the system dynamics. We have two options for representing the system dynamics when the initial conditions are nonzero: (1) SSR and (2) the integrator-block method. We solve this problem using the SSR approach and show the integrator-block method in the next example.

The reader can verify that a possible SSR of the system defined by Eq. (C.3) is

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 0 & - 4 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 0. 7 \end{array} \right] u \tag {C.4}

\mathbf {y} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 0 \end{array} \right] u \tag {C.5}
$$

where the state variables are $x _ { 1 } = z$ and $x _ { 2 } = \dot { z } ,$ , and the two output variables are $y _ { 1 } = x _ { 1 } = z$ and $y _ { 2 } = x _ { 2 } = \dot { z } .$ . Note that we have chosen to set the output vector y equal to the state vector x, and hence the output matrix C is the identity matrix. The Simulink model is constructed by dragging the State-Space block from the Continuous library to a new working template. The reader should note that while the State-Space block has one input port and one output port these ports can pass scalar or vector signals. In this case, we have a single input u and a vector output y. Double clicking the State-Space block opens a dialog box where the user can enter the appropriate numerical values for state-space matrices A, B, C, and D (see Fig. C.5). Note that we have used the MATLAB commands eye(2) for the $2 \times 2$ identity matrix C and zeros(2,1) for the $2 \times 1$ null matrix D. The reader should carefully note that even though the direct-link term is zero in the output equation (C.5), we must enter the D matrix as a $2 \times 1$ column vector of zeros. Failure to heed the proper SSR matrix dimensions is a common error of beginning Simulink users. The initial conditions for the state vector, $\mathbf { x } ( 0 ) = \left[ z ( 0 ) \ \dot { z } ( 0 ) \right] ^ { T }$ , are also entered in this dialog box shown in Fig. C.5.
