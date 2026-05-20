# 7.2.2 Missile Navigation System Description

In Section 7.2 we discussed briefly the role of the inertial navigation system. A general description of the navigation system, which is part of the NAM (navigation accuracy module), objectives, approach, performance requirements, and input/output requirements will be discussed in this section. The navigation accuracy module is an integral part of the mission planning system (MPS). The MPS is an interactive computer system that is used to develop cruise missile routes. More specifically, the MPS consists of the development of a route that satisfies the cruise missile’s constraints and the generation of the commands and data to be loaded into the onboard computer. The objectives of the MPS are:

(1) Navigation maps located to provide high probability of acquisition,   
(2) Guidance and control commands achievable by the cruise missile,   
(3) Achievable range, and   
(4) Low probability of clobber.

Furthermore, the navigation system is designed as a self-contained, stand-alone, primary software system element for the cruise missile MPS that will predict mission downtrack and crosstrack errors for any action point in support of routing function to develop acceptable cruise missile route definitions. The navigation system makes use of a covariance analysis approach for generating mission navigation data to the specified accuracy and confidence levels and within computer limitations. This approach requires selecting suitable system matrices that determine the error propagation of the cruise missile navigation system between position updates. Using route definition data stored in tables established by the calling program, the navigation system produces navigation data for new mission or partial rerun of mission by performing a navigation covariance analysis time simulation and updates the tables with the processed navigation data. An example of a flight route is shown in Figure 7.4.

![](image/3e2875702cbba257a0aff919a671e7bf5dab6abad825959e97b143c70a2195fc.jpg)

<details>
<summary>flowchart</summary>
