# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def on_on_chat(steps):
    agent.move(LEFT, steps)
player.on_chat("ml", on_on_chat)

def on_on_chat2():
    agent.turn(RIGHT)
player.on_chat("tr", on_on_chat2)

def on_on_chat3(steps2):
    agent.move(BACK, steps2)
player.on_chat("bk", on_on_chat3)

def on_on_chat4(steps3):
    agent.move(RIGHT, steps3)
player.on_chat("mr", on_on_chat4)

def on_on_chat5(steps4):
    agent.move(FORWARD, steps4)
player.on_chat("fw", on_on_chat5)

def on_on_chat6():
    agent.turn(LEFT)
player.on_chat("tl", on_on_chat6)

def on_on_chat7():
    pass
player.on_chat("run", on_on_chat7)

def on_on_chat8(steps5):
    agent.move(UP, steps5)
player.on_chat("up", on_on_chat8)

def on_on_chat9(steps6):
    agent.move(DOWN, steps6)
player.on_chat("dw", on_on_chat9)

def on_on_chat10():
    agent.teleport_to_player()
player.on_chat("come", on_on_chat10)
def ObstacleCourse():
    agent.move(FORWARD, 4)
    agent.move(LEFT,4)
    agent.move(FORWARD,3)
    agent.move(UP,1)
    agent.move(FORWARD, 1)
    agent.move(UP,1)
    agent.move(FORWARD, 1)
    agent.move(UP,1)
    agent.move(FORWARD, 3)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
player.on_chat("go", ObstacleCourse)
def Chat():
    for count in range(5):
        agent.move(FORWARD,1)
player.on_chat("say", Chat)
def Chop(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN,height)
    agent.collect_all()
player.on_chat("chop",Chop)
def mine(length):
    for i in range(length):
        agent.move(FORWARD,1)
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.destroy(UP)
        agent.collect_all()
player.on_chat("mine", mine)
def BuildWall(height, width):
    for j in range(width):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP,1)
        agent.move(RIGHT, 1)
        agent.move(DOWN,height)
player.on_chat("buildwall", BuildWall)
def buildroof(length,width):
    for a in range(width):
        for x in range(length):
            agent.move(FORWARD,1)
            agent.place(DOWN)
        agent.move(RIGHT,1)
        agent.move(BACK,length)
player.on_chat("buildroof", buildroof)
def Digdown():
    while agent.detect(AgentDetection.BLOCK, DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN,1)
player.on_chat("digdown", Digdown)
def buildbridge(length,width):
    for i in range(width):
        for j in range(length):
            agent.move(FORWARD,1)
            agent.place(DOWN)
        agent.move(RIGHT,1)
        agent.move(BACK,length)
player.on_chat("buildbridge", buildbridge)
