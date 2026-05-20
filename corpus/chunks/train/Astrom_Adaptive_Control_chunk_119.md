# EXAMPLE 2.10 Loss of identifiability due to feedback

Consider a system described by

$$y (t + 1) + a y (t) = b u (t) \tag {2.49}$$

Assume that the parameters $a$ and $b$ should be estimated in the presence of the feedback

$$u (t) = - k y (t) \tag {2.50}$$

Multiplying Eq. (2.50) by $\alpha$ and adding to Eq. (2.49) give

$$y (t + 1) + (a + \alpha k) y (t) = (b - \alpha) u (t)$$

This shows that any parameters such that

$$
\begin{array}{l} \hat {a} = a + \alpha k \\ \hat {b} = b - \alpha \\ \end{array}
$$

give the same input-output relation. The above equation represents a straight line

$$\hat {b} = b + \frac {1}{k} (a - \hat {a}) \tag {2.51}$$

in parameter space (see Fig. 2.6). The least-squares loss function (2.2) has the same value for all parameters on this line. $\square$

The problem with lack of identifiability due to feedback disappears if a linear feedback of sufficiently high order is used. Then the columns of the matrix $\Phi$ given by Eq. (2.48) are no longer linearly dependent. Another possibility is to have a time-varying feedback. For example, in Example 2.10 it is sufficient to have a feedback of the form

$$u (t) = - k _ {1} y (t) - k _ {2} y (t - 1)$$

![](image/784d815db3e14698066c1115e81e9da3e15835bcee0b1d9058e44941e3029782.jpg)

<details>
<summary>text_image</summary>

â
b
Slope -1/k
True value
a
â
</details>

Figure 2.6 Illustration of lack of uniqueness in closed-loop identification.

with $k_{2} \neq 0$ . Another possibility is to use a feedback law

$$u (t) = - k (t) y (t)$$

where k varies with time. For instance, in Example 2.10 it is sufficient to use two values of the gain. Each value of the gain corresponds to a straight line with slope -1/k in parameter space. Two lines give a unique intersection.

In adaptive systems there is a natural time variation in the feedback because the feedback gains are based on parameter estimates. In a typical case the variance of the parameters decreases as 1/t, but more complex behavior is also possible. The following example shows what can happen.
