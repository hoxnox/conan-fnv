cmake_minimum_required(VERSION 2.8)
add_library(fnv
    ./fnv32.c  
    ./fnv64.c  
    ./hash_32a.c  
    ./hash_32.c  
    ./hash_64a.c  
    ./hash_64.c  
    ./have_ulong64.c
    ./test_fnv.c)
install(TARGETS fnv DESTINATION lib)
install(FILES "fnv.h" DESTINATION include)
install(FILES "longlong.h" DESTINATION include)
