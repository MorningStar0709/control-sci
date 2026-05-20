(b) Compute a unique velocity vector ${ \bf V } _ { c }$ to intersect the terminal point at the specified time. Compute the local gravitational acceleration g, where $\mathbf { g } =$ $- ( \mu / r ^ { 3 } ) \mathbf { r }$ .

(c) Compare the calculated velocity $\mathbf { V } _ { c }$ to the actual velocity of the missile $\mathbf { V } _ { m }$ to produce $\mathbf { V } _ { g }$ .

(d) Produce the steering command $\mathbf { u } = ( u _ { 1 } , u _ { 2 } )$ on the basis of $\mathbf { \sigma } _ { \mathbf { 1 } T } = k ( \mathbf { V } _ { c } - \mathbf { V } _ { m } ) - \mathbf { g }$ where:

(1) $u _ { 1 }$ is the angle of the thrust vector a $T$ .

(2) $u _ { 2 }$ is $t _ { b o }$ or t such that $\| \mathbf { V } _ { g } \| = 0$

This algorithm, in general, requires the solution of a highly nonlinear set of differential equations at each control point for a rather simple description of the terminal conditions. If this computation is accomplished in an onboard computer, the computation cycle is usually long and complicated, since a closed-form solution of the equations of motion is not usually possible.

In summary, the explicit guidance philosophy requires the existence of closedform or approximate closed-form guidance equations describing a set of general terminal conditions in terms of current control and state variables such that an explicit value of control can be computed at every admissible $x \in E ^ { n }$ . These guidance equations usually take the form of polynomials that are generated for each particular application. This implies that the desired terminal conditions can be easily varied or modified before actual guidance is initiated or even modified to some degree during the guidance phase.

Explicit guidance is also well suited to a mobile launcher. In this case, the missile designer wants to have the capability of being able to launch the vehicle at any geographical location and at any time. Within certain mission bounds, this type of system requirement can readily be met using an explicit guidance method.
