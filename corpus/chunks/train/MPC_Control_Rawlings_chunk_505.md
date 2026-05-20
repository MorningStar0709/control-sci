# Example 4.31: Sampling independent random variables

Consider two independent random variables ξ, η, whose probability density satisfies

$$p _ {\xi , \eta} (x, y) = p _ {\xi} (x) p _ {\eta} (y)$$

and assume we have samples of the two marginals

$$\xi \sim \{x _ {i}, w _ {x i} \} \quad w _ {x i} = 1 / s _ {x}, \quad i = 1, \dots , s _ {x}\eta \sim \{y _ {j}, w _ {y j} \} \quad w _ {y j} = 1 / s _ {y}, \quad j = 1, \dots , s _ {y}$$

We have many valid options for creating samples of the joint density. Here are three useful ones.

(a) Show the following is a valid sample of the joint density

$$\{(x _ {i}, y _ {j}), w _ {i j} \} \quad w _ {i j} = 1 / (s _ {x} s _ {y}), \quad i = 1, \dots , s _ {x}, \quad j = 1, \dots , s _ {y}$$

Notice we have $s _ { x } s _ { y }$ total samples of the joint density.

(b) If $s _ { x } = s _ { y } = s$ , show the following is a valid sample of the joint density

$$\{(x _ {i}, y _ {i}), w _ {i} \} \quad w _ {i} = 1 / s, \quad i = 1, \dots , s$$

Notice we have s total samples of the joint density unlike the previous case in which we would have $s ^ { 2 }$ samples.

(c) If we have available (or select) only a single sample of $\xi '$ s marginal, $s _ { x } = 1$ and $s _ { y } = s$ samples of $\eta ^ { \prime } s$ marginal, show the following is a valid sample of the joint density

$$\{(x _ {1}, y _ {i}), w _ {y i} \} \quad w _ {y i} = 1 / s, \quad i = 1, \dots , s$$

Here we have generated again s samples of the joint density, but we have allowed unequal numbers of samples of the two marginals.
