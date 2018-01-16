// Copyright 1998-2017 Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "ObjectMacros.h"
#include "ScriptMacros.h"

PRAGMA_DISABLE_DEPRECATION_WARNINGS
#ifdef PIANOPLAYERVR_ReadTxtFile_generated_h
#error "ReadTxtFile.generated.h already included, missing '#pragma once' in ReadTxtFile.h"
#endif
#define PIANOPLAYERVR_ReadTxtFile_generated_h

#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_RPC_WRAPPERS \
 \
	DECLARE_FUNCTION(execLoadTxt) \
	{ \
		P_GET_PROPERTY(UStrProperty,Z_Param_FileNameA); \
		P_GET_PROPERTY_REF(UStrProperty,Z_Param_Out_SaveTextA); \
		P_FINISH; \
		P_NATIVE_BEGIN; \
		*(bool*)Z_Param__Result=UReadTxtFile::LoadTxt(Z_Param_FileNameA,Z_Param_Out_SaveTextA); \
		P_NATIVE_END; \
	}


#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_RPC_WRAPPERS_NO_PURE_DECLS \
 \
	DECLARE_FUNCTION(execLoadTxt) \
	{ \
		P_GET_PROPERTY(UStrProperty,Z_Param_FileNameA); \
		P_GET_PROPERTY_REF(UStrProperty,Z_Param_Out_SaveTextA); \
		P_FINISH; \
		P_NATIVE_BEGIN; \
		*(bool*)Z_Param__Result=UReadTxtFile::LoadTxt(Z_Param_FileNameA,Z_Param_Out_SaveTextA); \
		P_NATIVE_END; \
	}


#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_INCLASS_NO_PURE_DECLS \
private: \
	static void StaticRegisterNativesUReadTxtFile(); \
	friend PIANOPLAYERVR_API class UClass* Z_Construct_UClass_UReadTxtFile(); \
public: \
	DECLARE_CLASS(UReadTxtFile, UBlueprintFunctionLibrary, COMPILED_IN_FLAGS(0), 0, TEXT("/Script/PianoPlayerVR"), NO_API) \
	DECLARE_SERIALIZER(UReadTxtFile) \
	enum {IsIntrinsic=COMPILED_IN_INTRINSIC};


#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_INCLASS \
private: \
	static void StaticRegisterNativesUReadTxtFile(); \
	friend PIANOPLAYERVR_API class UClass* Z_Construct_UClass_UReadTxtFile(); \
public: \
	DECLARE_CLASS(UReadTxtFile, UBlueprintFunctionLibrary, COMPILED_IN_FLAGS(0), 0, TEXT("/Script/PianoPlayerVR"), NO_API) \
	DECLARE_SERIALIZER(UReadTxtFile) \
	enum {IsIntrinsic=COMPILED_IN_INTRINSIC};


#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_STANDARD_CONSTRUCTORS \
	/** Standard constructor, called after all reflected properties have been initialized */ \
	NO_API UReadTxtFile(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get()); \
	DEFINE_DEFAULT_OBJECT_INITIALIZER_CONSTRUCTOR_CALL(UReadTxtFile) \
	DECLARE_VTABLE_PTR_HELPER_CTOR(NO_API, UReadTxtFile); \
DEFINE_VTABLE_PTR_HELPER_CTOR_CALLER(UReadTxtFile); \
private: \
	/** Private move- and copy-constructors, should never be used */ \
	NO_API UReadTxtFile(UReadTxtFile&&); \
	NO_API UReadTxtFile(const UReadTxtFile&); \
public:


#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_ENHANCED_CONSTRUCTORS \
	/** Standard constructor, called after all reflected properties have been initialized */ \
	NO_API UReadTxtFile(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get()) : Super(ObjectInitializer) { }; \
private: \
	/** Private move- and copy-constructors, should never be used */ \
	NO_API UReadTxtFile(UReadTxtFile&&); \
	NO_API UReadTxtFile(const UReadTxtFile&); \
public: \
	DECLARE_VTABLE_PTR_HELPER_CTOR(NO_API, UReadTxtFile); \
DEFINE_VTABLE_PTR_HELPER_CTOR_CALLER(UReadTxtFile); \
	DEFINE_DEFAULT_OBJECT_INITIALIZER_CONSTRUCTOR_CALL(UReadTxtFile)


#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_PRIVATE_PROPERTY_OFFSET
#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_12_PROLOG
#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_GENERATED_BODY_LEGACY \
PRAGMA_DISABLE_DEPRECATION_WARNINGS \
public: \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_PRIVATE_PROPERTY_OFFSET \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_RPC_WRAPPERS \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_INCLASS \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_STANDARD_CONSTRUCTORS \
public: \
PRAGMA_ENABLE_DEPRECATION_WARNINGS


#define PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_GENERATED_BODY \
PRAGMA_DISABLE_DEPRECATION_WARNINGS \
public: \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_PRIVATE_PROPERTY_OFFSET \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_RPC_WRAPPERS_NO_PURE_DECLS \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_INCLASS_NO_PURE_DECLS \
	PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h_15_ENHANCED_CONSTRUCTORS \
private: \
PRAGMA_ENABLE_DEPRECATION_WARNINGS


#undef CURRENT_FILE_ID
#define CURRENT_FILE_ID PianoPlayerVR_Source_PianoPlayerVR_ReadTxtFile_h


PRAGMA_ENABLE_DEPRECATION_WARNINGS
