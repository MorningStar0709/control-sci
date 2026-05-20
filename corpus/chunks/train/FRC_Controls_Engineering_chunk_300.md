$$\mathbf {P} _ {k + 1} ^ {+} = \mathrm{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-}) - \mathbf {K} _ {k + 1} \mathbf {v} _ {k + 1})$$

Factor out $\mathbf x _ { k + 1 } - \hat { \mathbf x } _ { k + 1 } ^ { - }$ to the right.

$$\mathbf {P} _ {k + 1} ^ {+} = \mathrm{cov} ((\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-}) - \mathbf {K} _ {k + 1} \mathbf {v} _ {k + 1})$$

Covariance is a linear operator, so it can be applied to each term separately. Covariance squares terms internally, so the negative sign on ${ \bf K } _ { k + 1 } { \bf v } _ { k + 1 }$ is removed.

$$\mathbf {P} _ {k + 1} ^ {+} = \mathrm{cov} ((\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-})) + \mathrm{cov} (\mathbf {K} _ {k + 1} \mathbf {v} _ {k + 1})$$

Now just evaluate the covariances.

$$
\begin{array}{l} \mathbf {P} _ {k + 1} ^ {+} = \left(\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}\right) \operatorname{cov} \left(\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-}\right) \left(\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}\right) ^ {\top} \\ + \mathbf {K} _ {k + 1} c o v (\mathbf {v} _ {k + 1}) \mathbf {K} _ {k + 1} ^ {\top} \\ \mathbf {P} _ {k + 1} ^ {+} = (\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) \mathbf {P} _ {k + 1} ^ {-} (\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) ^ {\top} + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top} \tag {9.18} \\ \end{array}
$$

This is the Joseph form of the covariance update equation, which is valid for all Kalman gains.

![](image/b394b4bff75eed3db8f6b284e44a7609391cbeeda70a5b7edb347518e4e04f69.jpg)

The Joseph form is helpful in floating point implementations of the Kalman filter since it has better numerical stability than the optimal Kalman gain form discussed later.
