Assume that $P _ { 0 }$ and P have the same number of right-half plane poles, $W _ { 2 }$ is stable, and

$$\left| \operatorname{Re} \left\{\Delta_ {2} \right\} \right| \leq \alpha , \quad \left| \Im \left\{\Delta_ {2} \right\} \right| \leq \beta .$$

Derive the necessary and sufficient conditions for the feedback system to be robustly stable.

Problem 8.14 Let $P = \left\lceil \begin{array} { l l } { P _ { 1 1 } } & { P _ { 1 2 } } \\ { P _ { 2 1 } } & { P _ { 2 2 } } \end{array} \right\rceil \in \mathcal { R H } _ { \infty }$ be a two-by-two transfer matrix. Find sufficient (and necessary, if possible) conditions in each case so that $\mathcal { F } _ { u } ( P , \Delta )$ is stable for all possible stable $\Delta$ that satisfies the following conditions, respectively:

1. at each frequency

$$\mathrm{Re} \Delta (j \omega) \geq 0, \quad | \Delta (j \omega) | < \alpha$$

2. at each frequency

$$\mathrm{Re} \Delta (j \omega) e ^ {\pm j \theta} \geq 0, \quad | \Delta (j \omega) | < \alpha$$

where $\theta \geq 0 .$ .

3. at each frequency

$$\operatorname{Re} \Delta (j \omega) \geq 0, \Im \Delta (j \omega) \geq 0, \operatorname{Re} \Delta (j \omega) + \Im \Delta (j \omega) < \alpha$$

Problem 8.15 Let $P = ( I + \Delta W ) P _ { 0 }$ such that P and $P _ { 0 }$ have the same number of unstable poles for all admissible $\Delta , \| \Delta \| _ { \infty } < \gamma$ . Show that K robustly stabilizes P if and only if K stabilizes $P _ { 0 }$ and

$$\left\| W P _ {0} K (I + P _ {0} K) ^ {- 1} \right\| _ {\infty} \leq 1.$$

Problem 8.16 Give appropriate generalizations of the preceding problem to other types of uncertainties.

Problem 8.17 Let $K = I$ and

$$
P _ {0} = \left[ \begin{array}{c c} \frac {1}{s + 1} & \frac {2}{s + 3} \\ \frac {1}{s + 1} & \frac {1}{s + 1} \end{array} \right].
$$

1. Let $P = P _ { 0 } + \Delta$ with $\| \Delta \| _ { \infty } \leq \gamma$ . Determine the largest $\gamma$ for robust stability.

2. Let $\Delta = \left[ \begin{array} { c c } { k _ { 1 } } & \\ & { k _ { 2 } } \end{array} \right] \in \mathbb { R } ^ { 2 \times 2 }$ . Determine the stability region.

Problem 8.18 Repeat the preceding problem with

$$
P _ {0} = \left[ \begin{array}{c c} \frac {s - 1}{(s + 1) ^ {2}} & \frac {5 s + 1}{(s + 1) ^ {2}} \\ \frac {- 1}{(s + 1) ^ {2}} & \frac {s - 1}{(s + 1) ^ {2}} \end{array} \right].
$$
