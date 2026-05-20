# 9.5.3 Simulation of PID controllers

Looking again at equation (9.8), we can see from the far right hand side that the PID controller has two zeros and one pole. A system with more zeros than poles cannot be physically realized and is called improper. Often this condition is ignored because the plant has enough poles to make the overall forward path $( C ( s ) P ( s ) )$ proper. However, what if you would like to make and sell a PID controller box 3? It needs to be realizable all by itself !

We may also have this problem building a computer simulation if we dene the controller in our script as a separate system and our computer simulation package cannot simulate an improper system. To x this we simply add another pole to the PID controller at a high enough frequency so that it does not aect our response. This imediately raises two questions

1. Why doesn't a high frequency pole aect the system?   
2. How high is high enough?

For question one, consider the Bode plot of the basic one-pole system

$$P (s) = \rho / (s + \rho)$$

for $\omega < < \rho , P ( j \omega ) = 1$ . Its magnitude is 1 and its phase angle is 0. Thus for frequencies substantially below $\rho , P ( s )$ has no eect.

For question two, let us set ρ to be 10 times higher than the highest pole or zero of our system. Technically we should know the zeros of the PID controller to do this, but if we assume that the zeros of a good controller will be in the neighborhood of the poles of the plant, then 10 times greater than the highest frequency plant pole/zero will also be far from the PID controller zeros.

$$\rho = 1 0 \times p z _ {m a x}$$

where $p z _ { m a x }$ is the highest pole or zero in the system.

Thus we will add a pole, ρ, to the PID controller in our simulations as follows:

$$C _ {P I D 2} (s) = \frac {\rho (K _ {P} s + K _ {i} + K _ {D} s ^ {2})}{s (s + \rho)} = \frac {\rho K _ {D} (s ^ {2} + \frac {K _ {P}}{K _ {D}} s + \frac {K _ {I}}{K _ {D}})}{s (s + \rho)}$$

Now $C _ { P I D 2 }$ is proper because it has the same number of poles and zeros, two. Thus, we can simulate it and it is also physically realizable.
