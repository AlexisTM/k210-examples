#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import subprocess
import sys
from kflash import KFlash

def main():
  parser = argparse.ArgumentParser(
                    prog = 'run.py',
                    description = 'Make a binary out of the app and flash it to the board.')
  parser.add_argument('-r', '--ram', action='store_true', help = "Flash the firmware to the ram.")
  parser.add_argument('-t', '--terminal', action='store_true', help = "Open a terminal after successful flash.")
  parser.add_argument('elffile', help = "The elf file generated with rust")
  args = parser.parse_args()
  binary_path = args.elffile
  firmware_path = binary_path + ".bin"
  objcopy_cmd = f"riscv64-unknown-elf-objcopy -O binary {binary_path} {firmware_path}"
  print(f"Creating the firmware with: {objcopy_cmd}")
  objcopy_cmd = objcopy_cmd.split(" ")
  process = subprocess.run(objcopy_cmd, check=True)
  print(f"Firmware written at: {firmware_path}")

  options = ""
  if args.ram:
    options += "--sram"
  if args.terminal:
    options += "--terminal"

  flash_cmd = f"python kflash.py --verbose {options} {firmware_path}"
  print(f"Flashing the board with: {flash_cmd}")
  flash_cmd.split(" ")
  process = subprocess.run(flash_cmd, check=True)

if __name__ == "__main__":
  main()
