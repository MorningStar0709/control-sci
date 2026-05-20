Let now ψ be defined as the heading of the missile’s velocity vector, measured relative to north. Also, a positive heading will correspond to a positive rotation about the z-axis. The direction cosines defining the trajectory are propagated every 60 seconds. Next, we note that the heading $( \psi )$ and the time required to travel along a great circle path from route point (j) to the route point (j + 1) will be computed here for the free flight trajectory only. From the law of cosines for spherical triangles, the heading angle is obtained from the relation [8]

$$\cos \psi = \{\sin \phi_ {2} - \sin \phi_ {1} \cos (\rho / a ^ {\prime}) \} / \cos \phi_ {1} [ \sin (\rho / a ^ {\prime}) ], \tag {7.8}$$

where

$$a ^ {\prime} = \text { average radius of the Earth },\phi_ {1} = \text { latitude of the initial (or present) position },\phi_ {2} = \text { latitude of the target position },\rho = \text { great circle distance (i.e., from one waypoint to the next) }.$$

The direction cosines at the launch position are initialized as follows:

$$C _ {x x} = \cos \phi_ {L}, \quad C _ {y x} = \sin \phi_ {L} \sin \lambda_ {L},C _ {x y} = 0, \quad C _ {y y} = - \cos \lambda_ {L},C _ {x z} = - \sin \phi_ {L}, \quad C _ {y z} = \cos \phi_ {L} \sin \lambda_ {L},$$

where $\phi _ { L } , \lambda _ { L }$ are the missile launch latitude and longitude, respectively. This definition of direction cosines forces the wander angle to zero at launch. The time to reach the target can be calculated from the relation [8]

$$\delta t _ {T} = (a ^ {\prime} / V _ {j}) \cos^ {- 1} [ \sin \phi_ {j} \sin \phi_ {T} + \cos \phi_ {j} \cos \phi_ {T} \cos (\lambda_ {T} - \lambda_ {j}) ], \tag {7.9}$$

where

$$\phi_ {j} = \text { latitude of the } j \text { th route point },\phi_ {T} = \text { latitude of the target },\lambda_ {j} = \text { longitude of the } j \text { th route point },\lambda_ {T} = \text { longitude of the target },V _ {j} = \text { air vehicle ground speed at the } j \text { th route point. }$$

The time at which route point (j + 1) will be reached is given by

$$t _ {j + 1} = t + \delta t _ {j}. \tag {7.10}$$

Finally, the ground velocity components of $V _ { j }$ for the free flight route point indices, $j = 0 , 1 , 2 , 3 , \ldots$ , are given by

$$V _ {x j} = (\cos \psi_ {j} \cos \alpha + \sin \psi_ {j} \sin \alpha) V _ {j}, \tag {7.11a}V _ {y j} = (- \cos \psi_ {j} \sin \alpha + \sin \psi_ {j} \cos \alpha) V _ {j}. \tag {7.11b}$$

For the Kaman filter discussed in Section 7.2.2, the 15 error state equations for the free flight are as follows:
