# Discussion

Linear plant inversion in theorem 7.8.1 compensates for reference dynamics that don’t follow how the model inherently behaves. If they do follow the model, the feedforward has nothing to do as the model already behaves in the desired manner. When this occurs, $\mathbf { r } _ { k + 1 } - \mathbf { A r } _ { k }$ will return a zero vector.

For example, a constant reference requires a feedforward that opposes system dynamics that would change the state over time. If the system has no dynamics, then $\mathbf { A } = \mathbf { I }$ and thus

$$\mathbf {u} _ {k} = \mathbf {B} ^ {+} (\mathbf {r} _ {k + 1} - \mathbf {I r} _ {k})\mathbf {u} _ {k} = \mathbf {B} ^ {+} (\mathbf {r} _ {k + 1} - \mathbf {r} _ {k})$$

For a constant reference, $\mathbf { r } _ { k + 1 } = \mathbf { r } _ { k }$

$$\mathbf {u} _ {k} = \mathbf {B} ^ {+} (\mathbf {r} _ {k} - \mathbf {r} _ {k})\mathbf {u} _ {k} = \mathbf {B} ^ {+} (\mathbf {0})\mathbf {u} _ {k} = \mathbf {0}$$

so no feedforward is required to hold a system with no dynamics at a constant reference, as expected.

Figure 7.11 shows plant inversion applied to a second-order CIM motor model. Plant inversion accounts for the motor back-EMF and eliminates steady-state error.
