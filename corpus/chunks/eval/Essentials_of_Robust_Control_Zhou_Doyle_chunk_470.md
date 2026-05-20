(in fact, the optimal controllers for $P _ { 1 }$ and $P _ { 2 }$ are $K = 0 . 9 9$ and $K = 1 . 0 1$ , respectively). While the stability margin for the closed-loop system with $P _ { 3 }$ is

$$b _ {P _ {3}, K _ {1}} = 0. 0 9 9 5,$$

which is far away from its optimal value, $b _ { \mathrm { o b t } } ( P _ { 3 } ) = 0 . 4 3 0 7$ , and results in poor performance of the closed loop. In fact, it is not hard to find a controller that will perform well for both $P _ { 1 }$ and $P _ { 2 }$ but will destabilize $P _ { 3 }$ .

Of course, this does not necessarily mean that all controllers performing reasonably well with $P _ { 1 }$ and $P _ { 2 }$ will do badly with $P _ { 3 }$ , merely that some do — the unit feedback being an example. It may be harder to find a controller that will perform reasonably well with all three plants; the maximally stabilizing controller of $P _ { 3 }$ ,

$$K _ {3} = \frac {2 . 0 9 5 4 s + 1 0 . 8 1 8 4}{s + 2 3 . 2 6 4 9},$$

is a such controller, which gives

$$b _ {P _ {1}, K _ {3}} = 0. 4 3 0 7, \quad b _ {P _ {2}, K _ {3}} = 0. 4 1 2 6, \quad \text { and } \quad b _ {P _ {3}, K _ {3}} = 0. 4 3 0 7.$$

The step responses under this control law are shown in Figure 17.6.

![](image/718f3cc4aeec8ca619f70f9c141c2b0dbd20f1150c1aa394df7c50ff7ae3b083.jpg)

<details>
<summary>line</summary>

| x | P1 | P2 | P3 |
| --- | --- | --- | --- |
| 0.0 | 0.85 | 0.85 | 0.00 |
| 0.1 | 0.87 | 0.87 | 0.60 |
| 0.2 | 0.88 | 0.89 | 0.95 |
| 0.3 | 0.89 | 0.91 | 1.05 |
| 0.4 | 0.90 | 0.92 | 1.03 |
| 0.5 | 0.91 | 0.93 | 1.01 |
| 0.6 | 0.92 | 0.94 | 1.00 |
| 0.7 | 0.93 | 0.95 | 1.00 |
| 0.8 | 0.94 | 0.96 | 1.00 |
| 0.9 | 0.95 | 0.97 | 1.00 |
| 1.0 | 0.96 | 0.98 | 1.00 |
</details>

Figure 17.6: Closed-loop step responses with $K _ { 3 } = \frac { 2 . 0 9 5 4 s + 1 0 . 8 1 8 4 } { s + 2 3 . 2 6 4 9 }$
