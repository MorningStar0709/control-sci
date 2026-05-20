# Example 7.11 Translation of a computer-controlled system with two loops

The system illustrated in Fig. 7.31(a) has two measured analog signals, $y_1$ and $y_2$ , and one analog command signal, $u_r$ . The analog signals are scanned by a multiplexer and converted to digital form. The computer calculates the control signal, which is fed to the process via the D-A converter. Figure 7.31(h) is obtained by the procedure given in Example 7.10. We now introduce

$$F _ {1} (s) = G _ {1} (s) \frac {1}{s} \left(1 - e ^ {- s h}\right)F _ {2} (s) = G _ {2} (s) F _ {1} (s)$$

The Laplace transforms of the output signals are then given by

$$Y _ {1} (s) = F _ {1} (s) U ^ {*} (s)Y _ {2} (s) = F _ {2} (s) U ^ {*} (s)$$

Hence

$$Y _ {1} ^ {*} (s) = \left(F _ {1} (s) U ^ {*} (s)\right) ^ {*} = F _ {1} ^ {*} (s) U ^ {*} (s)Y _ {2} ^ {*} (s) = \left(F _ {2} (s) U ^ {*} (s)\right) ^ {*} = F _ {2} ^ {*} (s) U ^ {*} (s)$$

It follows from (7.33) and (7.37) that

$$Y _ {1} (z) = \bar {F} _ {1} (z) U (z)Y _ {2} (z) = \bar {F} _ {2} (z) U (z)$$

Let the calculations performed by the control computer be represented by

$$U (z) = H _ {c} (z) U _ {c} (z) - H _ {1} (z) Y _ {1} (z) - H _ {2} (z) Y _ {2} (z)$$

The relationship between the output, $Y_{2}$ , and the sampled command signal, $U_{c}$ , is

$$Y _ {2} (z) = \frac {H _ {c} (z) \bar {F} _ {2} (z)}{1 + H _ {1} (z) \bar {F} _ {1} (z) + H _ {2} (z) \bar {F} _ {2} (z)} U _ {r} (z)$$

Notice, however, that the relationship between the analog signals $y_{1}$ and $u_{c}$ cannot be represented by a simple pulse-transfer function because of the periodic nature of the sampled-data system.

With the introduction of the sampled signals as sequences and pulse-transfer functions, the system can be represented as in Fig. 7.31(c).
