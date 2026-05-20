# 3.4 OPERATIONAL-AMPLIFIER CIRCUITS

An operational amplifier (“op-amp”) is a modern electronic device that is used to amplify (“gain”) an input voltage signal. They can also be used in circuits to construct filters that remove a desired range of frequencies from the input signal. Op amps were initially developed in the 1940s and during their evolution have utilized vacuum tubes, transistors, and integrated circuits. We do not investigate the inner-working details of an op amp; instead this section focuses on basic op-amp circuits.

Figure 3.12 shows the schematic diagram of an op amp that has two terminals on the input (left) side and one output terminal (right side). The input terminals with the negative and positive signs are known as the inverting and noninverting terminals, respectively. The output voltage $e _ { O }$ of the op amp shown in Fig. 3.12 is

$$e _ {O} = K (e _ {B} - e _ {A}) \tag {3.63}$$

where K is the “voltage gain” of the op amp, which is usually very large and on the order of 105 V/V.

The analysis of op-amp circuits is greatly simplified by utilizing what is known as an ideal op amp. An ideal op amp has the following characteristics:

1. The input terminals of the op amp draw negligible current.   
2. The voltage difference at the input terminals $e _ { B } - e _ { A }$ is zero.   
3. The gain K is infinite.

These ideal op-amp characteristics show that it is difficult to determine the output voltage $e _ { O }$ using the configuration in Fig. 3.12 and Eq. (3.63) as the input $e _ { B } - e _ { A } \approx 0$ and the gain K is infinite. We can see that using a “negative feedback” circuit connection from the output terminal to the inverting (negative) input terminal (not shown in Fig. 3.12) causes the second idealized condition. All of the op-amp circuits that we consider in this chapter utilize this negative feedback configuration, which we demonstrate in the following examples.
