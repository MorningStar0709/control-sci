# A–2–13. Linearize the nonlinear equation

$$z = x ^ {2} + 4 x y + 6 y ^ {2}$$

in the region defined by $8 \leq x \leq 1 0 , 2 \leq y \leq 4 .$

Solution. Define

$$f (x, y) = z = x ^ {2} + 4 x y + 6 y ^ {2}$$

Then

$$z = f (x, y) = f (\bar {x}, \bar {y}) + \left[ \frac {\partial f}{\partial x} (x - \bar {x}) + \frac {\partial f}{\partial y} (y - \bar {y}) \right] _ {x = \bar {x}, y = \bar {y}} + \dots$$

where we choose $\bar { x } = 9 , \bar { y } = 3 .$ .

Since the higher-order terms in the expanded equation are small, neglecting these higherorder terms, we obtain

$$z - \bar {z} = K _ {1} (x - \bar {x}) + K _ {2} (y - \bar {y})$$

where

$$K _ {1} = \frac {\partial f}{\partial x} \Bigg | _ {x = \bar {x}, y = \bar {y}} = 2 \bar {x} + 4 \bar {y} = 2 \times 9 + 4 \times 3 = 3 0K _ {2} = \frac {\partial f}{\partial y} \Bigg | _ {x = \bar {x}, y = \bar {y}} = 4 \bar {x} + 1 2 \bar {y} = 4 \times 9 + 1 2 \times 3 = 7 2\bar {z} = \bar {x} ^ {2} + 4 \bar {x} \bar {y} + 6 \bar {y} ^ {2} = 9 ^ {2} + 4 \times 9 \times 3 + 6 \times 9 = 2 4 3$$

Thus

$$z - 2 4 3 = 3 0 (x - 9) + 7 2 (y - 3)$$

Hence a linear approximation of the given nonlinear equation near the operating point is

$$z - 3 0 x - 7 2 y + 2 4 3 = 0$$
