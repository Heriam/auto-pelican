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
            select_and_run_opt(_input=True)
    elif len(args) == 2:
        select_and_run_opt(_args=args[1])
    else:
        print('Invalid arguments. Only 1 argument is supported at most. Please try again and rerun the code as below:')
        print('python auto-pelican.py [option-number]')
        print_options()


# 选择并允许选项
def select_and_run_opt(_args=None, _input=False):
    # 初始化
    print_options()
    opt = None
    # 入参解析
    if _input and not _args:
        try:
            opt = input('Select option:')
        except KeyboardInterrupt as err:
            util.info('KeyboardInterrupt Exiting.')
            sys.exit(0)
        except (SyntaxError, NameError) as err:
            util.info('Invalid input. Please retype the number of intended option.')
    elif _args and not _input:
        opt = _args
    else:
        SyntaxError('Operations must and can only be selected by either interactive input or initial arguments.')
    # 执行操作
    if (type(opt) == int or opt.isdigit()) and (len(menu) > int(opt) >= 0):
        menu[int(opt)][1]()
    else:
        util.info('Invalid input. Please retype the number of intended option.')


if __name__ == '__main__':
    run()