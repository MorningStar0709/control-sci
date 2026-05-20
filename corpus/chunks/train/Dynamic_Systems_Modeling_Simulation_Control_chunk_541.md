# Example 10.2

Using the following parameters for the DC motor in Example 10.1, determine the poles of the closed-loop transfer function and describe the angular velocity response to an 8-V step input for the source voltage.

Inductance, L = 1.5 mH

Resistance, R = 0.5 Ω

Motor torque constant, $K _ { m } = 0 . 0 5 \mathrm { N - m / A }$

Back-emf constant, $K _ { b } = 0 . 0 5 \mathrm { V - s / r a d }$

Motor inertia, $J = 2 . 5 ( 1 0 ^ { - 4 } ) \mathrm { k g } \mathrm { - m } ^ { 2 }$

Motor friction coefficient, $b = 1 0 ^ { - 4 }$ N-m-s/rad

Equation (10.6) in Example 10.1 presents the closed-loop transfer function of the DC motor with source voltage $e _ { \mathrm { i n } } ( t )$ as the input and angular velocity ?? as the output

$$T (s) = \frac {K _ {m}}{(L s + R) (J s + b) + K _ {m} K _ {b}} = \frac {K _ {m}}{L J s ^ {2} + (L b + R J) s + R b + K _ {m} K _ {b}}$$

Using the numerical parameters for the DC motor, T(s) becomes

$$T (s) = \frac {0 . 0 5}{3 . 7 5 (1 0 ^ {- 7}) s ^ {2} + 1 . 2 5 1 5 (1 0 ^ {- 4}) s + 0 . 0 0 2 5 5} = \frac {1 . 3 3 3 3 (1 0 ^ {5})}{s ^ {2} + 3 3 3 . 7 3 s + 6 8 0 0}$$

This result can be verified using the MATLAB command feedback as shown in Example 10.1.

The transient response of the DC motor depends on its characteristic roots or poles of the closed-loop transfer function T(s). We compute the roots or poles by setting the denominator of $T ( s )$ to zero

$$s ^ {2} + 3 3 3. 7 3 s + 6 8 0 0 = 0$$

The closed-loop roots or poles are two real, negative values: $s _ { 1 } = - 2 1 . 8 0$ and $s _ { 2 } = - 3 1 1 . 9 3$ . Therefore, the transient response of the DC motor does not exhibit any oscillations (it is overdamped), but rather consists of two exponential functions $c _ { 1 } e ^ { - 2 1 . 8 0 t }$ and $c _ { 2 } e ^ { - 3 1 1 . 9 3 t }$ , which both “die out” by time $t = 0 . 1 8 4 ~ \mathrm { s }$ (note that the slowest root $s _ { 1 } = - 2 1 . 8 0$ has a time constant of $\tau _ { 1 } = 1 / 2 1 . 8 0 = 0 . 0 4 5 9$ s and hence the settling time is $4 \tau _ { 1 } = 0 . 1 8 4 \mathrm { s } )$ .

The steady-state motor speed can be computed from the product of the DC gain of the closed-loop transfer function T(s) and the 8-V step input. Because the DC gain of T(s) is $1 . 3 3 3 3 ( 1 0 ^ { 5 } ) / 6 8 0 0 = 1 9 . 6 0 8$ , the steady-state angular velocity is $( 8 \mathrm { V } ) ( 1 9 . 6 0 8 ) = 1 5 6 . 8 6$ rad/s (about 1498 revolutions per minute or rpm).

In summary, this example shows that the transient and steady-state response characteristics of a closed-loop system can be gleaned from knowledge of the poles and DC gain of the closed-loop transfer function; hence, we can use the techniques that were developed in Chapter 7. We can apply the analysis methods from Chapter 7 because both open-loop and closed-loop transfer functions are SISO systems.
