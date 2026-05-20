(i) Air Vehicle Control Software: The software provides basic flight profile commands, which are Mach number, clearance altitude, and climb/dive rate limits for each flight segment including bank angle commands for steering to the ground track defined by the waypoints (see item “m” below) in the guidance route.
(j) Terrain Following: The guidance system performs all required terrain-following functions.
In case a “breaklock” occurs due to jamming or malfunction of the radar altimeter, the guidance system will command the missile to climb to a safe altitude utilizing the backup baro/inertial altitude system.
Upon reacquisition of radar altimeter data, the guidance system will command the missile back to the terrain-following mode.
(k) Terrain Correlation (TC): This system is used to update the navigation systems to correct drift errors and provide the navigation system with a finite position fix.
This function is accomplished by averaging altitude over a waypoint, calculating

position and time, and adjustment of mean sample altitude. This system furnishes terrain altitude to the guidance computer and thus to the navigation system. The system utilizes stored map data, which are loaded prior to flight (see also Section 7.3).

(l) Navigation: The guidance system utilizes a 15-state Kalman filter navigation system using terrain correlation (TC) fixes. The guidance system software contains the equation for instrument compensation, velocity, and position computations. Navigation is three-dimensional with the vertical channel slaved to an external reference, barometric, or radar altimeter. The inertial navigation system determines missile position, velocity, attitude, and altitude. Moreover, the guidance system has the capability for air alignment and accepts initial conditions for navigation computation from the carrier aircraft, including retargeting.
