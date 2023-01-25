K210 Examples
=============

This is a personal repo to experience embedded Rust, with the RISC-V k210.

Quickstart
-------

```bash
cargo run # Builds, create the binary & flashes it
```

Running openocd
--------

Use Zadig to convert the driver to WinUSB:

```bash
openocd -f interface/ftdi/dp_busblaster.cfg -f openocd.cfg
```

On Windows:
-----------

Use "Zadig" to convert the driver to WinUSB: http://zadig.akeo.ie

Another OpenOCD version (0.11.0): https://xpack.github.io/openocd/
Zadig is available under "Windows Tools" in the release tab.

k210 doc for openocd (0.2.3): https://github.com/kendryte/openocd-kendryte/wiki
