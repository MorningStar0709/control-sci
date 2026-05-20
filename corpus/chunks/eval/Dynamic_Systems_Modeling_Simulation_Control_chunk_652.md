![](image/fbb89a5839f04294c6b3c3ea54155bea58a3e92d3c48a0960d8d4ffce73b4c97.jpg)

<details>
<summary>line</summary>

| Time, s | Driver | Floor |
| --- | --- | --- |
| 0.0 | 1.0 | 0.0 |
| 0.5 | -1.5 | -0.7 |
| 1.0 | 1.3 | 0.8 |
| 1.5 | -1.2 | -0.8 |
| 2.0 | 1.2 | 0.8 |
| 2.5 | -1.2 | -0.8 |
| 3.0 | 1.2 | 0.0 |
</details>

Figure 11.7 Frequency response of driver acceleration for input frequency = 1 Hz.

The frequency-response results presented by Figs. 11.6a–c can be succinctly summarized by a Bode diagram of the seat-suspension system, where the output is defined as the driver displacement $z _ { 2 }$ . Because the Bode diagram displays the frequency-response information for a single input and single output, we must re-derive the SSR in terms of the sole independent input, which is floor displacement $z _ { 0 } ( t )$ . In this case, the definition of the second state variable $x _ { 2 }$ must be altered, and subsequently the $4 \times 1$ input matrix B differs from the $4 \times 2$ input matrix presented by Eq. (11.2) for the case of two (dependent) inputs (for details, see Problem 5.32, Chapter 5). The following MATLAB commands define the desired SSR (with $u = z _ { 0 } ( t )$ as the single input and $z _ { 2 }$ as the single output) and then plot the Bode diagram:

```matlab
>> m1 = 20;    % seat mass, kg
>> m2 = 50;    % driver mass, kg
>> k1 = 7410;    % suspension stiffness, N/m
>> k2 = 8230;    % cushion stiffness, N/m
>> b1 = 1430;    % suspension friction, N-s/m
>> b2 = 153;    % cushion friction, N-s/m
>> Arow1 = [0 1 0 0];    % row 1 of matrix A
>> Arow2 = [(-k1-k2)/m1 (-b1-b2)/m1 k2/m1 b2/m1];    % row 2 of matrix A
>> Arow3 = [0 0 0 1];    % row 3 of matrix A
>> Arow4 = [k2/m2 b2/m2 -k2/m2 -b2/m2];    % row 4 of matrix A
>> A = [Arow1 ; Arow2 ; Arow3 ; Arow4];    % system matrix A
>> Brow1 = b1/m1;    % row 1 of matrix B
>> Brow2 = (-b1^2 - b1*b2 + k1*m1)/m1^2;    % row 2 of matrix B
>> Brow3 = 0;    % row 3 of matrix B
>> Brow4 = b1*b2/(m1*m2);    % row 4 of matrix B
>> B = [Brow1 ; Brow2 ; Brow3 ; Brow4];    % input matrix B
>> C = [0 0 1 0];    % output y = x₃ = z₂
>> D = 0;    % direct-link (null)
>> sys = ss(A,B,C,D);    % build SSR sys
>> bode(sys)    % plot Bode diagram 
```
