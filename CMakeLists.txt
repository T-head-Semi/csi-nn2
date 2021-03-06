cmake_minimum_required(VERSION 3.3)
project(CSI-NN2)

enable_language(ASM)

option(USE_CSI_NN2_DEBUG "option for debug" ON)

option(BUILD_X86 "build x86" OFF)
option(BUILD_RISCV "build riscv" OFF)
option(BUILD_RISCV_ELF "build riscv elf" OFF)
option(BUILD_CSKY "build csky" OFF)
option(BUILD_CSKY_ELF "build csky elf" OFF)

# riscv linux compiler
if (BUILD_RISCV)
    if(IS_DIRECTORY $ENV{RISCV_GNU_GCC_PATH})
        set(RISCV_GNU_GCC $ENV{RISCV_GNU_GCC_PATH})
    else()
        set(RISCV_GNU_GCC "${PROJECT_SOURCE_DIR}/tools/gcc-toolchain/bin")
    endif()

    set(CMAKE_C_COMPILER ${RISCV_GNU_GCC}/riscv64-unknown-linux-gnu-gcc)
    set(CMAKE_CXX_COMPILER ${RISCV_GNU_GCC}/riscv64-unknown-linux-gnu-g++)
endif()

# riscv elf compiler
if (BUILD_RISCV_ELF)
    set(CMAKE_C_COMPILER riscv64-unknown-elf-gcc)
endif()

# csky linux compiler
if (BUILD_CSKY)
    set(CMAKE_C_COMPILER csky-abiv2-linux-gcc)
    set(CMAKE_ASM_COMPILER csky-abiv2-linux-gcc)
endif()

# csky elf compiler
if (BUILD_CSKY_ELF)
    set(CMAKE_C_COMPILER csky-abiv2-elf-gcc)
    set(CMAKE_ASM_COMPILER csky-abiv2-elf-gcc)
endif()

# CSI-NN2 debug module
if(USE_CSI_NN2_DEBUG)
    add_definitions(-D CSI_DEBUG)
endif()

# reduce elf size
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ffunction-sections -fdata-sections -Wl,--gc-sections")

# set warning as error
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Werror")

