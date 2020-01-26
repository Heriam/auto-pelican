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
    print('\n------------ supported options ------------\n')
    for i in range(len(menu)):
        print('[%s] %s' % (i, menu[i][0]))
    print('\n-------------------------------------------\n')


# 选择并允许选项
def select_and_run_opt():
    opt = ''
    print_options()
    try:
        opt = input('Select option:')
        if (type(opt) == int or opt.isdigit()) and (int(opt) < len(menu) and int(opt) >= 0):
            menu[int(opt)][1]()
        else:
            util.info('Invalid input: %s. Please retype the number of intended option.' % opt)
    except KeyboardInterrupt as err:
        util.info('KeyboardInterrupt Exiting.')
        sys.exit(0)
    except Exception as err:
        util.info('Invalid input: %s. Please retype the number of intended option.' % opt)


if __name__ == '__main__':
    util.info(str(util.system_info))
    while True:
        select_and_run_opt()
