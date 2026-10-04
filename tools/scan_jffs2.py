import struct, sys
d = open(sys.argv[1], 'rb').read()
jeb = int(sys.argv[2])            # erase size of the flash, e.g. 32768
nodes = []
for base in range(0, len(d), jeb):
    off, end = base, base + jeb
    while off + 12 <= end:
        magic, t, l = struct.unpack_from('<HHI', d, off)
        if magic != 0x1985:
            break
        nodes.append((off, t, l))
        off += (l + 3) & ~3
cross = [o for o, t, l in nodes if o // jeb != (o + l - 1) // jeb]
print(len(nodes), "nodes,", len(cross), "cross a", jeb, "byte boundary")
