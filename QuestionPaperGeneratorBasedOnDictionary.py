import random

capitals = {
            'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre','Tennessee':'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City','Vermont':'Montpelier',
            'Virginia': 'Richmond','Washington': 'Olympia','WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming':'Cheyenne'
            }

l=list(capitals.values())
key=list(capitals.keys())

for k in range(1,36):
    m=0
    filename=str(k)+". student"+str(k)+".txt"
    f=open(filename,"w")
    random.shuffle(key)
    for i in range(0,len(key)):
        m=m+1
        f.write(str(m)+". What is the capital of "+key[i]+"? \n")
        sam=random.sample(l,5)
        while(capitals[key[i]] not in sam):
            random.shuffle(l)
            sam=random.sample(l,5)
        for j in range(0,len(sam)):
            f.write(str(j)+". "+sam[j]+"\n")
        f.write("\n")
    f.close()
