# coding=UTF-8
import Iutils as util


# 读取配置
py_ver = util.config['install_python3_version']


# 更新系统
def _0_update_packages():
    util.shell('yum -y update', False)


# 安装 Python3
def _1_install_python3():
    if not (util.python_version[0] == 3 and util.python_version[1] >= 5):
        util.shell('yum -y groupinstall "Development Tools"', False)
        util.shell('yum -y install zlib zlib-devel libffi-devel maven openssl-devel wget', False)
        util.shell('wget https://www.python.org/ftp/python/%s/Python-%s.tgz' % (py_ver,py_ver))
        util.shell('tar -zxvf Python-%s.tgz' % py_ver)
        util.shell('cd Python-%s' % py_ver)
        util.shell('./configure prefix=/usr/local/python3')
        util.shell('make')
        util.shell('make install')
        util.shell('cd /usr/bin')
        util.shell('mv python python2', False)
        util.shell('mv pip pip2', False)
        util.shell('ln -s /usr/local/python3/bin/python3 /usr/bin/python', False)
        util.shell('ln -s /usr/local/python3/bin/pip3 /usr/bin/pip', False)
        util.shell('sed -i "s/#!\/usr\/bin\/python/#!\/usr\/bin\/python2/g" /usr/bin/yum', False)
        util.shell('sed -i "s/#!\/usr\/bin\/python/#!\/usr\/bin\/python2/g" /usr/libexec/urlgrabber-ext-down', False)
        util.shell('python -V', False)
        util.shell('pip -V', False)


# 安装 Pelican
def _2_install_pelican():
    util.shell('git clone git://github.com/getpelican/pelican.git')
    util.shell('cd pelican')
    util.shell('python setup.py install')
    util.shell('pip install markdown')