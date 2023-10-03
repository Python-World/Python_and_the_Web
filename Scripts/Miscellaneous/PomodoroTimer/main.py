import datetime
from datetime import datetime, timedelta

from pomodoro import Pomodoro


def main():
    # create pomodoro & begin first task

    task_goal = input("Enter the number of tasks you want to do today: ")
    task_length_minutes = input("Enter the length of each task: ")
    short_break_length = input("Enter the length of a short break: ")
    long_break_length = input("Enter the length of a long break: ")
    pomodoro = Pomodoro(
        task_goal, long_break_length, short_break_length, task_length_minutes
    )
    pomodoro.start_task()

    while True:
        # Initialize last_summary variable to 15 seconds in the past
        last_summary = pomodoro.timer_start - timedelta(seconds=15)

        # while the timer is running
        while pomodoro.get_time_remaining() > timedelta(seconds=0):
            current_time = datetime.now()

            # print a summary of the current timer every 15 seconds
            if (current_time - last_summary) > timedelta(seconds=15):
                pomodoro.print_summary()

                # update timer to track when the last summary was printed
                last_summary = current_time

        # if we are on a task, complete the task.  Otherwise, we start the task timer
        if pomodoro.timer_type == Pomodoro.TIMER_TASK:
            # complete the task
            pomodoro.complete_task()

            # check to see if need to continue to a break or stop the pomodoro
            if pomodoro.done():
                break
            if pomodoro.task_count % pomodoro.long_break_goal == 0:
                pomodoro.start_long_break()
            else:
                pomodoro.start_short_break()
        else:
            pomodoro.start_task()

    # we have met our pomodoro goal
    print("\nPomodoro Complete!")


if __name__ == "__main__":
    main()
