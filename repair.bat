@echo off
:start
echo Zamykanie railroads jezeli sa otwarte.
taskkill /f /im RailRoads.exe
echo Oczekiwanie na zamkniecie railroads jezeli sa otwarte
timeout 3 >nul
cls
set/p "cho=Wybierz dysk na ktorym zainstalowany jest railroads: "
%cho%:
set/p "cho=Wybierz lokalizacje pliku: "
cd "%cho%"
echo Usuwanie pliku RailRoads.exe
del RailRoads.exe
echo Usunieto
echo Pobieranie naprawionej wersji.
curl https://github.com/AdasAdasiek/railroads-repair/raw/main/files/RailRoads.exe -o RailRoads.exe
echo Pomyslnie naprawiono railroads.
pause >nul
