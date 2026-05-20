# EXAMPLE 5–2

For the system shown in Figure 5–13(a), determine the values of gain K and velocity-feedback constant $K _ { h }$ so that the maximum overshoot in the unit-step response is 0.2 and the peak time is 1 sec. With these values of K and $K _ { h }$ , obtain the rise time and settling time.Assume that $J = 1 \mathrm { k g } – \mathrm { m } ^ { 2 }$ and $B = 1 \mathrm { N } \mathrm { - m } / \mathrm { r a d } / \mathrm { s e c } .$ .

Determination of the values of K and $K _ { h }$ : The maximum overshoot $M _ { p }$ is given by Equation (5–21) as

$$M _ {p} = e ^ {- (\zeta / \sqrt {1 - \zeta^ {2}}) \pi}$$

This value must be 0.2. Thus,

$$e ^ {- (\zeta / \sqrt {1 - \zeta^ {2}}) \pi} = 0. 2$$

or

$$\frac {\zeta \pi}{\sqrt {1 - \zeta^ {2}}} = 1. 6 1$$

which yields

$$\zeta = 0. 4 5 6$$

The peak time $t _ { p }$ is specified as 1 sec; therefore, from Equation (5–20),

$$t _ {p} = \frac {\pi}{\omega_ {d}} = 1$$

or

$$\omega_ {d} = 3. 1 4$$

Since $\zeta$ is 0.456, $\omega _ { n }$ is

$$\omega_ {n} = \frac {\omega_ {d}}{\sqrt {1 - \zeta^ {2}}} = 3. 5 3$$

Since the natural frequency $\omega _ { n }$ is equal to $\sqrt { K / J }$ ,

$$K = J \omega_ {n} ^ {2} = \omega_ {n} ^ {2} = 1 2. 5 \mathrm{N-m}$$

Then $K _ { h }$ is, from Equation (5–25),

$$K _ {h} = \frac {2 \sqrt {K J} \zeta - B}{K} = \frac {2 \sqrt {K} \zeta - 1}{K} = 0. 1 7 8 \mathrm{sec}$$

Rise time $t _ { r } \colon$ From Equation (5–19), the rise time $t _ { r }$ is

$$t _ {r} = \frac {\pi - \beta}{\omega_ {d}}$$

where

$$\beta = \tan^ {- 1} \frac {\omega_ {d}}{\sigma} = \tan^ {- 1} 1. 9 5 = 1. 1 0$$

Thus, $t _ { r }$ is

$$t _ {r} = 0. 6 5 \mathrm{sec}$$

Settling time $t _ { s } \mathrm { : }$ : For the 2% criterion,

$$t _ {s} = \frac {4}{\sigma} = 2. 4 8 \mathrm{sec}$$

For the 5% criterion,

$$t _ {s} = \frac {3}{\sigma} = 1. 8 6 \mathrm{sec}$$

Impulse Response of Second-Order Systems. For a unit-impulse input $r ( t )$ , the corresponding Laplace transform is unity, or $R ( s ) = 1$ .The unit-impulse response C(s) of the second-order system shown in Figure 5-6 is

$$C (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}}$$

The inverse Laplace transform of this equation yields the time solution for the response $c ( t )$ as follows:

For $0 \leq \zeta < 1 .$ ,

$$c (t) = \frac {\omega_ {n}}{\sqrt {1 - \zeta^ {2}}} e ^ {- \zeta \omega_ {n} t} \sin \omega_ {n} \sqrt {1 - \zeta^ {2}} t, \quad \text { for } t \geq 0 \tag {5-26}$$

For z=1,

$$c (t) = \omega_ {n} ^ {2} t e ^ {- \omega_ {n} t}, \quad \text { for } t \geq 0 \tag {5-27}$$

$\operatorname { F o r } \zeta > 1 ,$
