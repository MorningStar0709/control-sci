# Passivity

We now present another stability theorem that is also based on the input-output point of view. The starting point is the notion of passivity, which is an abstract formulation of the idea of energy dissipation. Passive systems are common in engineering. A system composed only of components like resistors, capacitors, and inductors is one example from electrical engineering. A system composed of masses, springs, and dashpots is an example from mechanical engineering. When dealing with electrical systems, we will consider two-port systems in which the current is the input and the voltage is the output. The same concepts apply to mechanical systems, in which the variables are position and force.

Passivity is naturally associated with power dissipation. Such a concept can be defined for linear as well as nonlinear systems. Roughly speaking, the passivity theorem says that a feedback connection of one passive system and one strictly passive system is stable. To state the result formally, we need an abstract notion of passivity. We start with the operator view of systems, in which a system is represented by an operator mapping signals to signals. The signal space is assumed to be $L_{2e}$ with a scalar product defined by

$$\langle x \mid y \rangle = \int_ {0} ^ {\infty} x (s) y (s) d s = \int_ {0} ^ {T} x (s) y (s) d s$$

We have the following definition.
