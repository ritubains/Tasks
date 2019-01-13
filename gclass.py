# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:23:24 2019

@author: ritu bains
"""

import random



class Game():
    words = ["bob", "cool", "whatup"]

    secret_word = random.choice(words)
    def update_dashes(self,secret, cur_dash, rec_guess):
         result = ""
         for i in range(len(secret)):
              if secret[i] == rec_guess:
                  result = result + rec_guess 
              else:
                   result = result + cur_dash[i]
        
         return result
            
         
    
    def get_guess(self):
        dashes = "-" * len(self.secret_word)
        guesses_left = 10
        
     
        while guesses_left > -1 and not dashes == self.secret_word:
            print(dashes)
            print (str(guesses_left))
            guess = input("Guess:")
            if len(guess) != 1:
                print ("Your guess must have exactly one character!")
            elif guess in self.secret_word:
                print ("That letter is in the secret word!")
                dashes = update_dashes(self,self.secret_word, dashes, guess)
            else:
                print ("That letter is not in the secret word!")
                guesses_left -= 1
        if guesses_left < 0:
            print ("You lose. The word was: " + str(self.secret_word))
        else:
            print ("Congrats! You win. The word was: " + str(self.secret_word))
                
                
                
obj=Game()
obj.get_guess()
                
   
    
             
    
    
             
             
                  
             
                  
             
                  
              
              
                  
  
 
              
                  
      
     
          
             
  
             
                    
                       
                      
                   
                      
                     
      
   
    
  
   
    
    
    
    
  
 
  
  

  
  
   

    

get_guess()
    


  
    

