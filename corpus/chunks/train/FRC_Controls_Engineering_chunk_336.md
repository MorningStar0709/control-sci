# 10.2.3 What is a twist?

A 2D twist is an element of the tangent space of SE(2) (like the tangential distance traveled by the robot along an arc in SE(2)). We use the “pose exponential” to map a twist (an element of the tangent space) to an element of SE(2). In other words, we map a twist to a pose.

We call it a pose exponential because it’s an exponential map onto a pose. The term exponential is used because an exponential is the solution to integrating a differential equation whose derivative of a value is proportional to the value itself. For example, $\textstyle { \frac { d x } { d t } } = a x$ has the solution $x = x _ { 0 } e ^ { a t }$ .

We use the pose exponential to take encoder measurement deltas and gyro angle deltas (which are in the tangent space and are thus a twist) and turn them into a change in pose. This gets added to the pose from the last update.
