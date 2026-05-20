(1) Perform Kalman filter update of error covariance matrix at final map center of a voting group.   
(2) Compute the time until navigation update.   
(3) Compute the time delay $t _ { g }$ between update time and time of completion of correction maneuvers.   
(4) Evaluate next waypoint or target for comparison with $t _ { g }$ and set the error message flag if map group too close.

In performing the above functions, the NAM system must satisfy the following accuracy and validity requirements:

(1) Within 95% confidence, the probability to successfully overfly a specified map area associated with the route of flight. The probability calculated shall be within ±2% of the actual probability.

![](image/fcc93a52dc0c749da5f8ec9898d41a31b3e50836f8a673c5002b22b90b761b2b.jpg)

<details>
<summary>text_image</summary>

Planned ALCM route
±3σ corridor 3σ error ellipse
Nav guidance system update
Terrain correlation map
</details>

Fig. 7.5. Error ellipses.

(2) Within 90% confidence, the navigation error ellipse description at specified points along the route of flight. Ellipse dimensions shall be within ±10% of actual errors or 100 ft, whichever is greater (excluding launch platform error contribution).   
(3) Within 90% confidence, the CEP at specified points along the route within ±10% of the actual CEP value at the terminal point.   
(4) Within 95% confidence, the launch footprint such that the probability of successful overflight of any TC map satisfies the requirements of (1) above.

In addition to the above requirements, NAM must (a) estimate map overflight probability, (b) estimate position accuracy at the target, and (c) calculate the flight corridor widths and enroute position error ellipses. Figure 7.5 illustrates the concept of the error ellipses.
