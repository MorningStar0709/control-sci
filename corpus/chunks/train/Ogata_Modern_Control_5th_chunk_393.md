$$\omega = \pm 3 \sqrt {2}, \quad K = 9 \omega^ {2} = 1 6 2 \quad \text { or } \quad \omega = 0, \quad K = 0$$

The crossing points are at $\omega = \pm 3 \sqrt { 2 }$ and the corresponding value of gain K is 162. Also, a rootlocus branch touches the imaginary axis at v=0. Figure 6–98(b) shows a sketch of the root loci for the system.

Since the damping ratio of the dominant closed-loop poles is specified as 0.5, the desired closed-loop pole in the upper-half s plane is located at the intersection of the root-locus branch in the upper-half s plane and a straight line having an angle of $6 0 ^ { \circ }$ with the negative real axis.The desired dominant closed-loop poles are located at

$$s = - 1 + j 1. 7 3 2, \quad s = - 1 - j 1. 7 3 2$$

At these points, the value of gain K is 28. Hence,

$$a = \frac {K}{1 0} = 2. 8$$

Since the system involves two or more poles than zeros (in fact, three poles and no zero), the third pole can be located on the negative real axis from the fact that the sum of the three closedloop poles is –9. Hence, the third pole is found to be at

$$s = - 9 - (- 1 + j 1. 7 3 2) - (- 1 - j 1. 7 3 2)$$

or

$$s = - 7$$

A–6–20. Consider the system shown in Figure 6–99(a). Sketch the root loci of the system as the velocity feedback gain k varies from zero to infinity. Determine the value of k such that the closed-loop poles have the damping ratio z of 0.7.

Solution. The open-loop transfer function is

$$\text { Open - loop transfer function } = \frac {1 0}{(s + 1 + 1 0 k) s}$$

Since k is not a multilying factor, we modify the equation such that k appears as a multiplying factor. Since the characteristic equation is

$$s ^ {2} + s + 1 0 k s + 1 0 = 0$$

we rewrite this equation as follows:

$$1 + \frac {1 0 k s}{s ^ {2} + s + 1 0} = 0 \tag {6-38}$$

Define

$$1 0 k = K$$

Then Equation (6–38) becomes

$$1 + \frac {K s}{s ^ {2} + s + 1 0} = 0$$

![](image/443976066359cc183037a2e3645e4a3ad1b8e20311e59c307920a95de859585b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| Sum1["+"]
    Sum1 --> |+| Sum2["+"]
    Sum2 --> |10/(s+1)| A["10/(s)"]
    A --> |1/s| C["s"]
    C["s"] --> |k| Sum1
    C["s"] --> |k| Sum2
```
</details>

(a)

![](image/54a72a5a1ce556323b751695cb4acca1814a31030760ac463f5e8b3b4ebbcd75.jpg)

<details>
<summary>other</summary>

| Point | σ | jω |
| --- | --- | --- |
| K | 3.427 | 3.427 |
| 45.57° | -2 | 45.57 |
</details>

(b)   
Figure 6–99   
(a) Control system; (b) root-locus plot, where K=10k.
