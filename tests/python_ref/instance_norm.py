import struct
from torch import tensor
from torch.nn import functional as fn
import numpy as np


def instance_norm_f32():
    para = []
    # init the input data and parameters
    batch = int(np.random.randint(1, high=4, size=1))
    in_size_x = int(np.random.randint(32, high=64, size=1))
    in_size_y = int(np.random.randint(32, high=64, size=1))
    in_channel = int(np.random.randint(1, high=32, size=1))
    zero_point1 = int(np.random.randint(-6, high=6, size=1))
    std1 = int(np.random.randint(1, high=20, size=1))
    zero_point2 = int(np.random.randint(-6, high=6, size=1))
    std2 = int(np.random.randint(1, high=20, size=1))
    zero_point3 = int(np.random.randint(-6, high=6, size=1))
    std3 = int(np.random.randint(1, high=20, size=1))

    size_all = batch * in_channel * in_size_y * in_size_x

    src_in1 = np.random.normal(
        zero_point1, std1, (batch, in_channel, in_size_y, in_size_x)
    )
    src_in1 = src_in1.astype(np.float32)

    src_in2 = np.random.normal(zero_point2, std2, (in_channel))
    src_in2 = src_in2.astype(np.float32)

    src_in3 = np.random.normal(zero_point3, std3, (in_channel))
    src_in3 = src_in3.astype(np.float32)

    src_out = fn.instance_norm(
        tensor(src_in1), weight=tensor(src_in2), bias=tensor(src_in3)
    ).numpy()

    src_in_1 = src_in1.reshape(-1)
    src_in_2 = src_in2.reshape(-1)
    src_in_3 = src_in3.reshape(-1)

    src_out_1 = src_out.reshape(size_all)

    total_size = (len(src_in_1) + len(src_in_2) + len(src_in_3) + len(src_out_1)) + 5

    para.append(total_size)
    para.append(batch)
    para.append(in_size_y)
    para.append(in_size_x)
    para.append(in_channel)

    with open("instance_norm_data_f32.bin", "wb") as fp:
        data = struct.pack(("%di" % len(para)), *para)
        fp.write(data)
        data = struct.pack(("%df" % len(src_in_1)), *src_in_1)
        fp.write(data)
        data = struct.pack(("%df" % len(src_in_2)), *src_in_2)
        fp.write(data)
        data = struct.pack(("%df" % len(src_in_3)), *src_in_3)
        fp.write(data)
        data = struct.pack(("%df" % len(src_out_1)), *src_out_1)
        fp.write(data)
        fp.close()

    return 0


if __name__ == "__main__":
    instance_norm_f32()
    print("end")
