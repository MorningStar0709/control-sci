$$D _ {o} = \text { distance from the aircraft to the target },\psi_ {e} = \text { track angle error },\psi_ {e} ^ {\prime} = \text { modified track angle error }.$$

Figure 5.31 illustrates the direct mode.

When the aircraft approaches the target in the direct mode, the system establishes a track just as it does in the navigation mode. Steering cycles automatically to the centerline recovery mode when $\mathrm { D } _ { o } \leq 6 { , } 0 0 0$ feet. However, the track angle and crosstrack errors are modified to eliminate transients upon entering the new mode. The modified track angle error equation for $\psi _ { e } ^ { \prime }$ for automatic entry of the centerline recovery mode from the direct mode when $\mathrm { D } _ { o } \leq 6 { , } 0 0 0$ feet is given by

$$\psi_ {e} ^ {\prime} = \psi_ {e} + \sin^ {- 1} (C I / 6 0 0 0). \tag {5.70}$$

![](image/dd67b6c763c45cd8087867589d58c9336af33896b3c6c6d999a9bc5c77f68257.jpg)

<details>
<summary>text_image</summary>

X-body
V_N
ψ_TA
δ
V_g
V_E
</details>

Fig. 5.32. Wind velocity transformation.

In the discussion of Section 5.7, the bombing problem was treated without any wind present. Here we will briefly discuss the role the wind plays in the navigation process and subsequent accuracy of bombing. The navigation processing function is responsible for wind computations using prime ground speed (i.e., INS, Doppler, etc.). If INS or Doppler data are selected as prime, the winds can be computed as follows:

$$W _ {N} = - V _ {N / T A S} + V _ {N}, \tag {5.71a}W _ {E} = - V _ {E / T A S} + V _ {E}, \tag {5.71b}V _ {N} = V _ {g} \cos (\psi_ {T A} + \delta), \tag {5.71c}V _ {E} = V _ {g} \sin (\psi_ {T A} + \delta), \tag {5.71d}\psi_ {g} = \psi_ {T A} + \delta , \tag {5.71e}$$

where

$$
\begin{array}{c} V _ {N / T A S} = \text { north   component   of   the   true } \\ \text { airspeed(TAS) }, \end{array}

\begin{array}{c} V _ {E / T A S} = \text { east   component   of   the } \\ \text { true   airspeed, } \end{array}
V _ {g} = \text { ground speed },\delta = \text { drift angle },\psi_ {T A} = \mathrm{trueheadingangle},\psi_ {g} = \text { ground track angle }.
$$

If the INS or Doppler data are unavailable, corrections to wind estimates will be input from the system management and control function. The various relationships are illustrated in Figure 5.32.

![](image/f75622c0cb4db18f9b4004f969c02f83504a950e660edc81d710dd8fbaa9f1c8.jpg)

<details>
<summary>text_image</summary>

Cz
hs
RL
Specified point
hs
RE
RE
</details>

Fig. 5.33. Earth curvature definition.
