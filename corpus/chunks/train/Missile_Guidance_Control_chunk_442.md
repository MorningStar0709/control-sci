# 5.9 Covariance Analysis

An important tool in determining the target impact errors is the covariance analysis technique. Specifically, and as we have discussed in Section 4.8, a Kalman filter is often employed for estimating the position, velocity, and acceleration of a target. When the target motion and measurement models are linear and the measurement and motion modeling error processes are Gaussian, the Kalman filter provides the minimum mean-square error estimate of the target state. The dynamics model commonly assumed for a target in track is given by∗ [4]

$$X _ {k + 1} = F _ {k} X _ {k} + G _ {k} w _ {k}, \tag {5.32}$$

where $w _ { k } \sim N ( 0 , Q _ { k } )$ is the process noise and $F _ { k }$ defines a linear constraint on the dynamics. The target state vector $X _ { k }$ contains the position, velocity, and acceleration of the target at time k. The linear measurement model is given by

$$Y _ {k} = H _ {k} X _ {k} + n _ {k}, \tag {5.33}$$

where $Y _ { k }$ is normally the target position measurement with statistics $n _ { k } \sim N ( 0 , R _ { k } )$ . The Kalman filter equations associated with the dynamics model, (5.32), and the measurement model in (5.33) are given by the following equations [8]:

![](image/0d5628906cb4bed0752d600f4e62614137ce523c9732198f8045814ca0a65e73.jpg)

<details>
<summary>text_image</summary>

Z
Y
X
Bomb trajectory
Error ellipsoid at bomb release
Z
Propagated ellipsoid
Impact angle θi
Z'
Y, Y'
X
Ground plane
Normal plane
Error ellipse in the normal plane
Error ellipse in the ground plane
</details>

Fig. 5.23. The propagated error ellipsoid.

Time Update:

$$X _ {k \mid k - 1} = F _ {k - 1} X _ {k - 1 \mid k - 1} \tag {5.34}P _ {k \mid k - 1} = F _ {k - 1} P _ {k - 1 \mid k - 1} F _ {k - 1} ^ {T} + G _ {k - 1} Q _ {k - 1} G _ {k - 1} ^ {T} \tag {5.35}$$

Measurement Update:

$$K _ {k} = P _ {k \mid k - 1} H _ {k} ^ {T} [ H _ {k} P _ {k \mid k - 1} H _ {k} ^ {T} + R _ {k} ] ^ {- 1} \tag {5.36}X _ {k \mid k} = X _ {k \mid k - 1} + K _ {k} [ Y _ {k} - H _ {k} X _ {k \mid k - 1} ] \tag {5.37}P _ {k \mid k} = \left[ I - K _ {k} H _ {k} \right] P _ {k \mid k - 1} \tag {5.38}$$

where $X _ { o } \sim N ( \bar { X } _ { 0 } , P _ { 0 } )$ denotes the mean and error covariance of the state estimate, respectively.
