import random

class hangman:
  word = ""
  wordTracker = []
  lives = 7
  is_game_finished = False
  duplicate = []

  # getter method for word
  def get_word(self): 
      return self.word
  # setter method for word
  def set_word(self, x): 
      self.word = x 
  
  # getter method for wordTracker
  def get_wordTracker(self): 
      return self.wordTracker
  # setter method for wordTracker
  def set_wordTracker(self, x): 
      self.wordTracker = x 

  # getter method for word
  def get_lives(self): 
      return self.lives
  # setter method for word
  def set_lives(self, x): 
      self.lives = x 

  # getter method for word
  def get_is_game_finished(self): 
      return self.is_game_finished
  # setter method for word
  def set_is_game_finished(self, x): 
      self.is_game_finished = x 
  
  # getter method for duplicate
  def get_duplicate(self): 
      return self.duplicate
  # setter method for duplicate
  def set_duplicate(self, x): 
      self.duplicate = x 

  def select_rand_word(self):
    word_list = ["At", "And", "Bat", "Cat", "Bait", "Because", "Soccer", "Electronic", "Anime", "Fire", "Motorcycle", "Mars", "Astronaut", "Human", "Zombie"]
    rand_int = random.randint(0, len(word_list))
    rand_word_select = word_list[rand_int]

    return rand_word_select.lower()
  
  def print_hangman(self, life_num):
    white = " "
    if life_num == 0:
      print(white*4 + "+-------+")
      print(white*4 + "|" + white*7 + "|")
      print(white*4 + "|" + white*7 + "O")
      print(white*4 + "|" + white*6 + "/|\\")
      print(white*4 + "|" + white*6 + "/ \\")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")
    elif life_num == 1:
      print(white*4 + "+-------+")
      print(white*4 + "|" + white*7 + "|")
      print(white*4 + "|" + white*7 + "O")
      print(white*4 + "|" + white*6 + "/|\\")
      print(white*4 + "|" + white*6 + "/")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")
    elif life_num == 2:
      print(white*4 + "+-------+")
      print(white*4 + "|" + white*7 + "|")
      print(white*4 + "|" + white*7 + "O")
      print(white*4 + "|" + white*6 + "/|\\")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")
    elif life_num == 3:
      print(white*4 + "+-------+")
      print(white*4 + "|" + white*7 + "|")
      print(white*4 + "|" + white*7 + "O")
      print(white*4 + "|" + white*6 + "/|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")
    elif life_num == 4:
      print(white*4 + "+-------+")
      print(white*4 + "|" + white*7 + "|")
      print(white*4 + "|" + white*7 + "O")
      print(white*4 + "|" + white*6 + "/")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")
    elif life_num == 5:
      print(white*4 + "+-------+")
      print(white*4 + "|" + white*7 + "|")
      print(white*4 + "|" + white*7 + "O")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")
    elif life_num == 6:
      print(white*4 + "+-------+")
      print(white*4 + "|" + white*7 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")
    elif life_num == 7:
      print(white*4 + "+-------+")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print(white*4 + "|")
      print("==========")

  def duplicate_check(self, du_input):
    #w = self.get_word()
    du_list = self.get_duplicate()
    #print("du list:", du_list)
    duplicate_tf = False
    for i in range(0, len(du_list)):
      if(du_input == du_list[i]):
        duplicate_tf = True
        #print(du_input, "vs ", du_list[i])
        #print("is true")
        #if(duplicate_tf == True):
         # break
    return duplicate_tf

      

  def guess(self):
    letter = ""
    l_error_counter = 0
    word_length = len(self.get_word())
    my_guess = input("Guess a letter: ")
    my_guess.lower()
    

    is_duplicate = False
    is_duplicate = self.duplicate_check(my_guess)
    dupli = self.get_duplicate()
    dupli.append(my_guess)
    self.set_duplicate(dupli)

    print("Past Entries: ", self.get_duplicate())

    if(is_duplicate == True):
      print("\nYou already input this letter!\n")
    else:
      for i in range(0, word_length):
        letter = self.get_word()[i]
        if letter == my_guess:   #if it does match
          self.print_hangman(hm_game.get_lives())###
          self.tracker(i, letter)

        else:  #if does not match
          l_error_counter += 1
          if l_error_counter == word_length:
            print("\nWrong")
            life_decounter = self.get_lives()
            life_decounter -= 1
            self.set_lives(life_decounter)
            self.print_hangman(hm_game.get_lives())

          
  def init_fill_tracker(self):
    w_length = len(self.get_word())
    w_track = self.get_wordTracker()
    for i in range(0, w_length):
      #w_track.insert(i, "_")
      if w_length > len(w_track):
        w_track.append("")
      w_track[i] = "_"
    self.set_wordTracker(w_track)
    print(self.get_wordTracker())


  def tracker(self, track_i, track_l):
    track = self.get_wordTracker()
    track[track_i] = track_l
    self.set_wordTracker(track)
    print(self.get_wordTracker())
    # for i in range(0, len(track)):
    #   track_letter = track[i]
      # #code to see if element in list is empty
      # if track[i]:
      #     print('Found element!')
      #     print(track_letter)
      # else:
      #     print('Empty element.')
      #     print(" _ ")
  

  def game_finished_check(self):
    fin_track = self.get_wordTracker()
    fin_word = self.get_word()
    fin_length = len(self.get_word())
    new_track = ""
    for i in range(0, fin_length): 
      new_track += fin_track[i]

    if(new_track == fin_word):
      game_fin = True
      self.set_is_game_finished(game_fin)


#---------------------------------------------------
        
hm_game = hangman()
new_word = hm_game.select_rand_word()
hm_game.set_word(new_word)
#print("Secret Word: ", hm_game.get_word())
hm_game.print_hangman(hm_game.get_lives())
hm_game.init_fill_tracker()


gameloop = True
while gameloop == True:
  hm_game.guess()
  hm_game.game_finished_check()
  if hm_game.get_lives() == 0:
    print("Out of lives x( ")
    break
  elif hm_game.get_is_game_finished() == True:
    print("CONGRATS YOU FOUND THE WORD:", hm_game.get_word())
    break
  


#Note: dont try to run code like in Java's main method
#run code outside python is a scripting lang