# Example 9.14

We have a large industrial machine with the following plant model:

$$P (s) = \frac {(s + 1)}{(s + 2 . 0) (s + 0 . 7 + 0 . 2 j) (s + 0 . 7 - 0 . 2 j)}, H = 1$$

Our desired performance specications are:

$$T _ {S D} = 1. 3 3 \text {sec} \quad \% O S = 10 \% \quad S S E _ {D} = 0$$

(Note that with these specs, there is a specic pole location rather than a region.)

It is decreed that we shall use a PID controller, but we have no initial values for $\mathrm { \tilde { \it { K } } } _ { P } , { \cal K } _ { I } , { \cal K } _ { D } .$

To approach the manual design, we will use the root locus method to analyze performance of PID controllers. Because we need to plot zeros and poles of the controller, the most useful form of the PID controller (for this design method) is:

$$C (s) = \frac {K _ {D} (s + z _ {1}) (s + z _ {2})}{s}$$

(we can convert this to $K _ { P } , K _ { I } ,$ , and $K _ { D }$ using Equation 9.9.)
