# THEOREM 6.10 Universal stabilizer

The control law of Eqs. (6.92), with

$$f (\hat {\theta}, y) = y \hat {\theta} ^ {2} \cos \hat {\theta} \tag {6.93}g (\hat {\theta}, y) = y ^ {2}$$

and $\hat{\theta}(0) = 0$ , stabilizes Eq. (6.91).

Proof: The closed-loop system is described by

$$\frac {d y}{d t} = a y + b y \hat {\theta} ^ {2} \cos \hat {\theta}\frac {d \hat {\theta}}{d t} = y ^ {2}$$

Since $\hat{\theta}(0) = 0$ and $d\hat{\theta} / dt \geq 0$ , it follows that $\hat{\theta}(t)$ is nonnegative and nondecreasing. $\hat{\theta}(t)$ is also bounded, which is shown by contradiction. Hence assume that $\lim_{t \to \infty} \hat{\theta}(t) = \infty$ . Multiplication of the differential equation for $y$ by $y$ gives

$$y \frac {d y}{d t} = a y ^ {2} + b y ^ {2} \hat {\theta} ^ {2} \cos \hat {\theta} = a \frac {d \hat {\theta}}{d t} + b \hat {\theta} ^ {2} \cos \hat {\theta} \frac {d \hat {\theta}}{d t}$$

Integration with respect to time gives

$$y ^ {2} (t) = y ^ {2} (0) + 2 a \hat {\theta} (t) + 2 b \int_ {0} ^ {\hat {\theta} (t)} x ^ {2} \cos x d x$$

Hence

$$\frac {y ^ {2} (t)}{\hat {\theta} (t)} = \frac {y ^ {2} (0)}{\hat {\theta} (t)} + 2 a + \frac {2 b}{\hat {\theta} (t)} \int_ {0} ^ {\hat {\theta} (t)} x ^ {2} \cos x d x$$

But

$$\frac {1}{\hat {\theta}} \int_ {0} ^ {\hat {\theta}} x ^ {2} \cos x d x = \hat {\theta} \sin \hat {\theta} + 2 \cos \hat {\theta} - \frac {2}{\hat {\theta}} \sin \hat {\theta}$$

Hence

$$\lim _ {t \rightarrow \infty} \inf \frac {1}{\bar {\theta}} \int_ {0} ^ {\dot {\theta}} x ^ {2} \cos x d x = - \infty$$

This gives

$$\lim _ {\hat {\theta} \rightarrow \infty} \inf \frac {y ^ {2} (t)}{\hat {\theta} (t)} = - \infty$$

which is a contradiction because $y^{2}/\hat{\theta}$ is nonnegative. It thus follows that

$$\lim _ {t \rightarrow \infty} \hat {\theta} (t) = \theta^ {0} < \infty$$

(a)   
![](image/f9c692134705d00b1e76cb94d8eea622026cf3c60b6364707e82e3ccda9f6fab.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0.0 | -0.5 |
| 0.5 | -1.0 |
| 1.0 | 0.5 |
| 1.5 | 1.0 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
</details>

(b)   
![](image/b410e6d11e7b962049a575d0c3e46aced53923d0148cc05b1c81eb0f8a22791b.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0 | 0 |
| 1 | -8 |
| 2 | 0 |
| 3 | 0 |
</details>

![](image/2d206daf7a6ec06652c7ee5db82a39e375e4a3f27ebb7c2a2b779cb406ed6d92.jpg)

<details>
<summary>line</summary>
