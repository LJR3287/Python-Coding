def SearchMonsterName():
    monster_found = 0
    SearchName = input("what is the name of the monster you are looking for?")
    with open('Monsters.txt') as f:
        for line in f:
            parts = line.split(",")
            id = parts[0]
            monster_name = parts [1]
            if SearchName.upper() == monster_name.upper():
                print("Monster found")
                print("the id for the name "+SearchName+"is "+id)
                monster_found=1
                break
    if monster_found == 0:
        print("Monster Not found")

SearchMonsterName()
