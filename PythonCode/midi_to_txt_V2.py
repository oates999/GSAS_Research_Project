import music21

# Generates a filename for a part based on song name, instrument, and clef
def generate_file_name(s_part, s_name):
	_clef = s_part.flat.getElementsByClass('Clef')
	if len(_clef) > 0:
		return "%s__%s_%s.txt" %(s_name, s_part.partName, _clef[0].sign)
	else:
		return None

# Returns array of spanners from a part
def get_spanners_from_part(s_part):
	_spanners = s_part.getElementsByClass('Spanner')
	if len(_spanners) > 0:
		return _spanners
	return None
def generate_string_from_spanner(p_spanner):
	return "[SPANNER]%s[s]__beginOffset__[s]__endOffset__" %(p_spanner.classes[0])

# Returns array of measures from a part
def get_measures_from_part(s_part):
	_measures = s_part.getElementsByClass('Measure')
	return _measures
def generate_string_from_measure(p_measure):
	# Get time signature of measure
	_time_string = "NA"
	_time_signature = p_measure.flat.getElementsByClass('TimeSignature')
	if len(_time_signature) > 0:
		_time_string = "%s" %(_time_signature[0].ratioString)
	# Get key signature of measure
	_key_string = "NA"
	_keys = p_measure.flat.getElementsByClass(music21.key.KeySignature)
	if len(_keys) > 0:
		_key_string = "%d" %(_keys[0].sharps)
	# Get Metronome Mark (tempo)
	_tempo_string = "NA"
	_tempos = p_measure.flat.getElementsByClass(music21.tempo.MetronomeMark)
	if len(_tempos) > 0:
		_tempo_string = "[TEMPO]%s[t]%d" %(_tempos[0].text, _tempos[0].number)
	# Get dynamics of measure
	_dynamics_string = "none"
	_dynamics = p_measure.getElementsByClass('Dynamic')
	if len(_dynamics) > 0:
		_dynamics_string = ""
		for d in _dynamics:
			_dynamics_string += "[DYN]%s[d]%.2f" %(d.value, d.volumeScalar)
	# Get text expressions of measure
	_expressions_string = "none"
	_expressions = p_measure.getElementsByClass('TextExpression')
	if len(_expressions) > 0:
		_expressions_string = ""
		for e in _expressions:
			_expressions_string += "[EXP]%s" %(e.content)
	# Get notes in measure
	_notes_string = "none"
	_notes = p_measure.flat.getElementsByClass('Note')
	if len(_notes) > 0:
		_notes_string = ""
		for n in _notes:
			# Get articulations of note
			_articulation_string = "none"
			if len(n.articulations) > 0:
				_articulation_string = ""
				for a in n.articulations:
					_articulation_string += "[ART]%s" %(a.name)
			# Get expressions of note
			_expressions2_string = "none"
			if len(n.expressions) > 0:
				_expressions2_string = ""
				for e in n.expressions:
					_expressions2_string += "[EXP2]%s" %(e.name)
			# Get beams of note
			_beams_string = "none"
			if len(n.beams.getNumbers()) > 0:
				_beams_string = ""
				for b in n.beams.getNumbers():
					_beams_string += "[BEAM]%d[b]%s" %(b, n.beams.getByNumber(b).type)
			# Get ties of note
			_ties_string = "none"
			if n.tie is not None:
				_ties_string = n.tie.type
			# Full compilation of note string
			_notes_string += "[NOTE]%s[n]%s[n]%.2f[n]%d[n]%s[n]%s[n]%s[n]%s[n]%.2f[n]%d" %(n.nameWithOctave, n.duration.type, n.duration.quarterLength, n.duration.dots, _articulation_string, _expressions2_string, _beams_string, _ties_string, n.offset, n.measureNumber)
	# Gets chords in measure
	_chords_string = "none"
	_symbols_string = "none"
	_chords = []
	_symbols = []
	_chords_all = p_measure.getElementsByClass(music21.chord.Chord)
	for c in _chords_all:
		if type(c) is music21.harmony.ChordSymbol:
			_symbols.append(c)
		else:
			_chords.append(c)
	if len(_chords) > 0:
		_chords_string = ""
		for c in _chords:
			# Get pitches in chord
			_pitches_string = ""
			for p in c.pitches:
				_pitches_string += "[PITCH]%s" %(p.nameWithOctave)
			# Get articulations of note
			_articulation_string = "none"
			if len(c.articulations) > 0:
				_articulation_string = ""
				for a in c.articulations:
					_articulation_string += "[ART]%s" %(a.name)
			# Get expressions of note
			_expressions2_string = "none"
			if len(c.expressions) > 0:
				_expressions2_string = ""
				for e in c.expressions:
					_expressions2_string += "[EXP2]%s" %(e.name)
			# Get beams of note
			_beams_string = "none"
			if len(c.beams.getNumbers()) > 0:
				_beams_string = ""
				for b in c.beams.getNumbers():
					_beams_string += "[BEAM]%d[b]%s" %(b, c.beams.getByNumber(b).type)
			# Get ties of note
			_ties_string = "none"
			if c.tie is not None:
				_ties_string = c.tie.type
			# Full compilation of chord string
			_chords_string += "[CHORD]%s[c]%s[c]%.2f[c]%d[c]%s[c]%s[c]%s[c]%s[c]%.2f[c]%d" %(_pitches_string, c.duration.type, c.duration.quarterLength, c.duration.dots, _articulation_string, _expressions2_string, _beams_string, _ties_string, c.offset, c.measureNumber)
	if len(_symbols) > 0:
		_symbols_string = ""
		for s in _symbols:
			_symbols_string += "[SYMBOL]%s[s]%d" %(s.figure, s.measureNumber)
	# Get rests in measure
	_rests_string = "none"
	_rests = p_measure.flat.getElementsByClass('Rest')
	if len(_rests) > 0:
		_rests_string = ""
		for r in _rests:
			_rests_string += "[REST]%s[r]%.2f[r]%d[r]%.2f[r]%d" %(r.duration.type, r.duration.quarterLength, r.duration.dots, r.offset, r.measureNumber)

	return "[MEASURE]%d[m]%s[m]%s[m]%s[m]%s[m]%s[m]%s[m]%s[m]%s[m]%s" %(p_measure.measureNumber, _time_string, _key_string, _tempo_string, _dynamics_string, _expressions_string, _notes_string, _chords_string, _rests_string, _symbols_string)


def main(s_song, s_name):
	for s_part in s_song.parts:
		filename = generate_file_name(s_part, s_name)
		if filename is None:
			print("!-- Error: filename is None... skipping part")
			continue
		print(filename)
		f = open(filename, 'w')

		# Write spanner data to file
		p_spanners = get_spanners_from_part(s_part)
		if p_spanners is not None:
			for s in p_spanners:
				spanners_string = generate_string_from_spanner(s)
				f.write(spanners_string)
				print(spanners_string)
		else:
			f.write("none")
		f.write("[#]")
		# Write measure data to file
		p_measures = get_measures_from_part(s_part)
		for m in p_measures:
			measures_string = generate_string_from_measure(m)
			f.write(measures_string)
			print(measures_string)
		f.close()

if __name__ == '__main__':
	#s = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/4852461-The_House_of_the_Rising_Sun.mxl')
	#n = "HouseOfTheRisingSun"
	s = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/2163051-Game_of_Thrones_Easy_piano.mxl')
	n = "GameOfThronesEasy"
	s.show('text')
	main(s, n)