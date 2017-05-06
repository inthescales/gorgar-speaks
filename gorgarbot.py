import gorgarspeaks
from botbuddy import BotBuddy

credentials = {
    BotBuddy.creds_file_key : "creds.json"
}
    
buddy = BotBuddy()
buddy.setup(gorgarspeaks.speak, interval="4h", retry=True, credentials=credentials)
buddy.launch()
