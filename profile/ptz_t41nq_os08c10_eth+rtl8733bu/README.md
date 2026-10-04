# T41NQ + OS08C10 PTZ camera: profile draft

Based on `configs/cameras-exp/zintronic_ikpw530tv1_t41nq_gc5603_eth+rtl8733bu`.
Only hardware that is needed for boot and Wi-Fi is in the defconfig / thingino.json.

## Hardware seen on the board (from my integration scripts, not measured on the PCB)
| Function | GPIO | Notes |
|---|---|---|
| Wi-Fi enable (RTL8733BU) | 61 | active low, in thingino.json as `gpio.wlan` |
| White LED | 81 | active low, key name in thingino.json to be confirmed |
| IR-cut | 49 / 50 | 100 ms pulse; which pin is "day" to be confirmed |
| IR LEDs (12) | - | switched by the IR board's own light sensor, no software control |
| Pan/tilt motor | - | vendor `motor.ko`, module parameters `pan_all=1020 titl_all=240 titl_init=0 spd_self=600 spd_pan=1 spd_titl=1 spd_all=800` |

## Not included
The vendor `motor.ko` (stock module, GPL metadata, no source available to me) and
all other OEM files. The OS08C10 sensor driver and IQ file come from ingenic-sdk unchanged.

## Not tested
This defconfig is derived by hand from my working local profile and has not been
built as is; the local profile also contains Raptor and PTZ settings that are not
part of this draft.
