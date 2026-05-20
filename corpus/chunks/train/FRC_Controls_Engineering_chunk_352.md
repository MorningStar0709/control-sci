# 11.5.1 Inverse kinematics

The mapping from v and ω to the left and right wheel velocities $v _ { l }$ and $v _ { r }$ is derived as follows. Let $\vec { v } _ { c }$ be the velocity vector of the center of rotation, $\vec { v } _ { l }$ be the velocity vector of the left wheel, $\vec { v _ { r } }$ be the velocity vector of the right wheel, $r _ { b }$ is the distance from the center of rotation to each wheel, and $\omega$ is the counterclockwise turning rate around the center of rotation.

Once we have the vector equation representing the wheel’s velocity, we’ll project it onto the wheel direction vector using the dot product.

First, we’ll derive $v _ { l }$ .

$$\vec {v} _ {l} = v _ {c} \hat {i} + \omega \hat {k} \times r _ {b} \hat {j}\vec {v} _ {l} = v _ {c} \hat {i} - \omega r _ {b} \hat {i}\vec {v} _ {l} = (v _ {c} - \omega r _ {b}) \hat {i}$$

Now, project this vector onto the left wheel, which is pointed in the $\hat { i }$ direction.

$$v _ {l} = (v _ {c} - \omega r _ {b}) \hat {i} \cdot \frac {\hat {i}}{\| \hat {i} \|}$$

The magnitude of $\hat { i }$ is 1, so the denominator cancels.

$$v _ {l} = (v _ {c} - \omega r _ {b}) \hat {i} \cdot \hat {i}v _ {l} = v _ {c} - \omega r _ {b} \tag {11.1}$$

Next, we’ll derive $v _ { r }$ .

$$\vec {v} _ {r} = v _ {c} \hat {i} + \omega \hat {k} \times r _ {b} \hat {j}\vec {v} _ {r} = v _ {c} \hat {i} + \omega r _ {b} \hat {i}\vec {v} _ {r} = (v _ {c} + \omega r _ {b}) \hat {i}$$

Now, project this vector onto the right wheel, which is pointed in the $\hat { i }$ direction.

$$v _ {r} = (v _ {c} + \omega r _ {b}) \hat {i} \cdot \frac {\hat {i}}{\| \hat {i} \|}$$

The magnitude of $\hat { i }$ is 1, so the denominator cancels.

$$v _ {r} = (v _ {c} + \omega r _ {b}) \hat {i} \cdot \hat {i}v _ {r} = v _ {c} + \omega r _ {b} \tag {11.2}$$

So the two inverse kinematic equations are as follows.

$$v _ {l} = v _ {c} - \omega r _ {b} \tag {11.3}v _ {r} = v _ {c} + \omega r _ {b} \tag {11.4}$$
