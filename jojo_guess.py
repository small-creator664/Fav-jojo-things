import random

print ("i will guess your fav jojo(press a) fav part(Including spinoffs)(press b) fav villian(press c) fav stand(press d) fav jobro(press e)")
x = input()

if x == "a":
	liste = ["Jonathan Joestar(p1)", "Joseph Joestar", "Jotaro Kujo", "Josuke Higashikata(p4)", "Giorno Giovanna", "Jolyne Cujoh", "Jonathan Joestar(p7)", "JosukeHigashikata(p8)", "Jodio Joestar", "George Joestar I", "Mary Joestar", "Erina Pendleton Joestar", "George Joestar II", "Suzi Q Joestar", "Holy Kujo", "Sadao Kujo", "Shizuka Joestar", "Donatello Versus", "Rikiel", "Ungalo", "Green Baby", "Rina Higashikata", "George Joestar III", "Elizabeth Joestar", "Holy Joestar-Kira", "Yoshiteru Kira", "Kei Nijimura", "Josefumi Kujo", "Barbara Ann Joestar", "Dragona Joestar"]
	jojo = random.choice(liste)
	print (jojo)
elif x == "b":
	liste = ["part 1", "part 2", "part 3", "part 4", "part 5","Jolyne fly high with Gucci", "Thus Spoke Kishibe Rohan", "Dead Man's Questions", "Purple Haze Feedback", "Over Heaven", "JORGE JOESTAR", "Crazy Diamond's Demonic Heartbreak", "Iggy the Stray Dog", "The Book: 4th Another Day" "part 6", "part 7", "part 8", "part 9"]
	part = random.choice(liste)
	print (part)
elif x == "c":
	liste = ["Dio Brando", "Wang Chan", "Jack the Ripper", "Bruford", "Tarkus",
    "Kars", "Esidisi", "Wamuu", "Santana", "Stroheim", "Donovan",
    "DIO", "Vanilla Ice", "Hol Horse", "J. Geil", "Enya", "Mannish Boy",
    "Devo the Cursed", "Rubber Soul", "Nena", "ZZ", "Steely Dan", "Arabia Fats",
    "Cameo", "Midler", "N'Doul", "Oingo", "Boingo", "Anubis", "Mariah", "Alessi",
    "Daniel J. D'Arby", "Telence T. D'Arby", "Pet Shop",
    "Yoshikage Kira", "Akira Otoishi", "Anjuro Katagiri", "Keicho Nijimura",
    "Okuyasu Nijimura", "Tamami Kobayashi", "Hazamada Toshikazu", "Yukako Yamagishi",
    "Terunosuke Miyamoto", "Toyohiro Kanedaichi", "Masazo Kinoto", "Ken Oyanagi",
    "Mikiitaka Hazekura", "Shizuka Joestar",
    "Diavolo", "Risotto Nero", "Ghiaccio", "Prosciutto", "Pesci", "Melone",
    "Illuso", "Formaggio", "Cioccolata", "Secco", "Squalo", "Tiziano",
    "Carne", "Polpo",
    "Enrico Pucci", "Gwess", "Johngalli A.", "Thunder McQueen", "Mirashon",
    "Lang Rangler", "Viviano Westwood", "Sports Maxx", "Rykiel", "Donatello Versus",
    "Guccio", "Kenzou", "D an G", "Miuccia", "Ungalo",
    "Funny Valentine", "Diego Brando", "Ringo Roadagain", "Hot Pants",
    "Magenta Magenta", "Wekapipo", "Pocoloco", "Blackmore", "Mike O.", "Sandman",
    "Eleven Men's Company", "Axl RO", "Gaucho", "Doctor Ferdinand",
    "Tooru", "Jobin Higashikata", "Yotsuyu Yagiyama", "Daimon Tamaki",
    "Aisho Dainenjiyama", "Mamezuku Rai", "Ozon Baby", "Paper Moon King",
    "Urban Guerrilla", "Dolomite", "Poor Tom", "Satoru Akefu", "Kaato Higashikata",
    "Tamaki Damo",
    "Paco'nun ağabeyi", "Usagi Aloha'oe"]
	dusman = random.choice(liste)
	print (dusman)
