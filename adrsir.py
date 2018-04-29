#!/usr/bin/python3

import smbus

SLAVE_ADDR = 0x52
R1_WRITE_MEM_NUM  = 0x15 # bus-write(ADR,cmd,1)
R2_READ_DATA_LEN  = 0x25 # bus-read(ADR,cmd,3)
R3_READ_DATA      = 0x35 # bus-read(ADR,cmd,n)
W1_WRITE_MEM_NUM  = 0x19 # bus-write(ADR,cmd,1)
W2_WRITE_DATA_LEN = 0x29 # bus-write(ADR,cmd,3)
W3_WRITE_DATA     = 0x39 # bus-read(ADR,cmd,n)
W4_FLASH          = 0x49 # bus-read(ADR,cmd,n)
T1_START_TRANS    = 0x59 # bus-write(ADR,cmd,1)

bus = smbus.SMBus(1)

def read(num):
    bus.write_i2c_block_data(SLAVE_ADDR, R1_WRITE_MEM_NUM, [num])

    data = bus.read_i2c_block_data(SLAVE_ADDR, R2_READ_DATA_LEN, 3)
    block_len = (data[1]<<8) + data[2]
    if block_len == 0xFFFF:
        return None

    ir_data = []
    bus.read_i2c_block_data(SLAVE_ADDR, R3_READ_DATA, 1)
    for i in range(block_len):
        data = bus.read_i2c_block_data(SLAVE_ADDR, R3_READ_DATA, 4)
        ir_data += data

    ir_str_data = ''.join(map(lambda x:'{:02X}'.format(x), ir_data))
    return ir_str_data

def write(num, ir_str_data):
    ir_data = [int(ir_str_data[i:i+2],16) for i in range(0,len(ir_str_data),2)]
    bus.write_i2c_block_data(SLAVE_ADDR, W1_WRITE_MEM_NUM, [num])

    block_len = len(ir_data)//4
    bus.write_i2c_block_data(SLAVE_ADDR, W2_WRITE_DATA_LEN, [block_len>>8, block_len&0xFF])
    for i in range(block_len):
        bus.write_i2c_block_data(SLAVE_ADDR, W3_WRITE_DATA, ir_data[i*4:i*4+4])

    bus.write_i2c_block_data(SLAVE_ADDR, W4_FLASH, [num])

def trans(ir_str_data):
    ir_data = [int(ir_str_data[i:i+2],16) for i in range(0,len(ir_str_data),2)]

    block_len = len(ir_data)//4
    bus.write_i2c_block_data(SLAVE_ADDR, W2_WRITE_DATA_LEN, [block_len>>8, block_len&0xFF])
    for i in range(block_len):
        bus.write_i2c_block_data(SLAVE_ADDR, W3_WRITE_DATA, ir_data[i*4:i*4+4])

    bus.write_i2c_block_data(SLAVE_ADDR, T1_START_TRANS, [0])
