# Example 4.27: EKF and UKF

Consider the following set of reversible reactions taking place in a wellstirred, isothermal, gas-phase batch reactor

$$\mathrm{A} \underset {k _ {- 1}} {\overset {k _ {1}} {\rightleftharpoons}} \mathrm{B} + \mathrm{C} \quad 2 \mathrm{B} \underset {k _ {- 2}} {\overset {k _ {2}} {\rightleftharpoons}} \mathrm{C}$$

The material balance for the reactor is

$$
\begin{array}{l} \frac {d}{d t} \left[ \begin{array}{c} c _ {A} \\ c _ {B} \\ c _ {C} \end{array} \right] = \left[ \begin{array}{c c} - 1 & 0 \\ 1 & - 2 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{c} k _ {1} c _ {A} - k _ {- 1} c _ {B} c _ {C} \\ k _ {2} c _ {B} ^ {2} - k _ {- 2} c _ {C} \end{array} \right] \\ \frac {d x}{d t} = f _ {c} (x) \\ \end{array}
$$

with states and measurement

$$
x = \left[ \begin{array}{c c c} c _ {A} & c _ {B} & c _ {C} \end{array} \right] ^ {\prime} \quad y = R T \left[ \begin{array}{c c c} 1 & 1 & 1 \end{array} \right] x
$$

in which $c _ { j }$ denotes the concentration of species j in mol/L, R is the gas constant, and T is the reactor temperature in K. The measurement is the reactor pressure in atm, and we use the ideal gas law to model the pressure. The model is nonlinear because of the two second-order reactions. We model the system plus disturbances with the following discrete time model

$$x ^ {+} = f (x) + wy = C x + v$$

in which $f$ is the solution of the ODEs over the sample time, $\Delta ,$ , i.e, if $s ( t , x _ { 0 } )$ is the solution of ${ d x } / { d t } = f _ { c } ( x )$ with initial condition $x ( 0 ) =$ $x _ { 0 }$ at $t = 0$ , then $f ( x ) = s ( \Delta , x )$ . The state and measurement disturbances, w and $\nu ,$ , are assumed to be zero-mean independent normals with constant covariances $Q$ and R. The following parameter values are used in the simulations

$$
R T = 3 2. 8 4 \mathrm{mol} \cdot \mathrm{atm/L}\Delta = 0. 2 5 \quad k _ {1} = 0. 5 \quad k _ {- 1} = 0. 0 5 \quad k _ {2} = 0. 2 \quad k _ {- 2} = 0. 0 1
C = \left[ \begin{array}{c c c} 1 & 1 & 1 \end{array} \right] R T \quad P (0) = (0. 5) ^ {2} I \quad Q = (0. 0 0 1) ^ {2} I \quad R = (0. 2 5) ^ {2}

\overline {{x}} (0) = \left[ \begin{array}{c} 1 \\ 0 \\ 4 \end{array} \right] \qquad x (0) = \left[ \begin{array}{c} 0. 5 \\ 0. 0 5 \\ 0 \end{array} \right]
$$

The prior density for the initial state, $N ( \overline { { x } } ( 0 ) , P ( 0 ) )$ , is deliberately chosen to poorly represent the actual initial state to model a large initial disturbance to the system. We wish to examine how the different estimators recover from this large unmodeled disturbance.
