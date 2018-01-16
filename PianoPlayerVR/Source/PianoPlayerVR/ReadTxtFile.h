// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "ReadTxtFile.generated.h"

/**
 * 
 */
UCLASS()
class PIANOPLAYERVR_API UReadTxtFile : public UBlueprintFunctionLibrary
{
	GENERATED_BODY() public:
	UFUNCTION(BlueprintPure, Category = Custom, meta = (DisplayName = "Load data (string) from .txt file", CompactNodeTitle = "LoadTxtFile", Keywords = "LoadTxt"))
		static bool LoadTxt(FString FileNameA, FString& SaveTextA);
};