Design of ${ \bf \dot { \boldsymbol { G } } } _ { c 1 } ( \boldsymbol { s } )$ First, note that we assumed the noise input: $N ( s )$ to be zero. To obtain the response to the step-disturbance input, we assume that the reference input is zero. Then the block diagram which relates $Y ( s )$ and $D ( s )$ can be drawn as shown in Figure 8–40. The transfer function $Y ( s ) / D ( s )$ is given by

$$\frac {Y (s)}{D (s)} = \frac {G _ {p}}{1 + G _ {c 1} G _ {p}}$$

![](image/d2ee33bf6a26457b4551df3992372280d200450ba7975365d1b4e600152a27fc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    D["s"] --> |+| Sum
    Sum --> Gp["G_p(s)"]
    Gp --> Y["s"]
    Y["s"] --> |G_c1(s)| Sum
    Sum --> Gp
```
</details>

Figure 8–40 Control system.

where

$$G _ {c 1} (s) = K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right)$$

This controller involves one pole at the origin and two zeros. If we assume that the two zeros are located at the same place (a double zero), then $G _ { c 1 } ( s )$ can be written as

$$G _ {c 1} (s) = K \frac {(s + a) ^ {2}}{s}$$

Then the characteristic equation for the system becomes

$$1 + G _ {c 1} (s) G _ {p} (s) = 1 + \frac {K (s + a) ^ {2}}{s} \frac {5}{(s + 1) (s + 5)} = 0$$

or

$$s (s + 1) (s + 5) + 5 K (s + a) ^ {2} = 0$$

which can be rewritten as

$$s ^ {3} + (6 + 5 K) s ^ {2} + (5 + 1 0 K a) s + 5 K a ^ {2} = 0 \tag {8-8}$$

If we place the double zero between s=–3 and s=–6, then the root-locus plot of $G _ { c 1 } ( s ) G _ { p } ( s )$ may look like the one shown in Figure 8–41. The speed of response should be fast, but not faster than necessary, because faster response generally implies larger or more expensive components. Therefore, we may choose the dominant closed-loop poles at

$$s = - 3 \pm j 2$$

(Note that this choice is not unique. There are infinitely many possible closed-loop poles that we may choose from.)

Since the system is of third order, there are three closed-loop poles. The third one is located on the negative real axis to the left of point $s = - 5$ .

Let us substitute $s = - 3 + j 2$ into Equation (8–8).

$$(- 3 + j 2) ^ {3} + (6 + 5 K) (- 3 + j 2) ^ {2} + (5 + 1 0 K a) (- 3 + j 2) + 5 K a ^ {2} = 0$$

![](image/a68579bb1b8467c07b923950088e0a27c86bb7e1a51723cf51fdd76f2db33e66.jpg)

<details>
<summary>contour</summary>
