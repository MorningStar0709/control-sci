# Solution:

We need to prove that the expression represents a norm. Thus, it has to satisfy the following properties:

• The expression must be positive $\forall y ( x ) \ \in \ \mathbb { C } ^ { 0 }$ . We can observe that $y ( x )$ is always positive. The exponential term p lets the expression be positive. Therefore, the integral defined for $b > a$ will also let the expression be positive. The result will be elevated to the $1 / p$ exponential, which makes the total expression always positive.   
• Given $c \in \mathbb { R }$ , we have that:

$$\left| \left| c y \right| \right| _ {\mathcal {L} _ {p}} = \left(\int_ {a} ^ {b} | c y (x) | ^ {p} d x\right) ^ {1 / p} = \left(\int_ {a} ^ {b} | c | ^ {p} | y (x) | ^ {p} d x\right) ^ {1 / p} \tag {48}$$

So, we can move c out of the integral and get the result:

$$\left(\mid c \mid^ {p} \int_ {a} ^ {b} \mid c \mid^ {p} \mid y (x) \mid^ {p} d x\right) ^ {1 / p} = \mid c \mid \left(\int_ {a} ^ {b} \mid c \mid^ {p} \mid y (x) \mid^ {p} d x\right) ^ {1 / p} = \left| \mid c \mid \right| \cdot \left| \mid y (x) \right| \left| _ {\mathcal {L} _ {p}} \right. \tag {49}$$

• We want to show that only $y ( x ) = 0$ will make the norm zero. We can notice that, for our conditions, the only way to make the norm zero is either to have $a = b .$ , which contradicts our hypotesis, or to have $\mid y ( x ) \mid = 0 ;$ ; the only way is of course to have $y ( x ) = 0$ .   
• We want to show that the triangle inequality holds, which means that:

$$\left(\int_ {a} ^ {b} | y (x) + z (x) | ^ {p} d x\right) ^ {1 / p} \leq \left(\int_ {a} ^ {b} | y (x) | ^ {p} d x\right) ^ {1 / p} + \left(\int_ {a} ^ {b} | z (x) | ^ {p} d x\right) ^ {1 / p} \tag {50}$$

However, the exponential function is a convex function. Therefore, the following will hold:

$$\mid y (x) + z (x) \mid^ {p} \leq \mid y (x) \mid^ {p} + \mid z (x) \mid^ {p} \tag {51}$$

The integral function maintains the inequality:

$$\left(\int_ {a} ^ {b} | y (x) + z (x) | ^ {p} d x\right) \leq \left(\int_ {a} ^ {b} | y (x) | ^ {p} d x\right) + \left(\int_ {a} ^ {b} | z (x) | ^ {p} d x\right) \tag {52}$$

And the other exponential function too:

$$\left(\int_ {a} ^ {b} | y (x) + z (x) | ^ {p} d x\right) ^ {1 / p} \leq \left[ \left(\int_ {a} ^ {b} | y (x) | ^ {p} d x\right) + \left(\int_ {a} ^ {b} | z (x) | ^ {p} d x\right) \right] ^ {1 / p} \tag {53}$$

The new exponential is also a convex function. Therefore, the following the chain of equations hold:

$$\left[ \left(\int_ {a} ^ {b} | y (x) | ^ {p} d x\right) + \left(\int_ {a} ^ {b} | z (x) | ^ {p} d x\right) \right] ^ {1 / p} \leq \dots\dots \leq \left(\int_ {a} ^ {b} | y (x) | ^ {p} d x\right) ^ {1 / p} + \left(\int_ {a} ^ {b} | z (x) | ^ {p} d x\right) ^ {1 / p}$$

Thus proving our hypothesis.

![](image/f177e0a82fee7ead98d483bd9ceca885c401eb8ce51551234ff737b736484ed9.jpg)
