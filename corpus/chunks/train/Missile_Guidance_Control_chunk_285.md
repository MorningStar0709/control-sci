The initial condition $\lambda _ { o }$ can be computed from (4.25a). Substitution of (4.40) into (4.43) yields [17]

$$\dot {\lambda} (R / R _ {o}) = \dot {\lambda} _ {o} (R / R _ {o}) e ^ {(N ^ {\prime} - 2)}. \tag {4.44}$$

The solution of this differential equation tends to zero for the interceptor–target closing; that is, $( d R ( t ) / d t ) < 0$ . When $N ^ { \prime } { = } 2$ , a constant target maneuver is required, and $d \lambda / d t$ is constant during the flight. For values of $N ^ { \prime }$ greater than 2, the acceleration required at intercept reduces to zero. This is a highly desirable situation, since this early correction of the heading error preserves the full maneuvering capabilities of the missile at intercept to overcome the effects of a late target maneuver or of target noise. Furthermore, (4.44) shows that $d \lambda / d t$ is maximum at the beginning of the flight, decreases linearly to zero for $N ^ { \prime } { = } 3$ , and approaches the value of zero asymptotically for $N ^ { \prime } > 3$ . The collision course condition $d \lambda ( t ) / d t = 0$ is satisfied at the final (or intercept) point $R = 0$ , with a vanishing turning rate $d \gamma _ { m } / d t = 0$ . Figure 4.12 shows a plot of $( \dot { \lambda } / \dot { \lambda } _ { o } ) \mathrm { v s . } ( R / R _ { o } )$ , wherein the target is assumed to fly from left to right.

Consider now a maneuvering target. For simplicity, we will assume that in the estimation of the LOS rate $d \lambda / d t$ , the target maneuvers so that the right-hand side of (4.42) remains constant. Exact computations show that in proportional navigation, $d R / d t$ varies very little during flight. The solution of (4.42) is now given by

$$\frac {d \lambda}{d t} = (\dot {\gamma} _ {t} v _ {t} \cos (\gamma_ {t} - \lambda)) / \dot {R} (2 - N ^ {\prime}) \{1 - e ^ {- (N ^ {\prime} - 2) \xi} \}. \tag {4.45}$$

![](image/98e5a3d1d5aafb8796a990ad7d122be1ae70ab2ff55dcef6ee9563ff57820b7c.jpg)

<details>
<summary>line</summary>

| R/R₀ | N' = 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 0.8 | ~1.2 | ~1.0 | ~0.8 | ~0.6 | ~0.4 |
| 0.6 | ~1.4 | ~1.0 | ~0.6 | ~0.4 | ~0.2 |
| 0.4 | ~1.6 | ~1.0 | ~0.4 | ~0.2 | ~0.1 |
| 0.2 | ~1.8 | ~1.0 | ~0.2 | ~0.1 | ~0.05 |
| 0.0 | ~2.0 | ~1.0 | ~0.0 | ~0.0 | ~0.0 |
</details>

Fig. 4.12. Plot of $( \dot { \lambda } / \dot { \lambda } _ { o } )$ vs. $( R / R _ { o } )$ with $N ^ { \prime }$ as parameter for a nonmaneuvering target.

Eliminating ξ from (4.45) by using (4.40), one obtains
