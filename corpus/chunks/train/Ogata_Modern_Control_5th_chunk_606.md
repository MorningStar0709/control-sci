Since the denominators of $Y ( s ) / D ( s )$ and $Y ( s ) / R ( s )$ are the same, the denominator of $Y ( s ) / D ( s )$ determines also the response characteristics for the reference input. To satisfy the third requirement, we refer to the zero-placement method and choose the closed-loop transfer function $Y ( s ) / R ( s )$ to be of the following form:

$$\frac {Y (s)}{R (s)} = \frac {(2 a + c) s ^ {2} + (a ^ {2} + b ^ {2} + 2 a c) s + (a ^ {2} + b ^ {2}) c}{s ^ {3} + (2 a + c) s ^ {2} + (a ^ {2} + b ^ {2} + 2 a c) s + (a ^ {2} + b ^ {2}) c}$$

in which case the third requirement is automatically satisfied.

Our problem then becomes a search of a set or sets of desired closed-loop poles in terms of $a , b ,$ and c in the specified region, such that the system will satisfy the requirement on the response to the unit-step reference input that the maximum overshoot be between 19% and 2% and the settling time be less than 1 sec. (If an acceptable set cannot be found in the search region, we need to widen the region.)

In the computational search, we need to assume a reasonable step size. In this problem, we assume it to be 0.2.

MATLAB Program 8–8 produces a table of sets of acceptable values of a, b, and c. Using this program, we find that the requirement on the response to the unit-step reference input is met by any of the 23 sets shown in the table in MATLAB Program 8–8. Note that the last row in the table corresponds to the last search point. This point does not satisfy the requirement and thus it should simply be ignored. (In the program written, the last search point produces the last row in the table whether or not it satisfies the requirement.)

MATLAB Program 8–8   
```matlab
t = 0:0.01:4;
k = 0;
for i = 1:21;
    a(i) = 6.2 - i * 0.2;
    for j = 1:21;
    b(j) = 6.2 - j * 0.2;
    for h = 1:31;
    c(h) = 12.2 - h * 0.2;
    num = [0 2 * a(i) + c(h) a(i)^2 + b(j)^2 + 2 * a(i) * c(h) (a(i)^2 + b(j)^2) * c(h)];
    den = [1 2 * a(i) + c(h) a(i)^2 + b(j)^2 + 2 * a(i) * c(h) (a(i)^2 + b(j)^2) * c(h)];
    y = step(num, den, t);
    m = max(y);
    s = 401; while y(s) > 0.98 & y(s) < 1.02;
    s = s - 1; end;
    ts = (s - 1) * 0.01;
    if m < 1.19 & m > 1.02 & ts < 1.0;
    k = k + 1;
    table(k,:) = [a(i) b(j) c(h) m ts];
    end
    end
    end
end 
```

(continues on next page)
