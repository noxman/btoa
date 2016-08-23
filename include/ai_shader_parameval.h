/*
 * Arnold API header file
 * Copyright (c) 1998-2009 Marcos Fajardo, (c) 2009-2016 Solid Angle SL
 */

/**
 * \file 
 * Manual evaluation of shader inputs and their networks
 */

#pragma once
#include "ai_array.h"
#include "ai_color.h"
#include "ai_matrix.h"
#include "ai_vector.h"
#include "ai_types.h"

// forward declarations
struct AtShaderGlobals;
struct AtNode;

/** \defgroup ai_shader_parameval Parameter Evaluation API
 * 
 * \details
 * This API allows shader writers to retrieve the value of a given parameter.
 * If the parameter is linked to another shader, the child shader will be
 * executed and its output will be returned.
 *
 * This is the recommended mechanism for parameter evaluation inside a shader.
 * Note that, for parameters that are not linked, the AiNodeGet* API
 * (AiNodeGetInt(), etc) also returns the static value of the parameter.
 * For both consistency and optimal performance, it is recommended
 * to always use the AiShaderEvalParam* API described in this module.
 *
 * \{                                                                              
 */       

/** \name Parameter Evaluation Macros
 *
 * These macros evaluate a shader parameter of a specific type.
 *
 * There is a different macro for each supported parameter data type.
 * This is the version that users will want to invoke most often
 * since it passes the current shader globals and node by default.
 * For example:
 * \code
 * enum LambertParams {
 *    p_Kd,
 *    p_Kd_color
 * };
 * 
 * node_parameters
 * {
 *    AiParameterFlt("Kd", 0.7f);
 *    AiParameterRgb("Kd_color", 1, 1, 1);
 *    // note that parameter ordering must match the enum above
 * }
 *
 * shader_evaluate
 * {
 *    float kd = AiShaderEvalParamFlt(p_Kd);
 *    ...
 * }
 * \endcode 
 *
 * Please refer to ai_shader_parameval.h for a description of the functions
 * called by these macros. 
 *
 * \param pid  Index in the shader's parameter enum list
 * \return     Parameter value of the corresponding type. If the requested
 *             type doesn't match the parameter's true type, but the types
 *             are "link compatible", this query will silently perform the 
 *             appropiate conversion; otherwise if the types are not compatible
 *             a value of zero (or the closest thing to 0 for the requested type,
 *             such as NULL or black) will be returned. 
 *
 * \{
 */
#define AiShaderEvalParamByte(pid)   AiShaderEvalParamFuncByte (sg,node,pid)
#define AiShaderEvalParamInt(pid)    AiShaderEvalParamFuncInt  (sg,node,pid)
#define AiShaderEvalParamUInt(pid)   AiShaderEvalParamFuncUInt (sg,node,pid)
#define AiShaderEvalParamBool(pid)   AiShaderEvalParamFuncBool (sg,node,pid)
#define AiShaderEvalParamFlt(pid)    AiShaderEvalParamFuncFlt  (sg,node,pid)
#define AiShaderEvalParamRGB(pid)    AiShaderEvalParamFuncRGB  (sg,node,pid)
#define AiShaderEvalParamRGBA(pid)   AiShaderEvalParamFuncRGBA (sg,node,pid)
#define AiShaderEvalParamVec(pid)    AiShaderEvalParamFuncVec  (sg,node,pid)
#define AiShaderEvalParamPnt(pid)    AiShaderEvalParamFuncPnt  (sg,node,pid)
#define AiShaderEvalParamPnt2(pid)   AiShaderEvalParamFuncPnt2 (sg,node,pid)
#define AiShaderEvalParamStr(pid)    AiShaderEvalParamFuncStr  (sg,node,pid)
#define AiShaderEvalParamPtr(pid)    AiShaderEvalParamFuncPtr  (sg,node,pid)
#define AiShaderEvalParamArray(pid)  AiShaderEvalParamFuncArray(sg,node,pid)
#define AiShaderEvalParamMtx(pid)    AiShaderEvalParamFuncMtx  (sg,node,pid)
#define AiShaderEvalParamEnum(pid)   AiShaderEvalParamFuncEnum (sg,node,pid)
/*\}*/

/*\}*/

/*
 * Function form, only if you want to explicitly change shader globals and/or
 * node yourself. Otherwise it is recommended that you use the macros provided
 * above.
 *
 * \param sg    A shader globals context
 * \param node  The shader node whose parameter we want to evaluate
 * \param pid   Index in the shader's parameter enum list
 * \return      Parameter value of the corresponding type
 */
AI_API AtByte        AiShaderEvalParamFuncByte (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API int           AiShaderEvalParamFuncInt  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API unsigned int  AiShaderEvalParamFuncUInt (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API bool          AiShaderEvalParamFuncBool (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API float         AiShaderEvalParamFuncFlt  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API AtColor       AiShaderEvalParamFuncRGB  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API AtRGBA        AiShaderEvalParamFuncRGBA (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API AtVector      AiShaderEvalParamFuncVec  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API AtPoint       AiShaderEvalParamFuncPnt  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API AtPoint2      AiShaderEvalParamFuncPnt2 (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API const char*   AiShaderEvalParamFuncStr  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API void*         AiShaderEvalParamFuncPtr  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API AtArray*      AiShaderEvalParamFuncArray(AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API AtMatrix*     AiShaderEvalParamFuncMtx  (AtShaderGlobals* sg, const AtNode* node, int pid);
AI_API int           AiShaderEvalParamFuncEnum (AtShaderGlobals* sg, const AtNode* node, int pid);
