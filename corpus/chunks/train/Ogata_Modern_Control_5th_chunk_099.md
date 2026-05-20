Electronic Controllers. In what follows we shall discuss electronic controllers using operational amplifiers. We begin by deriving the transfer functions of simple operationalamplifier circuits.Then we derive the transfer functions of some of the operational-amplifier controllers. Finally, we give operational-amplifier controllers and their transfer functions in the form of a table.

![](image/fb1ad8ba252241c5edbacf6a11c932a00a4de40bddf080f4102ae4f1e39308e0.jpg)

<details>
<summary>text_image</summary>

R₁
eᵢ
C₁
Isolating
amplifier
(gain K)
R₂
C₂
eₒ
</details>

Figure 3–12 Electrical system.

Figure 3–13 Operational amplifier.   
![](image/e5e95d3de5f5e9d8aa9844661b4dd3852fb8e5a6480201b8488e830084e950dc.jpg)

<details>
<summary>text_image</summary>

e₁
e₂
+
-
eₒ
</details>

Operational Amplifiers. Operational amplifiers, often called op amps, are frequently used to amplify signals in sensor circuits. Op amps are also frequently used in filters used for compensation purposes. Figure 3–13 shows an op amp. It is a common practice to choose the ground as 0 volt and measure the input voltages $e _ { 1 }$ and $e _ { 2 }$ relative to the ground. The input $e _ { 1 }$ to the minus terminal of the amplifier is inverted, and the input $e _ { 2 }$ to the plus terminal is not inverted.The total input to the amplifier thus becomes $e _ { 2 } ~ - ~ e _ { 1 }$ . Hence, for the circuit shown in Figure 3–13, we have

$$e _ {o} = K \left(e _ {2} - e _ {1}\right) = - K \left(e _ {1} - e _ {2}\right)$$

where the inputs $e _ { 1 }$ and $e _ { 2 }$ may be dc or ac signals and K is the differential gain (voltage gain). The magnitude of K is approximately $1 0 ^ { 5 } \sim 1 0 ^ { 6 }$ for dc signals and ac signals with frequencies less than approximately 10 Hz. (The differential gain K decreases with the signal frequency and becomes about unity for frequencies of 1 MHz \~ 50 MHz.) Note that the op amp amplifies the difference in voltages $e _ { 1 }$ and $e _ { 2 }$ . Such an amplifier is commonly called a differential amplifier. Since the gain of the op amp is very high, it is necessary to have a negative feedback from the output to the input to make the amplifier stable. (The feedback is made from the output to the inverted input so that the feedback is a negative feedback.)
