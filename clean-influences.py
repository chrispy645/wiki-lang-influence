from sys import stdin


body = stdin.read().split('\n')

# name
#influenced by
#influenced

db = dict()
# db['php'] = {'influenced':[]}

for i in range(0, len(body), 3):
	chunk = body[i:i+3]
	if len(chunk) < 3:
		break
	if chunk[1] != '' and chunk[2] != '':
		lang = chunk[0]
		influenced_by = chunk[1].split(',')
		influenced = chunk[2].split(',')
		#print lang,
		#print influenced_by,
		#print influenced
		if lang not in db:
			db[lang] = { 'influenced': [] }
			
		for elem in influenced_by:
			if elem not in db:
				db[elem] = { 'influenced': [] }
			# e.g. if python was influenced by C, then
			# db['C']['influenced'].append('Python')
			db[elem]['influenced'].append(lang)
			
		for elem in influenced:
			if elem not in db:
				db[elem] = { 'influenced': [] }
			# e.g. if python influenced C, then
			# db['Python']['influenced'].append('C')
			db[lang]['influenced'].append(elem)
			
for key in db:
	influenced = db[key]['influenced']
	for inf in influenced:
		print "\t" +  '"' + key + '"' + " -> " +  '"' + inf + '"'