# 17.3.4 Flywheel

Here’s a problem formulation for flywheel MPC.

$$\min _ {\mathbf {x} _ {0: N}, \mathbf {u} _ {0: N - 1}} \sum_ {k = 0} ^ {N - 1} \left((\mathbf {r} - \mathbf {x} _ {k}) ^ {\top} \mathbf {Q} (\mathbf {r} - \mathbf {x} _ {k}) + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k}\right)$$

${ \mathrm { s u b j e c t ~ t o ~ } } \mathbf { x } _ { 0 } = { \mathrm { c u r r e n t ~ s t a t e } }$

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {k}\mathbf {u} _ {m i n} \leq \mathbf {u} _ {k} \leq \mathbf {u} _ {m a x}$$

where $\mathbf { x } _ { k } = \left[ { \boldsymbol { \omega } } \right] ^ { \mathsf { T } } , \mathbf { u } _ { k } = \left[ V \right] ^ { \mathsf { T } }$ , and r is the reference. Figure 17.4 shows the closedloop response, which is identical to infinite-horizon LQR with a plant inversion feedforward.
