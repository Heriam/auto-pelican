# coding=UTF-8
import sys
import Iutils as util
import os
import site


# 读取配置
py_ver = util.config['install_python3_version']
blog_path = util.config['blog_path']
github_email = util.config['github_email']
sitePkgDir = site.getsitepackages()[0]


# 更新系统
def _0_update_packages_centos_only():
    util.shell('yum -y update', exit4fail=False)
    util.info('System updated successfully.')


# 安装 Python3
def _1_install_python3_centos_only():
    if not (util.python_version[0] == 3 and util.python_version[1] >= 5):
        util.shell('yum -y groupinstall "Development Tools"', exit4fail=False)
        util.shell('yum -y install zlib zlib-devel libffi-devel maven openssl-devel wget', exit4fail=False)
        util.shell('wget https://www.python.org/ftp/python/%s/Python-%s.tgz' % (py_ver,py_ver))
        util.shell('tar -zxvf Python-%s.tgz' % py_ver)
        util.shell('cd Python-%s && ./configure prefix=/usr/local/python3 && make && make install' % py_ver)
        if os.path.exists('/usr/bin/python'):
            if not os.path.exists('/usr/bin/python2'):
                util.shell('mv /usr/bin/python /usr/bin/python2')
            else:
                util.shell('rm -rf /usr/bin/python')
            util.shell('ln -s /usr/local/python3/bin/python3 /usr/bin/python')
        if os.path.exists('/usr/bin/pip'):
            if not os.path.exists('/usr/bin/pip2'):
                util.shell('mv /usr/bin/pip /usr/bin/pip2')
            else:
                util.shell('rm -rf /usr/bin/pip')
        util.shell('ln -s /usr/local/python3/bin/pip3 /usr/bin/pip')
        util.shell('pip install --upgrade pip')
        util.shell('sed -i "s/\/usr\/bin\/python/\/usr\/bin\/python2/g" /usr/bin/yum')
        util.shell('sed -i "s/\/usr\/bin\/python/\/usr\/bin\/python2/g" /usr/libexec/urlgrabber-ext-down')
        util.shell('echo "export PATH=$PATH:/usr/local/python3/bin/" >> /etc/environment')
        util.shell('source /etc/environment')
        if util.shell('python -V', exit4fail=False) and util.shell('pip -V', exit4fail=False):
            util.info('Python3 installed successfully.')
        else:
            util.error('Python3 installation failed.')
        sys.exit(0)
    else:
        util.info('Python3 already installed.')


def _2_enable_git_ssh():
    if not os.path.exists('/root/.ssh/id_rsa.pub'):
        util.shell('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -P "" -C "%s"' % github_email)
    util.shell('cat ~/.ssh/id_rsa.pub')
    util.info('SSH public key has been printed to the console. You can now add it to your Github account.')


# 安装 Pelican
def _3_setup_pelican():
    # pip 安装 Pelican
    util.shell('pip install pelican Markdown')
    # git clone 博客输入内容
    util.shell('git clone https://github.com/Heriam/blog.git %s' % blog_path)
    # git clone 博客输出内容
    util.shell('mkdir %s/output' % blog_path)
    util.shell('git clone git@github.com:Heriam/heriam.github.io.git %s/output/heriam.github.io' % blog_path)
    # 配置Github.com和Coding.net国内网双DNS
    util.shell('cd %s && cp -f config output/heriam.github.io/.git/' % blog_path)
    # git clone 基于tuxlite_tbs的自定义博客主题
    util.shell('git clone https://github.com/Heriam/tuxlite_tbs.git %s/tuxlite_tbs' % blog_path)
    # 安装 基于tuxlite_tbs的自定义主题
    util.shell('pelican-themes -i %s/tuxlite_tbs' % blog_path)
    # git clone 插件库
    util.shell('git clone https://github.com/getpelican/pelican-plugins.git %s/pelican-plugins' % blog_path)
    # 安装结束
    util.info('Pelican setup successfully.')


# 发布更新
def _4_publish_updates():
    # 更新博客主题
    util.shell('cd %s/tuxlite_tbs && git pull' % blog_path)
    util.shell('pelican-themes -U %s/tuxlite_tbs' % blog_path)
    # 更新博客内容
    util.shell('cd %s && git pull' % blog_path)
    # 更新双DNS配置
    util.shell('cd %s && cp -f config output/heriam.github.io/.git/' % blog_path)
    # 升级博客插件
    util.shell('cd %s/pelican-plugins && git pull' % blog_path)
    # 发布更新
    util.shell('cd %s && make github' % blog_path)
    # 更新结束
    util.info('Updates published successfully.')


# 安装更新脚本
def _5_update_scriptify():
    with open('/usr/local/bin/update-blog', 'w+') as f:
        f.write('#!/bin/bash\n')
        f.write('python %sauto-pelican.py 3' % util.env_absolute_path)
    util.shell('chmod 777 /usr/local/bin/update-blog')
    util.info('Script generated successfully.')


# 卸载 Blog
def _6_uninstall_pelican():
    util.shell('rm -rf %s' % blog_path)
    util.shell('rm -rf /usr/local/bin/update-blog')
    util.shell('pelican-themes -r tuxlite_tbs')
    util.info('Pelican uninstalled successfully.')