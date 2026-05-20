# Computational Aspects

The LQ-control law can be determined by a combination of spectral factorization and solution of linear Diophantine equations. Recall, however, the fundamental difficulty that arises from poor numerical conditioning of polynomial equations (see Sec. 9.6).

![](image/0c878d716a885c1e86c7b71f8d8f12d0b81a5c6e85ea1471bc65e9c7d97d694e.jpg)

<details>
<summary>line</summary>

| Time | Output variance (dotted) | Output variance (dash-dot) | Output variance (dashed) | Output variance (solid) |
| --- | --- | --- | --- | --- |
| 0 | ~3.8 | ~2.5 | ~2.0 | ~1.5 |
| 1 | ~3.5 | ~2.5 | ~2.0 | ~1.5 |
| 2 | ~3.8 | ~2.5 | ~2.0 | ~1.5 |
</details>

Figure 12.10 Variations of the output variance $P_{y}$ in Example 12.16 with time for regulators having the sampling periods h = 0.2 (solid), h = 0.5 (dashed), h = 1 (dashed-dotted), and h = 2 (dotted).
