# coding=UTF-8
import sys
import Iutils as util
import subprocess


# 读取配置
py_ver = util.config['install_python3_version']


# 更新系统
def _0_update_packages():
    util.shell('yum -y update', exit4fail=False)


# 安装 Python3
def _1_install_python3():
    if not (util.python_version[0] == 3 and util.python_version[1] >= 5):
        util.shell('yum -y groupinstall "Development Tools"', exit4fail=False)
        util.shell('yum -y install zlib zlib-devel libffi-devel maven openssl-devel wget', exit4fail=False)
        util.shell('wget https://www.python.org/ftp/python/%s/Python-%s.tgz' % (py_ver,py_ver))
        util.shell('tar -zxvf Python-%s.tgz' % py_ver)
        util.shell('cd Python-%s && ./configure prefix=/usr/local/python3 && make && make install' % py_ver)
        util.shell('mv /usr/bin/python /usr/bin/python2')
        util.shell('ln -s /usr/local/python3/bin/python3 /usr/bin/python')
        util.shell('mv /usr/bin/pip /usr/bin/pip2', exit4fail=False)
        util.shell('ln -s /usr/local/python3/bin/pip3 /usr/bin/pip', exit4fail=False)
        util.shell('pip install --upgrade pip', exit4fail=False)
        util.shell('sed -i "s/#!\/usr\/bin\/python/#!\/usr\/bin\/python2/g" /usr/bin/yum')
        util.shell('sed -i "s/#!\/usr\/bin\/python/#!\/usr\/bin\/python2/g" /usr/libexec/urlgrabber-ext-down')
        util.shell('echo "export PATH=$PATH:/usr/local/python3/bin/" >> /etc/environment')
        util.shell('source /etc/environment')
        if util.shell('python -V', exit4fail=False) and util.shell('pip -V', exit4fail=False):
            util.info('Python3 installed successfully.')
        else:
            util.error('Python3 installation failed.')
        sys.exit(0)
    else:
        util.info('Python3 already installed.')


# 安装 Pelican
def _2_install_pelican():
    util.shell('pip install pelican Markdown')
    util.shell('mkdir blog')
    p = subprocess.Popen('cd blog && pelican-quickstart', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(p.stdout.readlines())
