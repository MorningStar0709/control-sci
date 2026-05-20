If we rerun the simulation 500 times and plot versus time the fraction of particles that are inside the 95% contour of the true conditional density, we obtain the result shown in Figure 4.27. The optimal importance function is able to maintain about 20% of the particles in the 95% probability ellipse. With the optimal importance function and resampling, more than 90% of the particles are inside the 95% probability ellipse. The earlier warning about sample impoverishment applies here as well. -

![](image/2375c9857ec72ab675c600fcc5480d78705f06e2fdcebca6c621fd9f9c7602a3.jpg)

<details>
<summary>line</summary>

| k | with resampling | without resampling |
| --- | --- | --- |
| 0 | 0.95 | 0.95 |
| 1 | 0.68 | 0.18 |
| 2 | 0.71 | 0.17 |
| 3 | 0.80 | 0.16 |
| 4 | 0.84 | 0.16 |
| 5 | 0.89 | 0.17 |
</details>

Figure 4.27: Fraction of particles inside the 95% contour of the true conditional density versus time; with and without resampling; average of 500 runs.
