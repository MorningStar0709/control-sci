# Theorem 9.2.2 — Luenberger observer with separate predict/update.

Predict step

$$\hat {\mathbf {x}} _ {k + 1} ^ {-} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {B} \mathbf {u} _ {k} \tag {9.5}$$

Update step

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {A} ^ {- 1} \mathbf {L} (\mathbf {y} _ {k} - \hat {\mathbf {y}} _ {k}) \tag {9.6}\hat {\mathbf {y}} _ {k} = \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-} \tag {9.7}$$

See appendix D.2.1 for a derivation.
