import subprocess
import sys
import Iutils as util


# 读取配置
ver = util.config['install_python3_version']


# 更新系统
def update_packages():
    util.shell('yum -y update', False)


# 安装 Python3
def install_python3():
    if not (util.python_version[0] == 3 and util.python_version[1] >= 5):
        util.shell('yum -y groupinstall "Development Tools"')
        util.shell('yum -y install zlib zlib-devel libffi-devel maven openssl-devel wget')
        util.shell('wget https://www.python.org/ftp/python/%s/Python-%s.tgz' % (ver,ver))
        util.shell('tar -zxvf Python-%s.tgz' % ver)
        util.shell('cd Python-%s' % ver)
        util.shell('./configure')
        util.shell('make')
        util.shell('make install')
    if not util.shell('pip3 -V', False):





# 安装 Pelican
def install_pelican():
    util.shell('git clone git://github.com/getpelican/pelican.git')
    util.shell('cd pelican')
    util.shell('python setup.py install')
    util.shell('pip install markdown')