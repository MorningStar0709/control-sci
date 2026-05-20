# Example 8.9

Figure 8.1 shows a single-disk mechanical system, where a motor provides torque $T _ { \mathrm { i n } } ( t )$ directly to the rotor inertia J. Obtain the angular velocity response of this mechanical system if the rotor is initially spinning at $\omega ( 0 ) =$ 120 rad/s (1146 rpm) and the input torque is a step function of magnitude 15 N-m (applied at $t > 0 )$ ). The rotor moment of inertia is $J = 0 . 4 \mathrm { k g } – \mathrm { m } ^ { 2 }$ and the viscous friction coefficient is $b = 0 . 0 6 \mathrm { N - m { - } s / r a d } .$ .

A first-order mathematical model of the mechanical system was derived in Example 2.7 and is repeated below

$$J \dot {\omega} + b \omega = T _ {\mathrm{in}} (t) \quad \text { with } \quad \omega (0) = 1 2 0 \mathrm{rad/s} \tag {8.21}$$

![](image/3be9f629caee95b8d338bf3fdf84da0d311d610de8e4fe0435ab95d889d8045e.jpg)

<details>
<summary>text_image</summary>

Motor torque,
Tin(t)
θ
Axis
Rotor, J
Viscous
friction, b
</details>

Figure 8.1 Single-disk mechanical system for Example 8.9.

We begin by taking the Laplace transform of each term on the left- and right-hand sides of the governing I/O equation (8.21) and incorporating the single initial condition:

$\begin{array} { r l } { \mathrm { L e f t - h a n d ~ s i d e } ; } & { { } \mathcal { L } \{ J \dot { \omega } + b \omega \} = J \big ( s \Omega ( s ) - \omega ( 0 ) \big ) + b \Omega ( s ) } \end{array}$

$$= 0. 4 (s \Omega (s) - 1 2 0) + 0. 0 6 \Omega (s)$$

Right-hand side (step input): $\mathcal { L } \{ T _ { \mathrm { i n } } ( t ) \} = \frac { 1 5 } { s }$

where $\mathcal { L } \{ \omega ( t ) \} = \Omega ( s )$ is the Laplace transform of the angular velocity. Equating the left- and right-hand side terms yields

$$(0. 4 s + 0. 0 6) \Omega (s) - 4 8 = \frac {1 5}{s}$$

or, solving for the Laplace transform $\Omega ( s )$

$$\Omega (s) = \frac {4 8 s + 1 5}{s (0 . 4 s + 0 . 0 6)} = \frac {1 2 0 s + 3 7 . 5}{s (s + 0 . 1 5)} \tag {8.22}$$

The two poles of $\Omega ( s )$ are distinct and are located at $s = 0$ and $s = - 0 . 1 5$ , and the partial-fraction expansion of Eq. (8.22) is

$$\Omega (s) = \frac {1 2 0 s + 3 7 . 5}{s (s + 0 . 1 5)} = \frac {a _ {1}}{s} + \frac {a _ {2}}{s + 0 . 1 5}$$

The residues are

$$\left. a _ {1} = s \Omega (s) \right| _ {s = 0} = \left. \frac {1 2 0 s + 3 7 . 5}{s + 0 . 1 5} \right| _ {s = 0} = \frac {3 7 . 5}{0 . 1 5} = 2 5 0\left. a _ {2} = (s + 0. 1 5) \Omega (s) \right| _ {s = - 0. 1 5} = \left. \frac {1 2 0 s + 3 7 . 5}{s} \right| _ {s = - 0. 1 5} = \frac {1 9 . 5}{- 0 . 1 5} = - 1 3 0$$

Therefore, the Laplace transform Ω(s) in partial-fraction form is
