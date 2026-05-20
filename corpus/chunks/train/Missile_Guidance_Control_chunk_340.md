Minimum Fuel: This entails the transferring of an arbitrary initial state $x ( t _ { o } ) = x _ { o }$ to a specified target set in a specified amount of time while minimizing some linear combination of the absolute value of the controls. For the minimum-fuel problem,

$$J (u) = \int_ {t _ {0}} ^ {t _ {f}} \left[ \sum_ {i = 1} ^ {m} c _ {i} | u _ {i} (t) | \right] d t, \tag {4.138}$$

where $c _ { i }$ is a proportionality constant, $c _ { i } > 0$ .

Minimum Energy: This entails the transferring of an arbitrary initial state $x ( t _ { 0 } ) = x _ { o }$ to a specified target set in a specified amount of time while minimizing some weighted combination of the squares of the controls. For the minimum-energy problem,

$$J (u) = \int_ {t _ {0}} ^ {t _ {f}} [ u ^ {T} (t) R u (t) ] d t \tag {4.139}$$

which is the norm of the control with weighting positive definite matrix R. A matrix R is positive definite, denoted by $R > 0 ;$ , if $y ^ { T } R y > 0$ for all $y \neq 0$ , and positive semidefinite denoted by $R \geq 0 ,$ , if $y ^ { T } R y \ge 0$ for all y.

Terminal Control: This entails the minimization of the deviations (weighted if so desired) of the final system state values from some desired values. For the terminal control problem,

$$J (u) = [ x (t _ {f}) - d (t _ {f}) ] ^ {T} H [ x (t _ {f}) - d (t _ {f}) ], \tag {4.140}$$

where $d ( t _ { f } )$ is the desired final value of the states and the weighting matrix H is positive semidefinite $( \mathrm { i } . \mathrm { e } . , H \geq 0 )$ .

Tracking Control: This entails minimization of the deviations (weighted if so desired) of the system state values from some desired values throughout the interval of operation. For the tracking-control problem,

$$J (u) = \int_ {t _ {0}} ^ {t _ {f}} [ x (t) - d (t) ] ^ {T} Q [ x (t) - d (t) ] d t. \tag {4.141a}$$

For bounded controls;

$$
\begin{array}{l} J (u) = \int_ {t _ {0}} ^ {t _ {f}} ([ x (t) - d (t) ] ^ {T} Q [ x (t) - d (t) ] \\ + u ^ {T} (t) R u (t)) d t. \tag {4.141b} \\ \end{array}
$$

For unbounded (unconstrained) controls, the desired state value $d ( t )$ is defined throughout the interval $[ t _ { 0 } , t _ { f } ]$ while the weighing matrices $Q$ and R (possibly time varying) are $Q \geq 0$ and $R > 0$ .

Regulating Control: This is a special case of the tracking control where the desired state values are zero. For the regulating-control problem where the desired state value is zero throughout the interval $[ t _ { 0 } , t _ { f } ]$ , the performance measure is

$$J (u) = \int_ {t _ {0}} ^ {t _ {f}} [ x ^ {T} (t) Q x (t) + u ^ {T} (t) R u (t) ] d t, \quad Q \geq 0, \quad R > 0. \tag {4.142}$$
