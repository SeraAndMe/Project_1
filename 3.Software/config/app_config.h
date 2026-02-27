#ifndef APP_CONFIG_H
#define APP_CONFIG_H

// 应用配置
#define APP_VERSION "1.0.0"
#define APP_NAME "Embedded Application"

// 任务配置
#define TASK_STACK_SIZE 1024
#define TASK_PRIORITY 1

// 通信配置
#define UART_BAUDRATE 115200
#define I2C_SPEED 100000U // 100KHz
#define SPI_SPEED 1000000U // 1MHz

#endif // APP_CONFIG_H
