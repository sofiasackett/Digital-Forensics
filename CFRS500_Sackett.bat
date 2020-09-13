@echo off
rem Sofia Sackett
rem CFRS 500
rem Spring 2020
rem March 8 2020

rem Get user input for boot drive letter, name, and model of the current computer
:BOOTDRIVE
set /p bootdrive= "Enter the boot drive letter of this computer: "
IF NOT DEFINED bootdrive (goto :BOOTDRIVE) 

:COMPUTERNAME
set /p computername= "Enter the name of this computer: "
IF NOT DEFINED computername (goto :COMPUTERNAME) 

:COMPUTERMODEL
set /p computermodel= "Enter this computer's model: "
IF NOT DEFINED computermodel (goto :COMPUTERMODEL)
	
rem If cfrs500 does not exist, then create it
IF NOT EXIST %bootdrive%:\cfrs500 (mkdir %bootdrive%:\cfrs500) ELSE (cd %bootdrive%:\cfrs500)


rem Check if casefile.txt exists and either go to DONE or exit
IF EXIST %bootdrive%:\cfrs500\casefile.txt (goto :DONE) ELSE (goto :ERROR)

:ERROR
echo Casefile.txt already exists in the cfrs500 folder.
exit /b

rem Output bootdrive, computername, and computermodel to casefile.txt
:DONE
echo Boot drive letter: %bootdrive%>%bootdrive%:\cfrs500\casefile.txt
echo Computer name: %computername%>>%bootdrive%:\cfrs500\casefile.txt
echo Computer model: %computermodel%>>%bootdrive%:\cfrs500\casefile.txt

rem Output the following variables to text files within the cfrs500 directory
set>%bootdrive%:\cfrs500\set.txt 
systeminfo>%bootdrive%:\cfrs500\systeminfo.txt
getmac>%bootdrive%:\cfrs500\getmac.txt
ipconfig /displaydns>%bootdrive%:\cfrs500\displaydns.txt

rem Copy System.evtx to cfrs500\sys.evtx
copy %bootdrive%:\Windows\System32\winevt\Logs\System.evtx %bootdrive%:\cfrs500\sys.evtx

rem For loop to execute hostname and output to a text file
mkdir %bootdrive%:\cfrs500\casefile
for /f "tokens=*" %%G in ('hostname') do set host=%%G
echo %host%>%bootdrive%:\cfrs500\casefile\host.txt 

rem If statement to determine if sys.evtx was successfully created
IF EXIST %bootdrive%:\cfrs500\sys.evtx (echo sys.evtx successfully created) ELSE (echo sys.evtx wasn't successfully created)


