$\Delta t _ { A i }$ = atmospheric propagation delays and other errors (note: this delay is, converted into distance along the propagation path).

The other symbols have been defined above. The value of $c \Delta t _ { u }$ represents the range equivalent of the user clock error.

Because GPS position is referenced to a common grid, the World Geodetic System – 1984 (WGS-84), the civil and military position data can be standardized on a worldwide basis. The user equipment set (UE Set) is capable of converting WGS-84 to other commonly used data when operating with other map and data products. Therefore, the UE coordinates are commonly expressed in the WGS-84 frame. By reading the navigation message, the receiver can compute the coordinates of each satellite by means of the broadcast ephemeris data.

The WGS-84 ellipsoid reference frame in which all equations are written is defined in Table 7.2 (see also Appendix A) [8], [10]:

The following WGS-84 ellipsoid relations are useful:

$$b = a (1 - f),f = 1 - (b / a),e ^ {2} = 1 - (1 - f) ^ {2} = f (2 - f) \{\text {Also}: e = [ 1 - (b ^ {2} / a ^ {2}) ] ^ {1 / 2} \},R _ {N} = a / \left[ 1 - e ^ {2} \sin^ {2} \phi \right] ^ {1 / 2},X = \left(R _ {N} + h\right) \cos \phi \cos \lambda ,Y = \left(R _ {N} + h\right) \cos \phi \sin \lambda ,Z = \left[ R _ {N} \left(1 - e ^ {2}\right) + h \right] \sin \phi ,$$

where

$$R _ {N} = \text { radius curvature of the prime vertical },\phi = \text { latitude },\lambda = \text { longitude },h = \text { altitude }.$$

The origin of the WGS-84 coordinate system is at the center of mass of the Earth, with the (X, Y, Z) axes defined as follows:

X-axis: Intersection of the WGS-84 reference meridian plane and the plane of the equator, corresponding to the average terrestrial pole of 1900–1905. The WGS-84 meridian is 0.554” east of the zero meridian (near Greenwich).

Y -axis: Measured in the plane of the equator and 90◦ east of the X-axis.

Z-axis: Parallel to the direction of the conventional international origin, that is, coincident with the Earth’s mean rotation axis 1900-1905.
