# 6.3 Selection of Weighting Functions

The selection of weighting functions for a specific design problem often involves ad hoc fixing, many iterations, and fine tuning. It is very hard to give a general formula for the weighting functions that will work in every case. Nevertheless, we shall try to give some guidelines in this section by looking at a typical SISO problem.

Consider an SISO feedback system shown in Figure 6.1. Then the tracking error is $e = r - y = S ( r - d ) + T n - S P d _ { i }$ . So, as we have discussed earlier, we must keep |S| small over a range of frequencies, typically low frequencies where r and d are significant. To motivate the choice of our performance weighting function $W _ { e }$ , let $L = P K$ be a standard second-order system

$$L = \frac {\omega_ {n} ^ {2}}{s (s + 2 \xi \omega_ {n})}$$

It is well-known from the classical control theory that the quality of the (step) time response can be quantified by rise time $t _ { r }$ , settling time $t _ { s } ,$ and percent overshoot $1 0 0 M _ { p } \%$ . Furthermore, these performance indices can be approximately calculated as

$$t _ {r} \approx \frac {0 . 6 + 2 . 1 6 \xi}{\omega_ {n}}, 0. 3 \leq \xi \leq 0. 8; t _ {s} \approx \frac {4}{\xi \omega_ {n}}; M _ {p} = e ^ {- \frac {\pi \xi}{\sqrt {1 - \xi^ {2}}}}, 0 < \xi < 1$$

The key points to note are that (1) the speed of the system response is proportional to $\omega _ { n }$ and (2) the overshoot of the system response is determined only by the damping ratio ξ. It is well known that the frequency $\omega _ { n }$ and the damping ratio $\xi$ can be essentially captured in the frequency domain by the open-loop crossover frequency and the phase margin or the bandwidth and the resonant peak of the closed-loop complementary sensitivity function T .

Since our performance objectives are closely related to the sensitivity function, we shall consider in some detail how these time domain indices or, equivalently, $\omega _ { n }$ and ξ are related to the frequency response of the sensitivity function

$$S = \frac {1}{1 + L} = \frac {s (s + 2 \xi \omega_ {n})}{s ^ {2} + 2 \xi \omega_ {n} s + \omega_ {n} ^ {2}}$$

![](image/7f18f1a188fea355d046e6a21959bcb60fbe32ad6ddf78debfb9633e278e4ffb.jpg)

<details>
<summary>line</summary>
