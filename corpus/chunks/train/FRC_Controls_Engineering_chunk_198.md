# 7.6 Pole placement

This is the practice of placing the poles of a closed-loop system directly to produce a desired response. Python Control offers several pole placement algorithms for generating controller or observer gains from a set of poles.

Since all our applications will be discrete systems, we’ll place poles in the discrete domain (the z-plane). The s-plane’s LHP maps to the inside of a unit circle (see figure 7.7).

Pole placement should only be used if you know what you’re doing. It’s much easier to let LQR place the poles for you, which we’ll discuss next.

![](image/e501bfd5ed74f9921728d4da3c1838c2419d62072bb00bc04e2d2c07be425d87.jpg)

<details>
<summary>heatmap</summary>

| Re | Im |
| --- | --- |
| -6 | 3 |
| -5 | 2 |
| -4 | 1 |
| -3 | 0 |
| -2 | -1 |
| -1 | -2 |
| 0 | -3 |
</details>

![](image/9f6f906bdb734fcdc973424b9fc1394e732c82453b8a0d80384a92882e13a9d5.jpg)

<details>
<summary>radar</summary>

| Re | Im |
| --- | --- |
| -1.0 | 0.0 |
| -0.5 | 0.25 |
| 0.0 | 0.5 |
| 0.5 | 0.75 |
| 1.0 | 1.0 |
</details>

Figure 7.7: Mapping of complex plane from continuous (left) to discrete (right)
