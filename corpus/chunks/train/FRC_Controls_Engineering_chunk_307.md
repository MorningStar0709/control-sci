# Theorem 9.6.3 — Kalman filter.

Predict step

$$\hat {\mathbf {x}} _ {k + 1} ^ {-} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {+} + \mathbf {B} \mathbf {u} _ {k} \tag {9.20}\mathbf {P} _ {k + 1} ^ {-} = \mathbf {A} \mathbf {P} _ {k} ^ {-} \mathbf {A} ^ {\top} + \mathbf {Q} \tag {9.21}$$

Update step

$$\mathbf {K} _ {k + 1} = \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} ^ {\top} (\mathbf {C P} _ {k + 1} ^ {-} \mathbf {C} ^ {\top} + \mathbf {R}) ^ {- 1} \tag {9.22}\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {K} _ {k + 1} \left(\mathbf {y} _ {k + 1} - \mathbf {C} \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {D u} _ {k + 1}\right) \tag {9.23}\mathbf {P} _ {k + 1} ^ {+} = \left(\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}\right) \mathbf {P} _ {k + 1} ^ {-} \left(\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}\right) ^ {\top} + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top} \tag {9.24}$$

A system matrix xˆ state estimate vector   
B input matrix u input vector   
C output matrix y output vector   
D feedthrough matrix Q process noise covariance   
P error covariance matrix R measurement noise covariance   
K Kalman gain matrix

where a superscript of minus denotes a priori and plus denotes a posteriori estimate (before and after update respectively).

C, D, Q, and R from the equations derived earlier are made constants here.

![](image/7690565ba932a413026786659001f1328d19827113b41ec6bb3a2e17e5ee3f7f.jpg)

To implement a discrete time Kalman filter from a continuous model, the model and continuous time Q and R matrices can be discretized using theorem 7.3.1.

Unknown states in a Kalman filter are generally represented by a Wiener (pronounced VEE-ner) process.[5] This process has the property that its variance increases linearly

<table><tr><td>Matrix</td><td>Rows × Columns</td><td>Matrix</td><td>Rows × Columns</td></tr><tr><td>A</td><td>states × states</td><td> $\hat{x}$ </td><td>states × 1</td></tr><tr><td>B</td><td>states × inputs</td><td>u</td><td>inputs × 1</td></tr><tr><td>C</td><td>outputs × states</td><td>y</td><td>outputs × 1</td></tr><tr><td>D</td><td>outputs × inputs</td><td>Q</td><td>states × states</td></tr><tr><td>P</td><td>states × states</td><td>R</td><td>outputs × outputs</td></tr><tr><td>K</td><td>states × outputs</td><td></td><td></td></tr></table>

Table 9.2: Kalman filter matrix dimensions

with time t.
