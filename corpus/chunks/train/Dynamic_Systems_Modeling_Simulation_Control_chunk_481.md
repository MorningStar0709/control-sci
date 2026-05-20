# Example 9.4

Figure 9.12 presents the block diagram of the simplified solenoid actuator–valve system from Example 7.4. If the input voltage $e _ { \mathrm { i n } } ( t )$ is a sine wave with a magnitude of 6 V and frequency of 10 Hz, determine the frequency response of the spool valve using analytical and numerical methods. The system has zero initial conditions at time $t = 0$ .

The input voltage signal $e _ { \mathrm { i n } } ( t )$ has frequency $f = 1 0$ Hz or 10 cycles per second. Therefore, the frequency in radians per second is $\omega = 2 \pi f = 6 2 . 8 3 1 9$ rad/s and the input voltage signal is

$$e _ {\mathrm{in}} (t) = 6 \sin 6 2. 8 3 1 9 t \mathrm{V} \tag {9.34}$$

The two transfer functions in Fig. 9.12 are

Solenoid: $G _ { 1 } ( s ) = { \frac { 1 2 } { 0 . 0 0 3 s + 1 . 5 } } = { \frac { F _ { \mathrm { e m } } ( s ) } { E _ { \mathrm { i n } } ( s ) } }$

$\mathrm { S p o o l ~ v a l v e } ; \quad G _ { 2 } ( s ) = { \frac { 1 } { 0 . 0 4 s ^ { 2 } + 1 6 s + 7 0 0 0 } } = { \frac { Y ( s ) } { F _ { \mathrm { e m } } ( s ) } }$

The overall system transfer function $G ( s )$ relating the valve position y (output) to the voltage $e _ { \mathrm { i n } } ( t )$ (input) can be obtained by multiplying the solenoid and spool-valve transfer functions

$$G (s) = G _ {1} (s) G _ {2} (s) = \frac {F _ {\mathrm{em}} (s)}{E _ {\mathrm{in}} (s)} \frac {Y (s)}{F _ {\mathrm{em}} (s)} = \frac {Y (s)}{E _ {\mathrm{in}} (s)} = \frac {1 2}{(0 . 0 0 3 s + 1 . 5) (0 . 0 4 s ^ {2} + 1 6 s + 7 0 0 0)}$$

Expanding the third-order denominator of $G ( s )$ we obtain

$$G (s) = \frac {1 2}{0 . 0 0 0 1 2 s ^ {3} + 0 . 1 0 8 s ^ {2} + 4 5 s + 1 0 , 5 0 0} \tag {9.35}$$

Because the input is a sine signal the frequency response $y _ { \mathrm { s s } } ( t )$ will also be a sine wave. Using Eq. (9.17) with $U _ { 0 } = 6 \mathrm { V }$ and $\omega = 6 2 . 8 3 1 9$ rad/s yields the frequency response of the spool valve

$$y _ {\mathrm{ss}} (t) = | G (j \omega) | 6 \sin (6 2. 8 3 1 9 t + \phi) \tag {9.36}$$

As with the previous examples, we need to compute the magnitude and phase of the sinusoidal transfer function for the given input frequency. The sinusoidal transfer function is computed by using Eq. (9.35) with $s = j \omega$

$$G (j \omega) = \frac {1 2}{0 . 0 0 0 1 2 (j \omega) ^ {3} + 0 . 1 0 8 (j \omega) ^ {2} + 4 5 (j \omega) + 1 0 , 5 0 0} \tag {9.37}$$

Noting that $j ^ { 3 } = - j$ and ${ j ^ { 2 } = - 1 }$ , Eq. (9.37) becomes

$$G (j \omega) = \frac {1 2}{(1 0 , 5 0 0 - 0 . 1 0 8 \omega^ {2}) + j (- 0 . 0 0 0 1 2 \omega^ {3} + 4 5 \omega)} \tag {9.38}$$

![](image/2016dba9d256fcddc5bb840e9381ab10af527bca7c85ed5e0e0d57c0f93e5207.jpg)

<details>
<summary>flowchart</summary>
