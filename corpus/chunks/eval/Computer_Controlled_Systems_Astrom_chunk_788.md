# 13.4 The Principle of Least Squares

According to Gauss the principle of least squares is that the unknown parameters of a model should be chosen in such a way that

the sum of the squares of the differences between the actually observed and computed values multiplied by numbers that measure the degree of precision is a minimum.

![](image/7963094be511679c390f43a1b2497146aa8b213fc3fcbfdd6a3702804f686b2e.jpg)

<details>
<summary>text_image</summary>

y
ε
ŷ = θ₁x + θ₂
x
</details>

Figure 13.1 Illustration of the variables in the least-squares problem when estimating the parameters of a straight line.

To be able to give an analytic solution, the computed values must be linear functions of the unknown parameters. In the framework of the general formulation of the identification problem given in the previous sections, the class of models is such that the model output is linear in the parameters and the criterion is a quadratic function. The purpose of this section is to formulate the least-squares problem and to give its solution.
