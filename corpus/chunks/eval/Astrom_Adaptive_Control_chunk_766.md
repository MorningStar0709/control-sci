The system uses a roll rate sensor together with course gyro and speed log to determine rudder commands that are superimposed on the ordinary autopilot commands and fed into the steering engine. The operating principle is that the roll movements created by the rudder are opposite those of the roll movements caused by the waves. These counteractive moves damp the roll motions of the ship. In designing the roll damping system it is important to have quick rudder motions. Slow and large motions will influence the course keeping. The Roll-Nix system is provided with an autopilot as an option. The adaptive feature of the roll damping system is necessary to handle different weather conditions and ship speed. The Kalman filter is used to obtain an accurate roll motion signal from the measured roll rate.

![](image/fe20e42a3747ae9875a21b839081db3258b3369bd93a78b81eada6656f5d8e3d.jpg)

<details>
<summary>line</summary>

| Time (s) | Value |
| --- | --- |
| 0 | ~5 |
| 50 | ~10 |
| 100 | ~5 |
| 150 | ~10 |
| 200 | ~5 |
| 250 | ~-15 |
| 300 | ~5 |
</details>

![](image/3b466793e5c32586131aaefafd21dafa922b80253f9680db72b6d3a475d6770d.jpg)

<details>
<summary>line</summary>

| Time (s) | Value |
| --- | --- |
| 0 | ~5 |
| 100 | ~10 |
| 200 | ~5 |
| 300 | ~5 |
</details>

Figure 12.16 Results from sea trials with an attack craft at 27 knots and stern quartering seas (4 Beaufort): (a) without Roll-Nix; (b) with Roll-Nix. The significant roll angle was reduced by 58%, and the maximum roll angle was reduced by 53%. (With courtesy of SSPA Maritime Consulting AB.)

Roll-Nix has been tested on several types of ships. For instance, the system has been tested on two Royal Swedish Navy ships: one attack craft and one mine layer. The sea trials show that a significant roll reduction of 45–60% can be obtained for both the standard deviation and the maximum angle of the roll. The result from a sea trial with an attack craft is shown in Fig. 12.16. The roll reduction increases with increasing speed and rudder rates. Tests were also done on the mine layer HMS Carlskrona in September 1987. The following quote from the captain, Commander Hallin, gives an illustration of the performance of the system.
