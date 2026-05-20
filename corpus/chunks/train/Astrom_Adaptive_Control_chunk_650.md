# EXAMPLE 11.3 Robust pole placement

Assume that we have obtained a controller $R^{0}$ , $S^{0}$ that gives a closed-loop system with the characteristic polynomial $A_{c}^{0}$ and that we want to improve its robustness by requiring that $S(-1) = 0$ . To do this, we introduce one more closed-loop pole. We choose

$$X (q) = q - x _ {0}$$

with $|x_0| < 1$ . The polynomial $Y$ can also be of first order. Equation (11.2) gives

$$S (q) = (q - x _ {0}) S ^ {0} (q) - (q - y _ {0}) A (q)$$

Requiring that $S(1) = 0$ gives

$$y _ {0} = - 1 + \frac {(1 + x _ {0}) S ^ {0} (- 1)}{A (- 1)}$$

The robust controller is then characterized by

$$R (q) = (q - x _ {0}) R ^ {0} (q) + (q - y _ {0}) B (q)S (q) = (q - x _ {0}) S ^ {0} (q) - (q - y _ {0}) A (q)$$

Notice that it is possible to proceed recursively to make the controller more and more complex.
