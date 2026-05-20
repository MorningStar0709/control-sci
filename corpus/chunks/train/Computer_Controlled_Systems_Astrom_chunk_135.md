# Example 2.14 Transform of a ramp

Consider a ramp signal defined by $y(kh) = kh$ for $k \geq 0$ . Then

$$Y (z) = 0 + h z ^ {- 1} + 2 h z ^ {- 2} + \dots = h (z ^ {- 1} + 2 z ^ {- 2} + \dots) = \frac {h z}{(z - 1) ^ {2}}$$

Some properties of the z-transform are collected in Table 2.2. Notice that the formulas for forward and backward time shifts are not the same. This is a consequence of the assumption that the time sequences are semi-infinite.

The z-transform can be used to solve difference equations; for instance,

$$\boldsymbol {x} (k + 1) = \Phi \boldsymbol {x} (k) + \Gamma u (k)y (k) = C x (k) + D u (k)$$

If the $z$ -transform of both sides is taken,

$$\sum_ {k = 0} ^ {\infty} z ^ {- k} x (k + 1) = z \left(\sum_ {k = 0} ^ {\infty} z ^ {- k} x (k) - x (0)\right) = \sum_ {k = 0} ^ {\infty} \Phi z ^ {- k} x (k) + \sum_ {k = 0} ^ {\infty} \Gamma z ^ {- k} u (k)$$

Hence

$$z (X (z) - x (0)) = \Phi X (z) + \Gamma U (z)X (z) = (z I - \Phi) ^ {- 1} \left(z x (0) + \Gamma U (z)\right)$$

and

$$Y (z) = C (z I - \Phi) ^ {- 1} z x (0) + \left(C (z I - \Phi) ^ {- 1} \Gamma + D\right) U (z)$$

The pulse-transfer function can now be introduced.

$$H (z) ^ {\ddagger} = C (z I - \Phi) ^ {- 1} \Gamma + D \tag {2.29}$$

which is the same as (2.26) with q replaced by z. The time sequence $y(k)$ can now be obtained using the inverse transform. The following theorem is analogous to that of continuous-time systems.

Table 2.2 Some properties of the z-transform.

1. Definition.

$$F (z) = \sum_ {k = 0} ^ {\infty} f (k h) z ^ {- k}$$

2. Inversion.

$$f (k h) = \frac {1}{2 \pi i} \oint F (z) z ^ {k - 1} d z$$

3. Linearity.

$$\mathcal {Z} \{a f + \beta g \} = a \mathcal {Z} f + \beta \mathcal {Z} g$$

4. Time shift.

$$\mathcal {Z} \{q ^ {- n} f \} = z ^ {- n} F\mathcal {Z} \{q ^ {n} f \} = z ^ {n} (F - F _ {1}) \text { where } F _ {1} (z) = \sum_ {j = 0} ^ {n - 1} f (j h) z ^ {- j},$$

5. Initial-value theorem.

$$f (0) = \lim _ {z \rightarrow \infty} F (z)$$

6. Final-value theorem.

If $(1 - z^{-1})F(z)$ does not have any poles on or outside the unit circle, then $\lim_{k\to \infty}f(kh) = \lim_{z\to 1}(1 - z^{-1})F(z)$ .

7. Convolution.

$$\mathcal {Z} \{f * g \} = \mathcal {Z} \left\{\sum_ {n = 0} ^ {k} f (n) g (k - n) \right\} = (\mathcal {Z} f) (\mathcal {Z} g)$$

THEOREM 2.5 The pulse response of (2.20) and the pulse-transfer function (2.29) are a z-transform pair, that is, $\mathcal{Z}\{h(k)\}=H(z)$ .
