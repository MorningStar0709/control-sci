# 11.7.1 Inverse kinematics

$$
\begin{array}{l} \vec {v} _ {w h e e l 1} = \vec {v} _ {r o b o t} + \vec {\omega} _ {r o b o t} \times \vec {r} _ {r o b o t 2 w h e e l 1} \\ \vec {v} _ {w h e e l 2} = \vec {v} _ {r o b o t} + \vec {\omega} _ {r o b o t} \times \vec {r} _ {r o b o t 2 w h e e l 2} \\ \vec {v} _ {\text {wheel3}} = \vec {v} _ {\text {robot}} + \vec {\omega} _ {\text {robot}} \times \vec {r} _ {\text {robot2wheel3}} \\ \vec {v} _ {\text {wheel4}} = \vec {v} _ {\text {robot}} + \vec {\omega} _ {\text {robot}} \times \vec {r} _ {\text {robot2wheel4}} \\ \end{array}
$$

where $\vec { v } _ { w h e e l }$ is the wheel velocity vector, $\vec { v } _ { r o b o t }$ is the robot velocity vector, $\vec { \omega } _ { r o b o t }$ is the robot angular velocity vector, $\vec { r } _ { r o b o t 2 w h e e l }$ is the displacement vector from the robot’s center of rotation to the wheel,[1] $\vec { v } _ { r o b o t } = v _ { x } \hat { \dot { i } } + v _ { y } \hat { \dot { j } }$ , and ${ \vec { r } } _ { r o b o t 2 w h e e l } =$ $r _ { x } \hat { i } + r _ { y } \hat { j }$ . The number suffixes denote a specific wheel in figure 11.4.

![](image/659591c5b5ce352e828d88817d366861f1654274be50b66f90a8ddc770a18f37.jpg)

<details>
<summary>text_image</summary>

v₁
v₂
v₃
v₄
+ x
+y
</details>

Figure 11.4: Swerve drive free body diagram
