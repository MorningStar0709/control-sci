These four equations show the fundamental benefits and design objectives inherent in feedback loops. For example, equation (6.1) shows that the effects of disturbance d on the plant output can be made “small” by making the output sensitivity function $S _ { o }$ small. Similarly, equation (6.4) shows that the effects of disturbance $d _ { i }$ on the plant input can be made small by making the input sensitivity function $S _ { i }$ small. The notion of smallness for a transfer matrix in a certain range of frequencies can be made explicit using frequency-dependent singular values, for example, $\overline { { \sigma } } ( S _ { o } ) < 1$ over a frequency range would mean that the effects of disturbance d at the plant output are effectively desensitized over that frequency range.

Hence, good disturbance rejection at the plant output $( y )$ would require that

$$\overline {{\sigma}} (S _ {o}) = \overline {{\sigma}} \left((I + P K) ^ {- 1}\right) = \frac {1}{\underline {{\sigma}} (I + P K)} \quad \text {(for disturbance at plant output,} d),{\overline {{\sigma}} (S _ {o} P)} = {\overline {{\sigma}} \left((I + P K) ^ {- 1} P\right) = \overline {{\sigma}} (P S _ {i}) \quad (\mathrm{fordisturbanceatplantinput,} d _ {i})}$$

be made small and good disturbance rejection at the plant input $( u _ { p } )$ would require that

$$\overline {{\sigma}} (S _ {i}) = \overline {{\sigma}} \left((I + K P) ^ {- 1}\right) = \frac {1}{\underline {{\sigma}} (I + K P)} \quad \text {(for disturbance at plant input, d_{i}),}\overline {{\sigma}} (S _ {i} K) = \overline {{\sigma}} \left(K (I + P K) ^ {- 1}\right) = \overline {{\sigma}} (K S _ {o}) \quad (\text { for disturbance at plant output, } d)$$

be made small, particularly in the low-frequency range where d and $d _ { i }$ are usually significant.

Note that

$$\underline {{\sigma}} (P K) - 1 \leq \underline {{\sigma}} (I + P K) \leq \underline {{\sigma}} (P K) + 1\underline {{\sigma}} (K P) - 1 \leq \underline {{\sigma}} (I + K P) \leq \underline {{\sigma}} (K P) + 1$$

then

$$\frac {1}{\underline {{\sigma}} (P K) + 1} \leq \overline {{\sigma}} (S _ {o}) \leq \frac {1}{\underline {{\sigma}} (P K) - 1}, \text { if } \underline {{\sigma}} (P K) > 1\frac {1}{\underline {{\sigma}} (K P) + 1} \leq \overline {{\sigma}} (S _ {i}) \leq \frac {1}{\underline {{\sigma}} (K P) - 1}, \text { if } \underline {{\sigma}} (K P) > 1$$

These equations imply that
