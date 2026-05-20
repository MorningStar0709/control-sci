<details>
<summary>line</summary>

| x | y (solid line) | y (dashed line) |
| --- | --- | --- |
| 10^-2 | ~10^-5 | ~10^-4 |
| 10^-1 | ~10^-3 | ~10^-2 |
| 10^0 | ~10^0 | ~10^-1 |
| 10^1 | ~10^2 | ~10^0 |
| 10^2 | ~10^3 | ~10^2 |
</details>

Figure 8.7: $\Delta _ { m }$ (dashed line) and a bound $W _ { m }$ (solid line)

Note that this $W _ { m }$ is not proper since $G _ { 0 }$ and G do not have the same relative degrees. To get a proper $W _ { m } .$ , we need to choose a nominal model $G _ { 0 }$ having the same the relative order as that of G.

The following terminologies are used in this book:

Definition 8.1 Given the description of an uncertainty model set Π and a set of performance objectives, suppose $P \in \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf } } } \mathbf { \mathbf { \mathbf { \mathbf } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf } } } \mathbf { \mathbf { \mathbf { \mathbf } } } } } }$ is the nominal design model and K is the resulting controller. Then the closed-loop feedback system is said to have

Nominal Stability (NS): if K internally stabilizes the nominal model P .

Robust Stability (RS): if K internally stabilizes every plant belonging to Π.

Nominal Performance (NP): if the performance objectives are satisfied for the nominal plant P .

Robust Performance (RP): if the performance objectives are satisfied for every plant belonging to Π.

The nominal stability and performance can be easily checked using various standard techniques. The conditions for which the robust stability and robust performance are satisfied under various assumptions on the uncertainty set Π will be considered in the following sections.

Related MATLAB Commands: magfit, drawmag, fitsys, genphase, vunpck, vabs, vinv, vimag, vreal, vcjt, vebe
