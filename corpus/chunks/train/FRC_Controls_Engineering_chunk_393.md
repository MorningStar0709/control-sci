# Moment of inertia J

We’ll use empirical measurements of linear and angular velocity to determine J. First, we’ll derive the equation required to perform a linear regression using velocity test data.

$$\tau_ {1} = \mathbf {r} \times \mathbf {F}\tau_ {1} = r m a$$

where $\tau _ { 1 }$ is the torque applied by a drive motor during only linear acceleration, $r$ is the wheel radius, m is the robot mass, and a is the linear acceleration.

$$\tau_ {2} = I \alpha$$

where $\tau _ { 2 }$ is the torque applied by a drive motor during only angular acceleration, I is the moment of inertia (same as J), and α is the angular acceleration. If a constant voltage is applied during both the linear and angular acceleration tests, $\tau _ { 1 } = \tau _ { 2 }$ . Therefore,

$$r m a = I \alpha$$

Integrate with respect to time.

$$r m v + C _ {1} = I \omega + C _ {2}r m v = I \omega + C _ {3}v = \frac {I}{r m} \omega + C _ {3} \tag {12.37}$$

where $v$ is linear velocity and $\omega$ is angular velocity. $C _ { 1 } , C _ { 2 }$ , and $C _ { 3 }$ are arbitrary constants of integration that won’t be needed. The test procedure is as follows.

1. Run the drivetrain forward at a constant voltage. Record the linear velocity over time using encoders.   
2. Rotate the drivetrain around its center by applying the same voltage as the linear acceleration test with the motors driving in opposite directions. Record the angular velocity over time using a gyroscope.   
3. Perform a linear regression of linear velocity versus angular velocity. The slope of this line has the form $\frac { I } { r m }$ as per equation (12.37).   
4. Multiply the slope by rm to obtain a least squares estimate of I.

This page intentionally left blank
