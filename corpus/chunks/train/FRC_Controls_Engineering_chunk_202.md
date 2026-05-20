# 7.7.2 The mathematical definition

Instead of placing the poles of a closed-loop system manually, the linear-quadratic regulator (LQR) places the poles for us based on acceptable relative error and control effort costs. This method of controller design uses a quadratic function for the costto-go defined as the sum of the error and control effort over time for the linear system

![](image/b54d098873a49d65c477b924afecc98389070adf3a8e335050dc9b02a8ab3384.jpg)

<details>
<summary>surface_3d</summary>

| Position | Velocity | Cost-to-go |
| --- | --- | --- |
| -1.0 | 0.0 | 25000 |
| -0.5 | 0.5 | 15000 |
| 0.0 | 1.0 | 5000 |
| 0.5 | 0.5 | 10000 |
| 1.0 | 0.0 | 25000 |
</details>

Figure 7.8: Cost-to-go for elevator model

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k}.J = \sum_ {k = 0} ^ {\infty} \left(\mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {Q} \mathbf {x} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R} \mathbf {u} _ {k}\right)$$

where J represents a trade-off between state excursion and control effort with the weighting factors Q and R. LQR is a control law u that minimizes the cost functional. Figure 7.8 shows the optimal cost-to-go for an elevator model. Pole placement, on the other hand, will have a cost-to-go above this for an arbitrary state vector (in this case, an arbitrary position-velocity pair).

The cost-to-go looks effectively constant along the velocity axis because the velocity is contributing much less to the cost-to-go than position.[7] In other words, it’s much more expensive to correct for a position error than a velocity error. This difference in cost is reflected by LQR’s selected position feedback gain of $K _ { p } = 2 3 4 . 0 4 1$ and selected velocity feedback gain of $K _ { d } = 5 . 6 0 3$ .

The minimum of LQR’s cost functional is found by setting the derivative of the cost functional to zero and solving for the control law $\mathbf { u } _ { k }$ . However, matrix calculus is used instead of normal calculus to take the derivative.

The feedback control law that minimizes J is shown in theorem 7.7.1.
