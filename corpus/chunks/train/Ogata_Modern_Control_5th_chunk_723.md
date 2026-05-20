$$\mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} (0) = \mathbf {C} \left[ \alpha_ {0} (t) \mathbf {I} + \alpha_ {1} (t) \mathbf {A} + \alpha_ {2} (t) \mathbf {A} ^ {2} + \dots + \alpha_ {m - 1} (t) \mathbf {A} ^ {m - 1} \right] \mathbf {x} (0) = \mathbf {0}$$

Consequently, for a certain $\mathbf { x } ( 0 )$ ,

$$\mathbf {y} (t) = \mathbf {C x} (t) = \mathbf {C e} ^ {\mathbf {A} t} \mathbf {x} (0) = \mathbf {0}$$

which implies that, for a certain ${ \bf x } ( 0 ) , { \bf x } ( 0 )$ cannot be determined from $\mathbf { y } ( t )$ . Therefore, the rank of matrix P must be equal to n.

Next we shall obtain the sufficient condition. Suppose that rank $\mathbf { P } = n$ . Since

$$\mathbf {y} (t) = \mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} (0)$$

by premultiplying both sides of this last equation by $e ^ { \mathbf { A } ^ { * } t } \mathbf { C } ^ { * }$ , we get

$$e ^ {\mathbf {A} ^ {*} t} \mathbf {C} ^ {*} \mathbf {y} (t) = e ^ {\mathbf {A} ^ {*} t} \mathbf {C} ^ {*} \mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} (0)$$

If we integrate this last equation from 0 to t, we obtain

$$\int_ {0} ^ {t} e ^ {\mathbf {A} * t} \mathbf {C} * \mathbf {y} (t) d t = \int_ {0} ^ {t} e ^ {\mathbf {A} * t} \mathbf {C} * \mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} (0) d t \tag {9-124}$$

Notice that the left-hand side of this equation is a known quantity. Define

$$\mathbf {Q} (t) = \int_ {0} ^ {t} e ^ {\mathbf {A} * t} \mathbf {C} * \mathbf {y} (t) d t = \text { known quantity } \tag {9-125}$$

Then, from Equations (9–124) and (9–125), we have

$$\mathbf {Q} (t) = \mathbf {W} (t) \mathbf {x} (0) \tag {9-126}$$

where

$$\mathbf {W} (t) = \int_ {0} ^ {t} e ^ {\mathbf {A} * \tau} \mathbf {C} * \mathbf {C} e ^ {\mathbf {A} \tau} d \tau$$

It can be established that $\mathbf W ( t )$ is a nonsingular matrix as follows: $\mathrm { I f } \left| \mathbf { W } ( t ) \right|$ were equal to 0, then

$$\mathbf {x} ^ {*} \mathbf {W} (t _ {1}) \mathbf {x} = \int_ {0} ^ {t _ {1}} \| \mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} \| ^ {2} d t = 0$$

which means that

$$\mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} = \mathbf {0}, \quad \mathrm{for} 0 \leq t \leq t _ {1}$$

which implies that rank $\mathbf { P } < n$ . Therefore, $\mathbf { \left| W ( \right|} t )  \neq 0 , \operatorname { o r } \mathbf { W } ( t )$ is nonsingular. Then, from Equation (9–126), we obtain

$$\mathbf {x} (0) = \left[ \mathbf {W} (t) \right] ^ {- 1} \mathbf {Q} (t) \tag {9-127}$$

and $\mathbf { x } ( 0 )$ can be determined from Equation (9–127).

Hence, we have proved that $\mathbf { x } ( 0 )$ can be determined from $\mathbf { y } ( t )$ if and only if rank $\mathbf { P } = n$ . Note that $\mathbf { x } ( 0 )$ and $\mathbf { y } ( t )$ are related by

$$\mathbf {y} (t) = \mathbf {C e} ^ {\mathbf {A} t} \mathbf {x} (0) = \alpha_ {0} (t) \mathbf {C x} (0) + \alpha_ {1} (t) \mathbf {C A x} (0) + \dots + \alpha_ {n - 1} (t) \mathbf {C A} ^ {n - 1} \mathbf {x} (0)$$
