# 14.1.1 Examples

While this is a linear regression, we can fit nonlinear functions by making the contents of X nonlinear functions of the independent variables. For example, we can find the quadratic equation $y = a x ^ { 2 } + b x + c$ that best fits a set of x-y tuples. Lets assume we have a set of observations as follows.

$$y _ {1} = a x _ {1} ^ {2} + b x _ {1} + cy _ {n} = a x _ {n} ^ {2} + b x _ {n} + c$$

We want to find a, b, and c, so let’s factor those out.

$$
\left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {n} \end{array} \right] = \left[ \begin{array}{c c c} x _ {1} ^ {2} & x _ {1} & 1 \\ \vdots & \vdots & \vdots \\ x _ {n} ^ {2} & x _ {n} & 1 \end{array} \right] \left[ \begin{array}{c} a \\ b \\ c \end{array} \right]
$$

Plug these matrices into equation (14.1) to obtain the coefficients $a , b ,$ and $c .$

$$
\mathbf {y} = \left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {n} \end{array} \right] \quad \mathbf {X} = \left[ \begin{array}{c c c} x _ {1} ^ {2} & x _ {1} & 1 \\ \vdots & \vdots & \vdots \\ x _ {n} ^ {2} & x _ {n} & 1 \end{array} \right] \quad \boldsymbol {\beta} = \left[ \begin{array}{c} a \\ b \\ c \end{array} \right]
$$
