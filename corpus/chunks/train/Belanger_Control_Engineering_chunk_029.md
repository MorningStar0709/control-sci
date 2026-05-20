A system that can be described by a finite number of state variables is called a lumped system. Not all systems are of this type. For example, to predict the motion of a vibrating string, we need to know the initial position and velocity of every point along the string's length. But those are functions of the distance variable, and a function has an infinite number of points; it cannot be specified by a finite number of variables. There are many such systems in practice—for example, a flexible link of a robotic manipulator, a packed distillation column, a transmission line. They are usually represented by partial differential equations and are called distributed systems. Fortunately, it is almost always possible to approximate a distributed system by use of a lumped system; that is why, except for rare excursions, this book is concerned with lumped systems.

State equations have the further advantage of being in a form suitable for numerical solution. Mathematically,

$$\mathbf {x} (t) = \mathbf {x} (t _ {0}) + \int_ {t _ {0}} ^ {t} \mathbf {f} [ \mathbf {x} (\tau), \mathbf {u} (\tau), \tau ] d \tau . \tag {2.12}$$

The integration in Equation 2.12 cannot be carried out directly, because $\mathbf{x}(\tau), t_0 \leq \tau < t$ , is not known in advance; this integral is not a quadrature.

The numerical solution of differential equations has been, and continues to be, the subject of much investigation $[1,2]$ . Today the problems are well understood, and many software packages have been developed to solve differential equations.
