$$\delta_ {a} = \frac {1}{4} (- \delta_ {1} - \delta_ {2} + \delta_ {3} + \delta_ {4}),\delta_ {Y} = \frac {1}{2} (\delta_ {1} + \delta_ {3}),\delta_ {Z} = \frac {1}{2} (\delta_ {2} + \delta_ {4}).$$

The effective aileron deflection $\delta _ { a }$ is obtained by differential fin commands and is used to calculate a rolling moment, assumed to vary linearly with $\delta _ { a }$ , but with a slope varying with Mach number. Figure 3.42 shows the rotation and further limiting required to calculate the four individual commands to the fin servos.

An alternative way of expressing the fin deflections is to consider Figure 3.43. Here we use a coordinate system with the X-axis (roll) pointing along the missile’s longitudinal axis, the Y -axis (pitch) pointing to the right, and the Z-axis (yaw) pointing down.

The corresponding equations of motion can be written as follows [1], [3], [12]:

![](image/4e9926132f36d02b1e54d8c518bc241712dd0a6855ef9055c44a9d254477ad4d.jpg)

<details>
<summary>text_image</summary>

δ₄
+
ζ
+
δ₃
+
③
④
+ ξ
X
η
δ₁
+
Y
①
②
+
δ₂
Z
</details>

Fig. 3.43. Fin (control surface) deflections.

Pitch rudder angle:

$$\eta = \frac {1}{2} (\delta_ {1} - \delta_ {3}).$$

Yaw rudder angle:

$$\zeta = \frac {1}{2} (\delta_ {2} - \delta_ {4}).$$

Roll rudder angle:

$$\xi = \frac {1}{4} (\delta_ {1} + \delta_ {2} + \delta_ {3} + \delta_ {4}).$$

The equations of motion can now be written as follows:

Longitudinal Equations:

$$\Sigma X \colon m (u - r v + q w) = \frac {1}{2} \rho V ^ {2} S C _ {X} + F _ {X} + m g _ {X},\Sigma Z \colon m (w - q u + p v) = \frac {1}{2} \rho V ^ {2} S C _ {Z} + F _ {Z} + m g _ {Z} + F _ {\eta} \cdot \eta ,\Sigma \mathrm{M}: I _ {Z} \left(\frac {d q}{d t}\right) = \frac {1}{2} \rho V ^ {2} S d C _ {M} + (I _ {Y} - I _ {X}) r p + (m X _ {G} ^ {2} - I _ {Y}) q + x _ {s} F _ {\eta} \cdot \eta .$$

Yaw (Lateral) Equations:

$$
\Sigma \mathrm{Y} \colon m (v - p w + r u) = \frac {1}{2} \rho V ^ {2} S C _ {Y} + F _ {Y} + m g _ {Y} + F _ {\eta} \cdot \zeta ,
\begin{array}{l} \Sigma \mathrm{N}: I _ {Z} \left(\frac {d r}{d t}\right) = \frac {1}{2} \rho V ^ {2} S d C _ {N} + (I _ {Y} - I _ {X}) q p \\ + (m X _ {G} ^ {2} - I _ {Z}) r + x _ {s} F _ {\eta} \cdot \xi . \\ \end{array}
$$

Roll Equations:

$$I _ {X} \left(\frac {d p}{d t}\right) = \frac {1}{2} \rho V ^ {2} S d C _ {L} + y _ {s} F _ {\xi} \cdot \xi(F _ {\xi} = F _ {\eta} = 0; P _ {k} = 0).$$

(Assumptions: $q = 0 , V = \mathrm { c o n s t a n t } , u = V , p = 0 )$ , where
