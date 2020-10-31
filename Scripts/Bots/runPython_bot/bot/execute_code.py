'''
This module is responsible for handling the execution of python code given by the telegram user.
'''


import subprocess
from subprocess import TimeoutExpired


def run(update):
    '''
    This function takes an Telegram `update` object, passed by the `reply` function in runPython_bot module, and returns the result after executing update.message.text.
    '''

    def execute_py(code):
        '''
        This function takes a string of python code and executes it in a subprocess of timeout 30s, and returns the standard out and standard error.

        Learn more about subprocesses from the official docs of Python 
        https://docs.python.org/3/library/subprocess.html

        For a shorter intro read this stack overflow answer 
        https://stackoverflow.com/questions/64606880/how-to-get-the-python-interactive-shell-output-of-a-python-code-in-a-variable
        '''

        proc = subprocess.Popen(['/usr/bin/python3.8', '-c', code],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            stdout, stderr = proc.communicate(timeout=30)
        except TimeoutExpired:
            return '', '😢 Timeout is 30s. I have limited resources. You may increase the timeout and run this bot on your own server if required.'
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def func(input_text):
        '''
        This function is a helper function which does some validation job before passing the code to execute_py.
        '''

        restricted_words = ['quit', 'input', 'open', 'import']
        if any(word in input_text for word in restricted_words):
            # block usage of this words for security and performance issues
            out = f'☹️ SECURITY ISSUE: You have used a restricted word \n {restricted_words}'
            return out
        stdout, stderr = execute_py(input_text)
        if str(stdout) or str(stderr):
            out = f'{stdout} \n{stderr}'
            return out
        return None

    input_text = update.message.text
    out = func(input_text)
    if not out:
        try:
            out = str(eval(input_text))
            # if there is no output, it may be due to the fact that the code does not have print and is a python expression. 
            # so the bot evaluates it using eval()
        except Exception as e:
            out = f'''😔 If you are planning to write lines after this line then try writing them in a single message. \n**To print something, try using print function**\n Executing your code gave no stdout or stderr. \nSo I tried to evaluate it by using eval(). That raised the following error \n {e}'''
    return out
