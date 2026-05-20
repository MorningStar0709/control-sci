# C.1.2 Minimization

Given theorem 5.12.1 and corollary 5.12.3, find the minimum of J by taking the partial derivative with respect to $\mathbf { u } _ { k }$ and setting the result to 0.

$$\frac {\partial \mathbf {J}}{\partial \mathbf {u} _ {k}} = 2 \mathbf {B} ^ {\top} \mathbf {Q} (\mathbf {B u} _ {k} - (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})) + 2 \mathbf {R u} _ {k}\mathbf {0} = 2 \mathbf {B} ^ {\top} \mathbf {Q} (\mathbf {B u} _ {k} - (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})) + 2 \mathbf {R u} _ {k}\mathbf {0} = \mathbf {B} ^ {\top} \mathbf {Q} (\mathbf {B u} _ {k} - (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})) + \mathbf {R u} _ {k}\mathbf {0} = \mathbf {B} ^ {\top} \mathbf {Q} \mathbf {B} \mathbf {u} _ {k} - \mathbf {B} ^ {\top} \mathbf {Q} (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}) + \mathbf {R u} _ {k}\mathbf {B} ^ {\top} \mathbf {Q} \mathbf {B} \mathbf {u} _ {k} + \mathbf {R} \mathbf {u} _ {k} = \mathbf {B} ^ {\top} \mathbf {Q} (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})(\mathbf {B} ^ {\top} \mathbf {Q} \mathbf {B} + \mathbf {R}) \mathbf {u} _ {k} = \mathbf {B} ^ {\top} \mathbf {Q} (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})\mathbf {u} _ {k} = \left(\mathbf {B} ^ {\top} \mathbf {Q} \mathbf {B} + \mathbf {R}\right) ^ {- 1} \mathbf {B} ^ {\top} \mathbf {Q} \left(\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}\right)$$

Theorem C.1.1 — QR-weighted linear plant inversion. Given the discrete model $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } + \mathbf { B } \mathbf { u } _ { k }$ , the plant inversion feedforward is

$$\mathbf {u} _ {k} = \mathbf {K} _ {f f} (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})$$

where $\mathbf { K } _ { f f } = ( \mathbf { B } ^ { \mathsf { T } } \mathbf { Q } \mathbf { B } + \mathbf { R } ) ^ { - 1 } \mathbf { B } ^ { \mathsf { T } } \mathbf { Q } , \mathbf { r } _ { k + 1 }$ is the reference at the next timestep, and $\mathbf { r } _ { k }$ is the reference at the current timestep.

Figure C.1 shows plant inversion applied to a second-order CIM motor model.

Plant inversion isn’t as effective with both Q and R cost because the R matrix penalized control effort. The reference tracking with no cost matrices is much better.

![](image/180ca9e988e403c5ab1a026087a60b92bd17aa209ebd6944cacef94d6e224af0.jpg)

<details>
<summary>line</summary>
