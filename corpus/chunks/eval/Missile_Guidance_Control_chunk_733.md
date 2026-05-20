$$C E P = 0. 5 6 3 \sigma_ {u} + 0. 6 1 4 \sigma_ {v} \quad \text { if } \sigma_ {v} < 0. 3 5 \sigma_ {u}, \tag {7.6a}$$

and otherwise,

$$C E P = 0. 6 7 4 \sigma_ {u} + 0. 0 7 8 6 \sigma_ {v} + 0. 2 7 5 3 \left(\sigma_ {v} ^ {2} / \sigma_ {u}\right) + 1. 1 0 8 \left(\sigma_ {v} ^ {3} / \sigma_ {u} ^ {2}\right). \tag {7.6b}$$

The value calculated for CEP is output to the IOBT; flags are reset so that further integration along the leg will continue at the 60-second rate.

12.3 Output Navigation Update Data: This submodule stores update data from calculations at the final map center of a map area into the IOBT. These data consist of position and heading at map center, error ellipse after update, error ellipse prior to update, time at map center (update time) covariance matrix, and time delay to finish update data correlation.

12.4 Output Probability of Overflight: This submodule calculates probability of overflight at each map center and outputs the value of crossstrack probability of overflight and of downtrack probability of overflight into the IOBT. This submodule also compares the calculated probability to the specified threshold probability allowed and sets an error flag if probability is too low.

12.5 Launch Footprint Computations: For the first map on a route, the launch footprint computations submodule is invoked to determine the area within which the missile may be launched and successfully navigate to the first waypoint and then to the first map such that the probability of overflight of that map meets with specified success criteria. This computation involves determining the shape of two curves centered on the first waypoint and two azimuth angles from the first waypoint defining a “keyhole.”

12.6 Output Error Messages: This submodule places error messages into IOBT records for transfer to the main error table described above.
