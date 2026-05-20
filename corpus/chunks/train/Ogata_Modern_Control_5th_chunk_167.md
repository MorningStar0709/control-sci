If the resistance $R _ { d }$ is removed (replaced by the line-sized tubing), what control action do we get? If the resistance $R _ { i }$ is removed (replaced by the line-sized tubing), what control action do we get?

Solution. Let us assume that when $e = 0$ the nozzle–flapper distance is equal to $\bar { X }$ and the control pressure is equal to $\hat { P } _ { c }$ In the present analysis, we shall assume small deviations from the. respective reference values as follows:

$$
\begin{array}{l} e = \text {   small   error   signal   } \\ x = \text {   small   change   in   the   nozzle - flapper   distance   } \\ \end{array}
p _ {c} = \text { small change in the control pressure }p _ {\mathrm{I}} = \text { small pressure change in bellows I due to small change in the control pressure }p _ {\mathrm{II}} = \text { small pressure change in bellows II due to small change in the control pressure }y = \text { small displacement at the lower end of the flapper }
$$

In this controller, $p _ { c }$ is transmitted to bellows I through the resistance $R _ { d }$ . Similarly, $p _ { c }$ is transmitted to bellows II through the series of resistances $R _ { d }$ and $R _ { i }$ .The relationship between $p _ { I }$ and $p _ { c }$ is

$$\frac {P _ {I} (s)}{P _ {c} (s)} = \frac {1}{R _ {d} C s + 1} = \frac {1}{T _ {d} s + 1}$$

where $T _ { d } = R _ { d } C = \mathrm { d e r i v a t i v e }$ time. Similarly, $p _ { \mathrm { I I } }$ and $p _ { \mathrm { I } }$ are related by the transfer function

$$\frac {P _ {\mathrm{II}} (s)}{P _ {\mathrm{I}} (s)} = \frac {1}{R _ {i} C s + 1} = \frac {1}{T _ {i} s + 1}$$

where $T _ { i } = R _ { i } C = \mathrm { i n t e g r a l }$ time. The force-balance equation for the two bellows is

$$\left(p _ {\mathrm{I}} - p _ {\mathrm{II}}\right) A = k _ {s} y$$

where $k _ { s }$ is the stiffness of the two connected bellows and A is the cross-sectional area of the bellows. The relationship among the variables e, x, and y is

$$x = \frac {b}{a + b} e - \frac {a}{a + b} y$$

The relationship between $p _ { c }$ and x is

$$p _ {c} = K x \quad (K > 0)$$

![](image/9287750fc7313771480c12b4fc85e89603fc9da29786295845c334cb66197243.jpg)

<details>
<summary>text_image</summary>

e
a
b
I
II
C
C
Ri
Rd
Ps
X̄ + x
P̄c + pI
P̄c + pII
P̄c + pc
</details>

Figure 4–30 Schematic diagram of a pneumatic controller.

From the equations just derived, a block diagram of the controller can be drawn, as shown in Figure 4–31(a). Simplification of this block diagram results in Figure 4–31(b).

The transfer function between $P _ { c } ( s )$ and $E ( s )$ is
