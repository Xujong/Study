# 17.4 pdb调试
import pdb


def mean(nums):
    top = sum(nums)
    bot = len(nums)
    return float(top) / float(bot)


pdb.set_trace()  # 跟踪点设置在程序起始点(17.4.1)
a_list = [1, 2, 3, 4, 5, 6, 10, "one hundred"]  # 输入a_list
# a_list的值错误：求和函数不能处理字符串值“one hundred”
mean(a_list)
