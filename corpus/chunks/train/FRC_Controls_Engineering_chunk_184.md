# 7.1.2 Discrete system behavior

Figure 7.2 shows the impulse responses in the time domain for systems with various pole locations in the complex plane (real numbers on the x-axis and imaginary numbers on the y-axis). Each response has an initial condition of 1.

![](image/f669a3601a8fc62aa32c49b03c657564f702df3826715c74711439fe29a9a9d2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Unstable"] --> B["LHP"]
    B --> C["RHP"]
    C --> D["Re"]
    D --> E["Stable"]
    E --> F["Unstable"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
```
</details>

Figure 7.2: Discrete impulse response vs pole location

As ω increases in $s = j \omega$ , a pole in the discrete plane moves around the perimeter of the unit circle. Once it hits $\frac { \omega _ { s } } { 2 }$ (half the sampling frequency) at (−1, 0), the pole wraps around. This is due to poles faster than the sample frequency folding down to below the sample frequency (that is, higher frequency signals alias to lower frequency ones).

Placing the poles at (0, 0) produces a deadbeat controller. An $\mathrm { N } ^ { \mathrm { t h } }$ -order deadbeat controller decays to the reference in N timesteps. While this sounds great, there are other considerations like control effort, robustness, and noise immunity.

Poles in the left half-plane cause jagged outputs because the frequency of the system dynamics is above the Nyquist frequency (twice the sample frequency). The discretized signal doesn’t have enough samples to reconstruct the continuous system’s dynamics. See figures 7.3 and 7.4 for examples.

![](image/dcd98874c307829720c073f53ff46fcf0f76be04e2b31fc1575540c068ed9b4d.jpg)

<details>
<summary>line</summary>

| Time (s) | Single pole in RHP | Single pole in LHP |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 2.5 | 0.6 |
| 2 | 2.5 | 0.6 |
| 3 | 2.5 | 0.6 |
| 4 | 2.5 | 0.6 |
| 5 | 2.5 | 0.6 |
| 6 | 2.5 | 0.6 |
</details>

Figure 7.3: Single poles in various locations in discrete plane

![](image/02bf19ff5f300aac300895726d896c81db0c5debededf172844e3fc1eabfe445.jpg)

<details>
<summary>line</summary>

| Time (s) | Complex conjugate poles in LHP | Complex conjugate poles in RHP |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 0.5 | 0.5 | 3.0 |
| 1.0 | 0.6 | 1.5 |
| 1.5 | 0.4 | 2.2 |
| 2.0 | 0.4 | 1.8 |
| 2.5 | 0.4 | 1.9 |
| 3.0 | 0.4 | 1.9 |
| 3.5 | 0.4 | 1.9 |
| 4.0 | 0.4 | 1.9 |
| 4.5 | 0.4 | 1.9 |
| 5.0 | 0.4 | 1.9 |
| 5.5 | 0.4 | 1.9 |
| 6.0 | 0.4 | 1.9 |
</details>

Figure 7.4: Complex conjugate poles in various locations in discrete plane
