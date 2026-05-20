$$A _ {o} (q) v (t) = T (q) u _ {c} (t) - S (q) y (t) + \left(A _ {o} (q) - R (q)\right) u (t) \tag {11.1}u (t) = f (v (t))$$

A similar scheme can be used when the saturation is dynamic. Notice that the controller responds with the observer dynamics when the feedback is broken. A particularly simple case is when $A_{o}^{*} = 1$ , which corresponds to a deadbeat

![](image/56fb245bf9987d1724d1f09598f1fa642b11368b8b936fcc4b9ea220848a6f88.jpg)  
Figure 11.4 Simulation of adaptive control of the unstable process with a saturating actuator in Example 11.2.

observer. The controller is then

$$u (t) = f \left(T ^ {*} \left(q ^ {- 1}\right) u _ {c} (t) - S ^ {*} \left(q ^ {- 1}\right) y (t) + \left(1 - R ^ {*} \left(q ^ {- 1}\right)\right) u (t)\right)$$

We illustrate windup by an example.
