/*
 * Arnold API header file
 * Copyright (c) 1998-2009 Marcos Fajardo, (c) 2009-2016 Solid Angle SL
 */

/**
 * \file 
 * Message passing API for shader writers
 */

#pragma once
#include "ai_array.h"
#include "ai_color.h"
#include "ai_string.h"
#include "ai_vector.h"
#include "ai_types.h"

// forward declaration
struct AtShaderGlobals;

/** \defgroup ai_shader_message Shader Message Passing API
 *
 * \details
 * This message passing API allows the shader to write a message into the
 * messsage bank which can be retrieved by other shaders in the current/active
 * shading network.  A "message" consists of a value and an associated name.  To
 * retrieve a message (a value), one needs to provide the name of that message.
 *
 * The "lifetime" of these messages is for a single screen sample (it's
 * attached to the \ref AtShaderGlobals of the current pixel/sample).  So, if a single
 * camera ray recursively fires new rays, then the messages created
 * anywhere in that ray-tree will be accessible by any shader in
 * that ray-tree.  When the next camera ray is fired, the message bank will be
 * completely emptied.
 *
 * The message bank has a fixed number of slots, so it is possible that one
 * could fill the message bank.  In that case, all subsequent writes of new messages 
 * will fail.
 *
 * \{
 */

/** \name Message Retrieval Macros
 *
 * \details
 * These macros allow a shader to retrieve messages which have been written to
 * the message bank.  If the named message does not exist (has not been written
 * yet?), then false is returned.  Otherwise, true indicates a successful read.
 *
 * Please refer to ai_shader_message.h for a description of the
 * message-reading functions called by these macros.  
 *
 * \{
 */
#define AiStateGetMsgByte(name,val)  AiMessageGetByteFunc (sg,name,val)
#define AiStateGetMsgBool(name,val)  AiMessageGetBoolFunc (sg,name,val)
#define AiStateGetMsgInt(name,val)   AiMessageGetIntFunc  (sg,name,val)
#define AiStateGetMsgUInt(name,val)  AiMessageGetUIntFunc (sg,name,val)
#define AiStateGetMsgFlt(name,val)   AiMessageGetFltFunc  (sg,name,val)
#define AiStateGetMsgRGB(name,val)   AiMessageGetRGBFunc  (sg,name,val)
#define AiStateGetMsgRGBA(name,val)  AiMessageGetRGBAFunc (sg,name,val)
#define AiStateGetMsgVec(name,val)   AiMessageGetVecFunc  (sg,name,val)
#define AiStateGetMsgPnt(name,val)   AiMessageGetPntFunc  (sg,name,val)
#define AiStateGetMsgPnt2(name,val)  AiMessageGetPnt2Func (sg,name,val)
#define AiStateGetMsgStr(name,val)   AiMessageGetStrFunc  (sg,name,val)
#define AiStateGetMsgPtr(name,val)   AiMessageGetPtrFunc  (sg,name,val)
#define AiStateGetMsgArray(name,val) AiMessageGetArrayFunc(sg,name,val)
/*\}*/

/** \name Message Writing Macros
 *
 * \details
 * These macros allow a shader to write messages to
 * the message bank.  If the write has failed for some reason (perhaps there are 
 * already too many messages in the bank?) then false is returned.  Otherwise,
 * true indicates a successful write.
 *
 * Please refer to ai_shader_message.h for a description of the
 * message-writing functions called by these macros.
 *
 * \{
 */
#define AiStateSetMsgByte(name,val)  AiMessageSetByteFunc (sg,name,val)
#define AiStateSetMsgBool(name,val)  AiMessageSetBoolFunc (sg,name,val)
#define AiStateSetMsgInt(name,val)   AiMessageSetIntFunc  (sg,name,val)
#define AiStateSetMsgUInt(name,val)  AiMessageSetUIntFunc (sg,name,val)
#define AiStateSetMsgFlt(name,val)   AiMessageSetFltFunc  (sg,name,val)
#define AiStateSetMsgRGB(name,val)   AiMessageSetRGBFunc  (sg,name,val)
#define AiStateSetMsgRGBA(name,val)  AiMessageSetRGBAFunc (sg,name,val)
#define AiStateSetMsgVec(name,val)   AiMessageSetVecFunc  (sg,name,val)
#define AiStateSetMsgPnt(name,val)   AiMessageSetPntFunc  (sg,name,val)
#define AiStateSetMsgPnt2(name,val)  AiMessageSetPnt2Func (sg,name,val)
#define AiStateSetMsgStr(name,val)   AiMessageSetStrFunc  (sg,name,val)
#define AiStateSetMsgPtr(name,val)   AiMessageSetPtrFunc  (sg,name,val)
#define AiStateSetMsgArray(name,val) AiMessageSetArrayFunc(sg,name,val)
/*\}*/

