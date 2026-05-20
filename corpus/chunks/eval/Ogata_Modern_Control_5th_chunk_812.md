# EXAMPLE 10–10

Consider the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 1 \\ 0 & 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] u
$$

Show that the system cannot be stabilized by the state-feedback control scheme

$$u = - \mathbf {K x}$$

whatever matrix K is chosen. (Notice that this system is not state controllable.) Define

$$
\mathbf {K} = \left[ \begin{array}{c c} k _ {1} & k _ {2} \end{array} \right]
$$

Then

$$
\begin{array}{l} \mathbf {A} - \mathbf {B K} = \left[ \begin{array}{c c} - 1 & 1 \\ 0 & 2 \end{array} \right] - \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \left[ \begin{array}{l l} k _ {1} & k _ {2} \end{array} \right] \\ = \left[ \begin{array}{c c} - 1 - k _ {1} & 1 - k _ {2} \\ 0 & 2 \end{array} \right] \\ \end{array}
$$

Hence, the characteristic equation becomes

$$
\begin{array}{l} | s \mathbf {I} - \mathbf {A} + \mathbf {B K} | = \left| \begin{array}{c c} s + 1 + k _ {1} & - 1 + k _ {2} \\ 0 & s - 2 \end{array} \right| \\ = (s + 1 + k _ {1}) (s - 2) = 0 \\ \end{array}
$$

The closed-loop poles are located at

$$s = - 1 - k _ {1}, \quad s = 2$$

Since the pole at s=2 is in the right-half s plane, the system is unstable whatever K matrix is chosen. Hence, quadratic optimal control techniques cannot be applied to this system.

Let us assume that matrices Q and R in the quadratic performance index are given by

$$
\mathbf {Q} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right], \quad R = [ 1 ]
$$

and that we write MATLAB Program 10–18. The resulting MATLAB solution is

$$K = [ N a N N a N ]$$

(NaN means ‘not a number.’) Whenever the solution to a quadratic optimal control problem does not exist, MATLAB tells us that matrix K consists of NaN.

MATLAB Program 10–18   
% ---- Design of quadratic optimal regulator system ----
A = [-1 1;0 2];
B = [1;0];
Q = [1 0;0 1];
R = [1];
K = lqr(A,B,Q,R)
Warning: Matrix is singular to working precision.
K =
    NaN NaN
% **** If we enter the command [K,P,E] = lqr(A,B,Q,R), then *****
[K,P,E] = lqr(A,B,Q,R)
Warning: Matrix is singular to working precision.
K =
    NaN NaN
P =
    -Inf -Inf
    -Inf -Inf
E =
    -2.0000
    -1.4142

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - 1 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

The performance index J is given by
