# 11.7 Limitations and properties

Tustin's method creates a controller which only approximates the continuous time controller. However useful discrete time controllers can be made if the following properties and limitations are taken into account.

 If the continous time TF is stable then the discrete time version will be stable.   
 The DT controller will have the same features of its frequency response (number and frequency order of poles and zeros) as the CT controller.   
 Frequencies of the poles and zeros will in general be shifted.   
 For frequencies much less than the Nyquist rate $\left( f _ { N } \right)$ , the approximation will be very accurate.

To make sure the discrete time controller is accurate, make sure that $T < < \pi / p z$ where pz is the frequency of the highest pole or zero in the CT system (including both $C ( s )$ and $P ( s ) )$ ). For example, let

$$C _ {1} (s) = \frac {5 0 0 (s + 1 0)}{(s + 1) (s + 1 0 0)}$$

For this controller, $p z = 1 0 0 r a d / s e c$ . This is about $1 6 H z .$ We need to double this to account for Nyquist sampling and THEN multiply by 10 to make the frequencies of the poles much less than the Nyquist rate.

Thus a suitable sampling frequency would be $1 6 \times 2 \times 1 0 = 3 2 0$ samples/second. We would convert $C _ { 1 } ( s )$ to discrete time using $T = 0 . 0 0 3 1 2 5 = 1 / 3 2 0 s e c )$ .
