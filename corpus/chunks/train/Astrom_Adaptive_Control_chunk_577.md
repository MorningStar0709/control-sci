The parameters $K_{0}$ and $T_{i0}$ are also given in Table 9.1. Notice that they may change considerably even if the parameters of the state model do not change much. In many cases the model can be simplified to

$$G (s) = \frac {b}{s (s + a)} \tag {9.12}$$

where

$$b = b _ {0} \left(\frac {u}{l}\right) ^ {2} = b _ {2} \left(\frac {u}{l}\right) ^ {2} \tag {9.13}a = a _ {0} \left(\frac {u}{l}\right)$$

Table 9.1 Parameters of models for different ships.

<table><tr><td rowspan="2">Ship</td><td rowspan="2">Mine-sweeper</td><td rowspan="2">Cargo</td><td colspan="2">Tanker</td></tr><tr><td>Full</td><td>Ballast</td></tr><tr><td>Length (m)</td><td>55</td><td>161</td><td colspan="2">350</td></tr><tr><td> $a_{11}$ </td><td>-0.86</td><td>-0.77</td><td>-0.45</td><td>-0.43</td></tr><tr><td> $a_{12}$ </td><td>-0.48</td><td>-0.34</td><td>0.43</td><td>-0.45</td></tr><tr><td> $a_{21}$ </td><td>5.2</td><td>-3.39</td><td>-4.1</td><td>-1.98</td></tr><tr><td> $a_{22}$ </td><td>-2.4</td><td>-1.63</td><td>-0.81</td><td>-1.15</td></tr><tr><td> $b_1$ </td><td>0.18</td><td>0.17</td><td>0.10</td><td>0.14</td></tr><tr><td> $b_2$ </td><td>-1.4</td><td>-1.63</td><td>-0.81</td><td>-1.15</td></tr><tr><td> $K_0$ </td><td>2.11</td><td>-3.86</td><td>0.83</td><td>5.88</td></tr><tr><td> $T_{10}$ </td><td>-8.25</td><td>5.66</td><td>-2.88</td><td>-16.91</td></tr><tr><td> $T_{20}$ </td><td>0.29</td><td>0.38</td><td>0.38</td><td>0.45</td></tr><tr><td> $T_{30}$ </td><td>0.65</td><td>0.89</td><td>1.07</td><td>1.43</td></tr><tr><td> $a_0$ </td><td>-0.14</td><td>0.19</td><td>-0.28</td><td>-0.06</td></tr><tr><td> $b_0$ </td><td>-1.4</td><td>-1.63</td><td>-0.81</td><td>-1.15</td></tr></table>

This model is called the Nomoto model. Its gain b can be expressed approximately as follows:

$$b = c \left(\frac {u}{l}\right) ^ {2} \frac {A l}{D} \tag {9.14}$$

where D (in cubic meters) is the displacement, A (in square meters) is the rudder area, and c is a parameter whose value is approximately 0.5. The parameter a will depend on trim, speed, and loading. Its sign may change with the operating conditions.
