# 模糊逻辑控制的位置跟踪

(1) 模糊控制器设计程序: chap4\_2. m  
```matlab
% Fuzzy Controller Design
clear all;
close all;

a = newfis('fuzzf');

a = addvar(a,'input','e',[-0.3,0.3]); % Parameter e
a = addmf(a,'input',1,'NB','zmf',[-0.3,-0.1]);
a = addmf(a,'input',1,'NM','trimf',[-0.3,-0.2,0]);
a = addmf(a,'input',1,'NS','trimf',[-0.3,-0.1,0.1]);
a = addmf(a,'input',1,'Z','trimf',[-0.2,0,0.2]);
a = addmf(a,'input',1,'PS','trimf',[-0.1,0.1,0.3]);
a = addmf(a,'input',1,'PM','trimf',[0,0.2,0.3]);
a = addmf(a,'input',1,'PB','smf',[0.1,0.3]);

a = addvar(a,'input','ec',[-0.3,0.3]); % Parameter ec
a = addmf(a,'input',2,'NB','zmf',[-0.3,-0.1]);
a = addmf(a,'input',2,'NM','trimf',[-0.3,-0.2,0]);
a = addmf(a,'input',2,'NS','trimf',[-0.3,-0.1,0.1]);
a = addmf(a,'input',2,'Z','trimf',[-0.2,0,0.2]);
a = addmf(a,'input',2,'PS','trimf',[-0.1,0.1,0.3]);
a = addmf(a,'input',2,'PM','trimf',[0,0.2,0.3]);
a = addmf(a,'input',2,'PB','smf',[0.1,0.3]);

a = addvar(a,'output','u',[-30,30]); % Parameter u
a = addmf(a,'output',1,'NB','zmf',[-30,-30]);
a = addmf(a,'output',1,'NM','trimf',[-30,-20,0]);
a = addmf(a,'output',1,'NS','trimf',[-30,-10,10]);
a = addmf(a,'output',1,'Z','trimf',[-20,0,20]);
a = addmf(a,'output',1,'PS','trimf',[-10,10,30]);
a = addmf(a,'output',1,'PM','trimf',[0,20,30]);
a = addmf(a,'output',1,'PB','smf',[10,30]);

rulelist=[1 1 1 1 1; % Edit rule bas
    1 2 1 1 1;
    1 3 2 1 1;
    1 4 2 1 1; 
```

15311;   
16311;   
17411;

21111;   
2 2 2 1 1;   
23211;   
24311;   
25311;   
26411;   
27511;

31211;   
32211;   
3 3 3 1 1;   
34311;   
35411;   
36511;   
37511;

4 1 2 1 1;   
4 2 3 1 1;   
4 3 3 1 1;   
4 4 4 1 1;   
4 5 5 1 1;   
4 6 5 1 1;   
47611;

51311;   
52311;   
3411;   
4511;   
5511;   
6611;   
7611;

1311;   
2411;   
3511;   
4 5 1 1;   
5611;   
6 6 1 1;   
7 7 1 1;

1411;   
2511;   
3511;   
4611;   
5611;   
6711;   
7 7 1 1];

```matlab
a = addrule(a, rulelist);
% showrule(a)    % Show fuzzy rule base

a1 = setfis(a, 'DefuzzMethod', 'mom'); % Defuzzy
writefis(a1, 'fuzzf');    % save to fuzzy file "fuzz.fis" which can be
% simulated with fuzzy tool
a2 = readfis('fuzzf');
disp('----');
disp(' fuzzy controller table: e = [-3, +3], ec = [-3, +3]    ');
disp('----'); 
```

```matlab
Ulist = zeros(7, 7);

for i = 1:7
    for j = 1:7
    e(i) = -4 + i;
    ec(j) = -4 + j;
    Ulist(i, j) = evalfis([e(i), ec(j)], a2);
    end
    end

Ulist = ceil(Ulist)

figure(1);
plotfis(a2);
figure(2);
plotmf(a, 'input', 1);
figure(3);
plotmf(a, 'input', 2);
figure(4);
plotmf(a, 'output', 1); 
```
