Note that a terrain-following (TF) algorithm must be designed in order to optimize the use of the vehicle acceleration in following a flight path that matches the terrain contours. The system bases its altitude reference information on a down-looking radar altimeter. This information is processed by a digital filter in the computer to reduce the effect of noise and to derive clearance altitude rate. The navigation system provides the reference altitude for the system, which is a combination of inertial (i.e., vertical accelerometer) and barometric altitudes. This reference altitude is measured with respect to the mean sea level (MSL), and is also averaged over the cell distance. The measured terrain elevation is computed by subtracting the measured radar altitude from the reference altitude. If necessary, the measured terrain elevation value is then scaled and manipulated to get it into the same format as the reference matrix data. The resulting value is stored in the terrain elevation file for later correlation with the reference matrix. This process is repeated for each cell along the vehicle’s ground track while flying over the reference matrix area.

![](image/3f57adc9d5fb55996f372917daf4bcf7048d29e2ea02d3210a34b1ee53dd2262.jpg)

<details>
<summary>text_image</summary>

Reference altitude
Radar altitude
Radar altimeter
Actual elevation
Measured elevation
Mean sea level
d
</details>

Fig. 7.14. Terrain elevation measurement.

As discussed earlier, the TERCOM system yields a fix by comparison of a set of acquired data, in the form of a sequence of terrain elevation measurements, with a set of stored data in the form of a matrix of reference terrain elevations. Thus, consider Figure 7.15. The circles represent points at which the terrain altitude referred to the local mean value is determined from the contour maps or stereo-photographs.
