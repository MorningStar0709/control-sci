Matrix P is given by

$$
\mathbf {P} = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ - \mathbf {C} & 0 \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 2 0. 6 0 1 & 0 & 0 & 0 & - 1 \\ 0 & 0 & 0 & 1 & 0 \\ - 0. 4 9 0 5 & 0 & 0 & 0 & 0. 5 \\ 0 & 0 & - 1 & 0 & 0 \end{array} \right] \tag {10-52}
$$

The rank of this matrix can be found to be 5. Therefore, the system defined by Equation (10–51) is completely state controllable, and arbitrary pole placement is possible. MATLAB Program 10–6 produces the state feedback gain matrix Kˆ .

<table><tr><td>MATLAB Program 10-6</td></tr><tr><td>A = [0 1 0 0; 20.601 0 0 0; 0 0 0 1; -0.4905 0 0 0];B = [0;-1;0;0.5];C = [0 0 1 0];Ahat = [A zeros(4,1); -C 0];Bhat = [B;0];J = [-1+j*sqrt(3) -1-j*sqrt(3) -5 -5 -5];Khat = acker(Ahat,Bhat,J)Khat = -157.6336 -35.3733 -56.0652 -36.7466 50.9684</td></tr></table>

Thus, we get

$$
\mathbf {K} = \left[ \begin{array}{c c c c} k _ {1} & k _ {2} & k _ {3} & k _ {4} \end{array} \right] = \left[ \begin{array}{c c c c} - 1 5 7. 6 3 3 6 & - 3 5. 3 7 3 3 & - 5 6. 0 6 5 2 & - 3 6. 7 4 6 6 \end{array} \right]
$$

and

$$k _ {I} = - 5 0. 9 6 8 4$$

Unit Step-Response Characteristics of the Designed System. Once we determine the feedback gain matrix K and the integral gain constant $k _ { I } ,$ the step response in the cart position can be obtained by solving the following equation, which is obtained by substituting Equation (10–49) into Equation (10–35):

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \dot {\xi} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B} k _ {I} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \xi \end{array} \right] + \left[ \begin{array}{c} \mathbf {0} \\ 1 \end{array} \right] r \tag {10-53}
$$

The output y(t) of the system is $x _ { 3 } ( t )$ , or

$$
y = \left[ \begin{array}{l l l l l} 0 & 0 & 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \xi \end{array} \right] + [ 0 ] r \tag {10-54}
$$

Define the state matrix, control matrix, output matrix, and direct transmission matrix of the system given by Equations (10–53) and (10–54) as AA, BB, CC, and DD, respectively. MATLAB Program 10–7 may be used to obtain the step-response curves of the designed system. Notice that, to obtain the unit-step response, we entered the command

$$[ y, x, t ] = \operatorname{step} (A A, B B, C C, D D, 1, t)$$
