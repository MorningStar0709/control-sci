# Example 5.7

Note that the SSR of the DC motor in Example 5.6 does not depend on angular displacement of the rotor (??). Thus, this state variable can be eliminated. Obtain a “reduced-order” SSR of the DC motor in terms of two state variables: current I and angular velocity ??̇ . The two outputs (measurements) are the two state variables.

In Example 5.6, the second state variable $( x _ { 2 } = \theta )$ does not appear in the state equations (5.32)– (5.34), nor is it an output variable. Another way to recognize the system’s lack of dependence on angular displacement ?? is to note the three zeros in the second column of the state matrix A and the two zeros in the second column of the output matrix C (elements contained in the second columns of A and C are coefficients of the second state variable $x _ { 2 } )$ . Therefore, we can eliminate the second state equation (5.33) of our third-order SSR in Example 5.6. Furthermore, we can substitute $\omega = { \dot { \theta } }$ and ${ \dot { \omega } } = { \ddot { \theta } }$ in the electrical and mechanical modeling equations, or the first and third state equations (5.32) and (5.34). The armature circuit and mechanical modeling equations thus become

$$\dot {I} = \frac {1}{L} (- R I + e _ {\text { in }} (t) - K _ {b} \omega) \tag {5.40}\dot {\omega} = \frac {1}{J} (- b \omega + K _ {m} I - T _ {L}) \tag {5.41}$$

Note that both equations are first-order ODEs. Consequently, we need two state variables $( n = 2 )$ ). We choose the states $x _ { 1 } = I$ and $x _ { 2 } = \omega$ and inputs $u _ { 1 } = e _ { \mathrm { i n } } ( t ) , u _ { 2 } = T _ { L }$ . Substituting for the states and input variables in Eqs. (5.40) and (5.41) and using the matrix-vector format yields the state equation

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - R / L & - K _ {b} / L \\ K _ {m} / J & - b / J \end{array} \right] \mathbf {x} + \left[ \begin{array}{c c} 1 / L & 0 \\ 0 & - 1 / J \end{array} \right] \mathbf {u} \tag {5.42}
$$

Note that the A and B matrices for this reduced-order SSR are identical to the third-order state and input matrices in Eq. (5.38) with the second row removed (the state equation for angular displacement ??) and the second column removed from the third-order state matrix in Eq. (5.38). The output equation for the reduced-order SSR is
