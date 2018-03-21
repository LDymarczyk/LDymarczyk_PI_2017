##########################################
Programy dołączone do pracy inżynierskiej

Temat pracy: Generatory liczb losowych i pseudolosowych
Autor pracy: Laura Dymarczyk

Programy dostępne również pod adresem https://github.com/LDymarczyk/LDymarczyk_PI_2017

Wymagania:
	Praca tworzona w języku python 2.7.11
	Do uruchomienie programu generator_mic.py wymagane jest podłączone pod komputer aduino oraz biblioteka Serial
	We folderze generator_mic zawarty jest program napisany pod arduino, kompilator dostępny jest na oficjalnej stronie
	https://www.arduino.cc/en/Main/Software
	
##########################################

Folder o nazwie "pliki" zawiera wygenerowane przez funkcję MakePoints(n) z pliku MouseGen.py punkty pobrane z kursora myszy,
Są one podstawą eksperymentów dotyczących generatorów opartych na ruchach myszy. Eksperymenty te są zaimplementowane
w pliku MouseGen.py, a zarówno ciągi jak i wyniki testów zapisane są w foderze mouse.

Testy:
	programy w plikach: testy.py oraz testy2.py

Generator afiniczny:
	program realizujący: pseudolosowy_afiniczny.py
	miejsce zapisu wyników: afiniczny
	
Generator LFSR:
	program realizujący: lfsr.py
	miejsce zapisu wyników: lfsr
	
Generator BBS:
	program realizujący: BBS_gen.py
	miejsce zapisu wyników: bbs
	
Generator LFSR oraz BBS:
	program realizujący: LFSRiBBS.py
	miejsce zapisu wyników: lfsribbs
	
Generatory oparte o microfon:
	program realizujący: 	akceptacja_co_drugi
							generator_mic
							xorowanie
	miejsce zapisu wyników: danemic
							mic_codrugi
							mic_xor
	
Końcowy generator prawdziwie losowy:
	program realizujący: TRNG.py
	miejsce zapisu wyników: trng
	
