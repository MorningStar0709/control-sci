| θ/π | V₃⁰ |
| --- | --- |
| -1.0 | 20.0 |
| -0.9 | 18.0 |
| -0.8 | 16.0 |
| -0.7 | 14.0 |
| -0.6 | 12.0 |
| -0.5 | 10.0 |
| -0.4 | 8.0 |
| -0.3 | 6.0 |
| -0.2 | 4.0 |
| -0.1 | 2.0 |
| 0.0 | 2.0 |
| 0.1 | 2.0 |
| 0.2 | 2.0 |
| 0.3 | 3.0 |
| 0.4 | 5.0 |
| 0.5 | 7.0 |
| 0.6 | 9.0 |
| 0.7 | 11.0 |
| 0.8 | 13.0 |
| 0.9 | 15.0 |
| 1.0 | 17.0 |
</details>

Figure 2.4: Optimal cost $V _ { 3 } ^ { 0 } ( x )$ versus x = (cos(θ), sin(θ)), $\theta \in$ $[ - \pi , \pi ]$ on the unit circle; the discontinuity in $V _ { 3 } ^ { 0 }$ is caused by the discontinuity in $\mathcal { U } _ { 3 }$ as $\theta$ crosses the dashed line in Figure 2.3.

$$V _ {3} ^ {0} (x) = \min _ {\mathbf {u}} \left\{V _ {3} (x, \mathbf {u}) \mid \phi (3; x, \mathbf {u}) = 0 \right\}$$

and the implicit MPC control law is $\kappa _ { 3 } ( \cdot )$ where $\kappa _ { 3 } ( x ) = u ^ { 0 } ( 0 ; x )$ , the first element in the minimizing sequence $\mathbf { u } ^ { 0 } ( x )$ . It can be shown, using analysis presented later in this chapter, that the origin is asymptotically stable for the controlled system $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ ). That this control law is necessarily discontinuous may be shown as follows. If the control is strictly positive, any trajectory originating in the first quadrant $( x _ { 1 } , x _ { 2 } > 0 )$ moves away from the origin. If the control is strictly negative, any control originating in the third quadrant $( x _ { 1 } , x _ { 2 } ~ < ~ 0 )$ also moves away from the origin. But the control cannot be zero at any nonzero point lying in the domain of attraction. If it were, this point would be a fixed point for the controlled system, contradicting the fact that it lies in the domain of attraction.

In fact, both the value function $V _ { 3 } ^ { 0 } ( \cdot )$ and the MPC control law $\kappa _ { 3 } ( \cdot )$ are discontinuous. Figures 2.3 and 2.4 show how ${ \mathcal { U } } _ { 3 } ( x ) , \kappa _ { 3 } ( x )$ , and $V _ { 3 } ^ { 0 } ( x )$ vary as ${ \boldsymbol { x } } = ( \cos ( \theta ) , \sin ( \theta ) )$ ranges over the unit circle. A further conclusion that can be drawn from this example is that it is possible for the MPC control law to be discontinuous at points where the value function is continuous. -
