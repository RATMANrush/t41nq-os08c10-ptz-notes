# T41NQ + OS08C10 PTZ camera: patches and notes

Base revisions the patches were made against:
- thingino-firmware: d796c1381 (master)
- raptor: 334919328b6efaae21150e46b923248c9732919f
- raptor-hal: 8897102d5f893a5d09b3fa8c96528a8b1dab928d
- ingenic-sdk: d30c0af67b224e5ac1fd241968fb09ef0ad75e9f

Layout:
- `patches/thingino-firmware/` JFFS2 erase block size (illustrative: the real fix should take the value from the flash definition)
- `patches/ingenic-sdk/` T41NQ ORAM window in soc-nna
- `patches/raptor-hal/` T41 PersonDet interface (0001), T41 flip on the sensor only (0002)
- `patches/raptor/` T41 PersonDet result parser, PTZ tracking, tilt tuning, white light (0001-0011, apply in order)
- `profile/` camera profile draft for `configs/cameras-exp/`
- `tools/scan_jffs2.py` shows how many JFFS2 nodes cross an erase block boundary

Apply a patch from the root of the matching source tree: `patch -p1 < file.patch`.

Not included: OEM binaries (person-detection model and library, vendor motor.ko), firmware images, credentials.
