# 4.7.5 A Particle Filter Based on Importance Sampling

Motivated by the drawbacks of the simplest particle filter of the previous section, researchers have developed alternatives based on a more flexible importance function (Arulampalam, Maskell, Gordon, and Clapp, 2002). We present this approach next. Rather than start with the statistical property of most interest, $p ( x ( k ) | \mathbf { y } ( k ) )$ , consider instead the density of the entire trajectory of states conditioned on the measurements, $p ( \mathbf { x } ( k ) | \mathbf { y } ( k ) )$ , as we did in moving horizon estimation. Our first objective then is to obtain samples of $p ( \mathbf { x } ( k + 1 ) | \mathbf { y } ( k + 1 ) )$ ) from samples of $p ( \mathbf { x } ( k ) | \mathbf { y } ( k ) )$ and the model. We use importance sampling to accomplish this objective. Assume we have s weighted samples of the trajectory conditioned on measurements up to time $k$

![](image/e3da7bdec5ef72dc6622677ef3bee8071802c8495f3ac90517b5f6dbcbef977c.jpg)

<details>
<summary>line</summary>

| k | with resampling | without resampling |
| --- | --- | --- |
| 0 | 0.95 | 0.95 |
| 1 | 0.65 | 0.15 |
| 2 | 0.66 | 0.11 |
| 3 | 0.72 | 0.08 |
| 4 | 0.76 | 0.06 |
| 5 | 0.81 | 0.05 |
</details>

Figure 4.24: Fraction of particles inside the 95% contour of the true conditional density versus time; with and without resampling; average of 500 runs.

$$p (\mathbf {x} (k) | \mathbf {y} (k)) = \left\{\mathbf {x} _ {i} (k), \overline {{w}} _ {i} (k) \right\} \quad i = 1, \dots , s$$

in which the samples have been drawn from an importance function $q ,$ , whose properties will be chosen as we proceed further. The weights ${ \overline { { w } } } _ { i } ( k )$ are given by

$$w _ {i} (k) = \frac {h (\mathbf {x} _ {i} (k))}{q (\mathbf {x} _ {i} (k) | \mathbf {y} (k))}p (\mathbf {x} _ {i} (k) | \mathbf {y} (k)) = \frac {h (\mathbf {x} _ {i} (k))}{\int h (\mathbf {x} _ {i} (k)) d \mathbf {x} _ {i} (k)}\overline {{w}} _ {i} (k) = \frac {w _ {i} (k)}{\sum_ {j} w _ {j} (k)}$$

Notice $\mathbf { x } _ { i } ( k )$ is a set of ks n-vector samples, and, as in full information estimation, the storage requirements grow linearly with time. We remove this drawback subsequently, but for now we wish to obtain samples of $p ( \mathbf { x } ( k + 1 ) | \mathbf { y } ( k + 1 ) )$ ) in which $\mathbf { x } ( k + 1 ) = \{ x ( k + 1 ) , \mathbf { x } ( k ) \}$ and $\mathbf { y } ( k + 1 ) = \{ y ( k + 1 ) , \mathbf { y } ( k ) \}$ . We start with
