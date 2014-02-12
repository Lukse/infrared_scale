import ir_scale_utils

lines = ir_scale_utils.get_data('data/4-94,7kg.txt')
#lines = ir_scale_utils.get_data_serial('COM43')

weight = ir_scale_utils.get_real_weight(lines)
print 'Your weight is: %3.1f kg' % weight
