In weapon delivery, fixtaking of a specific target plays an important role. The primary fixtaking task is to calculate the range-to-target vector and associated display information. This vector is continuously computed in all modes, and in the air-to-ground weapon delivery modes (except EO) serves to define the location of the target. The range-to-target vector may be defined (1) by a latitude, longitude, and elevation, (2) as an offset from such, or (3) by the pilot visually designating the target. Fixtaking also converts radar-ranging measurements to a terrain elevation measurement when valid air-to-ground ranging data are available. The data are then used to correct the calculation of the vertical component of the range-to-target vector on a continuous (i.e., as long as data are valid) basis.

The most important fixtaking tasks are to calculate the range from present aircraft position to target and sighting point. Often, these calculations involve simple arithmetic operations on the proper data. Fixtaking employs a data table and uses pointers to select the proper set of data to be executed upon a set of “standard” equations. The vertical component of the range-to-target vector is the sum of the height above terrain, the vertical cursor associated with the basic range (which is zero unless the HUD target designator box is in the Earth curvature limit window), and the Earth’s curvature based on the horizontal components of the range-to-target vector. Note that the fundamental quantity involved in the calculation of the horizontal components of the range-to-target vector and range-to-sighting-point vector is the basic range. Finally, fixtaking computes the distance from the aircraft to the steerpoint using an

![](image/23da2030d29e668ecb8ed3b7be051a8b90dcf5823662f5d8978548ffb2eb9304.jpg)

<details>
<summary>text_image</summary>

MTT
θTT
MTT2
MGA
θF
MG
ψF
RR
RH
F0LC
F0
I
SG
Z
Y
X
TG
θT
Z
ψT
TOH
</details>

Fig. 5.35. Missile launch geometry.

Earth-fixed coordinate system. The key to these calculations is the determination of aircraft present position in this Earth-fixed coordinate system. This determination uses a nine-element direction cosine matrix, which relates the inertial platform to an Earth-fixed coordinate system [7].
