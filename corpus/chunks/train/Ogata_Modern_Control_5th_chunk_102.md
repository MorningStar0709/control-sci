The complex impedances $Z _ { 1 } ( s )$ and $Z _ { 2 } ( s )$ for this circuit are

$$Z _ {1} (s) = R _ {1} \quad \text { and } \quad Z _ {2} (s) = \frac {1}{C s + \frac {1}{R _ {2}}} = \frac {R _ {2}}{R _ {2} C s + 1}$$

The transfer function $E _ { o } ( s ) / E _ { i } ( s )$ is, therefore, obtained as

$$\frac {E _ {o} (s)}{E _ {i} (s)} = - \frac {Z _ {2} (s)}{Z _ {1} (s)} = - \frac {R _ {2}}{R _ {1}} \frac {1}{R _ {2} C s + 1}$$

which is, of course, the same as that obtained in Example 3-8.

Lead or Lag Networks Using Operational Amplifiers. Figure 3–18(a) shows an electronic circuit using an operational amplifier. The transfer function for this circuit can be obtained as follows: Define the input impedance and feedback impedance as $Z _ { 1 }$ and $Z _ { 2 }$ , respectively. Then

$$Z _ {1} = \frac {R _ {1}}{R _ {1} C _ {1} s + 1}, \quad Z _ {2} = \frac {R _ {2}}{R _ {2} C _ {2} s + 1}$$

Hence, referring to Equation (3–34), we have

$$\frac {E (s)}{E _ {i} (s)} = - \frac {Z _ {2}}{Z _ {1}} = - \frac {R _ {2}}{R _ {1}} \frac {R _ {1} C _ {1} s + 1}{R _ {2} C _ {2} s + 1} = - \frac {C _ {1}}{C _ {2}} \frac {s + \frac {1}{R _ {1} C _ {1}}}{s + \frac {1}{R _ {2} C _ {2}}} \tag {3-35}$$

Notice that the transfer function in Equation (3–35) contains a minus sign.Thus, this circuit is sign inverting. If such a sign inversion is not convenient in the actual application, a sign inverter may be connected to either the input or the output of the circuit of Figure 3–18(a). An example is shown in Figure 3–18(b). The sign inverter has the transfer function of

$$\frac {E _ {o} (s)}{E (s)} = - \frac {R _ {4}}{R _ {3}}$$

The sign inverter has the gain of $- R _ { 4 } / R _ { 3 }$ Hence the network shown in Figure 3–18(b). has the following transfer function:

$$\frac {E _ {o} (s)}{E _ {i} (s)} = \frac {R _ {2} R _ {4}}{R _ {1} R _ {3}} \frac {R _ {1} C _ {1} s + 1}{R _ {2} C _ {2} s + 1} = \frac {R _ {4} C _ {1}}{R _ {3} C _ {2}} \frac {s + \frac {1}{R _ {1} C _ {1}}}{s + \frac {1}{R _ {2} C _ {2}}}= K _ {c} \alpha \frac {T s + 1}{\alpha T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}} \tag {3-36}$$

![](image/67afb0cd15f97583889c8ef96d66cf566988e3f8c8207ad5758edecf8a573139.jpg)

<details>
<summary>text_image</summary>

Z1
C1
i1
R1
E'(s)
i2
C2
R2
Z2
E(s)
</details>

(a)

![](image/41fb0c803b50dbfdb8e104664fed7ae8d9df3ade59ded9a18dac9825814270ac.jpg)

<details>
<summary>text_image</summary>

C1
R1
C2
R2
Ei(s)
E(s)
R3
R4
Eo(s)
Lead or lag network
Sign inverter
</details>
