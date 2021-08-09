def main():
	fnames = ['John', 'Steven', 'Mary', 'Eveline', 'Patrice', 'George', 'Martin']
	print('Original list of names: ', fnames, '.', sep='')
	fname = input('Input the name to be changed ? ')

	try:
		fname_index = fnames.index(fname)
		new_fname = input('Type the new name: ')
		fnames[fname_index] = new_fname

		print('New list of names: ', fnames, '.', sep='')
	except ValueError:
		print('There\'s no such name on the list.')
		main()
		
	input()
main()
