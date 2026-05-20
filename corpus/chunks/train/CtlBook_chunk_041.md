# Example 1.10

Linearize the dierential equation

$$f _ {3} (t) = \ddot {x} - 0. 4 2 \dot {x} + 0. 0 1 (\dot {x}) ^ {3} + \sin (5 \dot {x}) + 1 6 x$$

about x˙ = 0 (We have omitted (t) from {x(t), x˙ (t), x¨(t)} to simplify notation.) x˙ is often the velocity of a physical part. Does a system do anything interesting if x˙ = 0? It can. Remember the linearization works in the neighborhood of the operating point  so we could say this linearization is valid for slow speeds (velocities near zero). That might be what we care about in our application.

The nonlinear part of this dierential equation can be taken out as a simple function, F n():

$$F n (y) = 0. 0 1 y ^ {3} + \sin (5 y)$$

where we are using the variable y just to avoid confusion with x, x˙ . Now we linearize F n(y) about y = 0:

$$\frac {d}{d y} F n (y) = 0. 0 3 y ^ {2} + 5 \cos (5 y)\hat {F} n (y) = F n (0) + \left. \frac {d}{d y} F n (y) \right| _ {y = 0} (y - 0) = 0 + 5 \cos (0) y = 5 y\hat {F} n (y) = 5 y$$

Plugging the linearized function back into the dierential equation:

$$f _ {3} (t) = \ddot {x} - 0. 4 2 \dot {x} + \hat {F} n (\dot {x}) + 1 6 xf _ {3} (t) = \ddot {x} - 0. 4 2 \dot {x} + 5 \dot {x} + 1 6 x = \ddot {x} + 4. 5 8 \dot {x} + 1 6 x$$

This LODE is a linearized version of our system which is valid in the neighborhood of x˙ = 0 (i.e. for low velocities).
