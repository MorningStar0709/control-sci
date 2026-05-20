# 7.8.2 Unmodeled dynamics

In addition to plant inversion, one can include feedforwards for unmodeled dynamics. Consider an elevator model which doesn’t include gravity. A constant voltage offset can be used compensate for this. The feedforward takes the form of a voltage constant because voltage is proportional to force applied, and the force is acting in only one direction at all times.

![](image/107a8498db49cf1b277090797c60e240f96afd5f0ff25ea81bd2689f7fcce7ab.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference (rad/s) | No feedforward (rad/s) | Plant inversion (rad/s) | Reference (A) | No feedforward (A) | Plant inversion (A) | Reference (V) | No feedforward (V) | Plant inversion (V) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 200 | 200 | 200 | 0 | 0 | 100 | 15 | 15 | 15 |
| 0.005 | 200 | 200 | 200 | 0 | 0 | 90 | 15 | 15 | 15 |
| 0.010 | 200 | 200 | 200 | 0 | 0 | 0 | 5 | 5 | 5 |
| 0.015 | 200 | 200 | 200 | 0 | 0 | 0 | 5 | 5 | 5 |
| 0.020 | 200 | 200 | 200 | 0 | 0 | 0 | 5 | 5 | 5 |
| 0.025 | 200 | 200 | 200 | 0 | 0 | 0 | 5 | 5 | 5 |
</details>

Figure 7.11: Second-order CIM motor response with plant inversion

$$u _ {k} = V _ {\text { app }} \tag {7.17}$$

where $V _ { a p p }$ is a constant. Another feedforward holds a single-jointed arm steady in the presence of gravity. It has the following form.

$$u _ {k} = V _ {\text { app }} \cos \theta \tag {7.18}$$

where $V _ { a p p }$ is the voltage required to keep the single-jointed arm level with the ground, and θ is the angle of the arm relative to the ground. Therefore, the force applied is greatest when the arm is parallel with the ground and zero when the arm is perpendicular to the ground (at that point, the joint supports all the weight).

Note that the elevator model could be augmented easily enough to include gravity and still be linear, but this wouldn’t work for the single-jointed arm since a trigonometric function is required to model the gravitational force in the arm’s rotating reference frame.[10]
