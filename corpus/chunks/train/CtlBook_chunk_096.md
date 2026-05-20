# 3.4.2 Simplication of Geared Systems

We can use the properties of gear transmission of rotation and torque to simplify the process of writing EOM.

Consider a damper driven by a set of gears (Figure 3.3)

We have

$$\tau_ {2} = B \dot {\theta_ {2}}$$

![](image/1a77ea3408598d4d561c04fe39ec3ca64ec221ad7a595e1ca6064c9ce4c13183.jpg)

<details>
<summary>text_image</summary>

τ₁,θ₁
N₁
I
J
N₂
</details>

Figure 3.4: A mass, spring, and damper driven by a set of gears.

Using the relationships above we have

$$\frac {1}{n} \tau_ {1} = B n \dot {\theta} _ {1}$$

or

$$\tau_ {1} = B n ^ {2} \dot {\theta} _ {1}$$

Suppose the system beyond the gears had some mass and spring in addition to the damper of Figure 3.3 as shown in Figure 3.4. The argument above would be very similar:

We have

$$\tau_ {2} = J \ddot {\theta} _ {2} + B \dot {\theta} _ {2} + K \theta_ {2}$$

Using the relationships above we have

$$\frac {1}{n} \tau_ {1} = J n \ddot {\theta} _ {1} + B n \dot {\theta} _ {1} + K n \theta_ {1}$$

or

$$\tau_ {1} = J n ^ {2} \ddot {\theta} _ {1} + B n ^ {2} \dot {\theta} _ {1} + K n ^ {2} \theta_ {1}$$

Let

$$\hat {J} = n ^ {2} J \qquad \hat {B} = n ^ {2} B \qquad \hat {K} = n ^ {2} K$$

The EOM becomes

$$\tau_ {1} = \hat {J} \ddot {\theta} _ {1} + \hat {B} \dot {\theta} _ {1} + \hat {K} \theta_ {1}$$

This is the EOM of a simpler system (Figure 3.5).

![](image/7fbebee5a7de3af0276b2ecf8bf96db6bf4f1ff476e6bb97322e32dfeac55693.jpg)

<details>
<summary>text_image</summary>

J
K
B
r₁,θ₁
</details>

Figure 3.5: Simplied equivalent system of a system modied from Figure 3.3
