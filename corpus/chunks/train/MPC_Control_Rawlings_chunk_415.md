# 3.6.2 Ancillary Controller

The purpose of the ancillary controller is to maintain the state of the uncertain system $x ^ { + } = f ( x , u ) + w$ close to the trajectory of the nominal system $z ^ { + } ~ = ~ f ( z , \bar { \kappa } _ { N } ( z ) )$ . The ancillary controller replaces the controller $u = \nu + K ( x - z )$ employed in the linear case. To obtain u in the nonlinear control, we determine a control sequence that minimizes the cost of the deviation between the trajectories of the two systems, $x ^ { + } = f ( x , u )$ and $z ^ { + } = f ( z , \bar { \kappa } _ { N } ( z ) )$ , with initial states x and z, respectively, and choose u to be the first element of this sequence. If the optimal control problem is properly posed, the resultant control u steers the state of the deterministic system $x ^ { + } ~ = ~ f ( x , u )$ toward the nominal trajectory, and, hence, as in the linear case, tends to keep the trajectory of the uncertain system $x ^ { + } = f ( x , u ) + w$ close to the nominal trajectory.

The ancillary controller is, therefore, based on the composite system

$$x ^ {+} = f (x, u) \tag {3.49}z ^ {+} = f (z, \bar {\kappa} _ {N} (z)) \tag {3.50}$$

The cost $V _ { N } ( x , z , { \bf u } )$ that measures the distance between the trajectories of these two systems is defined by

$$V _ {N} (x, z, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell \big (x (i) - z ^ {*} (i; z), u (i) - v ^ {*} (i; z) \big) \tag {3.51}$$
