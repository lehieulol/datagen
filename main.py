import generator
import parameter

'''
def two_element_list(string):
    """
    Custom type for argparse that takes a comma-separated string and returns
    a list with two elements.
    """
    elements = string.split(',')
    if len(elements) != 2:
        raise argparse.ArgumentTypeError("List must have exactly 2 elements")
    return [int(elements[0]), int(elements[1])]


parser = argparse.ArgumentParser(description='Model input')
parser.add_argument('--N', metavar='N', type=int, dest="num_target",
                    help='number of targets')
parser.add_argument('--qm', metavar='q_max', type=int, dest="q_max",
                    help='maximum q of all the targets', default=5)
parser.add_argument('--rs', metavar='r_s', type=float, dest="r_s",
                    help='sensing radius', default=40)
parser.add_argument('--rc', metavar='r_c', type=float, dest="r_c",
                    help='communication radius', default=80)
parser.add_argument('--rcl', metavar='r_cl', type=float, dest="r_cl",
                    help='cluster radius', default=80)
parser.add_argument('--ra', metavar='rand_q', type=bool, dest="rand_q",
                    help='random q or not', default=True)
parser.add_argument('--a', metavar='area', type=float, dest="area",
                    help='area width (=height)', default=1000)
parser.add_argument('--b', metavar='base', type=two_element_list, dest="base",
                    help='base station location', default=[0, 0])

args = parser.parse_args()
# arg_dict = vars(args)
# for key, value in arg_dict.items():
#     print(key, value)
'''

if __name__ == '__main__':
    for num_target in parameter.num_target:
        _generator = generator.Generator(num_target, parameter.q_max, parameter.r_s, parameter.r_c, parameter.r_cl,
                              parameter.area, parameter.rand_q, parameter.base)

        _generator.generate(f'.\\Output\\test_{num_target}.yaml')
