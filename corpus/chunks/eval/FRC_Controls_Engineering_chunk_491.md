# B.4.2 Following reference input matrix

The feedback control law above makes the open-loop system behave like $\mathbf { A } _ { r e f }$ , but the input dynamics are still that of the original system. Here’s how to make the input dynamics behave like $\mathbf { B } _ { r e f }$ . We want to find the $\mathbf { u } _ { i m f , k }$ that makes the real model follow the reference model.

$$\mathbf {x} _ {k + 1} = \mathbf {A x} _ {k} + \mathbf {B u} _ {i m f, k}\mathbf {z} _ {k + 1} = \mathbf {A} _ {r e f} \mathbf {z} _ {k} + \mathbf {B} _ {r e f} \mathbf {u} _ {k}$$

Let x = z.

$$\mathbf {x} _ {k + 1} = \mathbf {z} _ {k + 1}\mathbf {A} \mathbf {x} _ {k} + \mathbf {B} \mathbf {u} _ {i m f, k} = \mathbf {A} _ {r e f} \mathbf {x} _ {k} + \mathbf {B} _ {r e f} \mathbf {u} _ {k}\mathbf {B} \mathbf {u} _ {i m f, k} = \mathbf {A} _ {r e f} \mathbf {x} _ {k} - \mathbf {A} \mathbf {x} _ {k} + \mathbf {B} _ {r e f} \mathbf {u} _ {k}\mathbf {B} \mathbf {u} _ {i m f, k} = (\mathbf {A} _ {r e f} - \mathbf {A}) \mathbf {x} _ {k} + \mathbf {B} _ {r e f} \mathbf {u} _ {k}\mathbf {u} _ {i m f, k} = \mathbf {B} ^ {+} ((\mathbf {A} _ {r e f} - \mathbf {A}) \mathbf {x} _ {k} + \mathbf {B} _ {r e f} \mathbf {u} _ {k})\mathbf {u} _ {i m f, k} = - \mathbf {B} ^ {+} (\mathbf {A} - \mathbf {A} _ {r e f}) \mathbf {x} _ {k} + \mathbf {B} ^ {+} \mathbf {B} _ {r e f} \mathbf {u} _ {k}$$

The first term makes the open-loop poles match that of the reference model, and the second term makes the input behave like that of the reference model.
