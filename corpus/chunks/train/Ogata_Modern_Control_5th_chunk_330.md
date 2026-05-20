```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["\frac{10}{s(s+1)}"]
    C --> D["C(s)"]
    D --> E["G(s)"]
    E --> B
```
</details>

(a)

![](image/b63172d94de06222be8fad87bc0e2ce47f4f0093989569793452628d42ce7c80.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -1 | -j3 |
| -1 | -j1 |
| -1 | -j2 |
| -1 | -j3 |
| -1 | -j1 |
| -1 | -j2 |
| -1 | -j3 |
</details>

(b)

The closed-loop poles are located at

$$s = - 0. 5 \pm j 3. 1 2 2 5$$

The damping ratio of the closed-loop poles is $\zeta = ( 1 / 2 ) / \sqrt { 1 0 } = 0 . 1 5 8 1$ .The undamped natural frequency of the closed-loop poles is $\omega _ { n } = \bigvee 1 0 = 3 . 1 6 2 3 \mathrm { r a d / s e c }$ . Because the damping ratio is small, this system will have a large overshoot in the step response and is not desirable.

It is desired to design a lead compensator $G _ { c } ( s )$ as shown in Figure 6–40(a) so that the dominant closed-loop poles have the damping ratio $\zeta = 0 . 5$ and the undamped natural frequency $\omega _ { n } = 3 \mathrm { r a d / s e c }$ The desired location of the dominant closed-loop poles can be determined from.

$$s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2} = s ^ {2} + 3 s + 9= (s + 1. 5 + j 2. 5 9 8 1) (s + 1. 5 - j 2. 5 9 8 1)$$

as follows:

$$s = - 1. 5 \pm j 2. 5 9 8 1$$

![](image/47f972c5371a8c570ace59758250721b5d4d3fd803dda4d8c46f902f7b2afeaa.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["Gc(s)"]
    C --> D["10/(s(s+1))"]
    D --> E["C(s)"]
    E --> F["G(s)"]
    F --> B
```
</details>

Figure 6–40   
(a) Compensated system; (b) desired closed-loop pole location.

(a)   
![](image/e6756ec1febc47b83af3c366c8058c9db0648e38c7f28d4d5793b905d928dc87.jpg)

<details>
<summary>line</summary>

| σ | jω |
| --- | --- |
| -1.5 | j2.5981 |
| 0 | 0 |
</details>

[See Figure 6–40 (b).] In some cases, after the root loci of the original system have been obtained, the dominant closed-loop poles may be moved to the desired location by simple gain adjustment. This is, however, not the case for the present system. Therefore, we shall insert a lead compensator in the feedforward path.
