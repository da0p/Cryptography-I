def xOR(ba1: bytes, ba2: bytes):
    if len(ba1) != len(ba2):
        print("Len is not equal!")
        return None

    return bytes([a ^ b for a, b in zip(ba1, ba2)])

def pad(pt: str, limit: int) -> str:
    if len(pt) >= limit:
        print("No padding needed!")
        return pt
    
    padding = limit - len(pt)

    return pt + str(padding) * padding


def main():
    pt1 = "Pay Bob 100$"
    pt2 = "Pay Bob 500$"
    iv1 = bytes.fromhex("20814804c1767293b99f1d9cab3bc3e7")
    cp1 = bytes.fromhex("ac1e37bfb15599e5f40eef805488281d")

    pt1_padded = pad(pt1, len(cp1))
    pt2_padded = pad(pt2, len(cp1))

    xor_output = xOR(pt1_padded.encode("utf-8") , pt2_padded.encode("utf-8"))

    iv2 = xOR(iv1, xor_output)

    print("{} {}".format(iv2.hex(), cp1.hex()))

if __name__ == "__main__":
    main()