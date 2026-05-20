# Example 2.6

For the system of Example 2.3, let's nd the transfer function

$$G (s) = \frac {X (s)}{F (s)}$$

Using this transfer function we could compute the displacement as a function of the input force. There is only one mass and thus only one EOM. Starting with the EOM

$$M \ddot {x} + (B _ {1} + B _ {2}) \dot {x} + K x = f (t)$$

First take the Laplace Transform:

$$(L T) \quad M X (s) s ^ {2} + (B _ {1} + B _ {2}) X (s) s + K X (s) = F (s)$$

then we factor out X(s) from each term giving

$$X (s) \left(M s ^ {2} + \left(B _ {1} + B _ {2}\right) s + K\right) = F (s)$$

dividing through we get the transfer function

$$G (s) = \frac {X (s)}{F (s)} = \frac {1}{M s ^ {2} + (B _ {1} + B _ {2}) s + K}$$

We will nd it useful to normalize each transfer function before further analysis. This means that we will manipulate each polynomial in s so that the coecient of highest power of s is 11. This is accomplished by just dividing through by the coecient of the highest power of s as a nal step.
