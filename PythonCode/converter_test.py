import music21

s1 = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/2163051-Game_of_Thrones_Easy_piano.mxl')
s1.show('text')

s2 = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/4852461-The_House_of_the_Rising_Sun.mxl')
s2.show('text')

s1_chords = []
s1_chord_symbols = []
s1_chords_all = s1.flat.getElementsByClass(music21.chord.Chord)
for c in s1_chords_all:
	if type(c) is music21.harmony.ChordSymbol:
		s1_chord_symbols.append(c)
	else:
		s1_chords.append(c)
print("  chords: %d\n  chord symbols: %d" %(len(s1_chords), len(s1_chord_symbols)))
s1_key = s1.flat.getElementsByClass(music21.key.KeySignature)
print("  sharps: %d\n" %(s1_key[0].sharps))
s1_tempo = s1.flat.getElementsByClass(music21.tempo.MetronomeMark)[0]
print("  number: %d\n  text: %s" %(s1_tempo.number, s1_tempo.text))

s2_chords = []
s2_chord_symbols = []
s2_chords_all = s2.flat.getElementsByClass(music21.chord.Chord)
for c in s2_chords_all:
	if type(c) is music21.harmony.ChordSymbol:
		s2_chord_symbols.append(c)
	else:
		s2_chords.append(c)
print("  chords: %d\n  chord symbols: %d" %(len(s2_chords), len(s2_chord_symbols)))
s2_key = s2.flat.getElementsByClass(music21.key.KeySignature)
print("  sharps: %d\n" %(s2_key[0].sharps))