# 6.5.2 Location of Disturbance

Disturbances can enter the control loop at dierent locations besides summing with the output. First consider the disturbance injected into the error computation (e.g, a noisy sensor, Figure 6.7).

$$Y = G E = G (X + D - Y H)Y (1 + G H) = G X + G DY = \frac {G}{1 + G H} X + \frac {G}{1 + G H} D = \frac {G}{1 + G H} (X + D)$$

In this case the disturbance and the input are treated exactly the same. There is no disturbance rejection at all. In retrospect this makes sense since it would be impossible for the controller to distinguish between the disturbance and the desired input.

Now we consider a case in which $^ { 6 6 } G ^ { 9 }$ is split into two systems and the disturbance is injected between the two (Figure 6.8). As mentioned above, this is an important case where $G$ consists of a controller coupled to a plant such as an industrial machine or a vehicle.

This time we have

$$Y = G _ {2} (D + G _ {1} E)= G _ {2} \left(D + G _ {1} (X - Y H)\right)Y = G _ {2} D + G _ {1} G _ {2} X - Y G _ {1} G _ {2} HY (1 + G _ {1} G _ {2} H) = G _ {2} D + G _ {1} G _ {2} XY = \frac {G _ {2} D}{1 + G _ {1} G _ {2} H} + \frac {G _ {1} G _ {2} X}{1 + G _ {1} G _ {2} H}$$

Considering the case of a large loop gain, $G _ { 1 } G _ { 2 } H > > 1$ , we have the situation where the disturbance is reduced by $G _ { 1 } H ,$ , which could be more or less disturbance rejection than reduction by $G _ { 1 } G _ { 2 } H$ depending on the magnitudes of $G _ { 1 }$ and $G _ { 2 }$ .
