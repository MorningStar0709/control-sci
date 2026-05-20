# 7.4.3 The Terrain-Contour Matching (TERCOM) Concept

As stated in the introduction of Section 7.4.1, the TERCOM system uses an airborne altimeter and a data processor to correlate the measured terrain contours to obtain the best estimate of position. The transmission characteristics of the airborne altimeter include an operating frequency of approximately 4.4 GHz (incidental to operation) and a transmission type that is pulsed or CW. As the missile flies, the radar altimeter first measures the variations in the ground’s profile. These measured variations are then digitized and processed for input to a correlator for comparison with the stored data. The TERCOM system relies on a set of digital maps stored in the memory of the missile’s onboard computer. These maps consist of rectangular arrays of numbered squares representing the variation of ground elevation above sea level as a function of location. Consequently, as the missile approaches an area for which the computer memory has a map, the onboard radar altimeter starts providing a stream of groundelevation data. Furthermore, the computer, by comparing these data with the information it has in its memory, can accurately determine the actual trajectory of the missile and instruct the autopilot to return the missile to its planned trajectory. Four such corrective maneuvers are shown in the vertical overhead view in Figure 7.10.

From Figure 7.10, we note that there are four types of TERCOM maps that can be used by a cruise missile. Assuming that a cruise missile is deployed over water, these maps are as follows (1-largest, 4-smallest):

(1) landfall,   
(2) en route,   
(3) midcourse, and   
(4) terminal.

The map types differ in length, width, and cell size. The map width determines how far that map can be spaced from either the launch site or a previous TERCOM map and still yield an acceptably high probability of overflight. The cell size determines, in part, the accuracy of the TERCOM fix. The TERCOM maps become smaller and are spaced closer together as the missile approaches the target. As a result, because of the decreasing cell size, the updates become more accurate. A terminal accuracy on the order of 100 meters is considered feasible for the TERCOM system.
