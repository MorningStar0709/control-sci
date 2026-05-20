# Constant-Trace Algorithms

Another way to keep the P-matrix bounded is to scale the matrix at each iteration. A popular scheme is to scale it in such a way that the trace of the matrix is constant. An additional refinement is to also add a small unit matrix.

(a)   
![](image/2aa1dad8296da996e906fd7b6ef920792922a8f3a7aaac98f43ba3336f52c5cd.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | 1 |
| 25 | -1 |
| 50 | -1 |
| 100 | 1 |
| 125 | -1 |
| 150 | -1 |
</details>

(b)   
![](image/6af17c62b2fe9a17ee1e1cd76ac8c9434ff4bf90465e2527a484a7066281aeeb.jpg)

<details>
<summary>line</summary>

| Time | P11 |
| --- | --- |
| 0 | 4 |
| 25 | 1 |
| 50 | 0 |
| 100 | 0 |
| 150 | 0 |
</details>

(c)   
![](image/535aadf93a5098c9cee6fb2ea0e80c2f7aa2cd1d62dd827887e21589fd7f8523.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | 1.0 |
| 25 | -1.0 |
| 50 | -1.0 |
| 75 | 1.0 |
| 100 | 1.0 |
| 125 | -1.0 |
| 150 | -1.0 |
</details>

(d)   
![](image/f8570eaed66a34c594e5bcb918b103eff7a781352a5d64c055661484a8c970ee.jpg)

<details>
<summary>line</summary>

| Time | k₁ |
| --- | --- |
| 0 | -1.0 |
| 50 | 0.0 |
| 100 | 0.0 |
| 150 | 0.0 |
</details>

Figure 11.14 Illustration of how estimator windup can be avoided with conditional updating. Compare with Fig. 11.12.

This gives the so-called regularized constant-trace algorithm:

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + K (t) \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right)K (t) = P (t - 1) \varphi (t) (\lambda + \varphi (t) ^ {T} P (t - 1) \varphi (t)) ^ {- 1}\bar {P} (t) = \frac {1}{\lambda} \left(\bar {P} (t - 1) - \frac {P (t - 1) \varphi (t) \varphi^ {T} (t) P (t - 1)}{1 + \varphi (t) ^ {T} P (t - 1) \varphi (t)}\right) \tag {11.21}P (t) = c _ {1} \frac {\bar {P} (t)}{t r (\bar {P} (t))} + c _ {2} I$$

where $c_{1} > 0$ and $c_{2} \geq 0$ . Typical values for the parameters can be

$$c _ {1} / c _ {2} \approx 1 0 ^ {4}\varphi^ {T} \varphi \cdot c _ {1} \gg 1$$

The constant-trace algorithm may also be combined with conditional updating.
