Figure 14.1: The closed-loop frequency responses of $\overline { { \sigma } } ( T _ { z w } )$ with K (solid line) and K˜ (dashed line)

![](image/1ebae9a22b89a64908a7b0ff5635325c17c3f7c8ac6223b7f150163e214661da.jpg)

<details>
<summary>line</summary>

| frequency (rad/sec) | T | KS | SP | S |
| --- | --- | --- | --- | --- |
| 0.01 | 1.0 | 0.1 | 0.1 | 0.01 |
| 0.1 | 1.0 | 0.1 | 0.1 | 0.01 |
| 1 | 1.0 | 0.5 | 0.5 | 0.1 |
| 10 | 1.0 | 1.0 | 1.0 | 1.0 |
| 100 | 1.0 | 0.5 | 0.5 | 0.1 |
| 1000 | 1.0 | 0.1 | 0.1 | 0.01 |
| 10000 | 1.0 | 0.01 | 0.01 | 0.001 |
</details>

Figure 14.2: The frequency responses of S, T, KS, and $S P$ with K

Example 14.2 Consider again the two-mass/spring/damper system shown in Figure 4.2. Assume that $F _ { 1 }$ is the control force, $F _ { 2 }$ is the disturbance force, and the measurements of $x _ { 1 }$ and $x _ { 2 }$ are corrupted by measurement noise:

$$
y = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + W _ {n} \left[ \begin{array}{c} n _ {1} \\ n _ {2} \end{array} \right], \quad W _ {n} = \left[ \begin{array}{c c} \frac {0 . 0 1 (s + 1 0)}{s + 1 0 0} & 0 \\ 0 & \frac {0 . 0 1 (s + 1 0)}{s + 1 0 0} \end{array} \right].
$$

Our objective is to design a control law so that the effect of the disturbance force $F _ { 2 }$ on the positions of the two masses, $x _ { 1 }$ and $x _ { 2 }$ , are reduced in a frequency range $0 \leq \omega \leq 2$ . The problem can be set up as shown in Figure 14.3, where $W _ { e } = \left\lceil \begin{array} { c c } { W _ { 1 } } & { 0 } \\ { 0 } & { W _ { 2 } } \end{array} \right\rceil$ is the performance weight and $W _ { u }$ is the control weight. In order to limit the control force, we shall choose

$$W _ {u} = \frac {s + 5}{s + 5 0}.$$

![](image/0a430d4d8a45e1bdf8f872fc1b38dfa91fb983b3e65d382ebe7fed9e1770524b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    y --> K
    K --> uF1["u = F1"]
    uF1 --> Plant
    Plant --> x1["x1"]
    Plant --> x2["x2"]
    x1 --> We
    x2 --> We
    We --> z1
    w2[" w2 = [ n1\n n2 "] ]
    Wn[" Wn "]
    Wu[" Wu "]
    z2[" z2 "]
    Plant --> w1["F2"]
```
</details>

Figure 14.3: Rejecting the disturbance force $F _ { 2 }$ by a feedback control

Now let $u = F _ { 1 } , w = { \left[ \begin{array} { l } { F _ { 2 } } \\ { n _ { 1 } } \\ { n _ { 2 } } \end{array} \right] }$ ; then the problem can be formulated in an LFT form with
