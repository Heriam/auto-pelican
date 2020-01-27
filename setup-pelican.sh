#!/usr/bin/expect -f

set timeout -1

spawn cd ~/myBlog
spawn pelican-quickstart

expect {
    'Where do you want to create your new web site?' {send '\r'}
}

expect eof

exit