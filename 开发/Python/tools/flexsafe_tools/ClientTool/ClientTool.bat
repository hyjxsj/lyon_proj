::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAhASQ2MKm60OpEZ++Pv4Pq7tkISWPEAKd2DyqyxcbJDvxe1I6ko12lDkcgDAlVWewblZww7yQ==
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFAhASQ2MKm60OpEZ++Pv4Pq7gUEUUewrTIDU1vqLOOVz
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
title Windows Client Tester Tool
mode con cols=110 lines=30
color 2F

rem 创建同步目录b0
call:generateUserDir
:generateUserDir
if exist b0 (
   echo "已经存在文件夹b0"
) else (
md b0
)


:top
cls
echo ***************************注意：以下命令执行过程中均会直接会关闭Windows Client************************
echo ***************************注意：打包错误日志功能依赖7z程序：【C:\Program Files\7-Zip】****************
echo.
echo ------------------------------------------------------------------------------------------------------
echo.
echo 1. 删除boxsafe数据-------------------清空【C:\ProgramData\boxsafe】目录
echo.
echo 2. 删除用户数据----------------------清空该程序所在目录下名为【b0】的目录，【b0】用作同步目录
echo.
echo 3. 删除Boxsafe Log-------------------删除【C:\ProgramData\boxsafe】目录下所有Log，用于获取较为精准的Log
echo.
echo 4. 收集Boxsafe Log-------------------打包【C:\ProgramData\boxsafe】目录，保存于该程序boxsafeLogs目录
echo.
echo 5. 打开用户目录下的boxsafe目录-------打开用户目录下的【boxsafe】目录
echo.
echo 6. 删除用户目录下的boxsafe目录-------删除用户目录下的【boxsafe】下所有文件
echo.
echo ------------------------------------------------------------------------------------------------------

set /p a=请选择要执行的操作：

if %a% EQU 1 (call:delBoxsafeData)
if %a% EQU 2 (call:delRootData)
if %a% EQU 3 (call:clearLogs)
if %a% EQU 4 (call:collectLogs)
if %a% EQU 5 (call:openUserBoxsafeFolder)
if %a% EQU 6 (call:delUserBoxsafeFolder)
goto top

rem 关闭客户端
:stopApp
echo 正在关闭客户端...
taskkill /f /im Flexsafe.exe
taskkill /f /im Boxsafe.exe
GOTO:EOF

rem 删除用户数据
:delRootData
call:stopApp
SET user_root_dir=b0
del /q /s %user_root_dir%\*.*
for /f "delims=" %%a in ('dir /ad/b/s %user_root_dir%') do (rd /q /s "%%a")>nul
pause
GOTO:EOF

rem 删除boxsafe数据
:delBoxsafeData
call:stopApp
SET boxsafe_dir=C:\ProgramData\boxsafe
del /q /s %boxsafe_dir%\*.*
for /f "delims=" %%a in ('dir /ad/b/s %boxsafe_dir%') do (rd /q /s "%%a")>nul
pause
GOTO:EOF

rem 删除Log
:clearLogs
call:stopApp
SET log_dir=C:\ProgramData\boxsafe\logs
del /q /s %log_dir%\*.*
del /q /s C:\ProgramData\boxsafe\*.log
pause
GOTO:EOF

rem 收集Log
:collectLogs
call:stopApp
set zip=C:\Program Files\7-Zip\7z.exe
set ymd=%date:~0,4%%date:~5,2%%date:~8,2%
set hms=%time:~0,2%%time:~3,2%%time:~6,2%
set dt=%ymd%%hms%
set /p zip_name=请输入Log压缩文件名：
set dir=C:\ProgramData\boxsafe
echo "%zip%" 
echo "%dir%"
echo "%dt%-%zip_name%"
if exist boxsafeLogs (
   echo "已经存在文件夹boxsafeLogs"
) else (
md boxsafeLogs
)
"%zip%" a boxsafeLogs\%dt%-%zip_name%.7z "%dir%"
pause
GOTO:EOF

rem 打开用户目录下的boxsafe目录
:openUserBoxsafeFolder
if exist "%appdata%\..\Local\VirtualStore\ProgramData\boxsafe" (
   start ""  "%appdata%\..\Local\VirtualStore\ProgramData\boxsafe"
) else (
   echo 未找到用户目录下的boxsafe目录，请手动查找
)
pause
GOTO:EOF

rem 用户目录下的boxsafe目录
:delUserBoxsafeFolder
call:stopApp
if exist "%appdata%\..\Local\VirtualStore\ProgramData\boxsafe" (
   del /q /s %appdata%\..\Local\VirtualStore\ProgramData\boxsafe\*.*
   for /f "delims=" %%a in ('dir /ad/b/s %appdata%\..\Local\VirtualStore\ProgramData\boxsafe') do (rd /q /s "%%a")>nul
) else (
   echo 未找到用户目录下的boxsafe目录，请手动查找  
)
pause
GOTO:EOF
