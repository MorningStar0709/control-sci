# Reconstruction

The inversion of the sampling operation, that is, the conversion of a sequence of numbers $\{f(t_{k}): k \in Z\}$ to a continuous-time function $f(t)$ is called reconstruction. In computer-controlled systems, it is necessary to convert the control actions calculated by the computer as a sequence of numbers to a continuous-time signal that can be applied to the process. In digital filtering, it is similarly necessary to convert the representation of the filtered signal as a sequence of numbers into a continuous-time function. Some different reconstructions are discussed in this section.

![](image/8b70f4c0784e9b20fea26dffbb7fe6ada3f4867f64eff432d3f9de4703308232.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| -15 | 0.0 |
| -10 | 0.0 |
| -5 | 0.0 |
| 0 | 1.0 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
</details>

Figure 7.3 The impulse response of the Shannon reconstruction given by (7.7) when $h = 1$ .
