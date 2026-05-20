# MATLAB Program 10–34

% Design of quadratic optimal control system

$$
\begin{array}{l} A = [ 0 1 0 0; 2 0. 6 0 1 0 0 0; 0 0 0 1; - 0. 4 9 0 5 0 0 0 ]; \\ B = [ 0; - 1; 0; 0. 5 ]; \\ C = [ 0 0 1 0 ]; \\ D = [ 0 ]; \\ \text { Ahat } = [ \text { A   zeros } (4, 1); - \text { C   0 } ]; \\ \text { Bhat } = [ \mathrm{B}; 0 ]; \\ Q = [ 1 0 0 \quad 0 \quad 0 \quad 0 \quad 0; 0 \quad 1 \quad 0 \quad 0 \quad 0; 0 \quad 0 \quad 1 \quad 0 \quad 0; 0 \quad 0 \quad 0 \quad 1 \quad 0; 0 \quad 0 \quad 0 \quad 0 \quad 1 ]; \\ R = [ 0. 0 1 ]; \\ \text { Khat } = \text { lqr(Ahat,Bhat,Q,R) } \\ \mathrm{Khat} = \\ - 1 8 8. 0 7 9 9 - 3 7. 0 7 3 8 - 2 6. 6 7 6 7 - 3 0. 5 8 2 4 1 0. 0 0 0 0 \\ \end{array}
$$

Unit-Step Response. Once we have determined the feedback gain matrix K and the integral gain constant $k _ { I }$ , we can determine the unit-step response of the designed system.The system equation is

$$
\left[ \begin{array}{l} \dot {\mathbf {x}} \\ \dot {\boldsymbol {\xi}} \end{array} \right] = \left[ \begin{array}{l l} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} \\ \boldsymbol {\xi} \end{array} \right] + \left[ \begin{array}{l} \mathbf {B} \\ 0 \end{array} \right] u + \left[ \begin{array}{l} \mathbf {0} \\ 1 \end{array} \right] r \tag {10-178}
$$

[Refer to Equation (10–35).] Since

$$u = - \mathbf {K} \mathbf {x} + k _ {I} \xi$$

Equation (10–178) can be written as follows:

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \dot {\boldsymbol {\xi}} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B} k _ {I} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \boldsymbol {\xi} \end{array} \right] + \left[ \begin{array}{c} \mathbf {0} \\ 1 \end{array} \right] r \tag {10-179}
$$

The output equation is

$$
y = \left[ \begin{array}{c c} \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \boldsymbol {\xi} \end{array} \right] + [ 0 ] r
$$
