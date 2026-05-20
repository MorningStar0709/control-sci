The linearization procedure to be presented in the following is based on the expansion of nonlinear function into a Taylor series about the operating point and the retention of only the linear term. Because we neglect higher-order terms of the Taylor series expansion, these neglected terms must be small enough; that is, the variables deviate only slightly from the operating condition. (Otherwise, the result will be inaccurate.)

Linear Approximation of Nonlinear Mathematical Models. To obtain a linear mathematical model for a nonlinear system, we assume that the variables deviate only slightly from some operating condition. Consider a system whose input is x(t) and output is y(t). The relationship between y(t) and x(t) is given by

$$y = f (x) \tag {2-42}$$

If the normal operating condition corresponds to then Equation (2–42) may bex–, y–, expanded into a Taylor series about this point as follows:

$$
\begin{array}{l} y = f (x) \\ = f (\bar {x}) + \frac {d f}{d x} (x - \bar {x}) + \frac {1}{2 !} \frac {d ^ {2} f}{d x ^ {2}} (x - \bar {x}) ^ {2} + \dots \tag {2-43} \\ \end{array}
$$

where the derivatives dfdx, $d ^ { 2 } f / d x ^ { 2 } , \ldots$ are evaluated at $x = \bar { x }$ If the variation. $x \ : - \ : \bar { x }$ is small, we may neglect the higher-order terms in $x \ - \ { \bar { x } } .$ Then Equation (2–43) may be. written as

$$y = \bar {y} + K (x - \bar {x}) \tag {2-44}$$

where

$$\bar {y} = f (\bar {x})K = \frac {d f}{d x} \Bigg | _ {x = \bar {x}}$$

Equation (2–44) may be rewritten as

$$y - \bar {y} = K (x - \bar {x}) \tag {2-45}$$

which indicates that $y \mathrm { ~ - ~ } \bar { y }$ is proportional to $x \ : - \ : \bar { x }$ Equation (2–45) gives a linear math-. ematical model for the nonlinear system given by Equation (2–42) near the operating point $x = \bar { x } , y = \bar { y }$ .

Next, consider a nonlinear system whose output y is a function of two inputs $x _ { 1 }$ and $x _ { 2 } .$ , so that

$$y = f \left(x _ {1}, x _ {2}\right) \tag {2-46}$$

To obtain a linear approximation to this nonlinear system, we may expand Equation (2–46) into a Taylor series about the normal operating point $\overline { { x } } _ { 1 } , \overline { { x } } _ { 2 }$ Then Equation (2–46). becomes
