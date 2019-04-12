import subprocess
import os


class JustTest:
    def __init__(self, file, dir):
        self.file = file
        self.dir = dir

    def ex(self, command, infile):
        i = open(infile, 'r')
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=i)
        stdout, stderr = p.communicate()
        i.close()
        return stdout, stderr

    def test(self, n):
        for i in range(n):
            cur_file = os.path.join(self.dir, str(i), 'input.txt')
            output = self.ex(self.file, cur_file)
            print(f'"{i}": "{output[0].decode()}",')


a = JustTest('XX', 'foo')
a.test(10)
