# EXAMPLE 10–4

Design a type 1 servo system when the plant transfer function has an integrator. Assume that the plant transfer function is given by

$$\frac {Y (s)}{U (s)} = \frac {1}{s (s + 1) (s + 2)}$$

The desired closed-loop poles are $s = - 2 \pm j 2 { \sqrt { 3 } }$ and s=–10. Assume that the system configuration is the same as that shown in Figure 10–4 and the reference input r is a step function. Obtain the unit-step response of the designed system.

Define state variables $x _ { 1 } , x _ { 2 } .$ , and $x _ { 3 }$ as follows:

$$x _ {1} = yx _ {2} = \dot {x} _ {1}x _ {3} = \dot {x} _ {2}$$

Then the state-space representation of the system becomes

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-26}y = \mathbf {C x} \tag {10-27}$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & - 2 & - 3 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right]
$$

Referring to Figure 10–4 and noting that n=3, the control signal u is given by

$$u = - \left(k _ {2} x _ {2} + k _ {3} x _ {3}\right) + k _ {1} (r - x _ {1}) = - \mathbf {K} \mathbf {x} + k _ {1} r \tag {10-28}$$

where

$$
\mathbf {K} = \left[ \begin{array}{c c c} k _ {1} & k _ {2} & k _ {3} \end{array} \right]
$$

The state-feedback gain matrix K can be obtained easily with MATLAB. See MATLAB Program 10–4.

<table><tr><td>MATLAB Program 10-4</td></tr><tr><td>A = [0 1 0;0 0 0 1;0 -2 -3];B = [0;0;1];J = [-2+j*2*sqrt(3) -2-j*2*sqrt(3) -10];K = acker(A,B,J)K =160.0000 54.0000 11.0000</td></tr></table>

The state feedback gain matrix K is thus

$$\mathrm{K} = [ 1 6 0 \quad 5 4 \quad 1 1 ]$$

Unit-Step Response of the Designed System: The unit-step response of the designed system can be obtained as follows:

Since

$$
\mathbf {A} - \mathbf {B K} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & - 2 & - 3 \end{array} \right] - \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right] [ 1 6 0 \quad 5 4 \quad 1 1 ] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 6 0 & - 5 6 & - 1 4 \end{array} \right]
$$

from Equation (10–22) the state equation for the designed system is

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 6 0 & - 5 6 & - 1 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 6 0 \end{array} \right] r \tag {10-29}
$$

and the output equation is

$$
y = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] \tag {10-30}
$$

Solving Equations (10–29) and (10–30) for $y ( t )$ when r is a unit-step function gives the unit-step response curve $y ( t )$ versus t. MATLAB Program 10–5 yields the unit-step response. The resulting unit-step response curve is shown in Figure 10–5.
