#!/usr/bin/python

import sys
import re
import difflib


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CRIMSON = '\033[31m'
    GRASS = '\033[32m'


def color_diff(diff):
    for line in diff:
        if line.startswith('+'):
            yield bcolors.GRASS + line + bcolors.ENDC
        elif line.startswith('-'):
            yield bcolors.CRIMSON + line + bcolors.ENDC
        else:
            yield line


def print_config(config):
    print generate_config(config)


def generate_config(config):
    msg = config["comment"]
    msg += "\n"
    msg += "# %s = %s" % (config["key"], config["value"])
    msg += "\n"
    return msg


def parsing(filename):
    currentsection = ""
    currentlibraryname = ""

    config = {}
    msg = ""
    msgs = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if line == "\n":
            if msg is not "":
                msgs.append(msg)
            msg = ""
            continue
        msg += line

    for m in msgs:
        # is it section name?
        if re.findall(r"^\[(.+)\]", m):
            currentsection = re.findall(r"^\[(.+)\]\n", m)[0]
            config[currentsection] = {}
        elif re.findall(r"^#\n# From (.+)\n#\n$", m):
            currentlibraryname = re.findall(r"^#\n# From (.+)\n#\n$", m)[0]
        else:
            split_msgs = m.split("\n")
            comments = "\n".join(split_msgs[0:-2])
            parsed_key = re.findall(r"^#(.+?) =", split_msgs[-2])[0]
            parsed_values = re.findall(r"^#.+?= (.+?)$", split_msgs[-2])
            if not parsed_values:
                parsed_value = ""
            else:
                parsed_value = parsed_values[0]
            con = {"section": currentsection,
                   "library": currentlibraryname,
                   "comment": comments,
                   "key": parsed_key,
                   "value": parsed_value}
            config[currentsection][parsed_key] = con

    return config


def main():
    argv = sys.argv[1:]
    old = parsing(argv[0])
    new = parsing(argv[1])

    deleted_sections = sorted(set(old.keys()) - set(new.keys()))
    appended_sections = sorted(set(new.keys()) - set(old.keys()))
    same_sections = sorted(set(new.keys()) & set(old.keys()))

    print "%s----Deleted sections:----%s" % (bcolors.OKGREEN, bcolors.ENDC)
    for s in deleted_sections:
        for k, v in old[s].iteritems():
            # exist items
            print
            print "[%s]" % s
            print
            break
        for k, v in old[s].iteritems():
            print_config(v)
    print "%s-------------------------%s" % (bcolors.OKGREEN, bcolors.ENDC)
    print

    print "%s----Deleted items:----%s" % (bcolors.OKGREEN, bcolors.ENDC)
    for s in same_sections:
        deleted_items = sorted(set(old[s].keys()) - set(new[s].keys()))
        if deleted_items:
            # exist items
            print
            print "[%s]" % s
            print
            for d in deleted_items:
                print_config(old[s][d])
    print "%s-------------------------%s" % (bcolors.OKGREEN, bcolors.ENDC)
    print

    print "%s----Appended sections:----%s" % (bcolors.OKGREEN, bcolors.ENDC)
    for s in appended_sections:
        for k, v in new[s].iteritems():
            # exist items
            print
            print "[%s]" % s
            print
            break
        for k, v in new[s].iteritems():
            print_config(v)
    print "%s-------------------------%s" % (bcolors.OKGREEN, bcolors.ENDC)
    print

    print "%s----Appended items:----%s" % (bcolors.OKGREEN, bcolors.ENDC)
    for s in same_sections:
        appended_items = sorted(set(new[s].keys()) - set(old[s].keys()))
        if appended_items:
            # exist items
            print
            print "[%s]" % s
            print
            for a in appended_items:
                print_config(new[s][a])
    print "%s-------------------------%s" % (bcolors.OKGREEN, bcolors.ENDC)
    print

    print "%s----Changed default value:----%s" % (bcolors.OKGREEN, bcolors.ENDC)
    delay_msg = ""
    for s in same_sections:
        firstprint = True
        same_items = sorted(set(new[s].keys()) & set(old[s].keys()))
        if same_items:
            for si in same_items:
                if old[s][si]["value"] != new[s][si]["value"]:
                    if firstprint:
                        print
                        print "[%s]" % s
                        print
                        firstprint = False
                    print "%s%s* %s%s" % (bcolors.BOLD, bcolors.OKBLUE, old[s][si]["key"], bcolors.ENDC)
                    a = generate_config(old[s][si])
                    b = generate_config(new[s][si])
                    diff = difflib.ndiff(a.splitlines(1), b.splitlines(1))
                    diff = color_diff(diff)
                    print ''.join(list(diff))
                    continue

                if old[s][si]["comment"] != new[s][si]["comment"]:
                    if firstprint:
                        delay_msg += "\n"
                        delay_msg += "[%s]\n" % s
                        delay_msg += "\n"
                        firstprint = False
                    delay_msg += "%s%s* %s%s\n" % (bcolors.BOLD, bcolors.OKBLUE, old[s][si]["key"], bcolors.ENDC)
                    a = generate_config(old[s][si])
                    b = generate_config(new[s][si])
                    diff = difflib.ndiff(a.splitlines(1), b.splitlines(1))
                    diff = color_diff(diff)
                    delay_msg += ''.join(list(diff))
                    delay_msg += "\n"
    print "%s-------------------------%s" % (bcolors.OKGREEN, bcolors.ENDC)
    print

    print "%s----Changed comment:----%s" % (bcolors.OKGREEN, bcolors.ENDC)
    print delay_msg
    print "%s-------------------------%s" % (bcolors.OKGREEN, bcolors.ENDC)
    print

if __name__ == "__main__":
    sys.exit(main())
