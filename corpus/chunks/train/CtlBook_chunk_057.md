# 2.4 Equations of Motion

Let's assume a system componsed of multiple masses connected by springs and dampers among each other. A force $F _ { i }$ acts on each mass, Mi. D'Alembert's Principle equates the famous inertial force f = mx¨ to all the other forces acting on a body. In a form that we will use:

$$M _ {i} \ddot {x} + \sum_ {j} B _ {j} (\dot {x} _ {i} - \dot {x} _ {j}) + \sum_ {k} K _ {k} (x _ {i} - x _ {k}) = F _ {i} \tag {2.1}$$

where there are several damping components connected between the mass $M _ { i }$ and other masses indicated by j, and there are several spring components connected to some other masses indicated by k. We write this equation for each mass in the system.

Equation 2.1 is refered to as an Equation of Motion (EOM).

F indicates external forces imposed on the mass from sources other than springs and dampers in the system such as an actuator. If the translational system is vertical, the force of gravity would be one such force, $F = M g$ .

The signs in equations of motion can be tricky. There is really no correct sign for each term, because the equation is valid if you multiply both sides by −1. However if we stick with the following rules, we can write equations of motion in a consistent way so that we can easily keep signs straight:

 The positive term in each subtraction associated with B and K must be the displacement of the mass for which the current EOM is being written.   
 Keep all position sign conventions consistent. For example, all displacments positive to the right or positive facing up.   
 Keep the sign convention of the external applied force the same as for the displacements and keep it alone on the right-hand-side.
