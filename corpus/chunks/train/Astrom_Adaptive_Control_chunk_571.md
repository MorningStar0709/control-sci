# EXAMPLE 9.4 Nonlinear transformation of a pendulum

Consider the system

$$
\begin{array}{l} \frac {d x _ {1}}{d t} = x _ {2} \\ \frac {d x _ {2}}{d t} = - \sin x _ {1} + u \cos x _ {1} \tag {9.1} \\ \end{array}
y = x _ {1}
$$

![](image/b0a8725a1b8dafd7a6bf8917e8983cf9f757d28289b2801c6547fa8f406e06c5.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0 | 1.8 |
| 1 | 2.8 |
| 2 | 3.2 |
| 3 | 3.2 |
| 4 | 3.2 |
| 5 | 3.2 |
</details>

![](image/a57c10d7439b821fbbeae2745dfc3c926334694dfc84a4831ef401a89e5e7e6b.jpg)

<details>
<summary>line</summary>

| Time | y |
| --- | --- |
| 0 | 1.8 |
| 1 | 2.0 |
| 2 | 2.5 |
| 3 | 3.0 |
| 4 | 3.1 |
| 5 | 3.1 |
</details>

![](image/775bd57c2792734f7368e72d0d42e26caee092e0515409ba9357f1ad7baa0ed1.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | -30 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
</details>

![](image/ea92473001cbaeba8f2f0ace8c3bf2ee836d4c6607f5ba191f0ee6c6b9fb5fee.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | -5 |
| 1 | -2 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
</details>

Figure 9.6 The pendulum described by Eqs. (9.1), controlled by (a) the nonlinear controller of Eq. (9.3) and (b) the fixed-gain controller of Eq. (9.4). The desired characteristic equation (Eq. 9.2) is defined by $p_{1} = 2.8$ and $p_{2} = 4$ .

which describes a pendulum, where the acceleration of the pivot point is the input and the output y is the angle from a downward position. Introduce the transformed control signal

$$v (t) = - \sin x _ {1} (t) + u (t) \cos x _ {1} (t)$$

This gives the linear equations

$$
\frac {d x}{d t} = \left( \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right) x + \binom{0}{1} v
$$

Assume that $x_{1}$ and $x_{2}$ are measured, and introduce the control law

$$v (t) = - l _ {1} ^ {\prime} x _ {1} (t) - l _ {2} ^ {\prime} x _ {2} (t) + m ^ {\prime} u _ {c} (t)$$

The transfer function from $u_{e}$ to $y$ is

$$\frac {m ^ {\prime}}{s ^ {2} + l _ {2} ^ {\prime} s + l _ {1} ^ {\prime}}$$

Let the desired characteristic equation be

$$s ^ {2} + p _ {1} s + p _ {2} \tag {9.2}$$

which can be obtained with

$$l _ {1} ^ {\prime} = p _ {2} \quad l _ {2} ^ {\prime} = p _ {1} \quad m ^ {\prime} = p _ {2}$$

Transformation back to the original control signal gives

$$u (t) = \frac {v (t) + \sin x _ {1} (t)}{\cos x _ {1} (t)} = \frac {1}{\cos x _ {1} (t)} (- p _ {2} x _ {1} (t) - p _ {1} x _ {2} (t) + p _ {2} u _ {c} (t) + \sin x _ {1} (t)) \tag {9.3}$$
