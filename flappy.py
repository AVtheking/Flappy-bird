import pygame
from pygame.locals import*
import random
import pickle

pygame.init()
clock=pygame.time.Clock()
fps=60
screen_width=864
screen_height=636

#game variable
ground_scroll=0
scroll_speed=4
flying=False
game_over=False
pipe_gap=150
pipe_frequency=1500#miliseconds
last_pipe=pygame.time.get_ticks()-pipe_frequency
score=0
pass_pipe=False
frames=[]

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Flappy Bird')

#define fonts
font=pygame.font.SysFont('Bauhaus 93',60)
white=(255,255,255)


#background
bg=pygame.image.load('gallery/images/bg.png')
bg=pygame.transform.scale(bg,(screen_width,screen_height))
ground=pygame.image.load('gallery/images/ground.png')
button_img=pygame.image.load('gallery/images/restart.png')
# ground=pygame.transform.scale(ground,(screen_width,screen_height))
def draw_text(text,font,text_col,x,y):
    img=font.render(text,True,text_col)
    screen.blit(img,(x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x=100
    flappy.rect.y=int(screen_height/2)
    score=0#local variable
    return score


def replay():
    # Replay frames
    # flappy2 = Bird2(100, int(screen_height / 3))
    # bird_group.add(flappy2)
    class Bird(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)  # 2D game class
            self.images = []
            self.index = 0
            self.count = 0
            for num in range(1, 4):
                img = pygame.image.load(f'gallery/images/bird{num}.png')
                self.images.append(img)

            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.clicked = False

        def update(self):
            # gravity in the game
            if flying == True:
                self.vel += 0.5
                if self.vel > 8:
                    self.vel = 8
                if self.rect.bottom < 536:
                    self.rect.y += int(self.vel)

            if game_over == False:
                # jump
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.vel -= 10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                    # for event in pygame.event.get():
                    #
                    #         if event.type==pygame.QUIT:
                    #             pygame.quit()
                    #         if event.type == pygame.KEYDOWN:
                    #             if event.key==K_UP or event.key==K_SPACE:
                    #                 self.vel-=10

                # handle animation
                self.count += 1
                flap_cooldown = 5
                # feather speed
                if self.count > flap_cooldown:
                    self.count = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                self.image = self.images[self.index]

                # rotate image
                self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
            else:
                self.image = pygame.transform.rotate(self.images[self.index], -90)
            bird_group.update()
    for frame in frames:
        # Convert frame to surface and draw on screen
        surf = pygame.surfarray.make_surface(frame)
        screen.blit(surf, (0, 0))
        pygame.display.flip()

        # Wait for next frame
        clock.tick(fps)

    def save_frames(filename):
        # Save frames list to file
        with open(filename, 'wb') as f:
            pickle.dump(frames, f)

    def load_frames(filename):
        # Load frames list from file
        with open(filename, 'rb') as f:
            frames = pickle.load(f)




class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)#2D game class
        self.images=[]
        self.index=0
        self.count=0
        for num in range(1,4):
            img=pygame.image.load(f'gallery/images/bird{num}.png')
            self.images.append(img)

        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False

    def update(self):
        #gravity in the game
        if flying==True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 536:
                    self.rect.y += int(self.vel)

        if game_over==False:
        #jump
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel-=10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False

                # for event in pygame.event.get():
                #
                #         if event.type==pygame.QUIT:
                #             pygame.quit()
                #         if event.type == pygame.KEYDOWN:
                #             if event.key==K_UP or event.key==K_SPACE:
                #                 self.vel-=10






            #handle animation
            self.count+=1
            flap_cooldown=5
          #feather speed
            if self.count>flap_cooldown:
                self.count=0
                self.index+=1
                if self.index>=len(self.images):
                     self.index=0
            self.image=self.images[self.index]

            #rotate image
            self.image=pygame.transform.rotate(self.images[self.index],self.vel*-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)


# class Bird2(pygame.sprite.Sprite):
#     def __init__(self,x,y):
#         pygame.sprite.Sprite.__init__(self)#2D game class
#         self.images=[]
#         self.index=0
#         self.count=0
#         for num in range(1,4):
#             img=pygame.image.load(f'gallery/images/bird{num}.png')
#             self.images.append(img)
#
#         self.image=self.images[self.index]
#         self.rect=self.image.get_rect()
#         self.rect.center=[x,y]
#         self.vel=0
#         self.clicked=False
        # replay();
        # frames=[]

        # def update(self):
    #     #gravity in the game
    #     if flying==True:
    #         self.vel += 0.5
    #         if self.vel > 8:
    #             self.vel = 8
    #         if self.rect.bottom < 536:
    #                 self.rect.y += int(self.vel)
    #
    #     if game_over==False:
    #     #jump
    #         if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
    #             self.clicked=True
    #             self.vel-=10
    #         if pygame.mouse.get_pressed()[0]==0:
    #             self.clicked=False
    #
    #             # for event in pygame.event.get():
    #             #
    #             #         if event.type==pygame.QUIT:
    #             #             pygame.quit()
    #             #         if event.type == pygame.KEYDOWN:
    #             #             if event.key==K_UP or event.key==K_SPACE:
    #             #                 self.vel-=10
    #
    #
    #
    #
    #
    #
    #         #handle animation
    #         self.count+=1
    #         flap_cooldown=5
    #       #feather speed
    #         if self.count>flap_cooldown:
    #             self.count=0
    #             self.index+=1
    #             if self.index>=len(self.images):
    #                  self.index=0
    #         self.image=self.images[self.index]
    #
    #         #rotate image
    #         self.image=pygame.transform.rotate(self.images[self.index],self.vel*-2)
    #     else:
    #         self.image = pygame.transform.rotate(self.images[self.index], -90)


class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('gallery/images/pipe1.png')
        self.rect=self.image.get_rect()
        #position 1 is from the top and -1 from the bottom
        if position==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipe_gap/2)]
        if position==-1:
            self.rect.topleft=[x,y+int(pipe_gap/2)]

    def update(self):
        self.rect.x-=scroll_speed
        if self.rect.right<0:
            self.kill()

