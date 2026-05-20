# Theorem 9.7.1 — Kalman smoother.

Forward predict step

$$\hat {\mathbf {x}} _ {k + 1} ^ {-} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {+} + \mathbf {B} \mathbf {u} _ {k} \tag {9.36}\mathbf {P} _ {k + 1} ^ {-} = \mathbf {A} \mathbf {P} _ {k} ^ {-} \mathbf {A} ^ {\top} + \mathbf {Q} \tag {9.37}$$

Forward update step

$$\mathbf {K} _ {k + 1} = \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} ^ {\top} (\mathbf {C P} _ {k + 1} ^ {-} \mathbf {C} ^ {\top} + \mathbf {R}) ^ {- 1} \tag {9.38}\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {K} _ {k + 1} \left(\mathbf {y} _ {k + 1} - \mathbf {C} \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {D u} _ {k + 1}\right) \tag {9.39}\mathbf {P} _ {k + 1} ^ {+} = \left(\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C}\right) \mathbf {P} _ {k + 1} ^ {-} \tag {9.40}$$

Backward update step

$$\mathbf {K} _ {k} = \mathbf {P} _ {k} ^ {+} \mathbf {A} _ {k} ^ {\top} (\mathbf {P} _ {k + 1} ^ {-}) ^ {- 1} \tag {9.41}\hat {\mathbf {x}} _ {k \mid N} = \hat {\mathbf {x}} _ {k} ^ {+} + \mathbf {K} _ {k} \left(\hat {\mathbf {x}} _ {k + 1 \mid N} - \hat {\mathbf {x}} _ {k + 1} ^ {-}\right) \tag {9.42}\mathbf {P} _ {k \mid N} = \mathbf {P} _ {k} ^ {+} + \mathbf {K} _ {k} (\mathbf {P} _ {k + 1 \mid N} - \mathbf {P} _ {k + 1} ^ {-}) \mathbf {K} _ {k} ^ {\top} \tag {9.43}$$

Backward initial conditions

$$\hat {\mathbf {x}} _ {N \mid N} = \hat {\mathbf {x}} _ {N} ^ {+} \tag {9.44}\mathbf {P} _ {N \mid N} = \mathbf {P} _ {N} ^ {+} \tag {9.45}$$

![](image/e12e98adedf587303ce3e330e7ddba59db347d19797a85cfb150baded91d0990.jpg)

<details>
<summary>line</summary>

| Time (s) | Kalman filter | Kalman smoother |
| --- | --- | --- |
| 0 | 45 | 52 |
| 10 | 63 | 58 |
| 20 | 57 | 62 |
| 30 | 70 | 68 |
| 40 | 75 | 75 |
| 50 | 85 | 85 |
| 60 | 95 | 95 |
| 70 | 105 | 100 |
| 80 | 110 | 110 |
| 90 | 115 | 115 |
| 100 | 125 | 125 |
</details>

Figure 9.6: Robot position with Kalman smoother
