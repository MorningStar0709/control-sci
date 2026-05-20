The closed-loop poles of the observer are the eigenvalues of matrix $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C } .$ . The closed-loop poles of the pole-placement are the eigenvalues of matrix $\mathbf { A } - \mathbf { B } \mathbf { K }$ .

Referring to the duality problem between the pole-placement problem and observerdesign problem, we can determine $\mathbf { K } _ { e }$ by considering the pole-placement problem for the dual system. That is, we determine $\mathbf { K } _ { e }$ by placing the eigenvalues of ${ \bf A } ^ { * } - { \bf C } ^ { * } { \bf K } _ { e }$ at the desired place. Since ${ \bf K } _ { e } = { \bf K } ^ { * }$ , for the full-order observer we use the command

$$K _ {e} = a c k e r (A ^ {\prime}, C ^ {\prime}, L) ^ {\prime}$$

where L is the vector of the desired eigenvalues for the observer. Similarly, for the fullorder observer, we may use

$$\mathrm{K} _ {\mathrm{e}} = \text { place } (\mathrm{A} ^ {\prime}, \mathrm{C} ^ {\prime}, \mathrm{L}) ^ {\prime}$$

provided L does not include multiple poles. [In the above commands, prime (') indicates the transpose.] For the minimum-order (or reduced-order) observers, use the following commands:

$$\mathrm{K} _ {\mathrm{e}} = \text { acker } (\mathrm{Abb} ^ {\prime}, \mathrm{Aab} ^ {\prime}, \mathrm{L}) ^ {\prime}$$

or

$$\mathrm{K} _ {\mathrm{e}} = \text { place } (\mathrm{Abb} ^ {\prime}, \mathrm{Aab} ^ {\prime}, \mathrm{L}) ^ {\prime}\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \end{array} \right], \quad \mathbf {C} = \left[ \begin{array}{c c c} 1 & 0 & 0 \end{array} \right]
$$

Let us assume that we want to place the closed-loop poles at

$$s _ {1} = - 2 + j 2 \sqrt {3}, \quad s _ {2} = - 2 - j 2 \sqrt {3}, \quad s _ {3} = - 6$$

Then the necessary state-feedback gain matrix K can be obtained as follows:

$$
\mathbf {K} = \left[ \begin{array}{c c c} 9 0 & 2 9 & 4 \end{array} \right]
$$

(See MATLAB Program 10–10 for a MATLAB computation of this matrix K.)

Next, let us assume that the output y can be measured accurately so that state variable $x _ { 1 }$ (which is equal to y) need not be estimated. Let us design a minimum-order observer. (The minimum-order observer is of second order.) Assume that we choose the desired observer poles to be at

$$s = - 1 0, \quad s = - 1 0$$
