# Example 5.5

The system

$$G (s) = \frac {5 0}{(s + 0 . 0 5 + j 0 . 4) (s + 0 . 0 5 - j 0 . 4)}$$

is driven by an interrupted sinusoidal function

$$x (t) = \sin (1. 2 5 t) (u (t) - u (t - 1 0 0))$$

Recall that u(t), is the unit step function we learned when studying single sided Laplace Transform analysis with zero initial conditions. The second term, $- u ( t - 1 0 0 )$ , when combined with u(t), Turns o the sinusoid at t = 100 because for $t > 1 0 0 , u ( t ) - u ( t - 1 0 0 ) \stackrel { . } { = } 0 .$ . Numerically solving this system on the computer gives a response (below, right) which changes amplitude dramatically at both the turn ON transient (t = 0) and the turn OFF transient $( t = 1 0 0 )$ , but settles to a constant sinusoidal output (the steady state response) for 80 $< t < 1 0 0$ . Note that if the input sinusoid continued forever instead of shutting o at $t = 1 0 0$ , the steady state response would also continue forever.

It is also worth noting that the frequency of the response changes when the input turns o. This is because the steady state response is a forced response (i.e. of the same mathematical form as the input), while the turn o transient is a natural response, i.e. determined by the $\omega _ { n } , \zeta$ of the system.

![](image/15a9fcb47a5dd73c55a5141105e10aef4c60bd3cac34ffc858128d7ec2217b7b.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 1.0 |
| 10 | 0.95 |
| 20 | 0.85 |
| 30 | 0.75 |
| 40 | 0.65 |
| 50 | 0.55 |
| 60 | 0.45 |
| 70 | 0.35 |
| 80 | 0.25 |
| 90 | 0.15 |
| 100 | 0.0 |
| 110 | 0.0 |
| 120 | 0.0 |
| 130 | 0.0 |
| 140 | 0.0 |
| 150 | 0.0 |
| 160 | 0.0 |
| 170 | 0.0 |
| 180 | 0.0 |
| 190 | 0.0 |
| 200 | 0.0 |
</details>

![](image/919479a1ec7a0bfad3805baeb4825a472ef013624fda681ea3a284c34acadccb.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 120.0 |
| 10 | -100.0 |
| 20 | 70.0 |
| 30 | -50.0 |
| 40 | 50.0 |
| 50 | -30.0 |
| 60 | 40.0 |
| 70 | -20.0 |
| 80 | 30.0 |
| 90 | -10.0 |
| 100 | 60.0 |
| 110 | -40.0 |
| 120 | 30.0 |
| 130 | -20.0 |
| 140 | 10.0 |
| 150 | -5.0 |
| 160 | 5.0 |
| 170 | -2.0 |
| 180 | 2.0 |
| 190 | -1.0 |
| 200 | 1.0 |
</details>

Left: Input signal. Right: System response includes transients both when the sinusoid turns ON (t = 0)and when it turns OFF (t = 100). Eventually the ON transient dies out to a steady state response $( 7 5 < t < \mathrm { i } 0 0 )$ .

Frequency response analysis ignores the transient response (both ON and OFF type) and focuses entirely on the forced, steady state response. Since the steady state response is always of the same mathematical form as the input, we need only concern ourselves with dierences in amplitude and phase (between the input and output sinusoid).

Each root of the denominator of a transfer function is called a pole. Each root of the numerator is called a zero. Each pole and zero is a real or complex number which aects how the system responds to both transient and steady state inputs.
