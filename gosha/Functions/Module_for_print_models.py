def print_models(unprinted, completed):
	while unprinted:
		cur_design = unprinted.pop()
		print(f"Printing model: {cur_design}")
		completed.append(cur_design)

def show_completed(completed):
	print("\nThe following models have been printed: ")
	for complete in completed:
		print(complete)

unprinted = ['phone case', 'robot pend']
completed = []

print_models(unprinted[:], completed)
show_completed(completed)