<details>
<summary>line</summary>

| t | x(t) |
| --- | --- |
| 0 | 0.0095 |
| 2 | 0.1000 |
</details>

(b)   
Figure 5–54   
(a) Mechanical vibratory system; (b) step-response curve.

Hence

$$k = 2 0 \mathrm{lb} _ {\mathrm{f}} / \mathrm{ft}$$

Note that $M _ { p } = 9 . 5 \%$ corresponds to $\zeta = 0 . 6 .$ . The peak time $t _ { p }$ is given by

$$t _ {p} = \frac {\pi}{\omega_ {d}} = \frac {\pi}{\omega_ {n} \sqrt {1 - \zeta^ {2}}} = \frac {\pi}{0 . 8 \omega_ {n}}$$

The experimental curve shows that $t _ { p } = 2$ sec. Therefore,

$$\omega_ {n} = \frac {3 . 1 4}{2 \times 0 . 8} = 1. 9 6 \mathrm{rad/sec}$$

Since $\omega _ { n } ^ { 2 } = k / m = 2 0 / m$ , we obtain

$$m = \frac {2 0}{\omega_ {n} ^ {2}} = \frac {2 0}{1 . 9 6 ^ {2}} = 5. 2 \mathrm{slugs} = 1 6 7 \mathrm{lb}$$

(Note that 1 slug=1 $\mathrm { l b } _ { \mathrm { f } } { \mathrm { - s e c } } ^ { 2 } / \mathrm { f t } . )$ Then b is determined from

$$2 \zeta \omega_ {n} = \frac {b}{m}$$

or

$$b = 2 \zeta \omega_ {n} m = 2 \times 0. 6 \times 1. 9 6 \times 5. 2 = 1 2. 2 \mathrm{lb} _ {\mathrm{f}} / \mathrm{ft} / \sec$$

A–5–6. Consider the unit-step response of the second-order system

$$\frac {C (s)}{R (s)} = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

The amplitude of the exponentially damped sinusoid changes as a geometric series. At time $t = t _ { p } = \pi / \omega _ { d } .$ , the amplitude is equal to $e ^ { - ( \sigma / \omega _ { d } ) \pi }$ After one oscillation, or at. $t = t _ { p } + 2 \pi / \omega _ { d } = 3 \pi / \omega _ { d } .$ the amplitude is equal to $e ^ { - ( \sigma / \omega _ { d } ) 3 \pi }$ after another cycle of oscillation, the; amplitude is $e ^ { - ( \sigma / \omega _ { d } ) 5 \pi }$ The logarithm of the ratio of successive amplitudes is called the logarithmic. decrement. Determine the logarithmic decrement for this second-order system. Describe a method for experimental determination of the damping ratio from the rate of decay of the oscillation.

Solution. Let us define the amplitude of the output oscillation at $t = t _ { i }$ to be $x _ { i } ,$ , where $t _ { i } = t _ { p } + ( i - 1 ) T ( T =$ period of oscillation). The amplitude ratio per one period of damped oscillation is

$$\frac {x _ {1}}{x _ {2}} = \frac {e ^ {- (\sigma / \omega_ {d}) \pi}}{e ^ {- (\sigma / \omega_ {d}) 3 \pi}} = e ^ {2 (\sigma / \omega_ {d}) \pi} = e ^ {2 \zeta \pi / \sqrt {1 - \zeta^ {2}}}$$

Thus, the logarithmic decrement d is

$$\delta = \ln \frac {x _ {1}}{x _ {2}} = \frac {2 \zeta \pi}{\sqrt {1 - \zeta^ {2}}}$$
