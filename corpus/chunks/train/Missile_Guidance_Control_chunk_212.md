# 3.6 English Bias

In order to compensate any aircraft steering error (i.e., a missile aiming error) that exists at launch, an English bias (or lead angle error) signal is provided that will command the missile to turn after launch. The fundamental idea of this command is to provide the means of correcting missile heading error prior to lock-on to the target and thereby minimize the time required after speedgate∗ lock to solve the guidance problem and effect a satisfactory intercept. At launch, the computer supplies the interceptor missile with English bias commands, which simply are voltage analogues of the gimbal angles the missile should have in order to be on a collision course with the target. Each of these signals is compared correspondingly with its existing antenna gimbal angle during the boost phase to produce error signals, which in turn are used to direct the missile body axis to a collision course orientation.

![](image/866f2ddbab8f72a8187b9df2a43eacf51ad77385ebf66565b4eaa07df724f437.jpg)

<details>
<summary>text_image</summary>

Target
Impact
Head aim angle θ_H
English bias steers missile towards predicted collision point prior to speedgate lock
Lead angle error (LAE)
English bias command enabled after missile has cleared the aircraft at 0.6 sec after launch
</details>

Fig. 3.44. Effect of English bias commands.

More specifically, English bias commands guide the missile to the proper course as computed by the launching aircraft computer as shown in Figure 3.44. If the missile is to be launched at other than the desired lead angle, in-flight course correction commands, that is, English bias, are applied to the pitch/yaw autopilot. English bias has the ability to correct up to $2 5 ^ { \circ }$ of lead angle error. For example, upon missile speedgate lock on target video, $t _ { g o } ^ { * * } = \mathrm { L o c k } + 0 . 5 \mathrm { s } , \mathrm { p r e } \cdot t _ { g o } = \mathrm { L a u n c h } + 3 \mathrm { s }$ , English bias is switched out and axial compensation and homing guidance commands derived from target video are applied to the pitch/yaw autopilot $( \mathrm { t } _ { g o }$ is the time remaining before intercepting the target).
