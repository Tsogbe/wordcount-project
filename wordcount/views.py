from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def count(request):
	text = request.GET['fulltext']
	list_text = text.split()
	length = len(list_text)

	words_dict = {}

	for word in list_text:
		if word in words_dict:
			words_dict[word] += 1
		else:
			words_dict[word] = 1

	words_dict = dict(sorted(words_dict.items(), key = lambda x: x[1], reverse=True))

	return render(request, 'count.html', {'text': text, 'words_dict': words_dict, 'length': length})

def about(request):
	return render(request, 'about.html')