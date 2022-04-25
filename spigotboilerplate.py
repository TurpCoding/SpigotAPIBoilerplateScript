# Simple script to generate boilerplate code for your SpigotAPI projects.
# Currently generating boilerplate code for SpigotAPI apiversions: 1.18.2-R0.1-SNAPSHOT through x.x.x
# Version 1.0
# GitHub page:

import os.path
from argparse import ArgumentParser

parser = ArgumentParser(usage="spigotBoilerplate.py -v [--version] [API version] [optional arguments]\n\nAPI versions:"
                              "\n\n1.18.2-R0.1-SNAPSHOT \n\nfor more help type: spigotboilerplate.py -h\n\nDon't forget "
                              "to wrap the path argument in quotation marks if it contains whitespace.")

parser.add_argument('-v', '--version', help="Version of the spigot API for the boilerplate code."
                                            " (Default: 1.18.2-R0.1-SNAPSHOT)", nargs='?',
                                                default="1.18.2-R0.1-SNAPSHOT", const="1.18.2-R0.1-SNAPSHOT")

parser.add_argument('-p', '--path', help="The path where the boilerplate code files will be generated."
                                         " (Default: current directory).", nargs='?', default="./", const="./")
args = parser.parse_args()

# Generate the Main class boilerplate code.
with open(os.path.join(args.path, "Main.java"), "x") as mainWrite:
    with open("apiversions/" + args.version + "/Main.txt") as mainRead:
        for line in mainRead:
            mainWrite.write(line)

# Generate the CommandExecutor boilerplate code.
with open(os.path.join(args.path, "Command.java"), "x") as commandWrite:
    with open("apiversions/" + args.version + "/Command.txt") as commandRead:
        for line in commandRead:
            commandWrite.write(line)

# Generate the plugin.yml boilerplate code.
with open(os.path.join(args.path, "plugin.yml"), "x") as pluginymlWrite:
    with open("apiversions/" + args.version + "/Pluginyml.txt") as pluginymlRead:
        for line in pluginymlRead:
            pluginymlWrite.write(line)

print("Done.")