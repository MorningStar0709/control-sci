# Example 6.8: Nash equilibrium is unstable

Consider the following transfer function matrix for a simple two-input two-output system

$$
\left[ \begin{array}{c} y _ {1} (s) \\ y _ {2} (s) \end{array} \right] = \left[ \begin{array}{c c} G _ {1 1} (s) & G _ {1 2} (s) \\ G _ {2 1} (s) & G _ {2 2} (s) \end{array} \right] \left[ \begin{array}{c} u _ {1} (s) \\ u _ {2} (s) \end{array} \right]
$$

in which

$$
G (s) = \left[ \begin{array}{c c} \frac {1}{s ^ {2} + 2 (0 . 2) s + 1} & \frac {0 . 5}{0 . 2 2 5 s + 1} \\ \frac {- 0 . 5}{(0 . 5 s + 1) (0 . 2 5 s + 1)} & \frac {1 . 5}{0 . 7 5 s ^ {2} + 2 (0 . 8) (0 . 7 5) s + 1} \end{array} \right]
$$

Obtain discrete time models $( A _ { i j } , B _ { i j } , C _ { i j } )$ for each of the four transfer functions $G _ { i j } ( s )$ using a sample time of $T = 0 . 2$ and zero-order holds on the inputs. Set the control cost function parameters to be

$$\overline {{{Q}}} _ {1} = \overline {{{Q}}} _ {2} = 1 \quad \overline {{{P}}} _ {1 f} = \overline {{{P}}} _ {2 f} = 0 \quad R _ {1} = R _ {2} = 0. 0 1N = 3 0 \quad w _ {1} = w _ {2} = 0. 5$$

Compute the eigenvalues of the L matrix for this system using noncooperative MPC. Show the Nash equilibrium is unstable and the closed-loop system is therefore unstable. Discuss why this system is problematic for noncooperative control.
