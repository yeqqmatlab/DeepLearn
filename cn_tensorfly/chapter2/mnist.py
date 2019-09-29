# -*- coding:utf-8 -*-

import gzip
import sys
import struct

train_images = "/Users/yqq/Downloads/mnist_data/train-images-idx3-ubyte.gz"
train_labels = "/Users/yqq/Downloads/mnist_data/train-labels-idx1-ubyte.gz"
t10k_images = "/Users/yqq/Downloads/mnist_data/t10k-images-idx3-ubyte.gz"
t10k_labels = "/Users/yqq/Downloads/mnist_data/t10k-labels-idx1-ubyte.gz"


def read_labels(filename):

    labels = []

    with gzip.open(filename) as bytestream:
        index = 0
        buf = bytestream.read()
        bytestream.close()
        # 根据MINIST文件的描述，文件开始是用于校验的数字，`integer`格式，占用4个字节，位于0-4位置
        # 第二个描述文件的内容数量，`integer`格式，占用4个字节，位置4-8位置
        magic, numberOfLabels = struct.unpack_from('>II', buf, index)
        print(magic)
        print(numberOfLabels)
        # index += struct.calcsize('>II') #这里的结果是 +=8，为了直观，就直接填写8
        # 因为magic, numberOfLabels 占据前面8个字节，所以把下标移动到第 8 位，开始读取数字标签的内容
        index = 8
        while index < numberOfLabels:
            # 根据MINIST文件的描述，labels的数字是`unsigned byte`格式，占用一个字节，所以这里填写`B`
            num = int(struct.unpack_from('B', buf, index)[0])
            labels.append(num)
            # index += struct.calcsize('B')
            # 移动到下一个光标
            index += 1
    return labels


def read_images(filename, labels):

    # 把文件解压成字节流
    with gzip.open(filename) as bytestream:
        index = 0
        buf = bytestream.read()
        bytestream.close()
        # 根据MINIST文件的描述，文件开始是用于校验的数字，`integer`格式，占用4个字节，位于0-4位置
        # 第二个描述文件的内容数量，`integer`格式，占用4个字节，位置4-8位置
        magic, numberOfImages, rows, columns = struct.unpack_from('>IIII', buf, index)

        print(magic)
        print(numberOfImages)
        print(rows)
        print(columns)

        # index += struct.calcsize('>IIII') #这里的结果是 +=16，为了直观，就直接填写16
        # 因为magic, numberOfImages, rows, columns 占据前面16个字节，所以把下标移动到第 16 位，开始读取数字标签的内容
        index = 16

        for i in xrange(numberOfImages):
            # for i in xrange(5):
            # 打印对应的数字标签
            print(labels[i])
            for x in xrange(rows):
                for y in xrange(columns):
                    num = int(struct.unpack_from('B', buf, index)[0])
                    if num > 100:
                        sys.stdout.write(str(num) + " ")
                    elif num > 50:
                            sys.stdout.write(str(num) + "  ")
                    else:
                        sys.stdout.write(str('0   '))
            index += 1
        sys.stdout.write(str('\n'))
        sys.stdout.write(str('\n'))
        sys.stdout.flush()
    return


# 解析labels的内容，train_labels包含了60000个数字标签，返回60000个数字标签的数组
labels = read_labels(train_labels)
print(labels)
read_images(train_images, labels)
