# a posteriori estimate covariance update equation

The following is the definition of the a posteriori estimate covariance matrix.

$$\mathbf {P} _ {k + 1} ^ {+} = \mathrm{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {+})$$

Substitute in the a posteriori update equation and expand the measurement equations.

$$\mathbf {P} _ {k + 1} ^ {+} = \mathrm{cov} (\mathbf {x} _ {k + 1} - (\hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {K} _ {k + 1} (\mathbf {y} _ {k + 1} - \hat {\mathbf {y}} _ {k + 1})))\mathbf {P} _ {k + 1} ^ {+} = \operatorname{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} (\mathbf {y} _ {k + 1} - \hat {\mathbf {y}} _ {k + 1}))\mathbf {P} _ {k + 1} ^ {+} = \operatorname{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} (\left(\mathbf {C} _ {k + 1} \mathbf {x} _ {k + 1} + \mathbf {D} _ {k + 1} \mathbf {u} _ {k + 1} + \mathbf {v} _ {k + 1}\right)- \left(\mathbf {C} _ {k + 1} \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {D} _ {k + 1} \mathbf {u} _ {k + 1})\right))\mathbf {P} _ {k + 1} ^ {+} = \operatorname{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} (\mathbf {C} _ {k + 1} \mathbf {x} _ {k + 1} + \mathbf {D} _ {k + 1} \mathbf {u} _ {k + 1} + \mathbf {v} _ {k + 1}\left. - \mathbf {C} _ {k + 1} \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {D} _ {k + 1} \mathbf {u} _ {k + 1})\right)$$

Reorder terms.

$$\mathbf {P} _ {k + 1} ^ {+} = \operatorname{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} (\mathbf {C} _ {k + 1} \mathbf {x} _ {k + 1} - \mathbf {C} _ {k + 1} \hat {\mathbf {x}} _ {k + 1} ^ {-}\left. + \mathbf {D} _ {k + 1} \mathbf {u} _ {k + 1} - \mathbf {D} _ {k + 1} \mathbf {u} _ {k + 1} + \mathbf {v} _ {k + 1})\right)$$

The $\mathbf { D } _ { k + 1 } \mathbf { u } _ { k + 1 }$ terms cancel.

$$\mathbf {P} _ {k + 1} ^ {+} = \mathrm{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} (\mathbf {C} _ {k + 1} \mathbf {x} _ {k + 1} - \mathbf {C} _ {k + 1} \hat {\mathbf {x}} _ {k + 1} ^ {-} + \mathbf {v} _ {k + 1}))$$

Distribute ${ \bf K } _ { k + 1 }$ to $\mathbf { v } _ { k + 1 }$ .

$$\mathbf {P} _ {k + 1} ^ {+} = \mathrm{cov} (\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} ^ {-} - \mathbf {K} _ {k + 1} (\mathbf {C} _ {k + 1} \mathbf {x} _ {k + 1} - \mathbf {C} _ {k + 1} \hat {\mathbf {x}} _ {k + 1} ^ {-}) - \mathbf {K} _ {k + 1} \mathbf {v} _ {k + 1})$$

Factor out $\mathbf { C } _ { k + 1 }$ .
