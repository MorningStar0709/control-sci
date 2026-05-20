# 10.2.5 Lie groups

While we avoided the topic in our explanation, pose is what’s known as a Lie group (a group that is also a differentiable manifold). There’s a lot of mathematical and controls results developed around Lie groups, so we’re mentioning the connection here in case you want to search the Internet for more information.

![](image/de811626e0dac81bc61b908bd4475dc45427c8e7e0c0921749388666ea4a251d.jpg)

<details>
<summary>line</summary>

| Time (s) | Forward Euler | Pose exponential |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.2 | 0.0 |
| 1.0 | 1.0 | 0.0 |
| 1.5 | 1.0 | 0.0 |
| 2.0 | 1.0 | 0.0 |
| 2.5 | 1.0 | 0.0 |
| 3.0 | 1.0 | 0.0 |
| 3.5 | 0.2 | 0.0 |
| 4.0 | 0.0 | 0.0 |
</details>

Figure 10.3: Pose estimation comparison (y error vs time)

![](image/fa7f467589b1fc6b92cde9c301f8d8c747017830bc6d0eed972ec2209f0e72ee.jpg)

<details>
<summary>line</summary>

| Time (s) | Forward Euler | Pose exponential |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.75 | 0.0 |
| 1.0 | -0.1 | 0.0 |
| 1.5 | 0.0 | 0.0 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 0.0 | 0.0 |
| 3.0 | 0.15 | 0.0 |
| 3.5 | -0.8 | 0.0 |
| 4.0 | -0.1 | 0.0 |
</details>

Figure 10.4: Pose estimation comparison (heading error vs time)
