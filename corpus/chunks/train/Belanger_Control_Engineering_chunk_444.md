# Solution

The optimal state feedback gain is $K = [-40.0 - 37.37 - 190.6 - 54.73]$ . Figure 7.26 shows the angle responses for both the state feedback law and the observer-based control. The observer is implemented as

$$
\begin{array}{l} \dot {\psi} = - 4 \psi + 3. 6 \theta - u \\ = - 4 \psi + 3. 6 \theta - [ + 4 0. 0 x + 3 7. 3 7 v + 1 9 0. 6 \theta + 5 4. 7 3 \widehat {\omega} ]. \\ \end{array}
$$

Since $\widehat{\omega} = \psi + 4\theta$ , we get

$$\dot {\psi} = - 4 0. 0 x - 3 7. 3 7 v - 4 0 5. 9 \theta - 5 8. 7 3 \psi$$

and

$$u = 4 0. 0 x + 3 7. 3 7 v + 4 0 9. 5 \theta + 5 4. 7 3 \psi .$$

These last two equations are the state representation of the controller.

![](image/5b436399df8c2b520931bca75484f319e25fad1c23a17a7264eb7986f26ebdcb.jpg)

<details>
<summary>line</summary>

| Time(s) | State feedback | Observer feedback |
| --- | --- | --- |
| 0.0 | 0.25 | 0.25 |
| 0.5 | -0.1 | -0.3 |
| 1.0 | 0.0 | 0.15 |
| 1.5 | 0.0 | 0.0 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 0.0 | 0.0 |
| 3.0 | 0.0 | 0.0 |
</details>

Figure 7.26 Angle responses for state feedback and observer-based feedback, pendulum-on-cart system

The transform equation for $\psi(s)$ is

$$\psi (s) = \frac {- 1}{s + 5 8 . 7 3} (4 0. 0 x + 3 7. 3 7 v + 4 0 5. 9 \theta).$$

Hence,

$$u (s) = 4 0. 0 x + 3 7. 3 7 v + 4 0 9. 5 \theta - \frac {1}{s + 5 8 . 7 3} (4 0. 0 x + 3 7. 3 7 v + 4 0 5. 9 \theta).$$
