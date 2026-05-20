# EXAMPLE 6–10

Consider the system shown in Figure 6–61. Draw a root-locus diagram.Then determine the value of k such that the damping ratio of the dominant closed-loop poles is 0.4.

Here the system involves velocity feedback. The open-loop transfer function is

$$\text { Open - loop transfer function } = \frac {2 0}{s (s + 1) (s + 4) + 2 0 k s}$$

![](image/9ed35c50fd3db5fc335801bd0b2528f2bae1bd4648d92fe0bf90ed57a7b53caf.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> |+| A["×"]
    A --> |+| B["×"]
    B --> |20/(s+1)(s+4)| C["1/s"]
    C --> C["s"]
    C --> D["k"]
    D --> A
```
</details>

Figure 6–61 Control system.

Notice that the adjustable variable k does not appear as a multiplying factor. The characteristic equation for the system is

$$s ^ {3} + 5 s ^ {2} + 4 s + 2 0 k s + 2 0 = 0 \tag {6-26}$$

Define

$$2 0 k = K$$

Then Equation (6–26) becomes

$$s ^ {3} + 5 s ^ {2} + 4 s + K s + 2 0 = 0 \tag {6-27}$$

Dividing both sides of Equation (6–27) by the sum of the terms that do not contain K, we get

$$1 + \frac {K s}{s ^ {3} + 5 s ^ {2} + 4 s + 2 0} = 0$$

or

$$1 + \frac {K s}{(s + j 2) (s - j 2) (s + 5)} = 0 \tag {6-28}$$

Equation (6–28) is of the form of Equation (6–11).

We shall now sketch the root loci of the system given by Equation (6–28). Notice that the open-loop poles are located at $s = j 2 , s = - j 2 , s = - 5 ,$ , and the open-loop zero is located at s=0. The root locus exists on the real axis between 0 and –5. Since

$$\lim _ {s \rightarrow \infty} \frac {K s}{(s + j 2) (s - j 2) (s + 5)} = \lim _ {s \rightarrow \infty} \frac {K}{s ^ {2}}$$

we have

$$\text { Angles of asymptote } = \frac {\pm 1 8 0 ^ {\circ} (2 k + 1)}{2} = \pm 9 0 ^ {\circ}$$

The intersection of the asymptotes with the real axis can be found from

$$\lim _ {s \rightarrow \infty} \frac {K s}{s ^ {3} + 5 s ^ {2} + 4 s + 2 0} = \lim _ {s \rightarrow \infty} \frac {K}{s ^ {2} + 5 s + \cdots} = \lim _ {s \rightarrow \infty} \frac {K}{(s + 2 . 5) ^ {2}}$$

as

$$s = - 2. 5$$

The angle of departure (angle u) from the pole at $s = j 2$ is obtained as follows:

$$\theta = 1 8 0 ^ {\circ} - 9 0 ^ {\circ} - 2 1. 8 ^ {\circ} + 9 0 ^ {\circ} = 1 5 8. 2 ^ {\circ}$$

Thus, the angle of departure from the pole $s = j 2$ is 158.2°. Figure 6–62 shows a root-locus plot for the system. Notice that two branches of the root locus originate from the poles at $s = \pm j 2$ and terminate on the zeros at infinity. The remaining one branch originates from the pole at $s = - 5$ and terminates on the zero at s=0.
