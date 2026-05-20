# MATLAB Program 10–22

$\%$ ---------- Design of quadratic optimal control system

$$
A = [ 0 1 0; 0 0 1; 0 - 2 - 3 ];\mathrm{B} = [ 0; 0; 1 ];Q = [ 1 0 0 0 0; 0 1 0; 0 0 1 ];R = [ 0. 0 1 ];K = \operatorname{lqr} (A, B, Q, R)K =
\begin{array}{c c c} 1 0 0. 0 0 0 0 & 5 3. 1 2 0 0 & 1 1. 6 7 1 1 \end{array}
$$

Next we shall investigate the step-response characteristics of the designed system using the matrix K thus determined. The state equation for the designed system is

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u= \mathbf {A} \mathbf {x} + \mathbf {B} (- \mathbf {K x} + k _ {1} r)= (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B} k _ {1} r$$

and the output equation is

$$
y = \mathbf {C x} = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

To obtain the unit-step response, use the following command:

$$[ y, x, t ] = \operatorname{step} (A A, B B, C C, D D)$$

where

$$\mathbf {A} \mathbf {A} = \mathbf {A} - \mathbf {B} \mathbf {K}, \quad \mathbf {B} \mathbf {B} = \mathbf {B} \mathbf {k} _ {1}, \quad \mathbf {C} \mathbf {C} = \mathbf {C}, \quad \mathbf {D} \mathbf {D} = D$$

MATLAB Program 10–23 produces the unit-step response of the designed system. Figure 10–40 shows the response curves $x _ { 1 } , x _ { 2 } .$ , and $x _ { 3 }$ versus t on one diagram.
