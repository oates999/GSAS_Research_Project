import music21

s = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/4852461-The_House_of_the_Rising_Sun.mxl')

def main():
	s_song = music21.converter.parse(r'c:/Users/Jonathan Oates/Downloads/4852461-The_House_of_the_Rising_Sun.mxl')
	for p in s_song.parts:
		print(len(p.spanners))
		for sp in p.spanners:
			print(" ".join([repr(n) for n in sp]))













if __name__ == '__main__':
	main()