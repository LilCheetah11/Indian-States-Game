import turtle
import csv
import pandas


screen=turtle.Screen()
screen.setup(width=700,height=770,startx=400,starty=10)
screen.title("Indian States Game")

image="Indian States Game map.gif"
screen.addshape(image)

turtle.shape(image)

# data=pandas.read_csv("list-indian-states-and-capitals-28j.csv")

# all_states=data["State Name "].to_list
# # print(all_states)
# # def get_mouse_click_coor(x,y):
# #     print(x,y)


# # turtle.onscreenclick(get_mouse_click_coor)

# # turtle.mainloop()

# data_dict={
#     "States":all_states()
# }

# data_new=pandas.DataFrame(data_dict)
# data_new.to_csv("states_coor.csv")



data=pandas.read_csv("states_coor.csv")

all_states=data["States"].to_list

guessed_state=[]
score=0

while len(guessed_state)<28:
    

    answer_state=screen.textinput(title=f"{score}/28 States correct",prompt="Guess another state's name?").title()

    if answer_state=="exit".title():
        missing_states=[]
        for state in all_states():
            if state not in guessed_state:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)    
        new_data.to_csv("states_to_learn.csv")    
        break    
    if answer_state in all_states():
        score+=1
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data=data[data.States==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.States.item())

