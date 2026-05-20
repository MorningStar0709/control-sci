# Minimization

Given theorem 5.12.1, find the minimum of J by taking the partial derivative with respect to $\mathbf { u } _ { k }$ and setting the result to 0.

$$
\begin{array}{l} \frac {\partial \mathbf {J}}{\partial \mathbf {u} _ {k}} = 2 \mathbf {B} ^ {\top} \left(\mathbf {B u} _ {k} - \left(\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}\right)\right) \\ \mathbf {0} = 2 \mathbf {B} ^ {\top} \left(\mathbf {B u} _ {k} - \left(\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}\right)\right) \\ \mathbf {0} = 2 \mathbf {B} ^ {\top} \mathbf {B u} _ {k} - 2 \mathbf {B} ^ {\top} \left(\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}\right) \\ \mathbf {B} ^ {\top} \mathbf {B u} _ {k} = \mathbf {B} ^ {\top} \left(\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}\right) \\ \end{array}
2 \mathbf {B} ^ {\top} \mathbf {B u} _ {k} = 2 \mathbf {B} ^ {\top} \left(\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}\right)\mathbf {u} _ {k} = \left(\mathbf {B} ^ {\top} \mathbf {B}\right) ^ {- 1} \mathbf {B} ^ {\top} \left(\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}\right)
$$

$( \mathbf { B } ^ { \mathsf { T } } \mathbf { B } ) ^ { - 1 } \mathbf { B } ^ { \mathsf { T } }$ is the left Moore-Penrose pseudoinverse of B denoted by $\mathbf { B } ^ { + }$ .

Theorem 7.8.1 — Linear plant inversion. Given the discrete model $\mathbf { x } _ { k + 1 } ~ =$ $\mathbf { A x } _ { k } + \mathbf { B u } _ { k }$ , the plant inversion feedforward is

$$\mathbf {u} _ {k} = \mathbf {B} ^ {+} (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k}) \tag {7.16}$$

where $\mathbf { B } ^ { + }$ is the Moore-Penrose pseudoinverse of B, $\mathbf { r } _ { k + 1 }$ is the reference at the next timestep, and $\mathbf { r } _ { k }$ is the reference at the current timestep.
