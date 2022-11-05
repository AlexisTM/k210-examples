#![allow(warnings)]
#![no_std]
#![no_main]

extern crate panic_halt;

use k210_hal::stdout;
use riscv_rt::entry;
use k210_hal::prelude::*;
use k210_hal::pac as pac;
use k210_hal::stdout::Stdout;

#[entry]
fn main() -> ! {
    let p = pac::Peripherals::take().unwrap();

    // Configure clocks (TODO)
    let clocks = k210_hal::clock::Clocks::new();

    let serial = p.UARTHS.configure(115_200.bps(), &clocks);
    let (mut tx, rx) = serial.split();
    let mut stdout = Stdout(&mut tx);

    // Configure UART
    // let serial = p.UARTHS.constrain(115_200.bps(), &clocks);
    // let (mut tx, _) = serial.split();

    // let mut stdout = Stdout(&mut tx);

    // writeln!(stdout, "Hello, Rust!").unwrap();

    loop {
        writeln!(stdout, "Hello again!").unwrap();
    }
}