file(GLOB_RECURSE NN2_SRCS source/nn2/*.c source/utils/*.c)
file(GLOB_RECURSE REF_SRCS source/reference/*.c)
file(GLOB_RECURSE GREF_SRCS source/graph_ref/*.c)
file(GLOB_RECURSE OPENVX_SRCS source/openvx/*.c)
file(GLOB_RECURSE C906_SRCS source/c906_opt/*.c)
file(GLOB_RECURSE C908_SRCS source/c908/*.c)
file(GLOB_RECURSE THEAD_RVV_SRCS source/thead_rvv/*.c)
file(GLOB_RECURSE C860_SRCS source/c860_opt/*.S)
file(GLOB_RECURSE I805_REF_SRCS source/i805_ref/*.c)
file(GLOB_RECURSE I805_SRCS source/i805_opt/*.c source/i805_opt/*.S)
file(GLOB_RECURSE E804_SRCS source/e804_opt/*.c source/e804_opt/*.S)

include_directories(include)

option(CSINN_LAYER_BENCHMARK "Layer information and performance" OFF)
if(CSINN_LAYER_BENCHMARK)
    add_definitions(-DCSINN_LAYER_BENCHMARK)
    message(STATUS "Print the execution time of each layer - ON")
endif()

set(CMAKE_INSTALL_PREFIX "${PROJECT_SOURCE_DIR}/install")

if(BUILD_X86)
    # build x86_ref so
    LIST(APPEND X86_LST ${NN2_SRCS} ${REF_SRCS} ${GREF_SRCS})
    add_library(x86_share SHARED ${X86_LST})
    SET_TARGET_PROPERTIES(x86_share PROPERTIES OUTPUT_NAME "csi_nn2_ref_x86")
    set(X86_BUILD_FLAGS -DCSI_AVX_OPT -DCSI_BUILD_REF -DCSI_BUILD_GREF -mavx -mfma -fopenmp)
    target_compile_options(x86_share PRIVATE ${X86_BUILD_FLAGS})

    install(TARGETS x86_share DESTINATION lib)

endif()

if(BUILD_RISCV)
    # build rvv a
    LIST(APPEND RVV_LST ${NN2_SRCS} ${REF_SRCS} ${GREF_SRCS} ${THEAD_RVV_SRCS})
    add_library(rvv_static STATIC ${RVV_LST})
    SET_TARGET_PROPERTIES(rvv_static PROPERTIES OUTPUT_NAME "csi_nn2_rvv")
    set(RVV_BUILD_FLAGS -march=rv64gcv0p7_zfh_xtheadc -mabi=lp64d -DCSI_BUILD_RVV -DCSI_BUILD_REF -DCSI_BUILD_GREF)
    target_compile_options(rvv_static PRIVATE ${RVV_BUILD_FLAGS})

    install(TARGETS rvv_static DESTINATION lib)

    # build c906 a
    LIST(APPEND C906_LST ${NN2_SRCS} ${REF_SRCS} ${GREF_SRCS} ${THEAD_RVV_SRCS} ${C906_SRCS})
    add_library(c906_static STATIC ${C906_LST})
    SET_TARGET_PROPERTIES(c906_static PROPERTIES OUTPUT_NAME "csi_nn2_c906")
    set(C906_BUILD_FLAGS -march=rv64gcv0p7_zfh_xtheadc -mabi=lp64d -DCSI_BUILD_C906 -DCSI_BUILD_REF -DCSI_BUILD_GREF)
    target_compile_options(c906_static PRIVATE ${C906_BUILD_FLAGS})

    install(TARGETS c906_static DESTINATION lib)

    add_library(c906_share SHARED ${C906_LST})
    SET_TARGET_PROPERTIES(c906_share PROPERTIES OUTPUT_NAME "csi_nn2_c906")
    target_compile_options(c906_share PRIVATE ${C906_BUILD_FLAGS})

    install(TARGETS c906_share DESTINATION lib)

endif()

if(BUILD_RISCV_ELF)
    # build c906 elf a
    LIST(APPEND C906_LST ${NN2_SRCS} ${REF_SRCS} ${GREF_SRCS} ${THEAD_RVV_SRCS} ${C906_SRCS})
    add_library(c906_elf_static STATIC ${C906_LST})
    SET_TARGET_PROPERTIES(c906_elf_static PROPERTIES OUTPUT_NAME "csi_nn2_c906_rtos")
    set(C906_BUILD_FLAGS -march=rv64gcv0p7_zfh_xtheadc -mabi=lp64d -DCSI_BUILD_C906 -DCSI_BUILD_REF -DCSI_BUILD_GREF -DCSI_BUILD_RTOS)
    target_compile_options(c906_elf_static PRIVATE ${C906_BUILD_FLAGS})

    install(TARGETS c906_elf_static DESTINATION lib)

    # build ASP elf a
    LIST(APPEND ASP_LST ${NN2_SRCS} ${REF_SRCS} ${GREF_SRCS} ${ASP_SRCS})
    add_library(asp_elf_static STATIC ${ASP_LST})
    SET_TARGET_PROPERTIES(asp_elf_static PROPERTIES OUTPUT_NAME "csi_nn2_asp")
    set(ASP_BUILD_FLAGS -march=rv32imafdcp -mabi=ilp32d -DCSI_BUILD_ASP -DCSI_BUILD_REF -DCSI_BUILD_GREF -DCSI_BUILD_RTOS)
    target_compile_options(asp_elf_static PRIVATE ${ASP_BUILD_FLAGS})

    install(TARGETS asp_elf_static DESTINATION lib)
endif()

if(BUILD_CSKY)
    # build openvx so
    LIST(APPEND OPENVX_LST ${NN2_SRCS} ${OPENVX_SRCS})
    add_library(openvx_share SHARED ${OPENVX_LST})
    SET_TARGET_PROPERTIES(openvx_share PROPERTIES OUTPUT_NAME "csi_nn2_openvx")
    set(OPENVX_BUILD_FLAGS -mcpu=c860v -fPIC -DCSI_BUILD_OPENVX -mhard-float)
    target_compile_options(openvx_share PRIVATE ${OPENVX_BUILD_FLAGS})
    set(OPENVX_LINK_DIR ${CMAKE_CURRENT_SOURCE_DIR}/module/acuity-driver/driver/build/sdk/drivers)
    target_link_libraries(openvx_share PRIVATE -mcpu=c860v -fPIC -mhard-float -L${OPENVX_LINK_DIR} -lArchModelSw -lNNArchPerf -lOpenVX -lOpenVXU -lCLC -lVSC -lGAL -lNNGPUBinary -lovxlib -lOvx12VXCBinary)
    target_include_directories(openvx_share PRIVATE module/acuity-driver/lib/acuity-ovxlib-dev/include/)
    target_include_directories(openvx_share PRIVATE module/acuity-driver/driver/build/sdk/include/)

    install(TARGETS openvx_share DESTINATION lib)

    # build c860 a
    LIST(APPEND C860_LST ${NN2_SRCS} ${REF_SRCS} ${C860_SRCS})
    add_library(c860_static STATIC ${C860_LST})
    SET_TARGET_PROPERTIES(c860_static PROPERTIES OUTPUT_NAME "csi_nn2_c860")
    set(C860_BUILD_FLAGS -mcpu=c860v -DCSI_BUILD_REF)
    target_compile_options(c860_static PRIVATE ${C860_BUILD_FLAGS})

    install(TARGETS c860_static DESTINATION lib)
endif()

if(BUILD_CSKY_ELF)
    # build i805 ref a
    LIST(APPEND I805_REF_LST ${NN2_SRCS} ${REF_SRCS} ${I805_REF_SRCS})
    add_library(i805_ref_static STATIC ${I805_REF_LST})
    SET_TARGET_PROPERTIES(i805_ref_static PROPERTIES OUTPUT_NAME "csi_nn2_ref_i805")
    set(I805_REF_BUILD_FLAGS -DCSI_BUILD_REF_I805 -DCSI_MATH_DSP -DCSI_BUILD_RTOS -mcpu=i805)
    target_compile_options(i805_ref_static PRIVATE ${I805_REF_BUILD_FLAGS})
    target_include_directories(i805_ref_static PRIVATE include/include_xt800)

    install(TARGETS i805_ref_static DESTINATION lib)

    # build i805 a
    LIST(APPEND I805_LST ${NN2_SRCS} ${REF_SRCS} ${I805_SRCS})
    add_library(i805_static STATIC ${I805_LST})
    SET_TARGET_PROPERTIES(i805_static PROPERTIES OUTPUT_NAME "csi_nn2_i805")
    set(I805_BUILD_FLAGS -DCSI_BUILD_I805 -DCSI_MATH_DSP -DCSI_BUILD_RTOS -mcpu=ck805ef -mhard-float)
    target_compile_options(i805_static PRIVATE ${I805_BUILD_FLAGS})
    target_include_directories(i805_static PRIVATE include/include_xt800)

    install(TARGETS i805_static DESTINATION lib)

    # build e804 a
    LIST(APPEND E804_LST ${NN2_SRCS} ${REF_SRCS} ${E804_SRCS})
    add_library(e804_static STATIC ${E804_LST})
    SET_TARGET_PROPERTIES(e804_static PROPERTIES OUTPUT_NAME "csi_nn2_e804")
    set(E804_BUILD_FLAGS -DCSI_BUILD_E804 -mcpu=e804d -DCSI_BUILD_RTOS -mno-required-attr-fpu-abi)
    target_compile_options(e804_static PRIVATE ${E804_BUILD_FLAGS})
    target_include_directories(e804_static PRIVATE include/include_xt800)

    install(TARGETS e804_static DESTINATION lib)
endif()

install(DIRECTORY "include/." DESTINATION "include" FILES_MATCHING PATTERN "*.h")
