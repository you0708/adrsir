#!/usr/bin/python3

import adrsir
import os, sys, time
import argparse
import fcntl

BASE_DIR = os.path.dirname(__file__)
IR_DATA_DIR = os.path.join(BASE_DIR, "ir_data/")
LOCK_FILE = os.path.join(BASE_DIR, 'ir_control.lock')

def save_all(args):
    out_dir = IR_DATA_DIR + args.DIR
    print('[*] save stored IR data into {}'.format(out_dir))
    if os.path.isdir(out_dir) == False:
        os.makedirs(out_dir)
    for i in range(10):
        data = adrsir.read(i)
        if data:
            out_file = out_dir + '/ch{}.data'.format(i)
            fp = open(out_file, 'w')
            fp.write(data)
            fp.close()
            print('[*] saved {}'.format(out_file))
        time.sleep(1)

def restore_all(args):
    in_dir = IR_DATA_DIR + args.DIR
    print('[*] restore IR data from {}'.format(in_dir))
    if os.path.isdir(in_dir) == False:
        print('[!] {} does not exist'.format(in_dir))

    data = []
    for i in range(10):
        in_file = in_dir + '/ch{}.data'.format(i)
        if os.path.isfile(in_file) == False:
            continue
        with open(in_file, 'r') as fp:
            print('[*] writing {} into ch{}'.format(in_file, i))
            adrsir.write(i, fp.read())
            time.sleep(1)

    print('[*] restored')

def send_data(args):
    ifp = open(LOCK_FILE, 'r')
    fcntl.flock(ifp.fileno(), fcntl.LOCK_EX)

    filepath = IR_DATA_DIR + args.FILE
    print('[*] send {}'.format(filepath))
    if not os.path.isfile(filepath):
        print('[!] {} does not exist'.format(filepath))
        return

    with open(filepath, 'r') as fp:
        data = fp.read()
    adrsir.trans(data)

    time.sleep(0.5)
    fcntl.flock(ifp.fileno(), fcntl.LOCK_UN)
    ifp.close()

def main():
    parser = argparse.ArgumentParser(description='IR controller using ADRSIR')
    subparsers = parser.add_subparsers(help='You need to specify sub-command')
    parser_save = subparsers.add_parser('save', help='Save stored IR data as .data files')
    parser_save.add_argument('DIR', action='store', help='Output directory')
    parser_save.set_defaults(handler=save_all)
    parser_save = subparsers.add_parser('restore', help='Restore IR data to the memory')
    parser_save.add_argument('DIR', action='store', help='Input directory')
    parser_save.set_defaults(handler=restore_all)
    parser_send = subparsers.add_parser('send', help='Send specified IR data')
    parser_send.add_argument('FILE', action='store', help='Filename to send')
    parser_send.set_defaults(handler=send_data)

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()
    return

if __name__ == '__main__':
    main()
