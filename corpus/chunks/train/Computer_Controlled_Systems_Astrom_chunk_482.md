is sampled with $h = \pi/3\omega_{0}$ . Determine the frequencies $f, 0 \leq f \leq 3\omega_{0}/2\pi$ that are represented in the sampled signal.

7.10 Find $Y^{*}$ for the systems in Fig. 7.37.

![](image/9203d3f6755cfdde49c44a5749f55182aee511d309892dec438d15c88b7dfd23.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u"] --> B["ZOH"]
    B --> C["G₁"]
    C --> D["ZOH"]
    D --> E["G₂"]
    E --> F["y*"]
```
</details>

![](image/a8de714ac10ecfb370b74bea7cb2c94a975ee86f2638823af7930fecd41e1bda.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u"] --> B["ZOH"]
    B --> C["G₁"]
    C --> D["G₂"]
    D --> E["y*"]
```
</details>

![](image/58a72ea999a566cde4235fb660a200feab5dad71cf899a8446fa47d005c65db5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    u --> ZOH
    ZOH --> Σ
    Σ --> G
    G --> y*
    Σ --> ZOH
    ZOH --> -H
    -H --> Σ
```
</details>

Figure 7.37

7.11 Write a program to compute the frequency response of a sampled-data system. Let the following be the input to the program:

(a) The polynomials in the pulse-transfer function $H(z)$ .   
(b) The sampling interval.   
(c) The maximum and minimum frequencies.

Use the program to plot $H(\exp(i\omega h))$ for the normalized motor sampled with a zero-order hold and compare with the continuous-time system.
