# 6.8 Problems

Problem 6.1 Let P be an open-loop plant. It is desired to design a controller so that the overshoot $\leq 1 0 \%$ and settling time $\leq 1 0$ sec. Estimate the allowable peak sensitivity $M _ { s }$ and the closed-loop bandwidth.

Problem 6.2 Let ${ \cal L } _ { 1 } = \frac { 1 } { s ( s + 1 ) ^ { 2 } }$ be an open-loop transfer function of a unity feedback system. Find the phase margin, overshoot, settling time, and the corresponding $M _ { s }$ .

Problem 6.3 Repeat Problem 6.2 with

$$L _ {2} = \frac {1 0 0 (s + 1 0)}{(s + 1) (s + 2) (s + 2 0)}.$$

Problem 6.4 Let $P = \frac { 1 0 ( 1 - s ) } { s ( s + 1 0 ) }$ Use classical loop-shaping method to design a firstorder lead or lag controller so that the system has at least $3 0 ^ { \mathrm { o } }$ phase margin and as large a crossover frequency as possible.

Problem 6.5 Use the root locus method to show that a nonminimum phase system cannot be stabilized by a very high-gain controller.

Problem 6.6 Let $P = { \frac { 5 } { ( 1 - s ) ( s + 2 ) } }$ Design a lead or lag controller so that the system has at least $3 0 ^ { \mathrm { o } }$ phase margin with loop gain $\geq 2$ for any frequency $\omega \leq 0 . 1$ and the smallest possible bandwidth (or crossover frequency).

Problem 6.7 Use the root locus method to show that an unstable system cannot be stabilized by a very low gain controller.

Problem 6.8 Consider the unity-feedback loop with proper controller $K ( s )$ and strictly proper plant $P ( s )$ , both assumed square. Assume internal stability.

1. Let $w ( s )$ be a scalar weighting function, assumed in $\mathcal { R } \mathcal { H } _ { \infty }$ . Define

$$\epsilon = \| w (I + P K) ^ {- 1} \| _ {\infty}, \delta = \| K (I + P K) ^ {- 1} \| _ {\infty}$$

so  measures, say, disturbance attenuation and δ measures, say, control effort. Derive the following inequality, which shows that  and δ cannot both be small simultaneously in general. For every Re $s _ { 0 } \geq 0$

$$| w (s _ {0}) | \leq \epsilon + | w (s _ {0}) | \sigma_ {\min} [ P (s _ {0}) ] \delta .$$

2. If we want very good disturbance attenuation at a particular frequency, you might guess that we need high controller gain at that frequency. Fix ω with $j \omega$ not a pole of $P ( s )$ , and suppose

$$\epsilon := \sigma_ {\max} [ (I + P K) ^ {- 1} (j \omega) ] < 1.$$

Derive a lower bound for $\sigma _ { \mathrm { m i n } } [ K ( j \omega ) ]$ . This lower bound should blow up as $\epsilon \to 0$ .
