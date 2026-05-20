# D.2.1 Luenberger observer with separate prediction and update

To run a Luenberger observer with separate prediction and update steps, substitute the relationship between the Luenberger observer and Kalman filter matrices derived above into the Kalman filter equations.

Appendix D.2 shows that $\mathbf { L } = \mathbf { A } \mathbf { K } _ { k }$ . Since L and A are constant, one must assume ${ \bf K } _ { k }$ has reached steady-state. Then, $\mathbf { K } = \mathbf { A } ^ { - 1 } \mathbf { L }$ . Substitute this into the Kalman filter update equation.

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {K} (\mathbf {y} _ {k + 1} - \mathbf {C} \hat {\mathbf {x}} _ {k + 1} ^ {-})\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {A} ^ {- 1} \mathbf {L} (\mathbf {y} _ {k + 1} - \mathbf {C} \hat {\mathbf {x}} _ {k + 1} ^ {-})$$

Substitute in equation (9.4).

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {A} ^ {- 1} \mathbf {L} (\mathbf {y} _ {k + 1} - \hat {\mathbf {y}} _ {k + 1})$$

The predict step is the same as the Kalman filter’s. Therefore, a Luenberger observer run with prediction and update steps is written as follows.

Predict step

$$\hat {\mathbf {x}} _ {k + 1} ^ {-} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {B} \mathbf {u} _ {k} \tag {D.11}$$

Update step

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {A} ^ {- 1} \mathbf {L} \left(\mathbf {y} _ {k + 1} - \hat {\mathbf {y}} _ {k + 1}\right) \tag {D.12}\hat {\mathbf {y}} _ {k + 1} = \mathbf {C} \hat {\mathbf {x}} _ {k + 1} ^ {-} \tag {D.13}$$