/** \name Message Removal Macros
 *
 * \details
 * These macros allow a shader to remove messages from
 * the message bank.
 *
 * Please refer to ai_shader_message.h for a description of the
 * message-writing functions called by these macros.
 *
 * \{
 */
#define AiStateUnsetMsgByte(name)  AiMessageUnsetByteFunc (sg,name)
#define AiStateUnsetMsgBool(name)  AiMessageUnsetBoolFunc (sg,name)
#define AiStateUnsetMsgInt(name)   AiMessageUnsetIntFunc  (sg,name)
#define AiStateUnsetMsgUInt(name)  AiMessageUnsetUIntFunc (sg,name)
#define AiStateUnsetMsgFlt(name)   AiMessageUnsetFltFunc  (sg,name)
#define AiStateUnsetMsgRGB(name)   AiMessageUnsetRGBFunc  (sg,name)
#define AiStateUnsetMsgRGBA(name)  AiMessageUnsetRGBAFunc (sg,name)
#define AiStateUnsetMsgVec(name)   AiMessageUnsetVecFunc  (sg,name)
#define AiStateUnsetMsgPnt(name)   AiMessageUnsetPntFunc  (sg,name)
#define AiStateUnsetMsgPnt2(name)  AiMessageUnsetPnt2Func (sg,name)
#define AiStateUnsetMsgStr(name)   AiMessageUnsetStrFunc  (sg,name)
#define AiStateUnsetMsgPtr(name)   AiMessageUnsetPtrFunc  (sg,name)
#define AiStateUnsetMsgArray(name) AiMessageUnsetArrayFunc(sg,name)
/*\}*/

/** \name Message Inspection Functions
 *
 * \details
 * These functions let you loop over all available messages for a given sample.
 * This is mainly intended for debugging purposes.
 *
 * \{
 */

/**
 * This represents a message iterator. The actual contents of this struct are
 * private.
 */
typedef struct AtMessageIterator AtMessageIterator;

AI_API AtMessageIterator* AiMessageIterator(const AtShaderGlobals* sg);
AI_API bool               AiMessageIteratorGetNext(AtMessageIterator* iterator, const char** msg_name, int* msg_type);
/*\}*/

/*\}*/


#define AiCreateFuncs(_name, _type)                                                                                  \
AI_API AI_DEPRECATED bool AiMessageGet##_name##Func         (const AtShaderGlobals*,    const char*,        _type*); \
AI_API               bool AiMessageGet##_name##FuncAtString (const AtShaderGlobals*,    const AtString,     _type*); \
inline               bool AiMessageGet##_name##Func         (const AtShaderGlobals* sg, const AtString str, _type* x)\
{                                                                                                                    \
   return AiMessageGet##_name##FuncAtString(sg, str, x);                                                             \
}                                                                                                                    \
AI_API AI_DEPRECATED bool AiMessageSet##_name##Func         (AtShaderGlobals*,    const char*,        _type);  \
AI_API               bool AiMessageSet##_name##FuncAtString (AtShaderGlobals*,    const AtString,     _type);  \
inline               bool AiMessageSet##_name##Func         (AtShaderGlobals* sg, const AtString str, _type x) \
{                                                                                                              \
   return AiMessageSet##_name##FuncAtString(sg, str, x);                                                       \
}                                                                                                              \
AI_API               bool AiMessageUnset##_name##Func (AtShaderGlobals*,    const AtString);  \

AiCreateFuncs(Bool, bool)
AiCreateFuncs(Byte, AtByte)
AiCreateFuncs(Int, int)
AiCreateFuncs(UInt, unsigned int)
AiCreateFuncs(Flt, float)
AiCreateFuncs(RGB, AtRGB)
AiCreateFuncs(RGBA, AtRGBA)
AiCreateFuncs(Vec, AtVector)
AiCreateFuncs(Pnt, AtPoint)
AiCreateFuncs(Pnt2, AtPoint2)
AiCreateFuncs(Str, const char*)
AiCreateFuncs(Ptr, void*)
AiCreateFuncs(Array, AtArray*)
#undef AiCreateFuncs
