where d $P / d t$ is the roll acceleration, $d Q / d t$ is the pitch acceleration, and $d R / d t$ is the yaw acceleration. The set of equations (2.27a)–(2.27c) and (2.44d)–(2.44f) or $( 2 . 4 4 \mathrm { a } ) - ( 2 . 4 4 \mathrm { c } )$ represents the complete 6-DOF missile equations of motion. Specifically, equations (2.27) describe the translation, and equations (2.44) describe the rotation of a body. The set of equations (2.27) and (2.44) are six simultaneous nonlinear equations of motion, with six variables u, v, w, P , Q, and R, which completely describe the behavior of a rigid body. Moreover, these equations can be solved with a digital computer using numerical integration techniques. An analytical solution of sufficient accuracy can be obtained by linearizing these equations. These equations are also known as Euler’s equations. Note that $I _ { x } , I _ { y } , I _ { x z }$ are constant for a given rigid body because of our choice of coordinate axes. Due to the usual symmetry of the aircraft (or missile) about the $x - y$ plane, the products of inertia that involve y are usually omitted, and the moment equations may be rewritten as follows (note that for cruciform missiles with rotational symmetry, $I _ { y } = I _ { z }$ and $I _ { x z } = 0 )$ :

$$\Delta L = \dot {P} I _ {x} + Q R (I _ {z} - I _ {y}), \tag {2.45a}\Delta M = \dot {Q} I _ {y} + (I _ {x} - I _ {z}) P R, \tag {2.45b}\Delta N = \dot {R} I _ {z} + (I _ {y} - I _ {x}) P Q. \tag {2.45c}$$

It should be noted that the L and N equations indicate that a rolling or yawing moment excites angular velocities about all three axes. Therefore, except for certain cases, these equations cannot be decoupled. Solving (2.45a)–(2.45c) for d $P / d t , d Q / d t$ , and $d R / d t$ , we obtain the rotation accelerations as follows:

![](image/4d02a9f4e29106d3607e4cef749125f588b78cf54efab6e3bd3e1cc711dea988.jpg)

<details>
<summary>flowchart</summary>
