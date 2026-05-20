Figure 9.19 Step responses for the system (9.25) for different implementations and different values of $a$ : shift-operator controllable canonical form (Listing 9.3) (dashed), Jordan form (Listing 9.4) and $\delta$ -operator controllable canonical form (Listing 9.6) are both the full line. (a) $a = -0.9$ , (b) $a = -0.97$ , (c) $a = -0.98$ , and (d) $a = -0.99$ .

Figure 9.19 shows simulations using MATLAB $^{®}$ . The simulation is simply an iteration of the state equations in Listings 9.3, 9.4, and 9.6. The results are obtained when chopping the result of all operations to seven digits. The figure shows the results when different values of a are used. For a = -0.9 all the implementations give compatible results, as shown in Fig. 9.19(a). When a is decreased, the shift-operator controllable canonical form is very sensitive and the solution is inaccurate. The other two implementations give approximately the same results. They will, however, differ when even lower numerical precision is used. The modified Jordan form is better than the $\delta$ -operator controllable canonical form when a is decreased further.

The sensitivity of the shift-operator controllable form with respect to parameter changes is given by (9.18). Perturbing the characteristic equation with a constant term $\varepsilon$ ,

$$(z - 0. 9 9) ^ {4} + \varepsilon = 0$$

gives the roots

$$z = 0. 9 9 + (- \varepsilon) ^ {1 / 4}$$

The roots are moved from 0.99 to a circle with origin at 0.99 and the radius $r = |\varepsilon|^{1/4}$ . If $\varepsilon = 10^{-8}$ then $r = 10^{-2}$ ; that is, the system can be unstable even if the perturbation is very small.

Making a similar calculation for the $\delta$ companion form we get

$$(\delta + 0. 0 1) ^ {4} + \varepsilon = 0$$

which gives the roots

$$\delta = - 0. 0 1 + (- \varepsilon) ^ {1 / 4}$$

The roots are moved from -0.01 to a circle with origin at -0.01 and the radius $r = |\varepsilon|^{1/4}$ . If $\varepsilon = 10^{-8}$ then $r = 10^{-2}$ , which is the same as for the shift-operator case. Notice, however, that the relative variation in parameters required to make the system unstable is two orders of magnitude larger with the $\delta$ -operator. The $\delta$ companion form is thus less sensitive to parameter perturbations than the shift companion form. Notice, however, that the Jordan realizations in shift or $\delta$ -forms are superior.
