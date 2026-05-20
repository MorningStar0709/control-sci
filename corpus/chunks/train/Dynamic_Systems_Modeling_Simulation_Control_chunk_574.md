Clearly, the free response eventually “dies out” owing to the exponential functions $e ^ { - 2 t }$ and $e ^ { - 3 t }$ , which depend on the real parts of the characteristic roots. The particular (or forced) response is bounded if the input is bounded. Hence, the LTI system $G _ { P } ( s )$ is BIBO stable. If even one characteristic root had a positive real part, then the corresponding exponential function would diverge to infinity over time (an unbounded output) and the system would be unstable.

This simple example shows that the stability of an LTI closed-loop control system can be determined by computing the characteristic roots or poles of the closed-loop transfer function. The MATLAB roots command can be used to quickly calculate the roots of the characteristic equation. Suppose the system $G _ { P } ( s )$ defined by Eq. (10.35) is the plant in a closed-loop, unity-feedback system with a proportional controller $( K _ { P } )$ . The closed-loop transfer function is

$$T (s) = \frac {K _ {P} G _ {P} (s)}{1 + K _ {P} G _ {P} (s)} = \frac {K _ {P}}{0 . 5 s ^ {3} + 4 s ^ {2} + 2 3 s + 3 4 + K _ {P}} \tag {10.36}$$

The following MATLAB commands will compute the closed-loop poles (closed-loop roots) for a proportional gain $K _ { P } = 3 0$

```matlab
>> Kp = 30; % proportional gain setting
>> denT = [0.5 4 23 (34+Kp)]; % denominator of closed-loop T(s)
>> CLpoles = roots(denT) % compute closed-loop poles 
```

Executing the above MATLAB commands yields the closed-loop poles

```txt
CLpoles =
-1.8714 + 5.1540i
-1.8714 - 5.1540i
-4.2573 
```

Because all three closed-loop poles have negative real parts, the closed-loop system is BIBO stable.
