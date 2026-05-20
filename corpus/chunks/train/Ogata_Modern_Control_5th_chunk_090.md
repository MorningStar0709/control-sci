To derive the equations of motion for the system, consider the free-body diagram shown in Figure 3–5(b). The rotational motion of the pendulum rod about its center of gravity can be described by

$$I \ddot {\theta} = V l \sin \theta - H l \cos \theta \tag {3-9}$$

where I is the moment of inertia of the rod about its center of gravity.

The horizontal motion of center of gravity of pendulum rod is given by

$$m \frac {d ^ {2}}{d t ^ {2}} (x + l \sin \theta) = H \tag {3-10}$$

The vertical motion of center of gravity of pendulum rod is

$$m \frac {d ^ {2}}{d t ^ {2}} (l \cos \theta) = V - m g \tag {3-11}$$

The horizontal motion of cart is described by

$$M \frac {d ^ {2} x}{d t ^ {2}} = u - H \tag {3-12}$$

Since we must keep the inverted pendulum vertical, we can assume that# $\theta ( t )$ and $\dot { \theta } ( t )$ are small quantities such that sin $\theta \doteq \theta , \cos \theta = 1$ , and $\theta { \dot { \theta } } ^ { 2 } = 0$ Then, Equations (3–9) through (3–11). can be linearized. The linearized equations are

$$I \ddot {\theta} = V l \theta - H l \tag {3-13}m (\ddot {x} + l \ddot {\theta}) = H \tag {3-14}0 = V - m g \tag {3-15}$$

From Equations (3–12) and (3–14), we obtain

$$(M + m) \ddot {x} + m l \ddot {\theta} = u \tag {3-16}$$

From Equations (3–13), (3–14), and (3–15), we have

$$I \ddot {\theta} = m g l \theta - H l= m g l \theta - l (m \ddot {x} + m l \ddot {\theta})$$

or

$$(I + m l ^ {2}) \ddot {\theta} + m l \ddot {x} = m g l \theta \tag {3-17}$$

Equations (3–16) and (3–17) describe the motion of the inverted-pendulum-on-the-cart system. They constitute a mathematical model of the system.
