#include "drv_motor.h"

void motor_run_loop(void)
{
    motor_forward();
    delay_ms(3000);   // 正转3秒

    motor_stop();
    delay_ms(500);

    motor_backward();
    delay_ms(3000);   // 反转3秒

    motor_stop();
    delay_ms(500);
}