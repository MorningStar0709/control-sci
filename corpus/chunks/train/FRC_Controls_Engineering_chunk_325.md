# Theorem 9.8.1 — Extended Kalman filter.

Predict step

$$\mathbf {A} = \underbrace {\left. \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} \right| _ {\hat {\mathbf {x}} _ {k} ^ {+} , \mathbf {u} _ {k}}} _ {\text { Linearize } f (\mathbf {x}, \mathbf {u})} \tag {9.48}\mathbf {A} _ {k} = \underbrace {e ^ {\mathbf {A} T}} _ {\text { Discretize } \mathbf {A}} \tag {9.49}\hat {\mathbf {x}} _ {k + 1} ^ {-} = \underbrace {\mathrm{RK4} (f , \hat {\mathbf {x}} _ {k} ^ {+} , \mathbf {u} _ {k} , T)} _ {\text { Numerical integration }} \tag {9.50}\mathbf {P} _ {k + 1} ^ {-} = \mathbf {A} _ {k} \mathbf {P} _ {k} ^ {-} \mathbf {A} _ {k} ^ {\top} + \mathbf {Q} _ {k} \tag {9.51}$$

Update step

$$\mathbf {C} _ {k + 1} = \underbrace {\left. \frac {\partial h (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} \right| _ {\hat {\mathbf {x}} _ {k + 1} ^ {-} , \mathbf {u} _ {k + 1}}} _ {\text { Linearize } h (\mathbf {x}, \mathbf {u})} \tag {9.52}\mathbf {K} _ {k + 1} = \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} (\mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} + \mathbf {R} _ {k + 1}) ^ {- 1} \tag {9.53}\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {K} _ {k + 1} \left(\mathbf {y} _ {k + 1} - h \left(\hat {\mathbf {x}} _ {k + 1} ^ {-}, \mathbf {u} _ {k + 1}\right)\right) \tag {9.54}\mathbf {P} _ {k + 1} ^ {+} = \left(\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}\right) \mathbf {P} _ {k + 1} ^ {-} \left(\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}\right) ^ {\top} + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top} \tag {9.55}$$

f(x, u) continuous dynamical model xˆ state estimate vector

h(x, u) measurement model u input vector

T sample timestep duration y output vector

P error covariance matrix Q process noise covariance

K Kalman gain matrix R measurement noise covariance

where a superscript of minus denotes a priori and plus denotes a posteriori estimate (before and after update respectively).

![](image/b9ad42e38b79c473bb785451eefb6cfb115bd3f4e09650d30d0985523908feaa.jpg)

To implement a discrete time extended Kalman filter from a continuous model, the dynamical model can be numerically integrated via a method from section 7.9 and the continuous time Q and R matrices can be discretized using theorem 7.3.1.

<table><tr><td>Matrix</td><td>Rows × Columns</td><td>Matrix</td><td>Rows × Columns</td></tr><tr><td>A</td><td>states × states</td><td> $\hat{x}$ </td><td>states × 1</td></tr><tr><td>C</td><td>outputs × states</td><td>u</td><td>inputs × 1</td></tr><tr><td>P</td><td>states × states</td><td>y</td><td>outputs × 1</td></tr><tr><td>K</td><td>states × outputs</td><td>Q</td><td>states × states</td></tr><tr><td></td><td></td><td>R</td><td>outputs × outputs</td></tr></table>

Table 9.3: Extended Kalman filter matrix dimensions
