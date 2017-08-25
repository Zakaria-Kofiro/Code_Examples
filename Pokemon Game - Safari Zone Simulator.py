
#Safari Zone Simulator 



import tkinter as tk
import random


class Pokemon:
    """
    This class creates a Pokemon object with attributes such as
    its species, pokedex number, catch rate, and escape speed.  
    """
    def __init__(self, dex, species, catch, speed):
        self.__species = species
        self.__dex = dex
        self.__catch = catch
        self.__speed = speed 
    def __str__(self):
        return str(self.__species)
    def __repr__(self):
        return self.__species
    def dex(self):
        return self.__dex
    def catch(self):
        return self.__catch
    def prob(self):
        rate = self.__catch 
        return int((min(rate+1, 151)/449.5)*100)
    def speed(self):
        return self.__speed  







class SafariSimulator(tk.Frame):
    """
    This class creates the canvas for the game, and consists of the
    various methods that make up the game. This class needs a pokedex
    spreadsheet and sprite images to load up the game. 
    """
    def __init__(self, master=None):
        """
        Data file from pokedex.csv is read in and stored
        and used to randomly create a Pokemon object 
        """
        self.data = []
        file = open("pokedex.csv", "r")
        title = file.readline()
        line = file.readline()
        while line != "":
            pokemon = line.strip("\n").split(",")
            self.data.append(pokemon)
            line = file.readline()
        x = random.randint(1,150)
        self.poke = Pokemon(int(self.data[x][0]),self.data[x][1],int(self.data[x][2]),int(self.data[x][3]))
        
        
        #Instance Variables 
        self.pokeList = [] #this contains amount of pokemon the user has caught 
        self.balls = 30 #this keeps track of how many pokeballs the user has 
        
        #These lines set basic window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        """
        This method creates widgets for the canvas to display information
        about the game, along with allowing the user to interact with
        the game. 
        """

        #Creates a "throwButton" widget 
        self.throwButton = tk.Button(self)
        stringBall = "Throw Safari Ball " + "(" + str(self.balls) + " left)"
        self.throwButton["text"] = stringBall 
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack()
        
        #Creates a "Run Away" widget 
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()
        
        #Creates a status bar 
        string = "You encounter a wild " + str(self.poke)
        self.messageLabel = tk.Label(bg= "#bfbfbf" , text = string )
        self.messageLabel.pack(fill="x", padx=5, pady=5)



        #Displays an image of the current pokemon 
        self.image = tk.PhotoImage(file = "sprites/" + str(self.poke.dex()) + ".gif")
        self.imageLabel = tk.Label()
        self.imageLabel["image"] = self.image
        self.imageLabel.pack() 

        #Displays the catch rate of the pokemon
      
        string = "Your chance of catching it is " + str(self.poke.prob()) + "%!" 
        self.catchLabel = tk.Label(bg= "#bfbfbf" , text = string )
        self.catchLabel.pack(fill="x", padx=5, pady=5)
 
    def nextPokemon(self):
        """
        This method randomly generates a new pokemon, and then adjusts the
        information on screen to match the pokemon
        """
        x = random.randint(1,151)
        self.poke = Pokemon(int(self.data[x][0]),self.data[x][1],int(self.data[x][2]),int(self.data[x][3]))
        
        
        #messageLabel and catchRateLabel text is set to match this pokemon
        string2 = "You encounter a wild " + str(self.poke)
        self.messageLabel["text"] = string2

        string3 = "Your chance of catching it is " + str(self.poke.prob()) + "%!"
        self.catchLabel["text"] = string3

        
        #changes the pokemonImageLabel to show the right pokemon
        self.newImage = tk.PhotoImage(file = "sprites/" + str(self.poke.dex()) + ".gif")
        self.imageLabel["image"] = self.newImage
        self.imageLabel.pack() 
            
         
    def endAdventure(self):
        """ 
        This method displays adventure completion message, along with
        a list of pokemon the user caught during the game. 

        """
        self.throwButton.pack_forget()
        self.runButton.pack_forget()
        self.imageLabel.pack_forget()

        endgameString = "You're all out of balls, hope you had fun!"
        self.messageLabel["text"] = endgameString 
        
        
        #list captured pokemon
        if len(self.pokeList) == 0:
            self.catchLabel["text"] = "Oops, you caught 0 Pokemon."
        else:
            a = "" 
            for i in range(len(self.pokeList)):
                a = a + str(self.pokeList[i]) + "\n"
            endString = "You caught " + str(len(self.pokeList)) + " Pokemon:"
            self.catchLabel["text"] = endString + "\n" + a 

    def throwBall(self):
        """
        This method decrements the number of balls remaining as the user
        uses them throughout the game. When the number of pokeballs remaining
        reaches zero, the endAdventure() method is called to end the game. 
        """

   
        self.balls = self.balls - 1
        newBall = "Throw Safari Ball " + "(" + str(self.balls) + " left)"
        self.throwButton["text"] = newBall
        self.throwButton.pack() 
            #checks to see if endAdventure() should be called
        if self.balls == 0:
            self.endAdventure() 
            #otherwise, allows user to try to catch the pokemon
            #and generates a new one if it is caught 
        else:
            prob = self.poke.prob() 
            chance = random.randrange(100)
            if chance <= prob:
                self.pokeList.append(self.poke)
                self.nextPokemon()
                 
            else:
                notCaught = "Aargh! It escaped!"
                self.messageLabel["text"] = notCaught 
            
        




app = SafariSimulator(tk.Tk())
app.mainloop()


