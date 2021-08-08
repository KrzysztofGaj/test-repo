def main():
	imiona = ['Jakub', 'Stefan', 'Maria', 'Ewelina', 'Patrycja', 'Jurek', 'Marcin']
	print('Stara lista imion: ', imiona, '.', sep='')
	imię = input('Które imię ma zostać zamienione? ')

	try:
		imię_index = imiona.index(imię)
		nowe_imię = input('Podaj nowe imię: ')
		imiona[imię_index] = nowe_imię

		print('Nowa lista imon: ', imiona, '.', sep='')
	except ValueError:
		print('Takie imię nie zostało znalezione na liście.')
		
	input()
main()