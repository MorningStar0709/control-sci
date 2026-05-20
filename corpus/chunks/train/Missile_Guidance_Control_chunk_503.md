# CEP Computation

Compute the covariances at the target for each of the n error sources:

$$\sigma_ {D R} ^ {2} = \sum_ {i} ^ {n} \delta D R _ {i} ^ {2}, \tag {5.93a}$$

![](image/b0c437770c6a7e6d44298b9a0b4811f8d34e804e4923bdc2384199ac14330b22.jpg)

<details>
<summary>text_image</summary>

Y
+4
Impact points
x̄
MPI
+3
ith impact point
δDRi
xi
ȳ
+2
δCRi +4
Target
+1
Ri
θ
yi
X
+1 +2 +3 +4
Delivery heading
</details>

Fig. 5.37. Coordinate system for data measurement.

$$\sigma_ {C R} ^ {2} = \sum_ {i} ^ {n} \delta C R _ {i} ^ {2}, \tag {5.93b}\sigma_ {D R, C R} ^ {2} = \sum_ {i} ^ {n} \delta C R _ {i} \delta D R _ {i}. \tag {5.93c}$$

In general, the contours of equal probability will be ellipses for which the major and minor axes are DR, CR.

From Figure 5.38 we have the transformation of variables

$$x = x _ {C R} \cos \theta + y _ {D R} \sin \theta ,y = - x _ {C R} \sin \theta + y _ {D R} \cos \theta ,$$

where

$$
x = \text { cross - range miss distance },y = \text { down - range (azimuth) miss distance },
\begin{array}{c} \theta = \text { angle   measured   counterclockwise   from } \\ \text { weapon   delivery   heading, } \end{array}
R = \text { radial miss distance from target. }
$$

![](image/49a7b9f14720b9039d706993d7de971c5d3d38340583529685167360c54c637d.jpg)

<details>
<summary>text_image</summary>

yDR
x
y
θ
xCR
</details>

Fig. 5.38. Coordinate rotation geometry.

In matrix form,

$$
\left[ \begin{array}{l} x \\ y \end{array} \right] = \left[ \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right] \left[ \begin{array}{l} x _ {C R} \\ y _ {D R} \end{array} \right]. \tag {5.94}
$$

Taking the covariance matrix of (5.94) (using the expectation operator E) and after some algebra, we obtain

$$
\operatorname{cov} \left[ \begin{array}{l} x \\ y \end{array} \right] = E \left\{\left[ \begin{array}{l} x \\ y \end{array} \right] \left[ \begin{array}{l} x \\ y \end{array} \right] ^ {T} \right\} = \left[ \begin{array}{l l} \sigma_ {x} ^ {2} & 0 \\ 0 & \sigma_ {y} ^ {2} \end{array} \right]. \tag {5.95}
$$

The CEP is determined from the position error covariance matrix, denoted by

$$
P = \left[ \begin{array}{c c} p _ {1 1} & p _ {1 2} \\ p _ {2 1} & p _ {2 2} \end{array} \right].
$$

The elements of the position error covariance matrix indicate the standard deviations of and correlation between the north (or down-range) and east (or cross-range) position errors. They are given by
