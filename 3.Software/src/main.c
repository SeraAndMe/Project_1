int main(void)
{
    board_init();
    app_task_init();

    while(1) {
        app_task_run();
    }
}