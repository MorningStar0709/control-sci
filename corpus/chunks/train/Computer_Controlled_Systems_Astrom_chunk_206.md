# Practical Aspects of the Choice of the Sampling Period

Selection of the sampling period in sampled systems is a fundamental problem that will be discussed several times in this book. The proper choice depends on the properties of the signal, the reconstruction method, and the purpose of the system. In a pure signal-processing problem, the purpose is simply to record a signal digitally and to recover it from its samples. A reasonable criterion for selection may then be the size of the error between the original signal and the reconstructed signal. In signal-processing applications it can be justified to have sampling rates of several hundred samples per period.

A rational choice of the sampling rate in a closed-loop control system should be based on an understanding of its influence on the performance of the control system. It seems reasonable that the highest frequency of interest should be closely related to the bandwidth of the closed-loop system. The selection of sampling rates then can be based on the bandwidth or, equivalently, on the rise time of the closed-loop system. Reasonable sampling rates are 10 to 30 times the bandwidth, or 4 to 10 per rise time, which may seem slow in relation to the typical signal-processing problem. Comparatively low sampling rates can be used in control problems because the dynamics of many controlled systems are of low-pass character and their time constants are typically larger than the closed-loop response times. The contribution to the output from one sampling period then depends on the pulse area; it is comparatively insensitive to the pulse shape.

![](image/3f7bc3f003e141d3c40c2461d084c0a3e55f32b6b68c0e8ede5f0d11de151b69.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 1 | 0.3 |
| 2 | 0.8 |
| 3 | 1.2 |
| 4 | 1.3 |
| 5 | 1.2 |
| 6 | 1.1 |
| 7 | 1.0 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
</details>

![](image/37243ec60d962c8d754ec4c73c163080c42bbe5908b076ecda27ea59f34fe1cc.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 1 | 0.5 |
| 2 | 1 |
| 3 | 1.1 |
| 4 | 1 |
| 5 | 1 |
| 6 | 1 |
| 7 | 1 |
| 8 | 1 |
| 9 | 1 |
| 10 | 1 |
</details>

![](image/50b49453250606974d6faaf80cb458daf013f871fc0d1d99c0d4a97754a6e06b.jpg)

<details>
<summary>line</summary>

| x | Input |
| --- | --- |
| 0 | 0.5 |
| 1 | 0.0 |
| 2 | -0.5 |
| 3 | -0.5 |
| 4 | -0.5 |
| 5 | -0.5 |
| 6 | -0.5 |
| 7 | -0.5 |
| 8 | -0.5 |
| 9 | -0.5 |
| 10 | -0.5 |
</details>
