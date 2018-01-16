// Fill out your copyright notice in the Description page of Project Settings.

#include "ReadTxtFile.h"

bool UReadTxtFile::LoadTxt(FString FileNameA, FString& SaveTextA) {
	return FFileHelper::LoadFileToString(SaveTextA, *(FPaths::ProjectDir() + FileNameA));
}