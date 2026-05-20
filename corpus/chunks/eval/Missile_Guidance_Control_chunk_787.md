GPS position accuracy is dependent on the precision with which the range to the satellite being tracked can be measured and the geometry of those specific satellites with respect to the user. A number of factors contribute to range error measurement, such as atmospheric effects, satellite signal integrity, and receiver design. In addition, position accuracy is also determined by the code (P or C/A) being used for navigation. Satellite geometry for any given user is mainly determined by the number of operational satellites in orbit, the placement of those satellites, and to a lesser extent the location of the user. The GPS has been defined and specified for accuracy in navigation and positioning based upon operation in the stand-alone mode. This stand-alone performance is remarkable, considering all the variables involved. There are users, however, that have a requirement for greater real-time accuracy.

The position, velocity, and time accuracy capabilities of the GPS set can now be detailed in view of correlated factors such as the response times, vehicle dynamics, and hostile threats. The accuracy values delineated herein are averaged over all points on the Earth and at all times, and are based upon the following assumptions:

(a) The UE set is operating in the nominal receiver operational state and navigation mode.

(b) Graceful degradation of navigational accuracy will result with fewer than 21 satellites operating properly.

The GPS UE set calculated position, velocity, and time accuracies quoted in the open literature are as follows:

• Position (3-dimensional, derived from the P code): 16 meters SEP (spherical error probable).   
• Position (2-dimensional, derived from the P code): 8 meters CEP (circular error probable).   
• Velocity (3-dimensional): ≥ 0.1 m/sec rms (root mean square), any axis.   
• Time: 0.1 µsec (1σ ).   
• Position (2-dimensional, for civil users): 40 meters (CEP).

As discussed above, the accuracy of a navigation fix depends primarily on the geometry of the four satellites in view, which is characterized by the geometric dilution of precision (GDOP). The smaller the GDOP, the more accurate the navigation fix will be. Mathematically, the GDOP is expressed as [1], [7], [8]

$$G D O P = [ t r (G ^ {T} G) ^ {- 1} ] ^ {1 / 2}, \tag {7.22}$$

where G is a matrix and tr denotes the trace of the matrix. The matrix G is given by
