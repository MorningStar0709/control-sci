# Proportional controller

Using proportional controller transfer function $G _ { C } ( s ) { = } K _ { P } { = } 0 . 0 4 \ : \mathrm { V / m }$ , the forward transfer function of the system in Fig. 10.27 is

$$G (s) = \frac {2 K _ {P}}{s ^ {2} + 0 . 3 s} = \frac {0 . 0 8}{s (s + 0 . 3)}$$

Forward transfer function $G ( s )$ is type 1 because we can factor out one free integrator. The reference input, $r ( t ) = 0 . 0 1 t \mathrm { m }$ , is a ramp function with slope of 0.01 m/s. Table 10.3 shows that the steady-state position error for a type 1 system with a ramp input is

$$x _ {e} (\infty) = \frac {0 . 0 1}{K _ {\mathrm{sv}}}$$

where the static velocity error constant is

$$K _ {\mathrm{sv}} = \lim _ {s \rightarrow 0} s G (s) = \lim _ {s \rightarrow 0} \frac {0 . 0 8}{s + 0 . 3} = \frac {0 . 0 8}{0 . 3} = 0. 2 6 6 7$$

The steady-state position error for the ramp input is $x _ { e } ( \infty ) = 0 . 0 1 / K _ { \mathrm { s v } } = 0 . 0 3 7 5$ m (or 3.75 cm). Figure 10.28 shows the closed-loop position response $x ( t )$ to the ramp input $x _ { \mathrm { r e f } } ( t ) = 0 . 0 1 t ~ \mathrm { m }$ with a P-controller and gain $K _ { P } = 0 . 0 4 \ : \mathrm { V / m }$ . At steady state, the closed-loop position response x(t) clearly exhibits an offset error of 0.0375 m with respect to the reference ramp input.
