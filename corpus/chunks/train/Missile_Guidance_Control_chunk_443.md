As discussed earlier, we will consider the covariance matrices at the point of impact due to the errors at bomb release. Other error sources, such as those due to ballistic dispersion and pilot azimuth error, are statistically independent of errors at release and can therefore be treated separately. Furthermore, in establishing a simulation program, the initial covariance matrix at release is commonly determined by the Kalman filter and propagated to the ground plane (i.e., target impact point) where the resulting error ellipsoid is aligned with the target coordinates $( X _ { t } , Y _ { t } , Z _ { t } )$ . Therefore, the covariance matrix of the propagated ellipsoid is obtained in the $( X _ { t } , Y _ { t } , Z _ { t } )$ coordinate frame as illustrated in Figure 5.23.

In order to obtain the X-Y covariance matrix in the normal plane, which is required for computing the CEP radii, we must transform the propagated covariance matrix into the $( X , Y , Z )$ coordinate frame. Now, since the error ellipsoids are almost aligned with the $X _ { t } \mathrm { - a x i s }$ , we have

![](image/566a1a6948a56c8e0a30343c72fdfd799087686f86ea97aa715b4d221641ae66.jpg)

<details>
<summary>text_image</summary>

Bomb
trajectory
Z'
Z' sin θi
X
Normal plane
X = X' sin θi + Z' cos θi
The Y-error remains the same
in the normal & horizontal plane
X' = (error in x
cos θi)
Impact angle θi
Earth's surface
X'
θi
θi
X' sin θi
The errors in the horizontal
plane are larger because
they are ÷ by cos θi
</details>

Fig. 5.24. Transformation from the $X _ { t } { - } Z _ { t }$ frame into the X-axis and/or transformation from the $X ^ { \prime } – Z ^ { \prime }$ frame into the X-axis.

$$Y \cong Y _ {t}$$

and

$$\langle X, Y \rangle \cong \langle X _ {t}, Y _ {t} \rangle \cong 0$$

where $\langle \cdots \rangle$ denotes the cross-correlation components of the covariance matrix. Consequently, given the fact that $Y \cong Y _ { t }$ , we have

$$\sigma_ {Y} ^ {2} = \sigma_ {Y _ {t}} ^ {2}.$$

The transformation from the $X _ { t } – Y _ { t }$ plane to the X-Y plane is obtained from Figure 5.24 and is simply given by the equation

$$X = X _ {t} \sin \theta_ {i} + Z _ {t} \cos \theta_ {i}, \tag {5.39}$$

where $\theta _ { i }$ is the target impact angle. Therefore,