class Button:
    def __init__(self,image,x,y):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        #check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                # replay();
                action=True


        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action



bird_group=pygame.sprite.Group()
pipe_group=pygame.sprite.Group()
#flappy bird on screen
flappy=Bird(100,int(screen_height/2))


bird_group.add(flappy)


#restart button
button=Button(button_img,screen_width//2-50,screen_height//2-100)

run=True

while run:
    clock.tick(fps)

    #draw background
    screen.blit(bg,(0,0))# nothing will happen we need to add a function (update) function
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)

    #draw the ground
    screen.blit(ground, (ground_scroll, 536))

    #check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(str(score),font,white,int(screen_width/2),20)

    #check if bird hit the pipe
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or flappy.rect.top<0:
        game_over=True
# check if bird hit the ground
    if flappy.rect.bottom>536:
        game_over=True
        flying=False

    #draw ground
    if game_over==False and flying==True:
        #generating pipe
        time_now=pygame.time.get_ticks()
        if time_now-last_pipe>pipe_frequency:
            pipe_height=random.randint(-100,100)
            btm_pipe = Pipe(screen_width, int(screen_height / 2)+pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height / 2)+pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe=time_now
            # replay();

        #scrolling ground
        ground_scroll-=scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        pipe_group.update()

    if game_over==True:
       if  button.draw()==True:
           game_over=False
           # frames=[]
           score=reset_game()
           # flappy2 = Bird2(100, int(screen_height / 3))
           # bird_group.add(flappy2)
           # flappy = Bird(100, int(screen_height / 2))

           # bird_group.add(flappy)
       # if flying==True:
       #     replay();
           # frames=[]

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and flying==False and game_over==False:
            flying=True
    # frames=[]
    
    pygame.display.update()
pygame.quit()