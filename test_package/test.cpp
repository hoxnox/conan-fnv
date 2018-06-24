extern "C" {
#include <fnv.h>
}
#include <iostream>

int main(int argc, char *argv[])
{
    unsigned char data[] = {
        0xfe, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf9, 0x89, 0x48, 0xa3, 0xed, 0x97, 0xfd, 0xd3,
        0xfe, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x1e, 0x58, 0xff, 0xfe, 0xf4, 0xe7, 0x24,
        0xca, 0xd8,
        0x00, 0x19
    };

    std::cout << fnv_64a_buf(data, sizeof(data), (Fnv64_t)FNV1A_64_INIT) << std::endl;
    return 0;
}
