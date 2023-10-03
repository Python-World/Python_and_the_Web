from datetime import datetime, timedelta


class Pomodoro:
    """Mimics a Pomodoro timer, a time management tool that breaks work into intervals separated by
    breaks.
    """

    # define timer types
    TIMER_NONE = 0
    TIMER_TASK = 1
    TIMER_SHORT_BREAK = 2
    TIMER_LONG_BREAK = 3

    def __init__(
        self,
        task_goal,
        long_break_length,
        short_break_length,
        task_length_minutes,
    ):
        """
        Initialize a pomodoro timer
        """

        # define goals
        self.task_goal = int(task_goal)
        self.task_count = 0
        self.long_break_goal = int(task_goal) / 2
        self.task_length_minutes = int(task_length_minutes)
        self.short_break_length = int(short_break_length)
        self.long_break_length = int(long_break_length)

        # define task length
        self.task_length = timedelta(minutes=self.task_length_minutes)

        # define break periods
        self.short_break = timedelta(minutes=self.short_break_length)
        self.long_break = timedelta(minutes=self.long_break_length)

        # initialize timer
        self.timer_type = self.TIMER_NONE

        # initialize timer start and end
        self.timer_start = 0
        self.timer_end = 0

    def start_task(self):
        """
        Stars a task timer.
        """

        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.task_length
        self.timer_type = self.TIMER_TASK

        print("\n---- begin task {} ----\n".format(self.task_count + 1))

    def start_short_break(self):
        """
        Starts a short break timer.
        """

        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.short_break
        self.timer_type = self.TIMER_SHORT_BREAK

        print("\n---- begin short break ----\n")

    def start_long_break(self):
        """
        Starts a long break timer.
        """

        # set start & end times
        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.long_break
        self.timer_type = self.TIMER_LONG_BREAK

        print("\n---- begin long break ----\n")

    def complete_task(self):
        """
        Increases task count by 1.
        """

        # increase task counter
        self.task_count += 1

    def done(self):
        """
        Denotes whether the Pomodoro task goal has been met.

        Returns True if task goal has been met.  False otherwise.
        """
        return self.task_count == self.task_goal

    def get_time_remaining(self):
        """
        returns the amount of time remaining in the current timer in the form of a timedelta object.
        """
        return self.timer_end - datetime.now()

    def format_timedelta(self, td):
        """
        Formats a timedelta object to a string displaying minutes & seconds.
        """
        var = type(self)  # Dummy line
        var = td.total_seconds()
        # find seconds
        total_seconds = int(var)

        # 3600 seconds in an hour
        hours, remainder = divmod(total_seconds, 3600)

        # 60 seconds in a minute
        minutes, seconds = divmod(remainder, 60)

        return "{} hours {} mins {} secs".format(hours, minutes, seconds)

    def print_summary(self):
        """
        Prints a summary of the current timer type & time remaining.
        """

        task_name = "none"

        # format timer output
        if self.timer_type == self.TIMER_TASK:
            task_name = "task"
        elif self.timer_type == self.TIMER_SHORT_BREAK:
            task_name = "short break"
        elif self.timer_type == self.TIMER_LONG_BREAK:
            task_name = "long break"

        # format time remaining output
        time_remaining = self.format_timedelta(self.get_time_remaining())

        print("{} | time remaining: {}".format(task_name, time_remaining))
