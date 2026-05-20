Next, we obtain the observer gain matrix $K _ { e }$ for the minimum-order observer. MATLAB Program 10–31 produces $K _ { e } .$ . The result is

$$K _ {e} = 6$$

<table><tr><td>MATLAB Program 10-31</td></tr><tr><td>% Obtaining Ke ---- minimum-order observer</td></tr><tr><td>Aab = [1];</td></tr><tr><td>Abb = [-2];</td></tr><tr><td>LL = [-8];</td></tr><tr><td>Ke = acker(Abb&#x27;,Aab&#x27;,LL)&#x27;</td></tr><tr><td>Ke =</td></tr><tr><td>6</td></tr></table>

The response of the system with minimum-order observer to the initial condition can be obtained as follows: By substituting $u = - \mathbf { K } \widetilde { \mathbf { x } }$ into the plant equation given by Equation (10–79)

we find

$$
\begin{array}{l} \dot {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \widetilde {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \mathbf {x} + \mathbf {B} \mathbf {K} (\mathbf {x} - \widetilde {\mathbf {x}}) \\ = (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B} \left[ \begin{array}{c c} K _ {a} & K _ {b} \end{array} \right] \left[ \begin{array}{c} 0 \\ e \end{array} \right] \\ \end{array}
$$

or

$$\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B} K _ {b} e$$

The error equation is

$$\dot {e} = \big (A _ {b b} - K _ {e} A _ {a b} \big) e$$

Hence the system dynamics are defined by

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \dot {e} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B} K _ {b} \\ 0 & A _ {b b} - K _ {e} A _ {a b} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ e \end{array} \right]
$$

Based on this last equation, MATLAB Program 10–32 produces the response to the given initial condition. The resulting response curves are shown in Figure 10–53.
