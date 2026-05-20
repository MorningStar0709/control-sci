Additionally, the position error ellipse data are used to check whether adequate time is available to complete terrain-correlation processing and remove the position correction from the position update before arriving at the target. Furthermore, NAM also determines whether the waypoints surrounding the terrain correlation maps are correctly located. Since the terrain correlation process requires that the maps be overflown at the proper heading, this calculation can correct the waypoint preceding and following each map. More importantly, the navigation system must perform a procedure for recomputing the waypoint location. This procedure checks the location of waypoints in front of and behind each map and verifies that they form a geodesic path on the Earth ellipsoid. The geodesic path passes through the map center with the desired heading. A new waypoint is calculated, and if it is different from the input waypoint by 10 ft, the recomputed value is placed in the recomputed waypoint field of the data structure. The recomputed flag is set for the mission planner and/or system disposition. This procedure must also be performed on speed or altitude waypoints that may lie between map entries and exits.

Mathematical calculations performed within the NAM will produce results sufficiently accurate to ensure accuracy within the following tolerances:

$$
\begin{array}{l} \text { Latitude   and   Longitude: } \pm 0. 0 0 0 0 1 ^ {\circ}, \\ \text { Velocity: } \quad \pm 1. 0 \mathrm{m/sec}, \\ \text {   Heading:   } \pm 0. 1 ^ {\circ}, \\ \text {   Map   Cell   Size:   } \pm 1. 0 \text {   meter,   } \\ \text { Time: } \quad \pm 1. 0 \text {   second. } \\ \end{array}
$$

![](image/c6105598593cabf649b8c3d28f6fbc999618010a6dc069e5028912ae245e5946.jpg)

<details>
<summary>flowchart</summary>
