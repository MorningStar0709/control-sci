$$W _ {e} = \left(\frac {s / \sqrt [ k ]{M _ {s}} + \omega_ {b}}{s + \omega_ {b} \sqrt [ k ]{\varepsilon}}\right) ^ {k} \tag {6.7}$$

for some integer $k \geq 1$ .

The selection of control weighting function $W _ { u }$ follows similarly from the preceding discussion by considering the control signal equation

$$u = K S (r - n - d) - T d _ {i}$$

The magnitude of |KS| in the low-frequency range is essentially limited by the allowable cost of control effort and saturation limit of the actuators; hence, in general, the maximum gain $M _ { u }$ of KS can be fairly large, while the high-frequency gain is essentially limited by the controller bandwidth $\left( \omega _ { b c } \right)$ and the (sensor) noise frequencies. Ideally, one would like to roll off as fast as possible beyond the desired control bandwidth so that the high-frequency noises are attenuated as much as possible. Hence a candidate weight $W _ { u }$ would be

$$W _ {u} = \frac {s + \omega_ {b c} / M _ {u}}{\omega_ {b c}} \tag {6.8}$$

![](image/a6f0c3db66b0e630d6a57e3ec0a68dcf0955997d45e0f2dd73d327a281a2de18.jpg)  
Figure 6.8: Control weight $W _ { u }$ and desired KS

However, again the optimal control design techniques developed in this book cannot be applied directly to a problem with an improper control weighting function. Hence we shall introduce a far away pole to make $W _ { u }$ proper:

$$W _ {u} = \frac {s + \omega_ {b c} / M _ {u}}{\varepsilon_ {1} s + \omega_ {b c}} \tag {6.9}$$

for a small $\varepsilon _ { 1 } > 0$ , as shown in Figure 6.8. Similarly, if a faster rolloff is desired, one may choose

$$W _ {u} = \left(\frac {s + \omega_ {b c} / \sqrt [ k ]{M _ {u}}}{\sqrt [ k ]{\varepsilon_ {1}} s + \omega_ {b c}}\right) ^ {k} \tag {6.10}$$

for some integer $k \geq 1$ .

The weights for MIMO problems can be initially chosen as diagonal matrices with each diagonal term chosen in the foregoing form.
