# This script generates a folder structure for ljspeech-1.1 processing from mimic-recording-studio database
# Written as first python script (eg. helloworld) by Thorsten Mueller (MrThorstenM@gmx.net) on november 2019 without any warranty

import sqlite3
import os
from datetime import datetime
from shutil import copyfile

# please set following vars matching your environment
# ---------------------------------------------------

# Directory of mimic-recording-studio (eg: /home/thorsten/mimic-recording-studio)
directory_base_mrs = "/home/thorsten/tts/mimic-recording-studio"
# Output directory for ljspeech structure (eg: /tmp/tts)
directory_base_ljspeech = "/home/thorsten/tts"
# See /mimic-recording-studio/backend/audio_files/<id> (eg: 3beeae88-0777-2c8c-5c93-2e844a462e26)
speaker_id = "4aeeae88-0777-2c8c-5c93-2e844a462e49" 

# -----------------------
# end of environment vars

# Create needed folder structure for ljspeech-1.1
def folder_creation():
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y_%H-%M-%S")

    global directory_base_ljspeech
    directory_base_ljspeech = directory_base_ljspeech + "/ljspeech_" + dt_string + "/LJSpeech-1.1"

    if not os.path.exists(directory_base_ljspeech):
                os.makedirs(directory_base_ljspeech)

    if not os.path.exists(directory_base_ljspeech + "/wavs"):
                os.makedirs(directory_base_ljspeech + "/wavs")

def main():
    folder_creation()

    conn = sqlite3.connect(directory_base_mrs + '/backend/db/mimicstudio.db')
    c = conn.cursor()

    # Create new metadata.csv for ljspeech
    metadata = open(directory_base_ljspeech + "/metadata.csv",mode="w", encoding="utf8") 

    # todo: Check best order for performance of tacotron training
    for row in c.execute('SELECT audio_id, prompt, lower(prompt) FROM audiomodel ORDER BY length(prompt)'):
        metadata.write(row[0] + "|" + row[1] + "|" + row[2] + "\n")
        copyfile(directory_base_mrs + "/backend/audio_files/" + speaker_id + "/" + row[0] + ".wav",directory_base_ljspeech + "/wavs/" + row[0] + ".wav")

    metadata.close()
    conn.close()

if __name__ == '__main__':
    main()