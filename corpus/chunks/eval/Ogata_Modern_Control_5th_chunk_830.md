$$
\begin{array}{l} z (s) = P _ {1 1} w (s) + P _ {1 2} u (s) \\ y (s) = P _ {2 1} w (s) + P _ {2 2} u (s) \\ u (s) = K (s) y (s) \\ \end{array}
$$

we obtain

$$y (s) = P _ {2 1} w (s) + P _ {2 2} K (s) y (s)$$

Hence

$$[ I - P _ {2 2} K (s) ] y (s) = P _ {2 1} w (s)$$

or

$$y (s) = \left[ I - P _ {2 2} K (s) \right] ^ {- 1} P _ {2 1} w (s)$$

Therefore,

$$
\begin{array}{l} z (s) = P _ {1 1} w (s) + P _ {1 2} K (s) \left[ I - P _ {2 2} K (s) \right] ^ {- 1} P _ {2 1} w (s) \\ = \left\{P _ {1 1} + P _ {1 2} K (s) \left[ I - P _ {2 2} K (s) \right] ^ {- 1} P _ {2 1} \right\} w (s) \\ \end{array}
$$

Hence,

$$\Phi (s) = P _ {1 1} + P _ {1 2} K (s) \left[ I - P _ {2 2} K (s) \right] ^ {- 1} P _ {2 1} \tag {10-128}$$

EXAMPLE 10–15

Let us determine the P matrix in the generalized plant diagram of the control system considered in Example 10–14. We derived Inequality (10–125) for the control system to be robust stable. Rewriting Inequality (10–125), we have

$$\left\| \frac {W _ {m} K G}{1 + K G} \right\| _ {\infty} < 1 \tag {10-129}$$

If we define

$$\Phi_ {1} = \frac {W _ {m} K G}{1 + K G} \tag {10-130}$$

then Inequality (10–129) can be written as

$$\left\| \Phi_ {1} \right\| _ {\infty} < 1$$

Referring to Equation (10–128), rewritten as

$$\Phi = P _ {1 1} + P _ {1 2} K (I - P _ {2 2} K) ^ {- 1} P _ {2 1}$$

notice that if we choose the generalized plant P matrix as

$$
P = \left[ \begin{array}{c c} 0 & W _ {m} G \\ I & - G \end{array} \right] \tag {10-131}
$$

Then we obtain

$$
\begin{array}{l} \Phi = P _ {1 1} + P _ {1 2} K (I - P _ {2 2} K) ^ {- 1} P _ {2 1} \\ = W _ {m} K G (I + K G) ^ {- 1} \\ \end{array}
$$

which is exactly the same as $\Phi _ { 1 }$ in Equation (10–130).

We derived in Example 10–14 that if we wished to have the output y follow the input r as close as possible, we needed to make the $H _ { \infty }$ norm of $\Phi _ { 2 } ( s )$ , where

$$\Phi_ {2} = \frac {W _ {s}}{I + K G} \tag {10-132}$$

less than 1. [See Inequality (10–126).]

Note that the controlled variable z is related to the exogenous disturbance w by

$$z = \Phi (s) w$$

and referring to Equation (10–128)

$$\Phi (s) = P _ {1 1} + P _ {1 2} K \left(I - P _ {2 2} K\right) ^ {- 1} P _ {2 1}$$

Notice that if we choose the P matrix as

$$
P = \left[ \begin{array}{c c} W _ {s} & - W _ {s} G \\ I & - G \end{array} \right] \tag {10-133}
$$

then we obtain

$$
\begin{array}{l} \Phi = P _ {1 1} + P _ {1 2} K (I - P _ {2 2} K) ^ {- 1} P _ {2 1} \\ = W _ {s} - W _ {s} K G (I + K G) ^ {- 1} \\ = W _ {s} \left[ 1 - \frac {K G}{1 + K G} \right] \\ = W _ {s} \left[ \frac {1}{1 + K G} \right] \\ \end{array}
$$

which is the same as $\Phi _ { 2 }$ in Equation (10–132).
