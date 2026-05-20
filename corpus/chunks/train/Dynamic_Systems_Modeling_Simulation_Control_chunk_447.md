$$\Omega (s) = \frac {2 5 0}{s} + \frac {- 1 3 0}{s + 0 . 1 5}$$

and taking the inverse Laplace transform of Ω(s) yields the angular velocity response of the rotor

$$\omega (t) = 2 5 0 - 1 3 0 e ^ {- 0. 1 5 t} \mathrm{rad/s} \tag {8.23}$$

As a check, note that $\omega ( 0 ) = 2 5 0 - 1 3 0 e ^ { 0 } = 1 2 0$ rad/s as specified in the problem statement. The steady-state velocity response is $\omega ( \infty ) = 2 5 0 - 1 3 0 e ^ { - \infty } = 2 5 0$ rad/s. Recall from Chapter 7 that the transient response of a first-order system “dies out” in about four time constants. For this problem, the time constant is $\tau = J / b = 6 . 6 6 7$ s and consequently the rotor reaches its steady-state velocity at about 26.67 s. The transient part of the complete response [Eq. (8.23)] i $- 1 3 0 e ^ { - 0 . 1 5 t }$ rad/s, which decays to a “small” value $( < 2 . 4 ~ \mathrm { r a d / s }$ , or less than 2% of its initial value) at time $t = 2 6 . 6 7 ~ \mathrm { s }$ .

We can verify the initial and steady-state values by applying the initial- and final-value theorems to the Laplace transform, Eq. (8.22):

$\mathrm { I n i t i a l \ v a l u e : } \quad \omega ( 0 + ) = \operatorname* { l i m } _ { s \to \infty } s \Omega ( s ) = \operatorname* { l i m } _ { s \to \infty } \frac { 1 2 0 s ^ { 2 } + 3 7 . 5 s } { s ^ { 2 } + 0 . 1 5 s } = 1 2 0 \mathrm { \ r a d / s }$ = 120 rad/s

${ \mathrm { F i n a l ~ v a l u e } } \colon \omega ( \infty ) = \operatorname* { l i m } _ { s \to 0 } s \Omega ( s ) = \operatorname* { l i m } _ { s \to 0 } { \frac { 1 2 0 s ^ { 2 } + 3 7 . 5 s } { s ^ { 2 } + 0 . 1 5 s } } = { \frac { 3 7 . 5 } { 0 . 1 5 } } = 2 5 0 { \mathrm { ~ r a d / s } }$

As a check, we can use the following MATLAB commands to compute the inverse Laplace transform of Eq. (8.22)

>> syms s    % define Laplace variable s
>> W = (120*s + 37.5) / (s^2 + 0.15*s)    % define Ω(s) (capital W)
>> w = ilaplace(W)    % inverse Laplace transform, ω(t)
>> pretty(w)    % display w in math typeset

The result is

$$- 1 3 0 \exp (- 3 / 2 0 t) + 2 5 0$$

which matches Eq. (8.23), the angular velocity solution for ??(t).

As a final note, consider reworking this example using the methods of Chapter 7 where we directly solved the ODE. To begin, we rewrite the I/O equation (8.21) in the “standard form” of a first-order system

$$\frac {J}{b} \dot {\omega} + \omega = \frac {1}{b} T _ {\mathrm{in}} (t) \tag {8.24}$$
