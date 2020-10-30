import subprocess
from subprocess import TimeoutExpired


def run(update):
    def execute_py(code):
        proc = subprocess.Popen(['/usr/bin/python3.8', '-c', code],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            stdout, stderr = proc.communicate(timeout=30)
        except TimeoutExpired:
            return '', '😢 Timeout is 30s. I have limited resources. You may increase the timeout and run this bot on your own server if required.'
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def func(input_text):
        restricted_words = ['quit', 'input', 'open', 'import']
        if any(word in input_text for word in restricted_words):
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
        except Exception as e:
            out = f'''😔 If you are planning to write lines after this line then try writing them in a single message. \n**To print something, try using print function**\n Executing your code gave no stdout or stderr. \nSo I tried to evaluate it by using eval(). That raised the following error \n {e}'''
    return out
