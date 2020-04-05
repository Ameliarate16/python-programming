playlist = [
    {
        "title": "Be Glad I Love You (Go to Bed)",
        "genre": "Singer/Songwriter",
        "artist": "Bug Hunter",
        "year": "2018",
        "length": 3.65
    },
    {
        "title": "A Better Place, a Better Time",
        "genre": "Ska",
        "artist": "Streetlight Manifesto",
        "year": "2003",
        "length": 6.47
    },
    {
        "title": "Heretic Pride",
        "genre": "Singer/Songwriter",
        "artist": "The Mountain Goats",
        "year": "2008",
        "length": 3.72
    },
    {
        "title": "Be My Thrill",
        "genre": "Indie",
        "artist": "The Weepies",
        "year": "2010",
        "length": 2.53
    },
    {
        "title": "It's Alright",
        "genre": "Pop",
        "artist": "Mother Mother",
        "year": "2018",
        "length": 2.92
    },
    {
        "title": "Twilight Galaxy",
        "genre": "Indie",
        "artist": "Metric",
        "year": "2009",
        "length": 4.90
    },
    {
        "title": "Heart On My Sleeve",
        "genre": "Pop",
        "artist": "Mary Lambert",
        "year": "2014",
        "length": 3.15
    },
    {
        "title": "Heaven Help Me",
        "genre": "Hip Hop",
        "artist": "Lizzo",
        "year": "2019",
        "length": 3.37
    },
    {
        "title": "Between Two Lungs",
        "genre": "Pop",
        "artist": "Florence + The Machine",
        "year": "2009",
        "length": 4.15
    },
    {
        "title": "Dead Friend",
        "genre": "Punk Rock",
        "artist": "Against Me!",
        "year": "2014",
        "length": 3.03
    }
]

print("1. Print all the titles in the playlist", 
    "2. Print all the artists in the playlist", 
    "3. Print the total play length of the playlist", 
    "4. Determine the most popular genre in the playlist", 
    sep="\n")

choice = input("What would you like to do? ")[0]

if choice == "1":
    for song in playlist:
        print(song["title"])

elif choice == "2":
    artists = []
    
    for song in playlist:
        #don't repeat artists
        if song["artist"] not in artists:
            artists.append(song["artist"])
            print(song["artist"])

elif choice == "3":
    length = 0

    for song in playlist:
        length += song["length"]
    
    length = int(length)
    
    print(f"{length // 60} hours and {length % 60} minutes")

elif choice == "4":
    instances = {}
    most = ""

    for song in playlist:
        genre = song["genre"]
        #if it's a new genre, add to instances. otherwise increase the count
        if genre in instances:
            instances[genre] += 1
            #keep track of which genre has the highest number of instances
            if instances[genre] > instances[most]:
                most = genre
        
        else:
            instances[genre] = 1
            #if there's no most, add one
            if most == "":
                most = genre
    
    print(most)
        