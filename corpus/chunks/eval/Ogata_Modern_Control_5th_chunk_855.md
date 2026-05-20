# MATLAB Program 10–26

$$
A = \left[ \begin{array}{l l l l l l l l l l l l l l} 0 & 0 & 1 & 0; 0 & 0 & 0 & 1; - 3 6 & 3 6 & - 0. 6 & 0. 6; 1 8 & - 1 8 & 0. 3 & - 0. 3 \end{array} \right];
\mathrm{B} = [ 0; 0; 1; 0 ];J = [ - 2 + j ^ {*} 2 ^ {*} \text {sqrt} (3) - 2 - j ^ {*} 2 ^ {*} \text {sqrt} (3) - 1 0 - 1 0 ];K = \operatorname{acker} (A, B, J)K =
\begin{array}{l l l l} 1 3 0. 4 4 4 4 & - 4 1. 5 5 5 6 & 2 3. 1 0 0 0 & 1 5. 4 1 8 5 \end{array}
\mathrm{Aab} = [ 1 \quad 0; 0 \quad 1 ];A b b = [ - 0. 6 \quad 0. 6; 0. 3 \quad - 0. 3 ];
L = \left[ \begin{array}{c c} - 1 5 & - 1 6 \end{array} \right];
\mathrm{Ke} = \text { place } (\mathrm{Abb} ^ {\prime}, \mathrm{Aab} ^ {\prime}, \mathrm{L}) ^ {\prime}\text { place: ndigits } = 1 5\mathrm{Ke} =1 4. 4 0 0 0 \quad 0. 6 0 0 00. 3 0 0 0 \quad 1 5. 7 0 0 0
$$

Response to Initial Condition: Next, we obtain the response of the designed system to the given initial condition. Since

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uu = - \mathbf {K} \widetilde {\mathbf {x}}
\widetilde {\mathbf {x}} = \left[ \begin{array}{c} \mathbf {x} _ {a} \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \left[ \begin{array}{c} \mathbf {y} \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right]
$$

we have

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \widetilde {\mathbf {x}} = (\mathbf {A} - \mathbf {B} \mathbf {K}) \mathbf {x} + \mathbf {B} \mathbf {K} (\mathbf {x} - \widetilde {\mathbf {x}}) \tag {10-170}$$

Note that

$$
\mathbf {x} - \widetilde {\mathbf {x}} = \left[ \begin{array}{c} \mathbf {x} _ {a} \\ \hline \mathbf {x} _ {b} \end{array} \right] - \left[ \begin{array}{c} \mathbf {x} _ {a} \\ \hline \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \left[ \begin{array}{c} \mathbf {0} \\ \hline \mathbf {x} _ {b} - \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \left[ \begin{array}{c} \mathbf {0} \\ \hline \mathbf {e} \end{array} \right] = \left[ \begin{array}{c} \mathbf {0} \\ \hline \mathbf {I} \end{array} \right] \mathbf {e} = \mathbf {F e}
$$

where

$$
\mathbf {F} = \left[ \begin{array}{c} \mathbf {0} \\ \dots \\ \mathbf {I} \end{array} \right]
$$

Then, Equation (10–170) can be written as

$$\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B K F e} \tag {10-171}$$

Since, from Equation (10–94), we have

$$\dot {\mathbf {e}} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {e} \tag {10-172}$$

by combining Equations (10–171) and (10–172) into one equation, we have
