# coding=UTF-8
import sys
import inspect
import Iutils as util
import Ifuncs as func


# 初始化参数
args = sys.argv
path = args[0]
menu = inspect.getmembers(func, predicate=inspect.isfunction)


# 打印选项
def print_options():
    print('\n———————————— supported options ————————————\n')
    for i in range(len(menu)):
        print('[%s] %s' % (i, menu[i][0]))
    print('\n———————————————————————————————————————————\n')


# 运行入口
def run():
    if len(args) == 1:
        while True:
            select_and_run_opt()
    elif len(args) == 2:
        select_and_run_opt(args=args[1])
    else:
        print('Invalid arguments. Only 1 argument is supported at most. Please try again and rerun the code as below:')
        print('python auto-pelican.py [option-number]')
        print_options()


# 选择并允许选项
def select_and_run_opt(args=None):
    # 初始化
    print_options()
    # 入参解析
    try:
        if args:
            opt = args
        else:
            opt = input('Select option:')
        # 执行操作
        if (type(opt) == int or opt.isdigit()) and (len(menu) > int(opt) >= 0):
            menu[int(opt)][1]()
        else:
            util.info('Invalid input. Please retype the number of intended option.')
    except KeyboardInterrupt as err:
        util.info('Have a nice day. Bye bye!')
        sys.exit(0)
    except (SyntaxError, NameError, AttributeError) as err:
        util.info('Invalid input. Please retype the number of intended option.')


if __name__ == '__main__':
    run()