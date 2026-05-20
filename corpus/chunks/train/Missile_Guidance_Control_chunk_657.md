The model is set up to perform most of the calculations in the ECI coordinate frame. This frame’s origin is at the Earth’s center, with the positive X-axis aligned with zero degrees longitude, the positive Y -axis aligned with 90◦ longitude, and the positive Z-axis aligned with 90◦ north latitude (or vertical). The ECI frame accounts for the velocity induced by the rotation of the Earth.

(b) East-North-Up Coordinate Frame

Calculations of missile azimuth, pitch, and flight-path angle are usually calculated in the east-north-up frame. The origin of this frame is centered at the missile’s current ground track position defined by a latitude and longitude on the Earth’s surface. Here, the positive X-axis points to the east, the positive Y -axis points north, and the positive Z-axis points along the local vertical. The X- and Y -axes define the local ENU ground plane. The missile orientation is calculated relative to this point. Note that in our model we will assume that the Earth’s rotation rate has been set to zero.

(c) Missile Body-Axis Coordinate Frame

Calculations of forces acting on the missile are calculated in the body-axis coordinate frame. This frame is centered at the missile’s center of gravity (cg). The positive X-axis aligns with the missile’s longitudinal body-axis pointing out the nose of the missile, the positive Y -axis points in the direction perpendicular to the longitudinal body-axis and parallel to the local ENU ground plane, and the Z-axis points in the direction perpendicular to the X- and Y -axes such that a right-hand coordinate system is defined.

The rotation from the missile body-axis frame to the ECI coordinate frame will be described below. However, prior to rotation, the following quantities must be calculated for the current integration step:

$$\mathbf {R} = \text { missile position vector in } E C I \text { coordinates },\mathbf {V} = \text { missile velocity vector in } E C I \text { coordinates },\mathbf {1} _ {X} = \text { unit missile velocity vector in } E C I \text { coordinates },\mathbf {1} _ {Y} = \text { unit cross product of velocity and position vectors },= (\mathbf {V} \times \mathbf {R}) / (| \mathbf {V} \times \mathbf {R} |)\mathbf {1} _ {Z} = \text { cross product of } \mathbf {1} _ {X} \text { and } \mathbf {1} _ {Y} \text { vectors } = \mathbf {1} _ {X} \times \mathbf {1} _ {Y}.$$

The body-axis to ECI transformation matrix $T _ { b }$ is then defined as
