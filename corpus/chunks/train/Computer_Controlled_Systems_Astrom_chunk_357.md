# The Dahlin-Higham Algorithm

The Dahlin-Higham design method was popular in early digital process control design because the calculations required for the design are very simple. It is a special case of error feedback with complete cancellation, where the process pulse-transfer function has the form

$$H (z) = \frac {b}{z ^ {d} (z - a)} \tag {5.57}$$

and the desired closed-loop response is given by

$$H _ {c} (z) = \frac {1 - a _ {c}}{z ^ {d} (z - a _ {c})} \tag {5.58}$$

It follows from Eq. (5.56) that the controller is

$$\frac {S (z)}{R (z)} = \frac {z ^ {d} (z - a) (1 - a _ {c})}{b z ^ {d} (z - a _ {c}) - b (1 - a _ {c})} \tag {5.59}$$

The control law can be written as

$$u (k) = \frac {1 - a _ {c}}{b} \left(y (k) - a y (k - 1)\right) + a _ {c} u (k - 1) + (1 - a _ {c}) u (k - d - 1) \tag {5.60}$$

Because the algorithm is based on cancellation of all poles and zeros of the process, no poles or zeros can be allowed outside the unit disc. There will also be problems with ringing due to cancellation of stable but poorly damped zeros.
