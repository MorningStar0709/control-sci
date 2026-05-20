<table><tr><td>A = [0 1 0;0 0 0 1;-6 -11 -6];</td></tr><tr><td>B = [0;0;1];</td></tr><tr><td>J = [-2+j*2*sqrt(3) -2-j*2*sqrt(3) -6];</td></tr><tr><td>K = acker(A,B,J)</td></tr><tr><td>K =</td></tr><tr><td>90.0000 29.0000 4.0000</td></tr><tr><td>Abb = [0 1;-11 -6];</td></tr><tr><td>Aab = [1 0];</td></tr><tr><td>L = [-10 -10];</td></tr><tr><td>Ke = acker(Abb&#x27;,Aab&#x27;,L)&#x27;</td></tr><tr><td>Ke =</td></tr><tr><td>14</td></tr><tr><td>5</td></tr></table>

Referring to Equations (10–88) and (10–89), the equation for the minimum-order observer can be given by

$$\dot {\widetilde {\boldsymbol {\eta}}} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \widetilde {\boldsymbol {\eta}} + \left[ \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {K} _ {e} + \mathbf {A} _ {b a} - \mathbf {K} _ {e} A _ {a a} \right] y + \left(\mathbf {B} _ {b} - \mathbf {K} _ {e} B _ {a}\right) u \tag {10-100}$$

where

$$\widetilde {\boldsymbol {\eta}} = \widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} y = \widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} x _ {1}$$

Noting that

$$
\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 1 & - 6 \end{array} \right] - \left[ \begin{array}{c} 1 4 \\ 5 \end{array} \right] [ 1 \quad 0 ] = \left[ \begin{array}{c c} - 1 4 & 1 \\ - 1 6 & - 6 \end{array} \right]
$$

the equation for the minimum-order observer, Equation (10–100), becomes

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {\tilde {\eta}} _ {2} \\ \dot {\tilde {\eta}} _ {3} \end{array} \right] = \left[ \begin{array}{c c} - 1 4 & 1 \\ - 1 6 & - 6 \end{array} \right] \left[ \begin{array}{c} \tilde {\eta} _ {2} \\ \tilde {\eta} _ {3} \end{array} \right] + \left\{\left[ \begin{array}{c c} - 1 4 & 1 \\ - 1 6 & - 6 \end{array} \right] \left[ \begin{array}{c} 1 4 \\ 5 \end{array} \right] \right. \\ + \left[\begin{array}{c}0\\- 6\end{array}\right] - \left[\begin{array}{c}1 4\\5\end{array}\right] 0 \Bigg \} y + \left\{ \right.\left[\begin{array}{c}0\\1\end{array}\right] - \left[\begin{array}{c}1 4\\5\end{array}\right] 0 \Bigg \} u \\ \end{array}
$$

or
