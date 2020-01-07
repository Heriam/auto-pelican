import subprocess
import Iutils as util

def install_pelican():
    # 父进程等待子进程完成。返回退出信息(return code，相当于Linux exit code)
    if 0 != subprocess.call('git clone git://github.com/getpelican/pelican.git', shell=True):
        util.error('git clone pelican failed!')