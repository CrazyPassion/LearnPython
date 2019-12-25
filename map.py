# from project.utils import const
# https://michaelyou.github.io/2015/06/13/python中定义常量/
# https://juejin.im/entry/590804c844d9040069360941
global_map = [0, 2, 4, 6, 1, 3, 5, 7]
local2cell_rp3_rruportorder = [0, 1, 2, 3, 4, 5, 6, 7]
cellsetup_rruportorder_antennaid = [0, 1, 2, 3, 4, 5, 6, 7]

antenna_carrier = 1

tx_timedomain_data_index = global_map[
    cellsetup_rruportorder_antennaid[antenna_carrier]]
ref = []
for i in cellsetup_rruportorder_antennaid:
    ref.insert(global_map[i], i)

# dspantindex
tmpdspantindex = [0, 1, 2, 3, 4, 5, 6, 7]
rp3channelIdx = tmpdspantindex
realIdex = local2cell_rp3_rruportorder
dspantindex = realIdex

antoffset = []
for i in tmpdspantindex:
    antoffset.append(local2cell_rp3_rruportorder.index(ref[i]))
rruport = antoffset
print(rp3channelIdx)
print(dspantindex)
print(rruport)
print(tx_timedomain_data_index)
print(rruport[tx_timedomain_data_index])