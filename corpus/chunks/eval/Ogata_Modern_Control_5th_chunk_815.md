# MATLAB Program 10–20

% ---------- Design of quadratic optimal regulator system

$$
\begin{array}{l} A = [ 0 1 0; 0 0 1; - 3 5 - 2 7 - 9 ]; \\ B = [ 0; 0; 1 ]; \\ Q = [ 1 \quad 0 \quad 0; 0 \quad 1 \quad 0; 0 \quad 0 \quad 1 ]; \\ R = [ 1 ]; \\ [ K, P, E ] = \operatorname{lqr} (A, B, Q, R) \\ \end{array}
K =
$$

0.0143 0.1107 0.0676

$$P =$$

4.2625 2.4957 0.0143

2.4957 2.8150 0.1107

0.0143 0.1107 0.0676

$$E =- 5. 0 9 5 8- 1. 9 8 5 9 + 1. 7 1 1 0 \mathrm{i}- 1. 9 8 5 9 - 1. 7 1 1 0 \mathrm{i}$$

Next, let us obtain the response x of the regulator system to the initial condition x(0), where

$$
\mathbf {x} (0) = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right]
$$

With state feedback u=–Kx, the state equation for the system becomes

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u = (\mathbf {A} - \mathbf {B K}) \mathbf {x}$$

Then the system, or sys, can be given by

$$\text { sys } = \text { ss } (A - B ^ {*} K, \text { eye } (3), \text { eye } (3), \text { eye } (3))$$

MATLAB Program 10–21 produces the response to the given initial condition. The response curves are shown in Figure 10–38.