elif x == "d":
	liste = [ "Star Platinum", "Hierophant Green", "Magician's Red", "Silver Chariot",
    "Hermit Purple", "The Fool", "Death Thirteen", "Empress", "Emperor",
    "Hanged Man", "Strength", "Ebony Devil", "Yellow Temperance",
    "Justice", "High Priestess", "Geb", "Khnum", "Tohth", "Anubis",
    "Bastet", "Sethan", "Osiris", "Horus", "Atum", "Cream", "Tenore Sax",
    "Vanilla Ice", "Dio's World", "The World", "Crazy Diamond", "The Hand",
    "Echoes ACT1", "Echoes ACT2", "Echoes ACT3", "Bad Company",
    "Harvest", "Killer Queen", "Sheer Heart Attack", "Bites the Dust",
    "Heaven's Door", "Atom Heart Father", "Boy II Man", "Cheap Trick",
    "Cinderella", "Enigma", "Highway Star", "Jailhouse Lock",
    "Killer Queen Bites the Dust", "Love Deluxe", "Red Hot Chili Pepper",
    "Ratt", "Aqua Necklace", "Reverb Act 1", "Reverb Act 2", "Reverb Act 3",
    "Stray Cat", "Surface", "The Lock", "20th Century Boy",
    "Aerosmith", "White Album", "Black Sabbath", "Gold Experience",
    "Sticky Fingers", "Moody Blues", "Sex Pistols", "Purple Haze",
    "Spice Girl", "King Crimson", "Soft Machine", "Kraft Work",
    "Little Feet", "Man in the Mirror", "Beach Boy", "Grateful Dead",
    "Baby Face", "White Album Gentle Weeps", "Green Day", "Oasis",
    "Metallica", "Rolling Stones", "Chariot Requiem", "Gold Experience Requiem",
    "Stone Free", "Goo Goo Dolls", "Stone Ocean", "Kiss", "Weather Report",
    "Diver Down", "Foo Fighters", "Limp Bizkit", "Highway to Hell",
    "Marilyn Manson", "Burning Down the House", "Dragon's Dream",
    "Yo-Yo Ma", "Green, Green Grass of Home", "Jailhouse Lock",
    "Bohemian Rhapsody", "Planet Waves", "Survivor", "Jumping Jack Flash",
    "Manhattan Transfer", "Limp Bizkit", "Jailhouse Lock", "Bohemian Rhapsody",
    "Heavy Weather", "C-Moon", "Made in Heaven", "Tusk ACT1", "Tusk ACT2",
    "Tusk ACT3", "Tusk ACT4", "Ball Breaker", "Scan", "Cream Starter",
    "Dirty Deeds Done Dirt Cheap", "Scary Monsters", "In a Silent Way",
    "Mandom", "Catch the Rainbow", "Wired", "Tomb of the Boom 1",
    "Tomb of the Boom 2", "Boku no Rhythm wo Kiitekure", "Tubular Bells",
    "Sugar Mountain's Spring", "Hey Ya!", "Civil War", "20th Century Boy",
    "D4C Love Train", "Paisley Park", "Nut King Call", "Soft & Wet",
    "King Nothing", "Fun Fun Fun", "California King Bed", "Schott Key No.1",
    "Schott Key No.2", "Walking Heart", "I Am a Rock", "Doobie Wah!",
    "Love Love Deluxe", "Awaking III Leaves", "Paper Moon King", "Brain Storm",
    "Milagro Man", "Vitamin C", "Doctor Wu", "Wonder of U"]
	stand = random.choice(liste)
	print (stand)
elif x == "e":
 liste = ["Robert E.O. Speedwagon", "Will A. Zeppeli", "Smokey Brown", "Caesar Anthonio Zeppeli", "Rudol von Stroheim", "Mohammed Avdol", "Noriaki Kakyoin", "Jean Pierre Polnareff", "Iggy", "Koichi Hirose", "Okuyasu Nijimura", "Shigekiyo Yangu", "Rohan Kishibe", "Yukako Yamagishi", "Bruno Bucciarati", "Leone Abbacchio", "Guido Mista", "Narancia Ghirga", "Pannacotta Fugo", "Ghiaccio", "Emporio Alnino", "Foo Fighters", "Weather Report", "Narciso Anasui", "Gyro Zeppeli", "Hot Pants", "Lucy Steel", "Yasuho Hirose", "Rai Mamezuku", "Tooru"]
 jobro = random.choice(liste)
 print (jobro)