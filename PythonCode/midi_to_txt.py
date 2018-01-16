import music21

def get_measure_data(m):
	# Get time signature
	_times = m.getElementsByClass(music21.meter.TimeSignature)
	time_string = "NA"
	if len(_times) > 0:
		time_string = _times[0].ratioString
	measure_string = "NA"
	# Get notes
	_notes = m.getElementsByClass(music21.note.Note)
	note_string = ""
	if len(_notes) > 0:
		for n in _notes:
			note_string += "[NOTE]%s,%s,%s,%s,%s,%s,%s," %(n.offset, n.name, n.octave, n.duration.type, n.duration.quarterLength, n.duration.dots, n.measureNumber)
			_articulations = n.articulations
			if len(_articulations) > 0:
				for a in _articulations:
					note_string += "[ART]%s" %(a.name)
			else:
				note_string += "noArt"
			note_string += ","
			_beams = n.beams
			if len(_beams.getNumbers()) > 0:
				for b in _beams.getNumbers():
					note_string += "[BEAM]%d_%s" %(b, _beams.getByNumber(b).type)
			else:
				note_string += "noBeams"
			if n.tie is not None:
				note_string += ",%s" %(n.tie.type)
			else:
				note_string += ",untied"
			if measure_string == "NA":
				measure_string = "%s" %(m.measureNumber)
	else:
		note_string = "noNotes"
	# Get rests
	_rests = m.getElementsByClass(music21.note.Rest)
	rest_string = ""
	for r in _rests:
		rest_string += "[REST]%s,%s,%s,%s,%s" %(r.offset, r.duration.type, r.duration.quarterLength, r.duration.dots, r.measureNumber)
		if measure_string == "NA":
			measure_string = "%s" %(m.measureNumber)
	if rest_string == "":
		rest_string = "noRests"

	measure_data = { 'notes': note_string, 'rests': rest_string, 'time': time_string, 'number': measure_string }
	return measure_data

def main():
	s_song = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/2163051-Game_of_Thrones_Easy_piano.mxl')
	partCounter = 0
	for p in s_song.parts:
		filename_string = "%d_%s.txt" %(partCounter, p.partName)
		f = open(filename_string, 'w')

		p_measures = p.getElementsByClass('Measure')
		for m in p_measures:
			measure_data = get_measure_data(m)
			f.write("[MEASURE]%s|%s|%s|%s" %(measure_data['number'], measure_data['time'], measure_data['notes'], measure_data['rests']))
			print("[MEASURE]%s|%s|%s|%s\n" %(measure_data['number'], measure_data['time'], measure_data['notes'], measure_data['rests']))

		partCounter += 1


if __name__ == '__main__':
	main()