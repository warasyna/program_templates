#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
u"""
Explanation of this program
"""
import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser(description='Description of this program')
    parser.add_argument("-i",
                        default=None,
                        dest="input_file",
                        metavar="input_file",
                        required=True,
                        type=str,
                        help="Input file")
    parser.add_argument("-r",
                        default=None,
                        dest="rep",
                        metavar="replace_word",
                        required=False,
                        type=str,
                        help="A word with which the pattern text is replaced")
    parser.add_argument("-o",
                        default=None,
                        dest="output_file",
                        metavar="output_file",
                        required=True,
                        type=str,
                        help="Output file")
    return parser.parse_args()


def extract_and_replace(line, pattern, rep):
    res = None
    r = re.search(pattern, line)
    if r:
        extraction = r.group(1)
        print("Extract: {0}".format(extraction))
        if rep is not None:
            res = re.sub(extraction, rep, line)
    return res


def sample_func(input_file, rep, output_file):
    pattern = "hoge\s*(\S+)\s*hoge"
    output = list()
    with open(input_file) as f:
        for l in f.readlines():
            l = l.strip()
            r = extract_and_replace(l, pattern, rep)
            if r is not None:
                output.append(r)

    with open(output_file, mode='w') as f:
        for l in output:
            f.write(l + "\n")


def main():
    args = parse_args()
    sample_func(args.input_file, args.rep, args.output_file)


if __name__ == '__main__':
    main()
