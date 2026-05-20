# 9.5 The Closed Loop Design Problem

The design problem of closed loop controllers2 can be summarized as follows (Assume for simplicity that $H = 1 )$ .

Given a plant: $P ( s )$ , specify a controller, $C ( s )$ , for a closed loop system to meet some performance measure requirements compared to the open loop system, $\bar { \boldsymbol { P } } ( \bar { s } )$ . Where the closed loop response is governed by C(s)P (s)1+C(s)P (s) $\frac { C ( s ) P ( s ) } { 1 + C ( s ) P ( s ) }$

![](image/24e04b567aecfd860bcf9817a4b1dd8ff18b9bddf319c019395781061a2e0224.jpg)

<details>
<summary>text_image</summary>

INK BIRO
134.5 PV
122.0
OUT ALM RUN SV
AT/RUN
SET
</details>

Figure 9.7: Commercial PID temperature controller module. \$39.95 on Amazon.com (May 2025).

There are many generic transfer function types which have been used as controllers. Among the most common are:

<table><tr><td>Name</td><td>Transfer Function</td><td>Notes</td></tr><tr><td>Constant Gain</td><td>C(s) = K</td><td>Very simple!</td></tr><tr><td>Lead-Lag</td><td>C(s) =  $\frac{K(s+z)}{(s+p)}$ </td><td>Gain with one added pole and zero. Pole can reduce SSE, zero can increase stability.</td></tr><tr><td>PID</td><td>C(s) =  $\frac{K(s+z1)(s+z2)}{s}$ </td><td>“Proportional-Integral-Derivative,” three parameters to tune: pole at origin allows zero steady state error, zeros can “pull” plant poles where you want them. (usually requires a “regularization” pole.)</td></tr><tr><td>PD</td><td>C(s) = K(s + z1)</td><td>Removes the integral term from PID. Can increase stability relative to PID. Also may require regularization.</td></tr></table>

We will focus on the PID controller in the material below because it is so widely used. However, sometimes the simpler controllers above can provide a simpler and better solution so keep them in mind as options. Our design process (below) works for them all.
