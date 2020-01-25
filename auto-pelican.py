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
    print_options()
    try:
        opt = input('Select option [%s]:' % util.DEFAULT_OPTION)
        if not opt:
            menu[util.DEFAULT_OPTION][1]()
        elif (type(opt) == int or opt.isdigit()) and (int(opt) < len(menu) and int(opt) >= 0):
            menu[int(opt)][1]()
        else:
            util.info('Invalid input. Please retype the number of intended option.')
            select_and_run_opt()
    except SyntaxError as err:
        util.info('Invalid input. Please retype the number of intended option.')
        select_and_run_opt()


if __name__ == '__main__':
    util.info(str(util.system_info))
    select_and_run_opt()
