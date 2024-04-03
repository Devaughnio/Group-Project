class YouDontKnowAnythingAboutMe(object):
    def __init__(self):
        # Initialize all attributes to None
        self.w_bored = None
        self.f_color = None
        self.f_food = None
        self.f_movie_genre = None
        self.f_music = None
        self.f_animal = None
        self.f_sport = None
        self.f_dessert = None

    def welcome_message(self):
        print("*** Welcome To You Don't Know Anything About Me  ***")
        print("\n-----\nHow it works: ")
        print("There will be a list of choices.")
        print("The first player will choose the option best describing them.")
        print("The second player will choose the option they think represents player one.")
        print("Let's see how well you know each other.")
        print("You'll get your score at the end. Good Luck!!\n-----")
    
        
    def start_YouDontKnowAnythingAboutMe(self):
        start = input("\nAre you ready to begin?: ")
        if start == "yes":
            print("\n***\nYou Don't Know Anything About Me Loading...\n***")
        elif start == "no":
            print("\nSee you next time!")
            exit()
        else:
            print("\nInvalid entry.")
            exit()
    
    def play_game(self):
        print("*** Choices ***")
        print("\n-----\n")
        print("What do you do when you are bored: ")
        print("A. Read a book, B. Watch a Movie, C. Listen to music")
        while True:
            self.w_bored = input("\n-----\n Answer= ")
            if self.w_bored.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
                
        print("What is your favorite color:")
        print("A. Blue, B. Red, C. Green")
        while True:
            self.f_color = input("\n-----\n Answer= ")
            if self.f_color.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
                
        
        print("What is your favorite food:")
        print("A. Pizza, B. KFC, C. Burger King")
        while True:
            self.f_food = input("\n-----\n Answer= ")
            if self.f_food.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
                
                
        print("What is your favorite movie genre:")
        print("A. Comedy, B. Action, C. Drama")
        while True:
            self.f_movie = input("\n-----\n Answer= ")
            if self.f_movie.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
                
                
        print("What is your favorite music genre:")
        print("A. Dancehall, B. Soca, C. R&B")
        while True:
            self.f_music = input("\n-----\n Answer= ")
            if self.f_music.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
                
                
        print("What is your favorite animal:")
        print("A. Dog, B. Cat, C. Bird")
        while True:
            self.f_animal = input("\n-----\n Answer= ")
            if self.f_animal.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
            
        
        print("What is your favorite sport:")
        print("A. Football, B. Basketball, C. Volleyball")       
        while True:
            self.f_sport = input("\n-----\n Answer= ")
            if self.f_sport.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
                
        
        print("What is your favorite dessert:")
        print("A. Ice Cream, B. Cake, C. Pie")
        while True:
            self.f_dessert = input("\n-----\n Answer= ")
            if self.f_dessert.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
                
        print("\n-----")

    def answer(self):
        print("*** What would they choose? ***")
        correct = 0
        incorrect = 0
        print("\n-----\n")
        print(" What do they do when they are bored: ")
        print("A. Read a book, B. Watch a Movie, C. Listen to music")
        while True:
            a_w_bored = input("\n-----\n Answer= ")
            if a_w_bored.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_w_bored == self.w_bored:
            correct += 1
        else:
            incorrect += 1
                
        print("What is their favorite color:")
        print("A. Blue, B. Red, C. Green")
        while True:
            a_f_color = input("\n-----\n Answer= ")
            if a_f_color.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_f_color == self.f_color:
            correct += 1
        else:
            incorrect += 1
        
        print("What is their favorite food:")
        print("A. Pizza, B. KFC, C. Burger King")
        while True:
            a_f_food = input("\n-----\n Answer= ")
            if a_f_food.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_f_food == self.f_food:
            correct += 1
        else:
            incorrect += 1
            
        print("What is their favorite movie genre:")
        print("A. Comedy, B. Action, C. Drama")
        while True:
            a_f_movie_genre = input("\n-----\n Answer= ")
            if a_f_movie_genre.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_f_movie_genre == self.f_movie_genre:
            correct += 1
        else:
            incorrect += 1
               
        print("What is their favorite music genre:")
        print("A. Dancehall, B. Soca, C. R&B")
        while True:
            a_f_music = input("\n-----\n Answer= ")
            if a_f_music.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_f_music == self.f_music:
            correct += 1
        else:
            incorrect += 1
                    
        print("What is their favorite animal:")
        print("A. Dog, B. Cat, C. Bird")
        while True:
            a_f_animal = input("\n-----\n Answer= ")
            if a_f_animal.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_f_animal == self.f_animal:
            correct += 1
        else:
            incorrect += 1
            
        print("What is their favorite sport:")
        print("A. Football, B. Basketball, C. Volleyball")       
        while True:
            a_f_sport = input("\n-----\n Answer= ")
            if a_f_sport.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_f_sport == self.f_sport:
            correct += 1
        else:
            incorrect += 1
            
        print("What is their favorite dessert:")
        print("A. Ice Cream, B. Cake, C. Pie")
        while True:
            a_f_dessert = input("\n-----\n Answer= ")
            if a_f_dessert.upper() in ['A', 'B', 'C']:
                break
            else:
                print("Invalid response. Please enter 'A', 'B', or 'C'.")
        if a_f_dessert == self.f_dessert:
            correct += 1
        else:
            incorrect += 1
        
        print("\n-----")
        print("You got", correct, "correct and", incorrect, "incorrect.")
        
        if correct <= 2:
            print("You Don't Know Anything About Me")
        elif correct > 2 and correct <= 5:
            print("You Know a Little About Me")
        elif correct > 5 and correct <= 8:
            print("WOW!! You actually Know ME")
        

if __name__ == "__main__":
    knowledge = YouDontKnowAnythingAboutMe()
    knowledge.welcome_message()
    knowledge.start_YouDontKnowAnythingAboutMe()
    knowledge.play_game()
    knowledge.answer()
