# EXAMPLE 2–5 Linearize the nonlinear equation

$$z = x y$$

in the region $5 \leq x \leq 7 , 1 0 \leq y \leq 1 2$ . Find the error if the linearized equation is used to calculate the value of z when $x = 5 , y = 1 0$ .

Since the region considered is given by $5 \leq x \leq 7 , 1 0 \leq y \leq 1 2 .$ , choose $\bar { x } = 6 , \bar { y } = 1 1$ Then. $\bar { z } = \bar { x } \bar { y } = 6 6$ Let us obtain a linearized equation for the nonlinear equation near a point. $\begin{array} { r } { \bar { x } = 6 . } \end{array}$ , y– = 11.

Expanding the nonlinear equation into a Taylor series about point $x = \bar { x } , y = \bar { y }$ and neglecting the higher-order terms, we have

$$z - \bar {z} = a (x - \bar {x}) + b (y - \bar {y})$$

where

$$a = \frac {\partial (x y)}{\partial x} \Bigg | _ {x = \bar {x}, y = \bar {y}} = \bar {y} = 1 1b = \frac {\partial (x y)}{\partial y} \Bigg | _ {x = \bar {x}, y = \bar {y}} = \bar {x} = 6$$

Hence the linearized equation is

$$z - 6 6 = 1 1 (x - 6) + 6 (y - 1 1)$$

or

$$z = 1 1 x + 6 y - 6 6$$

When x=5, y=10, the value of z given by the linearized equation is

$$z = 1 1 x + 6 y - 6 6 = 5 5 + 6 0 - 6 6 = 4 9$$

The exact value of z is z=xy=50. The error is thus 50-49=1. In terms of percentage, the error is 2%.
