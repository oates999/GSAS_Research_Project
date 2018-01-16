import music21

s = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/4852461-The_House_of_the_Rising_Sun.mxl')

def main():
	s_song = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/4852461-The_House_of_the_Rising_Sun.mxl')
	for p in s_song.parts:
		p_notes = p.flat.getElementsByClass(music21.note.Note)
		for n in p_notes:
			n_tie = n.tie
			if n_tie is None:
				print("untied note")
			else:
				print("%s" %(n.tie.type))













if __name__ == '__main__':
	main()