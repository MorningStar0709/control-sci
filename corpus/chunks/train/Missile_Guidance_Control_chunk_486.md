The navigation/bomb steering algorithm is designed for both general navigation and for weapon delivery. However, the effective destination in the steering equation is modified according to the predicted crosstrack drift, CI (computed bomb drift, to be discussed later), of the impact prediction algorithm. We will now discuss the inclusion of the CI term into the steering during weapon delivery.

The direct mode is the primary mode for gravity weapon delivery and is entered upon the selection of bomb mode. Direct mode provides the shortest route to the target and the fastest elimination of the predicted impact errors. Centerline recovery mode steering is also available and provides weapon delivery along a specific path. Before proceeding to the minor modifications to the basic steering law for bomb steering, a simple explanation of the processing of the radar data will be given. The geometry is presented first, followed by simplified equations for processing the radar data into the steering.

Assume now that an offset aim point (OAP) is being used and the latitude and longitude of the OAP and the target are known. The basic assumption is that the relative latitude and longitude between the target and the OAP is not in error. Secondly, if the relative position is in error, there is no way to correct this during flight. The geometry of a typical situation before a tracking handle correction is shown in Figure 5.29.

Aircraft latitude and longitude are modified for use in bomb steering based on target position fix. This update is not applied to the prime data set values or the navigation filter. The N and E in the tracking handle buffer are converted to $\Delta \lambda$ and φ by

$$\Delta \lambda = (\Delta N / R _ {E}) (1 8 0 / \pi), \tag {5.63a}\Delta \phi = (\Delta E / R _ {E} \cos \lambda) (1 8 0 / \pi), \tag {5.63b}\lambda R _ {A / C} = \lambda_ {A / C} - \Delta \lambda , \tag {5.64a}\phi R _ {A / C} = \phi_ {A / C} - \Delta \phi , \tag {5.64b}$$

![](image/5bb61aadfd8e692764bff9b3c18916bd780e4fbec7cbff56d747846d124b1b1c.jpg)

<details>
<summary>text_image</summary>

N
+ΔEi
OAP
Target
+ΔNi
Radar cross hair location
Vg
A/C
+IP
IP = Initial point
A/C = Aircraft
</details>

Fig. 5.29. Geometry before tracking handle movement.

where
