# The Nyquist Criterion

The Nyquist criterion is a well-known stability test for continuous-time systems. It is based on the principle of arguments. The Nyquist criterion is especially useful for determining the stability of the closed-loop system when the open-loop system is given. The test can easily be reformulated to handle discrete-time systems.

Consider the discrete-time system in Fig. 3.5. The closed-loop system has the pulse-transfer function

$$H _ {c l} (z) = \frac {Y (z)}{U _ {c} (z)} = \frac {H (z)}{1 + H (z)}$$

![](image/1bd3db7deab5f31abbf6c1b0fba0ccaa44d90177f41da21e6a234e7484993b82.jpg)

<details>
<summary>line</summary>

| Real axis | Imaginary axis (Solid Line) | Imaginary axis (Dashed Line) |
| --- | --- | --- |
| -0.5 | ~0.0 | ~0.0 |
| 0.0 | ~-0.8 | ~-0.6 |
| 0.5 | ~-0.7 | ~-0.5 |
| 1.0 | ~0.0 | ~0.0 |
</details>

Figure 3.3 The frequency curve of (3.6) (dashed) and for (3.6) sampled with zero-order hold when h = 0.4 (solid).

![](image/2701c1fbd5566529711df204ee5d32f0e6a7e7fb042274fe7b9d3ec777815aa3.jpg)

<details>
<summary>line</summary>

| Frequency, rad/s | Gain (Solid Line) | Gain (Dashed Line) | Phase (Solid Line) | Phase (Dashed Line) |
| --- | --- | --- | --- | --- |
| 0.1 | 1.0 | 1.0 | 0.0 | 0.0 |
| 1.0 | ~0.5 | ~0.5 | ~-50 | ~-50 |
| 10.0 | ~0.01 | ~0.01 | ~-180 | ~-180 |
</details>

Figure 3.4 The Bode diagram of (3.6) (dashed) and of (3.6) sampled with zero-order hold when h = 0.4 (solid).

![](image/91e19a067d3d30d44b716f52c59a8a55a755b40f9c562557f69f90a3971fcb58.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["u_c"] --> B["Σ"]
    B --> C["H(z)"]
    C --> D["y"]
    D --> E["-1"]
    E --> B
    B --> F["e"]
```
</details>

Figure 3.5 A simple unit-feedback system.

The characteristic equation of the closed-loop system is

$$1 + H (z) = 0 \tag {3.7}$$
