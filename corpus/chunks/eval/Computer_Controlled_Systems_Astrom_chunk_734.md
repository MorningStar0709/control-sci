# Example 12.9 Minimum-variance control with unstable process zero

Consider the system in Example 12.8 where $d = 1$ and

$$
\begin{array}{l} \boldsymbol {B} ^ {+} (z) = 1 \\ \boldsymbol {B} ^ {-} (z) = \boldsymbol {B} (z) \\ B ^ {- *} (z) = z + 0. 9 \\ \end{array}
$$

Equation (12.32) becomes

$$z (z - 0. 7) (z + 0. 9) = (z - 1) (z - 0. 7) \left(z + f _ {1}\right) + (0. 9 z + 1) \left(g _ {0} z + g _ {1}\right)$$

Let $z = 0.7$ , $z = 1$ , and $z = -10 / 9$ . This gives

$$
\begin{array}{l} 0. 7 g _ {0} + g _ {1} = 0 \\ g _ {0} + g _ {1} = 0. 3 \\ f _ {1} = 1 \\ \end{array}
$$

The control law thus becomes

$$u (k) = - \frac {G (q)}{B ^ {+} (q) F (q)} y (k) = - \frac {q - 0 . 7}{q + 1} y (k)$$

The output is

$$y (k) = \frac {F (q)}{B ^ {- *} (q)} e (k - d + 1) = \frac {q + 1}{q + 0 . 9} e (k) = e (k) + \frac {0 . 1}{q + 0 . 9} e (k)$$

The variance of the output is

$$\mathrm{E} y ^ {2} = \left(1 + \frac {0 . 1 ^ {2}}{1 - 0 . 9 ^ {2}}\right) \sigma^ {2} = \frac {2 0}{1 9} \sigma^ {2} = 1. 0 5 \sigma^ {2}$$

which is about 5% larger than using the controller in Example 12.8. The variance of the control signal is $275\sigma^{2}/19 = 14.47\sigma^{2}$ . A simulation of the control law is shown in Fig. 12.6. The figure that the controller performs well. Compare also with Fig. 12.5, which shows the effect of canceling the unstable zero. Figure 12.7 shows the accumulated output loss $\sum y^{2}(k)$ and input loss $\sum u^{2}(k)$ when the controllers in Example 12.8 and this example are used. The controller (12.27) gives lower output loss, but an exponentially growing input loss, and the controller based on (12.31) gives an accumulated input loss that grows linearly with time.

![](image/64a78c56739ef24fce04004fa0f24d33d4f77059cd9c2202df88b1e3ac148a96.jpg)  
Figure 12.6 Simulation of the system in Example 12.9.

![](image/80b510b4643ba65134541f7aeafc54c748a2d5b9584a20c9048062a05d6504be.jpg)  
Figure 12.7 The accumulated output loss $\sum y^{2}(k)$ and input loss $\sum u^{2}(k)$ when the controllers (12.31) (solid) and (12.27) (dashed) are used.
