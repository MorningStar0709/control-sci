# EXAMPLE 9.8 pH control

Consider the problem of controlling the pH of an acid effluent that is fed to a stirred tank with volume V (in liters) and neutralized with NaOH. Let $c_{A}$ (in moles per liter) be the concentration of acid in the influent stream, and let q (in liters per second) be the flow of the effluent. Let $c_{B}$ (in moles per liter) be the concentration of the reagent. Assume that the reagent concentration is so high that the reagent flow u (in liters per second) is negligible in comparison with q. The system is modeled by a linear dynamic model, which describes the mixing dynamics as if there were no reactions, and a static nonlinear titration curve, which gives pH as a function of the concentrations. Let $x_{A}$ and $x_{B}$ be the concentrations of acid and base in the tank if there were no chemical reactions. Mass balances then give

$$\frac {d x _ {A}}{d t} = \frac {q}{V} \left(c _ {A} - x _ {A}\right) \tag {9.21}\frac {d x _ {B}}{d t} = \frac {u}{V} c _ {B} - \frac {q}{V} x _ {B}$$

The pH is given by Eq. (9.19). It is further assumed that the dynamics of the pH sensor and the pump together can be described by the transfer function

$$G (s) = \frac {1}{(1 + s T) ^ {2}}$$

A simple calculation indicates the difficulties in the control problem. Assuming proportional control with gain k, the linearized loop transfer function from the error in pH to pH becomes

$$G _ {0} (s) = \frac {c _ {B} k f ^ {\prime}}{q (1 + s T _ {m}) (1 + s T) ^ {2}}$$

where $T_{m}$ is the mixing time constant

$$T _ {m} = V / q$$

and $f'$ is the slope of the titration curve given by Eq. (9.20). The critical gain for stability is

$$k _ {c} = \frac {q}{f ^ {\prime} c _ {B} T} (2 + T / T _ {m}) (1 + T / T _ {m}) \approx \frac {2 q}{f ^ {\prime} c _ {B} T}$$

where the approximation holds for $T \ll T_{m}$ . Since the slope of the titration curve varies drastically with pH, the critical gain will vary accordingly. Some values for different values of the pH of the mixture are:

<table><tr><td>pH</td><td>Critical gain</td></tr><tr><td>7</td><td>0.009</td></tr><tr><td>8</td><td>0.046</td></tr><tr><td>9</td><td>0.46</td></tr><tr><td>10</td><td>4.6</td></tr></table>
