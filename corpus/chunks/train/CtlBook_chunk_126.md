# Example 5.2

Find the poles of the transfer function,

$$G (s) = \frac {4 0 0}{1 2 . 7 s ^ {2} + 3 0 4 . 8 s + 2 6 4 1 . 6}$$

and plot the step response by computer.

Applying the quadratic formula to get the roots of the denominator:

$$\{a, b \} = \frac {- 3 0 4 . 8 \pm \sqrt {3 0 4 . 8 ^ {2} - 4 \times 1 2 . 7 \times 2 6 4 1 . 6}}{2 \times 1 2 . 7}\{a, b \} = \{(- 1 2 + j 8), (- 1 2 - j 8) \}$$

In this case the poles are complex numbers.

Note that these numbers were kind of messy. This illustrates a good reason to normalize the denominator polynomial. Lets do the problem again but with a normalized denominator:

$$G (s) = \frac {3 . 1 5}{s ^ {2} + 2 4 s + 2 0 8}$$

Applying the quadratic formula to get the roots of the denominator:

$$\{a, b \} = \frac {2 4 \pm \sqrt {2 4 ^ {2} - 4 \times 2 0 8}}{2}$$

This is simplied because the $s ^ { 2 }$ coecient $( ^ { \ell } a ^ { \prime }$ in the quadratic formula) is one. The result is the same.

$$\{a, b \} = \{(- 1 2 + j 8), (- 1 2 - j 8) \}$$

Plotting the step response by computer:

![](image/74181fe62d71e6276dc4cbf6246d818f1c0b20dac2169305981ea8d02b66069e.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 1.0 |
| 0.2 | 1.6 |
| 0.3 | 1.9 |
| 0.4 | 1.95 |
| 0.5 | 1.95 |
| 0.6 | 1.95 |
| 0.7 | 1.95 |
| 0.8 | 1.95 |
| 0.9 | 1.95 |
| 1.0 | 1.95 |
</details>

There are lots of ways we could express the simple polynomial in the denominator of G(s) and we'll play around with a few:

$$G (s) = \frac {1}{s ^ {2} + u s + v} \qquad (u = - (a + b), \quad v = a b)$$

Now let's introduce a parameter $\omega _ { n }$ (pronounced omega-n):

$$\omega_ {n} = \sqrt {v} = \sqrt {a b}$$

and another one, $\zeta \ ^ { ( \mathrm { 6 } \mathfrak { c } _ { \mathrm { Z e t a } } , \mathfrak { Y } ) }$ :

$$\zeta = \frac {u}{2 \sqrt {v}} = \frac {- (a + b)}{2 \sqrt {a b}}$$

![](image/21ea66ebc73ae7a0b006cacdc20ca82b002cadda207af2ed535cdb3a82cd022b.jpg)

<details>
<summary>text_image</summary>

a → x
b → x
Re ⇒
- ωn
Im
ωd
ωn
θ → g = cos θ
Re
</details>

Figure 5.1: Complex conjugate poles in the complex plane can be represented in Cartesian Coordinates $( \sigma \dot { + } j \omega )$ or polar coordinates $\{ \zeta , \dot { \omega } _ { n } \}$

if we make these substitions, our transfer function becomes

$$G (s) = \frac {1}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

So far this is just playing around with notation. The point however is that ζ and $\omega _ { n } ,$ called the damping ratio and natural frequency respectively, give important insights not obvious from the poles (a, b) themselves.
