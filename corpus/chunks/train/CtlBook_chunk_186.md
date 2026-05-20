# Example 6.10

![](image/730ea068c26e6dda1b1c66cbb90e776baa4af96f68b3dfb4f284c087effcdca3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X[" X(s) "] --> +
    + --> A["100/(s+1) "]
    A --> B[" "]
    B --> y[" y(s) "]
    d["d(t) = 20u(t)"] --> A
```
</details>

As a nal example, for the system above, nd $Y ( s )$ and $y ( t ) = L ^ { - 1 } \left\{ Y ( s ) \right\}$ for x(t) = 0, X(s) = 0, d(t) = 20u(t).

$$Y (s) = \frac {G}{1 + G H} X (s) + \frac {1}{1 + G H} D (s)$$

Since X(s) = 0, and the Laplace transform of 20u(t) is $2 0 / s ,$

$$Y (s) = \frac {1}{1 + \frac {1 0 0}{(s + 1)}} D (s) = \frac {(s + 1)}{(s + 1 0 1)} 2 0 / s$$

Expanding this with partial fractions

$$\frac {2 0 (s + 1)}{s (s + 1 0 1)} = \frac {A _ {1}}{s} + \frac {A _ {2}}{(s + 1 0 1)}A _ {1} = \left. \frac {2 0 (s + 1)}{(s + 1 0 1)} \right| _ {s = 0} = \frac {2 0}{1 0 1} \approx 0. 2A _ {2} = \left. \frac {2 0 (s + 1)}{s} \right| _ {s - 1 0 1} = \frac {- 2 0 0 0}{- 1 0 1} \approx 2 0$$

Applying the inverse transform,

$$y (t) = 0. 2 u (t) + 2 0 e ^ {- 1 0 1 t}$$

![](image/01f9689231a894013db86cf555a9e8bdb9b43b0c2b21e257a1fd4b10276d8afb.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 20.0 |
| 0.1 | 1.0 |
| 0.2 | 0.5 |
| 0.3 | 0.3 |
| 0.4 | 0.2 |
| 0.5 | 0.1 |
| 0.6 | 0.1 |
| 0.7 | 0.1 |
| 0.8 | 0.1 |
| 0.9 | 0.1 |
| 1.0 | 0.1 |
</details>

The disturbance is reduced by about a factor of 100! (0.2u(t) compared to $2 0 u ( t ) )$ . Note however that the second term is a transient arising from the step input of the disturbance. Although this transient is over very quickly $\left( e ^ { - 1 0 1 t } \right)$ it has a signicant amplitude (20). Disturbance rejection cannot react instantly!

![](image/8dd62be06b135bb2d32261036890601b4d28cd1be84513d8db98667517c39e9c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> +
    + --> K["(S+1)(S+2)(S+3)"]
    K --> y
    y --> -
    - --> +
    - --> -
```
</details>

Figure 6.9: A closed loop negative feedback system with stable poles in the feed-forward path. K is a positive real constant, a gain.
