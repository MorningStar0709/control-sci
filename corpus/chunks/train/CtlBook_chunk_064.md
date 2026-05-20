# Example 2.5

Find the Equations of Motion for this electric circuit:

![](image/dbf8309974543ce124b35ae473b2342af0d79e65ae4cd3442ef71967d52501d3.jpg)

<details>
<summary>text_image</summary>

+
V(t)
-
L
R
C2
i1
i2
C1
</details>

![](image/f33414dda43310a3fb8a12ab3f642424060337836053614aaf181803eecd80f0.jpg)

<details>
<summary>text_image</summary>

f(t)
mL
X1
Kc1
BR
X2
Kc2
</details>

Electrical circuit (Left) and the corresponding mechanical system (Right).

Applying KVL to the two current loops (and ignoring the mechanical system) we get two LODE's:

$$L \frac {d i _ {1}}{d t} + (i _ {1} - i _ {2}) R + \frac {1}{C _ {1}} \int_ {0} ^ {t} (i _ {1} - i _ {2}) d t - v (t) = 0 \tag {2.3}\frac {1}{C _ {2}} \int_ {0} ^ {t} i _ {2} d t + \frac {1}{C _ {1}} \int_ {0} ^ {t} (i _ {2} - i _ {1}) d t + (i _ {2} - i _ {1}) R = 0 \tag {2.4}$$

Taking the LaPlace Transform (and assuming zero initial conditions),

$$I _ {1} (s) L s + \left(I _ {1} (s) - I _ {2} (s)\right) \left(R + \frac {1}{C _ {1} s}\right) = V (s) \tag {2.5}I _ {2} (s) (\frac {1}{C _ {2} s}) + (I _ {2} (s) - I _ {1} (s)) (R + \frac {1}{C _ {1} s}) \tag {2.6}$$

Collecting terms we get two Equations of Motion:

$$I _ {1} (s) (L s + R + \frac {1}{C _ {1} s}) + I _ {2} (s) (- R - \frac {1}{C _ {1} s}) = V (s) \tag {2.7}I _ {1} (s) \left(- R - \frac {1}{C _ {1} s}\right) + I _ {2} (s) \left(R + \frac {1}{C _ {1} s} + \frac {1}{C _ {2} s}\right) = 0 \tag {2.8}$$
