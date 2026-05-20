![](image/d7ec40e1600e0011315974d86f3fa20ab9044b0549ba97cdefac27aa460c1ace.jpg)

<details>
<summary>line</summary>

| Time, s | Angular position, θ(t), rad |
| --- | --- |
| 0.0 | 0.1 |
| 0.2 | 0.01 |
| 0.4 | 0.05 |
| 0.6 | 0.03 |
| 0.8 | 0.04 |
| 1.0 | 0.035 |
| 1.2 | 0.038 |
| 1.4 | 0.039 |
| 1.6 | 0.039 |
| 1.8 | 0.039 |
| 2.0 | 0.039 |
</details>

Figure 8.3 Step response of the rotational mechanical system (Example 8.10).

We can verify this result using the following MATLAB commands:

```matlab
>> syms s    % define Laplace variable s
>> numTh = 0.1*s^2 + 0.8*s + 12.5;    % define numerator of Θ(s)
>> denTh = s*(s^2 + 8*s + 325);    % define denominator of Θ(s)
>> Th = numTh/denTh;    % define Θ(s)
>> th = ilaplace(Th);    % inverse Laplace transform, θ(t)
>> pretty(th)    % display th in math typeset 
```

The result is

$$4 / 6 5 \exp (- 4 t) \cos (3 0 9 t) + \frac {1 6}{2 0 0 8 5} \frac {1 / 2}{3 0 9} \exp (- 4 t) \sin (3 0 9 t) + 1 / 2 6$$

Expressing the parameters using decimal representations the above solution becomes

$$0. 0 6 1 5 \exp (- 4 t) \cos (1 7. 5 7 8 4 t) + 0. 0 1 4 0 \exp (- 4 t) \sin (1 7. 5 7 8 4 t) + 0. 0 3 8 5$$

which is identical to the solution ??(t) presented by Eq. (8.36) and Fig. 8.3.

While the Laplace transformation offers a systematic approach to obtaining the dynamic response, it is this author’s opinion that direct analysis of the system’s I/O differential equation (as demonstrated in Chapter 7) provides a more intuitive approach. For example, the characteristic equation of this rotational mechanical system can be easily determined from the I/O equation (8.26)

$$0. 2 r ^ {2} + 1. 6 r + 6 5 = 0 \tag {8.37}$$
