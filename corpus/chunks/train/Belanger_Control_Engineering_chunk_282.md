# 5.6.2 Stability Condition Under Uncertainty

The plant model used in the design is called the nominal plant. It is a member of a family of possible models for the actual plant, given the uncertainty. Let this family be denoted by a set, P.

A control system is said to possess robust stability with respect to P if it is stable for every $P(s) \in \mathcal{P}$ . Robustness implies that the control system will be stable for all models that could be expected to represent the plant.

The following assumptions are made about $\mathcal{P}$ .

(i) It includes the nominal plant model $P_0(s)$ .   
(ii) All $P(s) \in \mathcal{P}$ have the same number of closed RHP poles (this assumption is mildly restrictive).   
(iii) For any $\omega$ , the locus of the complex numbers $P(j\omega)$ , $P \in \mathcal{P}$ , is a connected surface.

The solid curve in Figure 5.28 is the Nyquist plot of the loop gain $F(j\omega)P_0(j\omega)$ , i.e., the nominal loop gain. Consider a specific frequency, $\omega_0$ . The set $\mathcal{P}$ defines a whole set of possible complex values of $P(j\omega_0)$ , one of which is $P_0(j\omega_0)$ . To each of these values there corresponds a point $F(j\omega_0)P(j\omega_0)$ . As $P(j\omega_0)$ takes on all the values defined by $\mathcal{P}$ , a locus of points $F(j\omega_0)P(j\omega_0)$ is generated. This locus describes a surface or curve in the complex plane, with the nominal loop gain included. Each point on the nominal Nyquist plot is replaced by a surface; the result is that the plot is surrounded by a sheath containing Nyquist plots for every member of $\mathcal{P}$ .

![](image/bc05f1290f806405c57ffe6836397d98b184a55a2ec7c251a22dc2c7096ef6c1.jpg)

<details>
<summary>natural_image</summary>

Abstract geometric pattern with interlocking shapes and a curved arc, no text or symbols present
</details>

Figure 5.28 Set of Nyquist plots for a family of plants

If the closed-loop system is stable in the nominal case $P(s) = P_{0}(s)$ , then, by the first two preceding assumptions, stability for all $P \in P$ requires that the number of encirclements of the Nyquist plot of $F(s)P(s)$ be the same for all $P \in P$ . That will be the case if, and only if, every possible Nyquist plot “stays on the same side of” the $(-1,0)$ point as the plot for the nominal plant. This, in turn, will be true if the Nyquist “sheath” avoids the $(-1,0)$ point altogether. This is expressed mathematically as

$$| 1 + F (j \omega) P (j \omega) | > 0, \quad \text { all } P \in \mathcal {P} \text { and all } \omega . \tag {5.23}$$
