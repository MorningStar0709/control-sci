The ground signature used is terrain elevation, which is found by differencing the output of a pulsed radar altimeter and a barometric reference altitude maintained by the INS. This correlation processor is based on the mean absolute difference (MAD) processor discussed earlier in this chapter, with the means (i.e., mean values of altitude) removed from each profile. Using the MAD processor, a strip (i.e., profile) of measured ground elevations acquired along the vehicle’s flight path is correlated with each of the profiles within a reference map. The position of the minimum output of the MAD is the indicated fix position. However, it should be noted that the MAD indicated fix position is due to errors incurred during preparation of the reference map and measurement of the terrain profile. After the navigation system has been updated, position correction commands are sent to the flight control system, which flies the missile back into the intended course. Figure 7.22 illustrates that the planned course of the missile is down the center of the fix-taking area, and it is the planned course that the navigation system directs the missile along.

![](image/c2ba74412d8008b00430b74f30bb8791d96603e5bf14efee4f1f041e86f583c9.jpg)

<details>
<summary>text_image</summary>

Actual ground track
Planned ground track
Position error determined
Position error corrected
Position error
</details>

Fig. 7.22. Typical course correction after a position update.

However, with errors present in the navigation system, the actual ground track of the missile will be either to the left or right of the planned course. For simplicity, the vehicle’s downtrack position error will be ignored here. After the vehicle has flown over the fix-taking area and the TERCOM computations have been completed, the difference between the planned ground track and the actual position of the vehicle at the time the fix was made (i.e., at a map center), as determined by the correlation process, defines the downtrack and the crosstrack position errors, and these errors are sent to the navigation system for update. At the completion of navigation update, the position errors are corrected by sending course correction commands to the vehicle’s flight control system, which results in the vehicle flying back into the planned course.
