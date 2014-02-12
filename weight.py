import ir_scale_utils

lines = ir_scale_utils.get_data_serial('COM43')

packets = ir_scale_utils.preprocess(lines)
weight = ir_scale_utils.get_real_weight(packets)
print 'Your weight is: %3.1f kg' % weight

