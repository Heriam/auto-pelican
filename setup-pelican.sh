#!/usr/bin/expect -f

set timeout -1

spawn cd ~/myBlog
spawn pelican-quickstart

expect {
    'new web site? [.]' {send '\r'}
}

expect eof

exit