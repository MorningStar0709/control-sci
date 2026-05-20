# Balanced Model Reduction

Simple linear models/controllers are normally preferred over complex ones in control system design for some obvious reasons: They are much easier to do analysis and synthesis with. Furthermore, simple controllers are easier to implement and are more reliable because there are fewer things to go wrong in the hardware or bugs to fix in the software. In the case when the system is infinite dimensional, the model/controller approximation becomes essential. In this chapter we consider the problem of reducing the order of a linear multivariable dynamical system. There are many ways to reduce the order of a dynamical system. However, we shall study only one of them: the balanced truncation method. The main advantage of this method is that it is simple and performs fairly well.

A model order-reduction problem can, in general, be stated as follows: Given a fullorder model $G ( s )$ , find a lower-order model (say, an rth order model $G _ { r } )$ , such that G and $G _ { r }$ are close in some sense. Of course, there are many ways to define the closeness of an approximation. For example, one may desire that the reduced model be such that

$$G = G _ {r} + \Delta_ {a}$$

and $\Delta _ { a }$ is small in some norm. This model reduction is usually called an additive model reduction problem. We shall be only interested in $\mathcal { L } _ { \infty }$ norm approximation in this book. Once the norm is chosen, the additive model reduction problem can be formulated as

$$\inf _ {\deg (G _ {r}) \leq r} \| G - G _ {r} \| _ {\infty}.$$

In general, a practical model reduction problem is inherently frequency-weighted $( \mathrm { i . e . }$ , the requirement on the approximation accuracy at one frequency range can be drastically different from the requirement at another frequency range). These problems can, in general, be formulated as frequency-weighted model reduction problems:

$$\inf _ {\deg (G _ {r}) \leq r} \| W _ {o} (G - G _ {r}) W _ {i} \| _ {\infty}$$

with an appropriate choice of $W _ { i }$ and $W _ { o }$ . We shall see in this chapter how the balanced realization can give an effective approach to the aforementioned model reduction problems.
