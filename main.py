from math import trunc

class StoryTeller:
    def say(self, text):
        print(f"[ GAME ] : {text}")

    def ask(self, text, name):
        return input(f"[ GAME ] : {text}\n[ {name} ]: ")

class Character:
    def __init__(self, name, list_of_items, max_inv_len, isAlive):
        self.name = name
        self.list_of_items = list_of_items
        self.max_inv_len = max_inv_len
        self.isAlive = isAlive

    def stats(self):
        print(f"[ {self.name} ] : táskám tartalma: #{self.list_of_items}# táskámban lévő szabad helyek: {self.max_inv_len - len(self.list_of_items)}")

    def say(self, text):
        print(f"[ {self.name} ] : {text}")

class Dwarf:
    def __init__(self, name, list_of_questions):
        self.name = name
        self.list_of_questions = list_of_questions

    def say(self, text):
        print(f"[ Dwarf {self.name} ] : {text}")

    def ask(self, text, name):
        return input(f"[ Dwarf {self.name} ] : {text}\n[ {name} ]: ")

    def getQuestion(self, index):
        for key in self.list_of_questions[index]:
            return key
        
    def getAnsw(self, index):
        for key in self.list_of_questions[index]:
            return self.list_of_questions[index][key]

    def play(self, player):
        if player.isAlive == False:
            return player
        else:
            trys = 0
            while (trys <3):
                user_answ = self.ask(self.getQuestion(trys), player.name)
                if user_answ == self.getAnsw(trys):
                    self.say("Helyes válasz! Nem hittem volna hogy ezt kitalálod :( Tessék itt az élelemed")
                    player.list_of_items.append("élelem")
                    return player
                trys += 1
            self.say("Sajnos nem válaszoltál helyesen! Ezért mint ahogy itt --> aláírtad felnégyellek")
            player.isAlive = False
            return player

class Spider:
    def __init__(self, name, quest, answ):
        self.name = name
        self.quest = quest
        self.answ = answ

    def say(self, text):
        print(f"[ Spider {self.name} ] : {text}")

    def ask(self, text, name):
        return input(f"[ Spider {self.name} ] : {text}\n[ {name} ]: ")

    def play(self, player):
        if player.isAlive == False:
            return player
        else:
            u_answ = self.ask(self.quest, player.name)
            if u_answ == self.answ:
                self.say("Helyes válasz tovább mehetsz! És mostár vízed is van")
                player.list_of_items.append("víz")
                return player
            self.say("Helytelen válasz! Bele ragadtál a pókháloba :(")
            player.isAlive = False
            return player

class Door:
    def __init__(self, name):
        self.name = name

    def say(self, text):
        print(f"[ Door {self.name} ] : {text}")

    def ask(self, text, name):
        return input(f"[ Door {self.name} ] : {text}\n[ {name} ]: ")
    
    def chAnsw(self, pw):
        isValid = True
        for i in range(trunc(len(pw)/2)):
            if isValid:
                if pw[i] != pw[-(i+1)]:
                    isValid = False
        return isValid

    def addToPlayerInv(self, ch, player):
        first = self.matchIt(ch[0])
        sec = self.matchIt(ch[-1])

        player.list_of_items.append(first)
        player.list_of_items.append(sec)
        
    def matchIt(w):
        match w:
            case "1":
                return "gépfegyver"
            case"2":
                return "kés" 
            case "3": 
                return "gránát" 
            case "4":
                return "olló" 
            case "5":
                return "kanál"
            case "6": 
                return" futópad" 
            case "7":
                return" alma"



    def play(self, player):
        if player.isAlive == False:
            return player
        else:
            while True:
                answ = self.ask("Ráfogsz jönni??? vagy nem?", player.name)
                if self.chAnsw(answ):
                    list_of_nick_nacks = ["1: gépfegyver", "2: kés", "3: gránát", "4: olló", "5: kanál", "6: futópad", "7: alma"]
                    ch = self.ask(f"Helyes válasz nessze itt egy halom kaccat! #{list_of_nick_nacks}# (Válasz 2db ot, válaszodat igy formatáld: '1,2' ha a fegyvert és a kést szeretnéd)")
                    player = self.addToPlayerInv(ch, player)
                    return player
            

def main():
    #gen storyTeller
    game = StoryTeller()
    #gen player
    player = Character(game.ask("mi a neved?", "player"), [], 4, True)
    #Gen op
    dwarf0 = Dwarf("Erőske", [{"kerdes1?": "valasz1"}, {"kerdes2?": "valasz2"}, {"kerdes3?": "valasz3"}])
    spider0 = Spider("Soklábú", "50+50", "100")
    door0 = Door("Félős")
    
    #Game
    player = dwarf0.play(player)
    player.stats()
    player = spider0.play(player)
    player.stats()
    player = door0.play(player)
    player.stats()

    

main()