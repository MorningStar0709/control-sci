# MATLAB Program 10–28

% Obtaining matrices K and Ke.

$$
A = [ 0 1; 0 - 2 ];\mathrm{B} = [ 0; 4 ];C = [ 1 \quad 0 ];J = \left[ - 2 + j ^ {*} 2 ^ {*} \operatorname{sqrt} (3) - 2 - j ^ {*} 2 ^ {*} \operatorname{sqrt} (3) \right];
L = \left[ \begin{array}{c c} - 8 & - 8 \end{array} \right];
K = \operatorname{acker} (A, B, J)K =4. 0 0 0 0 \quad 0. 5 0 0 0\mathrm{Ke} = \text { acker } (A ^ {\prime}, C ^ {\prime}, L) ^ {\prime}\mathrm{Ke} =1 43 6
$$

Now we find the response of this system to the given initial condition. Referring to Equation (10–70), we have

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \dot {\mathbf {e}} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B K} \\ \mathbf {0} & \mathbf {A} - \mathbf {K} _ {e} \mathbf {C} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {e} \end{array} \right]
$$

This equation defines the dynamics of the designed system using the full-order observer. MATLAB Program 10–29 produces the response to the given initial condition.The resulting response curves are shown in Figure 10–52.
