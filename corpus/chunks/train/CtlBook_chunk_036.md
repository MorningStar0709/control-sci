# 1.5.1 Overview

Laplace Transforms can only be used on linear equations. In most of this course we focus on linear dierential equations but often real world applications involve non-linear functions. All is not lost if we can usefully approximate our non-linear function with a linear one. Our approach to linearization is to model the original function with a straight line.

Consider a nonlinear function, f(x). The linearized version of $f ( x ) , { \hat { f } } ( x )$ , can be constructed about a

![](image/3c680cf1ab92d8e8468b286d43e2c149b5a3c9490e5452ad3d5910c1ec31e56f.jpg)

<details>
<summary>text_image</summary>

f(x)
f(x₀)
df(x₀)/dx
"neighborhood"
x₀
x
</details>

Figure 1.2: Illustration of a linearized version of a non-linear function at an operating point.

specic operating point, $x _ { 0 } .$

$$\hat {f} (x) = f \left(x _ {0}\right) + \frac {d}{d x} f \left(x _ {0}\right) \left(x - x _ {0}\right)$$

${ \hat { f } } ( x )$ is a linear function of $x$ which is most accurate in the neighborhood of $x _ { 0 } .$ . It is also the rst two terms of a Taylor series expansion of $f ( x )$ . It is very helpful to visualize this process graphically by plotting the linearized function on top of the original function (Figure 1.2).
