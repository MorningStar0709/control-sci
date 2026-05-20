void PID_Init(struct PID_Data *data)
{
    data->States.I = 0;
    data->States.D = 0;
    data->States.yold = 0;
    data->Par.K = 4.4;
    data->Par.Ti = 0.4;
    data->Par.Td = 0.2;
    data->Par.Tt = 10;
    data->Par.N = 10;
    data->Par.b = 1;
    data->Par.ulow = -1;
    data->Par.uhigh = 1;
    data->Par.h = 0.03;
    data->Par.bi = data->Par.K*data->Par.h/data->Par.Ti;
    data->Par.ar = data->Par.h/data->Par.Tt;
    data->Par.bd = data->Par.K*data->Par.N*data->Par.Td/
(data->Par.Td+data->Par.N*data->Par.h);
data->Par.ad = data->Par.Td/(data->Par.Td+data->Par.N*data->Par.h);
} 
```

Listing 8.1 (Continued)   
```c
void PID_CalculateOutput(struct PID_Data *data) {

/* Proportional part */
    double P = data->Par.K*(data->Par.b*data->Signals.uc - data->Signals.y);

/* Derivative part */
    data->States.D = data->Par.ad * data->States.D - data->Par.bd * (data->Signals.y - data->States.yold);

/* Calculate control signal */
    data->Signals.v = P + data->States.I + data->States.D;

/* Handle actuator limitations */
    if ( data->Signals.v < data->Par.ulow ) {
    data->Signals.u = data->Par.ulow;
    } else if ( data->Signals.v > data->Par.uhigh ) {
    data->Signals.u = data->Par.uhigh;
    } else {
    data->Signals.u = data->Signals.v;
    }
}

void PID_UpdateStates(struct PID_Data *data) {
    /* Integral part */
    data->States.I = data->States.I + data->Par.bi*(data->Signals.uc - data->Signals.y) + data->Par.ar*(data->Signals.u - data->Signals.v);

data->States.yold = data->Signals.y;
}

void PID_Main() {
    Kernel_Time time;

PID_Init(&pid_data);
    Kernel_CurrentTime(&time);    /* Get current time */
    for (;;) {
    Kernel_IncTime(&time, 1000 * pid_data.Par.h);
    /* Increment "time" with h*/
    read_y(&(pid_data.Signals.y));
    read_uc(&(pid_data.Signals.uc));
    PID_CalculateOutput(&pid_data);
    write_u(pid_data.Signals.u);
    PID_UpdateStates(&pid_data);
    Kernel_WaitUntil(time);    /* Wait until "time" */
    }
} 
```
