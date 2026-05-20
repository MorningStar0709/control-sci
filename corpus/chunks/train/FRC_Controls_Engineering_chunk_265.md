$$\mathbf {x} _ {k + 1} - \hat {\mathbf {x}} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} - \left(\mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B u} _ {k} + \mathbf {L C e} _ {k}\right)\mathbf {e} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} - \left(\mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B u} _ {k} + \mathbf {L C e} _ {k}\right)\mathbf {e} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k} - \mathbf {A} \hat {\mathbf {x}} _ {k} - \mathbf {B u} _ {k} - \mathbf {L C e} _ {k}\mathbf {e} _ {k + 1} = \mathbf {A x} _ {k} - \mathbf {A} \hat {\mathbf {x}} _ {k} - \mathbf {L C e} _ {k}\mathbf {e} _ {k + 1} = \mathbf {A} (\mathbf {x} _ {k} - \hat {\mathbf {x}} _ {k}) - \mathbf {L C e} _ {k}\mathbf {e} _ {k + 1} = \mathbf {A e} _ {k} - \mathbf {L C e} _ {k}\mathbf {e} _ {k + 1} = (\mathbf {A} - \mathbf {L C}) \mathbf {e} _ {k} \tag {9.8}$$

For equation (9.8) to have a bounded output, the eigenvalues of A − LC must be within the unit circle. These eigenvalues represent how fast the estimator converges to the true state of the given model. A fast estimator converges quickly while a slow estimator avoids amplifying noise in the measurements used to produce a state estimate.

The effect of noise can be seen if it is modeled stochastically as

$$\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} ((\mathbf {y} _ {k} + \nu_ {k}) - \hat {\mathbf {y}} _ {k})$$

where $\nu _ { k }$ is the measurement noise. Rearranging this equation yields

$$\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \hat {\mathbf {y}} _ {k} + \nu_ {k})\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \hat {\mathbf {y}} _ {k}) + \mathbf {L} \nu_ {k}$$

As L increases, the measurement noise is amplified.
