# D.2 Kalman filter as Luenberger observer

A Luenberger observer is defined as

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \hat {\mathbf {y}} _ {k}) \tag {D.1}\hat {\mathbf {y}} _ {k} = \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-} \tag {D.2}$$

where a superscript of minus denotes a priori and plus denotes a posteriori estimate. Combining equation (D.1) and equation (D.2) gives

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-}) \tag {D.3}$$

The following is a Kalman filter that considers the current update step and the next predict step together rather than the current predict step and current update step.

Update step

$$\mathbf {K} _ {k} = \mathbf {P} _ {k} ^ {-} \mathbf {C} ^ {\top} (\mathbf {C P} _ {k} ^ {-} \mathbf {C} ^ {\top} + \mathbf {R}) ^ {- 1} \tag {D.4}\hat {\mathbf {x}} _ {k} ^ {+} = \hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {K} _ {k} (\mathbf {y} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-}) \tag {D.5}\mathbf {P} _ {k} ^ {+} = (\mathbf {I} - \mathbf {K} _ {k} \mathbf {C}) \mathbf {P} _ {k} ^ {-} \tag {D.6}$$

Predict step

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {+} + \mathbf {B} \mathbf {u} _ {k} \tag {D.7}\mathbf {P} _ {k + 1} ^ {-} = \mathbf {A} \mathbf {P} _ {k} ^ {+} \mathbf {A} ^ {\top} + \mathbf {Q} \tag {D.8}$$

Substitute equation (D.5) into equation (D.7).

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \mathbf {A} (\hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {K} _ {k} (\mathbf {y} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-})) + \mathbf {B} \mathbf {u} _ {k}\hat {\mathbf {x}} _ {k + 1} ^ {+} = \mathbf {A} \mathbf {x} _ {k} ^ {-} + \mathbf {A} \mathbf {K} _ {k} (\mathbf {y} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-}) + \mathbf {B} \mathbf {u} _ {k}\hat {\mathbf {x}} _ {k + 1} ^ {+} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {A} \mathbf {K} _ {k} (\mathbf {y} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-})$$

$\operatorname { L e t } \mathbf { L } = \mathbf { A } \mathbf { K } _ { k } .$

$$\hat {\mathbf {x}} _ {k + 1} ^ {+} = \mathbf {A} \hat {\mathbf {x}} _ {k} ^ {-} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} ^ {-}) \tag {D.9}$$

which matches equation (D.3). Therefore, the eigenvalues of the Kalman filter observer can be obtained by

$$
\begin{array}{l} \operatorname{eig} (\mathbf {A} - \mathbf {L C}) \\ \operatorname{eig} \left(\mathbf {A} - \left(\mathbf {A K} _ {k}\right) (\mathbf {C})\right) \\ \operatorname{eig} \left(\mathbf {A} \left(\mathbf {I} - \mathbf {K} _ {k} \mathbf {C}\right)\right) \tag {D.10} \\ \end{array}
$$
