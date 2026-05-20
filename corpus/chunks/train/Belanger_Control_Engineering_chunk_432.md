# Example 7.13 (Train)

For the train described in Examples 2.3 (Chapter 2) and 7.10, we wish to study the possibility of estimating the state vector with a rather small number of sensors. Specifically, two sensors are contemplated, to measure the velocity of the locomotive, $v_{1}$ , and the distance (or coupler extension) between the locomotive and the first car, $\Delta x_{2}$ . As in Example 7.10, the state is to be derived with respect to a 25-m/s steady speed over level terrain.

(a) Verify the observability of the system (with $x_{1}$ , the distance state component, deleted).   
(b) The velocity measurement is good to within $\pm 1$ m/s, and the coupler extension to within $\pm .02$ m. This suggests using $V = \mathrm{diag}[4\times 10^{-4}\quad 1]$ . The plant noise comes in the form of random forces (e.g., wind or sway-induced friction) added to the driving force, $F$ . This disturbance input, of the order of $3\mathrm{kN}$ , directly affects only $\Delta \dot{\nu}_{1}$ . We use

$$W = \operatorname{diag} [ 0 \quad 0 \quad 0 \quad 0 \quad 9 \quad 0 \quad 0 \quad 0 \quad 0 ].$$

Design an optimal observer.

(c) Simulate the train behavior for an initial state $\Delta x_{i} = \Delta v_{i} = 0$ , all $i$ ; a force pulse input $F(t)$ of $10\mathrm{kN}$ , of duration $10\mathrm{s}$ ; and an additive, unmeasured force of 2 kN, of duration 4 s. Calculate the estimates, using zero initial conditions for the observer and using only the known 10-kN pulse as the $F(t)$ fed to the observer.

(d) Simulate the train as in part (c), but with a coupler stiffness $K = 3.5 \times 10^{5}$ N/m instead of the nominal value $K = 2.5 \times 10^{5}$ N/m. Estimate a few state variables, using the observer designed for the nominal value of $K$ . (This is to assess robustness to parameter changes.)
