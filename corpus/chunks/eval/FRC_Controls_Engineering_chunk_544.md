# E.4.2 Discrete system behavior

Figure E.18 shows the impulse responses in the time domain for systems with various pole locations in the complex plane (real numbers on the x-axis and imaginary numbers on the y-axis). Each response has an initial condition of 1.

![](image/b4cb1da453e0bf229894ddd0b833b4e9023e56c8be9a6bc27a1b0aa9c76ad8de.jpg)

<details>
<summary>heatmap</summary>

| Re   | Im  |
| ---- | --- |
| -6   | 3   |
| -5   | 2   |
| -4   | 1   |
| -3   | 0   |
| -2   | -1  |
| -1   | -2  |
| 0    | -3  |
</details>

![](image/126ce50a958473fb431a94c958a9a9646f7b017c9e6f8ac860611e7ecc22d3f6.jpg)

<details>
<summary>radar</summary>

| Re    | Im    |
|-------|-------|
| -1.0  | 0.0   |
| -0.5  | 0.25  |
| 0.0   | 0.5   |
| 0.5   | 0.75  |
| 1.0   | 1.0   |
</details>

Figure E.17: Mapping of complex plane from s-plane (left) to z-plane (right)

As ω increases in $s = j \omega$ , a pole in the z-plane moves around the perimeter of the unit circle. Once it hits $\frac { \omega _ { s } } { 2 }$ (half the sampling frequency) at (−1, 0), the pole wraps around. This is due to poles faster than the sample frequency folding down to below the sample frequency (that is, higher frequency signals alias to lower frequency ones).

Placing the poles at (0, 0) produces a deadbeat controller. An $\mathrm { N } ^ { \mathrm { t h } }$ -order deadbeat controller decays to the reference in N timesteps. While this sounds great, there are other considerations like control effort, robustness, and noise immunity.

Poles in the left half-plane cause jagged outputs because the frequency of the system dynamics is above the Nyquist frequency (twice the sample frequency). The discretized signal doesn’t have enough samples to reconstruct the continuous system’s dynamics. See figures E.19 and E.20 for examples.

![](image/03510d0abda56dc430cebac5739df1ea6e36e1fd943979ccdf16b44fd5eb0d00.jpg)

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

Figure E.18: Discrete impulse response vs pole location

![](image/189fa865e78918e81d24daffe74bc9f87247f2458cef3b78605d82c5075ffd7c.jpg)

<details>
<summary>line</summary>
