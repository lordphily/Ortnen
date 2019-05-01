# JSBB Beschlüsse geortnet
1. Beschlüsse sammeln
2. Einzelne Beschlüsse in ods/exel nach Vorlage einpflegen
3. Als csv Datei exportieren
4. Python scipt ausführen

## Beschlüsse sammeln

Diese Aufgabe muss von fleißigen Menschen übernommen werden. Diese fleißigen Menschen können dann bestenfalls 2. und 3 bearbeiten

## Einzelne Beschlüsse in odt/exel Sammeln

 1. Benutzt die Vorlage "Erläuterung.ods" als Hilfe
 2. Die Datei "BeispielBeschluss.ods" kann zum Ausfüllen genutzt werden 
 3. Richtlinien für das Ausfüllen:
	1. Datum im Format TT.MM.JJJJ
	2. Antragstext ist der Angenommene/Abgelehnte Antragstext nach dem einplegen aller Änderungsanträge (so es welche gibt)
	3. Abstimmungsergebnisse sollte nach Möglichkeit in Zahlen angegeben werden. Wenn nicht mehr raus zu kriegen dann „Mehrheitlich“ und „In Unterzahl“ nutzen.
	4. Anhang(Zeile11) immer als PDF, wenn mehrere dann mit Komma(,) die Anhänge trennen. Die Titel der Anhänge in der Nächsten Zeile auch mit Komma(,) trennen.
	5. Wenn Änderungsanträge vohanden sind, dann in Zeile 24 ja eingeben und die nächsten 6 Zeilen ausfüllen. Wenn weitere Änderungsanträge sind, dann Lehrzeile lassen und die 6 Zeilen kopieren. USW.
	6. Änderungsanträge sollten möglichst genau beschreiben wo was geändert werden soll (Zeilennummer/Absatz/...)


## Export als CSV

 Jeden Beschluss als CSV Datei exportieren. Dabei folgendes beachten:
 1. Codierung: UTF8
 2. Feldtrenner: ;
 3. Zeichenkettentrenner: "

## Python skript ausführen
Python skript erst ausführen, wenn **alle zu beachtenden** Beschlüsse als CSV Datei vorliegen.