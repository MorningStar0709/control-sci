# Stiffness Elements

When a mechanical element stores energy due to a deformation or change in shape, it can be modeled as a stiffness element. In such cases, a fundamental relationship between force and the resulting deformation is required to model stiffness. The simplest force–deformation relationship is Hooke’s law, which states that the force required to stretch or compress a spring is proportional to the displacement. Figure 2.1 shows a spring that is fixed at its left end, but free at the right end. Suppose a tensile force F is applied at the right (free) end and x is the corresponding displacement of the free end from its equilibrium (unstretched) position. The force required to produce displacement x is

$$F = k x \tag {2.6}$$

where k is called the spring constant and has units of N/m. Clearly, Eq. (2.6) is a linear relationship between force and displacement. Figure 2.1 shows that the positive convention for displacement x is to the right and, therefore, the positive convention for force F is also to the right. If force F is compressive, then both F and x are negative and Eq. (2.6) is still valid.

![](image/5c4a192dd3b58b50f9da32a0857de5ad1ed53fbadec036b664c0b8a7adc932c6.jpg)

<details>
<summary>text_image</summary>

k
x
F
</details>

Figure 2.1 Force stretching the free end of a spring.

![](image/895c78a635a5e2068d51c66b93ea257f3d53bdebc6337d572def81951ba166ee.jpg)

<details>
<summary>text_image</summary>

x₁
F
k
x₂
F
</details>

Figure 2.2 Force deflecting the free ends of a spring.

When both ends of a spring are free to move, then the force required to stretch or compress a spring depends on the relative displacement

$$F = k (x _ {2} - x _ {1}) \tag {2.7}$$
