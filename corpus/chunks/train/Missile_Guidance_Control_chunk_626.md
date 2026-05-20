In the explicit guidance law, the launch portion of the trajectory is divided about equally in time into an open-loop and closed-loop phase. The open-loop phase is preprogrammed and consists of a vertical liftoff followed by a gravity turn to an approximate flight angle γ . The closed-loop phase, or guidance phase, is characterized by the computation of steering commands from the vehicle’s actual location $\mathbf { r } _ { T }$ , the desired range angle, and the time-of-flight T . Moreover, the closedloop phase of the launch trajectory is partitioned into a discrete set of control points $( t _ { 1 } , t _ { 2 } , \ldots , t _ { k } , \ldots , t _ { b o } )$ . The time duration between two neighboring points in this set is regulated by the time required for each computation cycle, which in turn produces a steering command and/or a cut-off signal. The terminal point (i.e., terminal conditions in this case) is described simply as the total range angle  (see Figure 6.1) and the total time of flight T , as given by (6.50) or (6.92).

Now by comparing the best estimate of the actual missile velocity ${ \bf V } _ { m } ( t _ { k } )$ to ${ \bf V } _ { c } ( t _ { k } )$ , the velocity-to-be-gained vector ${ \bf V } ( t _ { k } )$ is generated. Thus,

$$\mathbf {V} _ {g} (t _ {k}) = \mathbf {V} _ {c} (t _ {k}) - \mathbf {V} _ {m} (t _ {k}). \tag {6.170}$$

A simple steering philosophy is now apparent:

$$\mathbf {a} _ {e} = \mathbf {a} _ {T} + \mathbf {g},$$

where

$$\mathbf {a} _ {e} = \text { effective thrust acceleration },\mathbf {a} _ {T} = \text { actual thrust acceleration },\mathbf {g} = \text { gravitational acceleration at } \mathbf {r} (t _ {k}).$$

The steering philosophy is to align the effective thrust acceleration vector with $\mathbf { V } _ { g }$ ; thus

$$\mathbf {a} _ {e} = k \mathbf {V} _ {g},$$

where k is an arbitrary constant. Thus, using the above relations results in

$$\mathbf {a} _ {T} = k \left(\mathbf {V} _ {c} \left(t _ {k}\right) - \mathbf {V} _ {m} \left(t _ {k}\right)\right) - \mathbf {g},$$

as the steering law. The cut-off command is initiated when $\| \mathbf { V } _ { g } \| = 0$ . Thus, at burnout point the missile will continue on an unpowered trajectory to the terminal point. The following algorithm summarizes the computation cycle using the explicit guidance law:

(a) Measurement and generation of the best estimate of the vehicle’s state at each control point $t _ { k } ( t _ { 1 } , t _ { 2 } , \dots , t _ { k } , \dots t _ { b o } )$ .
