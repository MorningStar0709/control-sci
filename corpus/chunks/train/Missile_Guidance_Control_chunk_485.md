The system must provide the capability for a smooth transition from one course to another and to fly directly over a destination. The smooth transition from one course to another is called “turn short,” and the ability to fly directly over a destination is called overfly. Turn short is accomplished in minimum time. For gravity weapons release, the impact point cross-range miss distance is used to generate steering commands to the bomb release point. The bomb steering mode will be flagged via system management control. Bomb steering is accomplished by using the basic navigation steering. Overfly is automatically set when the bomb mode is initiated. The navigation steering mode used for bomb steering corresponds to the mode selected for navigation steering. If operating in the direct mode with overfly, the system automatically switches to centerline recovery when the range to go becomes less than a given value (e.g., 6,000 feet) in either navigation or bomb steering. The inputs to navigation steering include:

a. Prime data set from either the INS or alternative navigation.   
b. Steer point and tracking data from system management control.   
c. Computed gravity weapon crossrange drift from weapon delivery.   
d. Mode control flags from system management and control logic.

The prime data set inputs include the aircraft latitude, longitude, inertial coordinates, ground speed, and course, as well as the Earth radius and prime data validity. Steer point data include latitudes and longitudes of previous, current, and next destinations. The tracking data are crosshair corrections. The navigation steering outputs are:

a. Range-to-go to current destination.   
b. Range from current destination to next destination   
c. Time-to-go to current destination (or turn point in turn short).   
d. Estimated time from current destination to the next destination.   
e. Track angle error.   
f. Crosstrack error.   
g. Steering command to the automatic FCS.   
h. Flag for time to sequence between current and next destination.   
i. Ground track angle between current and next destination.

If there is insufficient data for steering outputs:

1. Set a flag for insufficient data. This flag is to be used by system management control.   
2. Set all steering outputs to zero.
