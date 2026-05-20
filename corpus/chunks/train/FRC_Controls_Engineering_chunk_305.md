# Simplified a posteriori estimate covariance update equation

If the optimal Kalman gain is used, the a posteriori estimate covariance matrix update equation can be simplified. First, we’ll manipulate the equation for the optimal Kalman gain.

$$\mathbf {K} _ {k + 1} = \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} \mathbf {S} _ {k + 1} ^ {- 1}\mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} = \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top}\mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top} = \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} \mathbf {K} _ {k + 1} ^ {\top}$$

Now we’ll substitute it into equation (9.19).

$$\mathbf {P} _ {k + 1} ^ {+} = \mathbf {P} _ {k + 1} ^ {-} - \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} \mathbf {K} _ {k + 1} ^ {\top} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} + \mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top}\mathbf {P} _ {k + 1} ^ {+} = \mathbf {P} _ {k + 1} ^ {-} - \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\mathsf {T}} \mathbf {K} _ {k + 1} ^ {\mathsf {T}} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} + (\mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\mathsf {T}} \mathbf {K} _ {k + 1} ^ {\mathsf {T}})\mathbf {P} _ {k + 1} ^ {+} = \mathbf {P} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}$$

Factor out $\mathbf { P } _ { k + 1 } ^ { - }$ to the right.

$$\mathbf {P} _ {k + 1} ^ {+} = (\mathbf {I} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1}) \mathbf {P} _ {k + 1} ^ {-}$$
