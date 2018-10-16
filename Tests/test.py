# from subprocess import Popen, PIPE
#
# p = Popen(['client_tester.exe', '56'], shell=True, stdout=PIPE, stdin=PIPE)
# result = p.stdout.readline().strip()
# print(result)
# value = "123"
# value = bytes(value, 'UTF-8')
# p.stdin.write(value)
# result = p.stdout.readline().strip()
# print(result)
# p.stdin.write(bytes("salam", 'UTF-8'))
# result = p.stdout.readline().strip()
# print(result)

from subprocess import Popen, PIPE

p = [Popen(['client_tester.exe', str(i)], shell=True, stdout=PIPE, stdin=PIPE) for i in range(2)]

for i in range(10):
    value = str(i) + '\n'
    value = bytes(value, 'UTF-8')  # Needed in Python 3.
    p[i % 2].stdin.write(value)
    p[i % 2].stdin.flush()
    result = p[i % 2].stdout.readline().strip()
    print(result)