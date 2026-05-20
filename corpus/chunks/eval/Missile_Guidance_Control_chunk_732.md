$$P = \Phi^ {\prime} P ^ {+} \Phi^ {\prime T} + Q ^ {\prime}, \tag {7.1}$$

where $\Phi ^ { \prime T }$ is the transpose of $\Phi ^ { \prime }$ . This procedure is repeated for second and third map centers of a three-map voting group, using stored values. The resulting error covariance matrix is the updated value that will later be output to the IOBT, enabling the mission planner to return to any map set and restart the covariance propagation. This submodule also sets and resets internal flags that indicate that the correlation process has been completed.

11.2 Compute Time Until Update: This submodule calculates the delay time for the third map of a voting group to finish correlating. (The time computation is performed on only those maps of a voting group that lie on a straight line). The delay is saved for later output to the IOBT. This module also calculates the time $t _ { u }$ at which correlation is completed. This value is saved for inertial computation to the time of update.

11.3 Compute Time Until Update Maneuver Complete: This submodule calculates the incremental time for the navigation error after update (and accounts for maximum downtrack error) to develop maneuver complete time $t _ { g }$ . This time is compared to the predicted time over target to verify that the missile has corrected and settled on a final heading before crossing the target. If this is not found to be the case, then an error message flag is generated to indicate that the final map group is too close to the target.

12. NAM Data Output: This module is composed of several submodules called upon for supplemental output calculations as necessary according to the type of IOBT data being processed.

12.1 Output Waypoint Error Ellipse: This submodule uses position covariance elements from the error covariance matrix to calculate error ellipse semimajor axis and semiminor axis one-sigma values and the heading of the ellipse as an angle from north to the semimajor axis. Error ellipses are calculated at waypoints, and just prior to and immediately after navigation update. The error ellipse is also calculated as a preparation for CEP.

12.2 Output Circular Error Probable CEP: This submodule is executed for CEP outputs to the IOBT. It accepts values of semimajor axis errors $\sigma _ { u }$ and semiminor axis error $\sigma _ { v }$ , and calculates the CEP according to [8]
