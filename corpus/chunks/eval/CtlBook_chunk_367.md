# 11.3.2 Sampling Theorem

A powerful theorem due to Nyquist and Claude Shannon, states that

If a continuous signal has bandwidth, B radians per second, and it is sampled (converted to a sampled signal) with a sampling interval $\begin{array} { r } { T \le \frac { \pi } { B } } \end{array}$ , then the continuous time signal can be reconstructed perfectly from the discrete time signal.

Equivalently,

If a continuous signal has bandwidth, b Hertz, and it is sampled (converted to a sampled signal) at a sampling rate $f _ { N } \geq 2 b$ , then the continuous time signal can be reconstructed perfectly from the discrete time signal.

fN is called the Nyquist Rate. Although this theorem is commonly applied to signals (such as music) we will also use fN to decide how to sample control systems.

Sampling Safety Real-world signals don't necessarily have zero energy beyond some arbitrary bandwidth, b. So how do we make sure there is no signal energy beyond $\scriptstyle { \frac { 1 } { 2 } } f _ { N }$ that will corrupt our control system? First, real systems often employ an analog anti-aliasing lter (a low-pass lter) to block energy below $\scriptstyle { { \frac { 1 } { 2 } } f _ { N } }$ . But analog lters do not block ALL energy above their cuto-frequency.

Engineers use rules-of-thumb to add a safety factor to the Nyquist rate. Here are two of them:

First, we can assume that the system has low-pass lters. The magnitude response of a low pass lter keeps going down with higher frequencies. Thus if we sample even faster than the Nyquist rate, there will be even lower signal energy below that new rate.
