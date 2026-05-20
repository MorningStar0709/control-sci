$$G _ {c} (s) G (s) = K \frac {T s + 1}{\beta T s + 1} G (s) = \frac {T s + 1}{\beta T s + 1} K G (s) = \frac {T s + 1}{\beta T s + 1} G _ {1} (s)$$

where

$$G _ {1} (s) = K G (s)$$

Determine gain K to satisfy the requirement on the given static velocity error constant.

2. If the gain-adjusted but uncompensated system $G _ { 1 } ( j \omega ) = K G ( j \omega )$ does not satisfy the specifications on the phase and gain margins, then find the frequency point where the phase angle of the open-loop transfer function is equal $1 0 - 1 8 0 ^ { \circ }$ plus the required phase margin. The required phase margin is the specified phase margin plus $5 ^ { \circ }$ to 12°. (The addition of $5 ^ { \circ }$ to $1 2 ^ { \circ }$ compensates for the phase lag of the lag compensator.) Choose this frequency as the new gain crossover frequency.

3. To prevent detrimental effects of phase lag due to the lag compensator, the pole and zero of the lag compensator must be located substantially lower than the new gain crossover frequency. Therefore, choose the corner frequency $\omega = 1 / T$ (corresponding to the zero of the lag compensator) 1 octave to 1 decade below the new gain crossover frequency. (If the time constants of the lag compensator do not become too large, the corner frequency $\omega = 1 / T$ may be chosen 1 decade below the new gain crossover frequency.)

Notice that we choose the compensator pole and zero sufficiently small. Thus the phase lag occurs at the low-frequency region so that it will not affect the phase margin.

4. Determine the attenuation necessary to bring the magnitude curve down to 0 dB at the new gain crossover frequency. Noting that this attenuation is -20 log $\beta ,$ de-, termine the value of $\beta .$ Then the other corner frequency (corresponding to the pole of the lag compensator) is determined from $\omega = 1 / ( \beta T )$ .

5. Using the value of K determined in step 1 and that of $\beta$ determined in step 4, calculate constant $K _ { c }$ from

$$K _ {c} = \frac {K}{\beta}G (s) = \frac {1}{s (s + 1) (0 . 5 s + 1)}$$

It is desired to compensate the system so that the static velocity error constant $K _ { v }$ is $5 \sec ^ { - 1 }$ , the phase margin is at least $4 0 ^ { \circ }$ , and the gain margin is at least 10 dB.

We shall use a lag compensator of the form

$$G _ {c} (s) = K _ {c} \beta \frac {T s + 1}{\beta T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\beta T}} \quad (\beta > 1)$$

Define

$$K _ {c} \beta = K$$

Define also

$$G _ {1} (s) = K G (s) = \frac {K}{s (s + 1) (0 . 5 s + 1)}$$
