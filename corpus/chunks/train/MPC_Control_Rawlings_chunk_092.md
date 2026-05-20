Combine arrival cost and measurement. We now combine the arrival cost and measurement for the next stage of the optimization to obtain

$$V _ {1} (x (1)) = \underbrace {V _ {1} ^ {-} (x (1))} _ {\text { prior }} + \underbrace {(1 / 2) \left| (y (1) - C x (1)) \right| _ {R ^ {- 1}} ^ {2}} _ {\text { measurement }}V _ {1} (x (1)) = \frac {1}{2} \left(\left| x (1) - \hat {x} ^ {-} (1) \right| _ {(P ^ {-} (1)) ^ {- 1}} ^ {2} + \left| y (1) - C x (1) \right| _ {R ^ {- 1}} ^ {2}\right)$$

We can see that this equation is exactly the form as (1.31) of the previous step, and, by simply changing the variable names, we have that

$$P (1) = P ^ {-} (1) - P ^ {-} (1) C ^ {\prime} \left(C P ^ {-} (1) C ^ {\prime} + R\right) ^ {- 1} C P ^ {-} (1)L (1) = P ^ {-} (1) C ^ {\prime} \left(C P ^ {-} (1) C ^ {\prime} + R\right) ^ {- 1}\hat {x} (1) = \hat {x} ^ {-} (1) + L (1) (\mathcal {Y} (1) - C \hat {x} ^ {-} (1))$$

and the cost function $V _ { 1 }$ is defined as

$$V _ {1} (x (1)) = (1 / 2) (x (1) - \hat {x} (1)) ^ {\prime} P (1) ^ {- 1} (x (1) - \hat {x} (1))$$

in which

$$\hat {x} ^ {-} (1) = A \hat {x} (0)P ^ {-} (1) = A P (0) A ^ {\prime} + Q$$

Recursion and termination. The recursion can be summarized by two steps. Adding the measurement at time k produces

$$P (k) = P ^ {-} (k) - P ^ {-} (k) C ^ {\prime} \left(C P ^ {-} (k) C ^ {\prime} + R\right) ^ {- 1} C P ^ {-} (k)L (k) = P ^ {-} (k) C ^ {\prime} \left(C P ^ {-} (k) C ^ {\prime} + R\right) ^ {- 1}\hat {x} (k) = \hat {x} ^ {-} (k) + L (k) (y (k) - C \hat {x} ^ {-} (k))$$

Propagating the model to time k + 1 produces

$$\hat {x} ^ {-} (k + 1) = A \hat {x} (k)P ^ {-} (k + 1) = A P (k) A ^ {\prime} + Q$$

and the recursion starts with the prior information $\hat { x } ^ { - } ( 0 ) = \overline { { x } } ( 0 )$ and $P ^ { - } \left( 0 \right)$ . The arrival cost, $V _ { k } ^ { - }$ , and arrival cost plus measurement, $V _ { k }$ , for each stage are given by

$$V _ {k} ^ {-} (x (k)) = (1 / 2) \left| x (k) - \hat {x} ^ {-} (k) \right| _ {(P ^ {-} (k)) ^ {- 1}}V _ {k} (x (k)) = (1 / 2) | x (k) - \hat {x} (k) | _ {(P (k)) ^ {- 1}}$$

The process terminates with the final measurement $y ( T )$ , at which point we have recursively solved the original problem (1.29).

We see by inspection that the recursion formulas given by forward DP of (1.29) are the same as those found by calculating the conditional density function in Section 1.4.2. Moreover, the conditional densities before and after measurement are closely related to the least squares value functions as shown below
