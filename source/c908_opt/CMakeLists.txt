
if(CONFIG_C908_SOURCE)
    list(APPEND C908_SRCS source/c908_opt/reorder.c)
    list(APPEND C908_SRCS source/c908_opt/setup.c)
    list(APPEND C908_SRCS source/c908_opt/shl_c908_f32_to_i8.S)
    list(APPEND C908_SRCS source/c908_opt/shl_c908_f32_to_u8.S)
endif()

if(CONFIG_C908_AVERAGEPOOL_FP32)
    list(APPEND C908_SRCS source/c908_opt/fp32/avgpool.c)
endif()

if(CONFIG_C908_AVERAGEPOOL_FP16)
    list(APPEND C908_SRCS source/c908_opt/fp16/avgpool.c)
endif()

if(CONFIG_C908_AVERAGEPOOL_INT8)
    list(APPEND C908_SRCS source/c908_opt/int8/avgpool.c)
endif()

if(CONFIG_C908_CONVOLUTION_FP32)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_1x1_fp32_pack1ton.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_1x1_fp32_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_1x1_fp32_packnto1.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_1x1_fp32.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_3x3_fp32_packn_1.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_3x3_fp32_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_3x3_fp32.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_gemm_fp32_pack1ton.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_gemm_fp32_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_gemm_fp32_packnto1.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution_gemm_fp32.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/convolution.c)
endif()

if(CONFIG_C908_CONVOLUTION_FP16)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_1x1_fp16_pack1ton.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_1x1_fp16_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_1x1_fp16_packnto1.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_1x1_fp16.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_3x3_fp16_packn_1.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_3x3_fp16_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_3x3_fp16.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_gemm_fp16_pack1ton.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_gemm_fp16_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_gemm_fp16_packnto1.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution_gemm_fp16.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/convolution.c)
endif()

if(CONFIG_C908_CONVOLUTION_INT8)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_1x1_int8_pack1ton.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_1x1_int8_packn.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_1x1_int8_packnto1.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_1x1_int8.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_3x3_int8_packn_1.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_3x3_int8_packn.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_3x3_int8.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_gemm_int8_pack1ton.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_gemm_int8_packn.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_gemm_int8_packnto1.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution_gemm_int8.c)
    list(APPEND C908_SRCS source/c908_opt/int8/convolution.c)
endif()

if(CONFIG_C908_CONVOLUTION_INT4)
    list(APPEND C908_SRCS source/c908_opt/int4/convolution.c)
endif()

if(CONFIG_C908_DEPTHWISE_CONVOLUTION_FP32)
    list(APPEND C908_SRCS source/c908_opt/fp32/depthwise_convolution.c)
endif()

if(CONFIG_C908_DEPTHWISE_CONVOLUTION_FP16)
    list(APPEND C908_SRCS source/c908_opt/fp16/depthwise_convolution.c)
endif()

if(CONFIG_C908_DEPTHWISE_CONVOLUTION_INT8)
    list(APPEND C908_SRCS source/c908_opt/int8/depthwise_convolution.c)
endif()

if(CONFIG_C908_DEPTHWISE_CONVOLUTION_INT4)
    list(APPEND C908_SRCS source/c908_opt/int4/depthwise_convolution.c)
endif()

if(CONFIG_C908_FULLYCONNECTED_FP32)
    list(APPEND C908_SRCS source/c908_opt/fp32/fullyconnected.c)
endif()

if(CONFIG_C908_FULLYCONNECTED_FP16)
    list(APPEND C908_SRCS source/c908_opt/fp16/fullyconnected.c)
endif()

if(CONFIG_C908_FULLYCONNECTED_INT8)
    list(APPEND C908_SRCS source/c908_opt/int8/fullyconnected.c)
endif()

if(CONFIG_C908_FULLYCONNECTED_INT4)
    list(APPEND C908_SRCS source/c908_opt/int4/fullyconnected.c)
endif()

if(CONFIG_C908_GEMM_FP32)
    list(APPEND C908_SRCS source/c908_opt/fp32/gemm_fp32_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/gemm_fp32_v256.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/gemm_fp32.c)
    list(APPEND C908_SRCS source/c908_opt/fp32/gemm_fp32_ncxhwx.S)
endif()

if(CONFIG_C908_GEMM_FP16)
    list(APPEND C908_SRCS source/c908_opt/fp16/gemm_fp16_packn.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/gemm_fp16_v256.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/gemm_fp16.c)
    list(APPEND C908_SRCS source/c908_opt/fp16/gemm_fp16_ncxhwx.S)
endif()

if(CONFIG_C908_GEMM_INT8)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int8_dot_packn.c)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int8_dot_v256.c)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int8_dot.c)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int8_packn.c)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int16_packn.c)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int8_dot_ncxhwx.S)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int8_ncxhwx.S)
    list(APPEND C908_SRCS source/c908_opt/int8/gemm_int16_ncxhwx.S)
endif()

if(CONFIG_C908_GEMM_INT4)
    list(APPEND C908_SRCS source/c908_opt/int4/gemm_int4_dot_ncxhwx.S)
endif()

if(CONFIG_C908_MAXPOOL_FP32)
    list(APPEND C908_SRCS source/c908_opt/fp32/maxpool.c)
endif()

if(CONFIG_C908_MAXPOOL_FP16)
    list(APPEND C908_SRCS source/c908_opt/fp16/maxpool.c)
endif()

if(CONFIG_C908_MAXPOOL_int8)
    list(APPEND C908_SRCS source/c908_opt/int8/maxpool.c)
endif()
