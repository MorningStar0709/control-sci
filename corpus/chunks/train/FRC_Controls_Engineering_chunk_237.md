# 8.7.1 Velocity subspace state-space model

By equations (12.35) and (12.36)

$$\dot {v} _ {l} = \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) (C _ {1} v _ {l} + C _ {2} V _ {l}) + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) (C _ {3} v _ {r} + C _ {4} V _ {r})\dot {v} _ {r} = \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) (C _ {1} v _ {l} + C _ {2} V _ {l}) + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) (C _ {3} v _ {r} + C _ {4} V _ {r})$$

Regroup the terms into states $v _ { l }$ and $v _ { r }$ and inputs $V _ { l }$ and $V _ { r }$ .

$$\dot {v} _ {l} = \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} v _ {l} + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} V _ {l}$$

![](image/302554dc1fd1c703a76602397bb4363137daa09d72dfa914e66d13f549c0f4c7.jpg)

<details>
<summary>text_image</summary>

ωl
ωr
J
r
rb
</details>

Figure 8.1: Differential drive dimensions

![](image/e2bc0e99eb2656a7789e93962fbad9d826528e842df99ac5bbc26d40602f5a4a.jpg)

<details>
<summary>text_image</summary>

v_l
v_r
θ
+x
+y
</details>

Figure 8.2: Differential drive coordinate frame

$$
+ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} v _ {r} + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} V _ {r}
\begin{array}{l} \dot {v} _ {r} = \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} v _ {l} + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} V _ {l} \\ + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} v _ {r} + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} V _ {r} \\ \end{array}
\dot {v} _ {l} = \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {1} v _ {l} + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {3} v _ {r}+ \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {2} V _ {l} + \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {4} V _ {r}\dot {v} _ {r} = \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {1} v _ {l} + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {3} v _ {r}+ \left(\frac {1}{m} - \frac {r _ {b} ^ {2}}{J}\right) C _ {2} V _ {l} + \left(\frac {1}{m} + \frac {r _ {b} ^ {2}}{J}\right) C _ {4} V _ {r}
$$

Factor out $v _ { l }$ and $v _ { r }$ into a column vector and $V _ { l }$ and $V _ { r }$ into a column vector.
