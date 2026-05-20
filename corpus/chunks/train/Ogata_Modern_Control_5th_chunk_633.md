![](image/40d1b8ef44c9f43810cc2c40101546ba062b02153b6ce1144cfe4d48da718cd6.jpg)

<details>
<summary>line</summary>

| t (sec) | Output |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.1 |
| 1.0 | 0.9 |
| 1.5 | 0.95 |
| 2.0 | 0.98 |
| 2.5 | 0.99 |
| 3.0 | 0.995 |
| 3.5 | 0.998 |
| 4.0 | 0.999 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
</details>

Figure 8–64 Unit-step response curve.

Next, we shall consider the case where we want to find all sets of variables that will satisfy the given specifications. A possible MATLAB program for this purpose is given in MATLAB Program 8–16. Note that in the table shown in the program, the last row of the table (k, :) or the first row of the sorttable should be ignored. (These are the last K and a values for searching purposes.)

```matlab
MATLAB Program 8–16
t = 0:0.01:5;
k = 0;
for i = 1:49;
    K(i) = 51-i*1;
    for j = 1:40;
    a(j) = 2.05-j*0.05;
    num = [K(i) 2*K(i)*a(j) K(i)*a(j)*a(j)];
    den = [1 6 5+K(i) 2*K(i)*a(j) K(i)*a(j)*a(j)];
    y = step(num,den,t);
    m = max(y);
    s = 501; while y(s) > 0.98 & y(s) < 1.02;
    s = s-1; end;
    ts = (s-1)*0.01;
    if m < 1.10 & m > 1.02 & ts < 3.0
    k = k+1;
    table(k,:) = [K(i) a(j) m ts];
    end
    end
end
table(k,:) = [K(i) a(j) m ts]
table = 
```

(continues on next page)

```matlab
32.0000 0.2000 1.0969 2.6400
31.0000 0.2000 1.0890 2.6900
30.0000 0.2000 1.0809 2.7300
29.0000 0.2500 1.0952 1.7800
29.0000 0.2000 1.0726 2.7800
28.0000 0.2000 1.0639 2.8300
27.0000 0.2000 1.0550 2.8900
2.0000 0.0500 0.3781 5.0000

sorttable = sortrows(table,3)

sorttable =
    2.0000 0.0500 0.3781 5.0000
    27.0000 0.2000 1.0550 2.8900
    28.0000 0.2000 1.0639 2.8300
    29.0000 0.2000 1.0726 2.7800
    30.0000 0.2000 1.0809 2.7300
    31.0000 0.2000 1.0890 2.6900
    29.0000 0.2500 1.0952 1.7800
    32.0000 0.2000 1.0969 2.6400

K = sorttable(7,1)

K =
    29

a = sorttable(7,2)

a =
    0.2500

num = [K 2*K*a K*a^2];
den = [1 6 5+K 2*K*a K*a^2];
y = step(num,den,t);
plot(t,y)

grid

hold

Current plot held

K = sorttable(2,1)

K=
    27

a = sorttable(2,2)

a=
    0.2000 
```

(continues on next page)

```matlab
num = [K 2*K*a K*a^2];
den = [1 6 5+K 2*K*a K*a^2];
y = step(num,den,t);
plot(t,y)
title('Unit-Step Response Curves')
xlabel('t (sec)')
ylabel('Output')
text(1.22,1.22,'K = 29, a = 0.25')
text(1.22,0.72,'K = 27, a = 0.2') 
```

Figure 8–65 Unit-step response curves.   
![](image/42ab7d1a736a7d418ac482a758585f0fc186b4cd255908bdd4faefce40b8c844.jpg)

<details>
<summary>line</summary>
