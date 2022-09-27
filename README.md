
# Ping-Log
A discord Bot to log every role ping on your Server

##  Installation

Clone the repo

    git clone https://github.com/Yuutokata/Ping-Log.git
    cd Ping-Log
  
Install the dependencies

    pip install -r requirements.txt

Start the Bot

    python launcher.py


### Installation with Docker

Build the docker Image

    docker build -t ping .


Run the docker Container

    docker run ping



## Setup

 - Token -> Your token
- Prefix -> your prefix
- Description -> Your description
- Activity -> What the game text
- Status -> The preference from the Bot
	 0 = Online
	 1 = Idl
	 2 = DnD
	 3 = Invisible

- Color -> Embed Color 
- Icon -> Footer Icon

- save -> true / false if the log should get saved
- guild -> Your guild ID

