With the model in theorem 8.7.4, y is uncontrollable at $v = 0$ because the row corresponding to y becomes the zero vector. This means the state dynamics and inputs can no longer affect y. This is obvious given that nonholonomic drivetrains can’t move sideways. Some DARE solvers throw errors in this case, but one can avoid it by linearizing the model around a slightly nonzero velocity instead.

The controller in theorem 8.7.4 results in figures 8.8 and 8.9, which show slightly better tracking performance than the previous formulation.

![](image/26d1472bd7d5d87926ae0d5ad6ea1ab6a40efcba49fb11d84264711afd96e375.jpg)

<details>
<summary>line</summary>

| x (m) | Reference | State |
| --- | --- | --- |
| 1.0 | 13.0 | 13.0 |
| 2.0 | 13.5 | 13.5 |
| 4.0 | 14.5 | 14.5 |
| 6.0 | 15.5 | 15.5 |
| 8.0 | 16.5 | 16.5 |
| 10.0 | 17.5 | 17.5 |
</details>

Figure 8.8: Linear time-varying differential drive controller x-y plot

![](image/d3036e2620938e3f298f39d69c57f65d051fa1031a7a25b200d9336be281be51.jpg)  
Figure 8.9: Linear time-varying differential drive controller response
