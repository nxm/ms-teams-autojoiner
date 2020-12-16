from discord_webhooks import DiscordWebhooks
from helper import Colors

def sendMessage(config, className, status):

    webhook = DiscordWebhooks(config['webhookURL'])
    webhook.set_footer(text='github.com/nxm')

    if status == 'success':
        print('{}Joined successfully!\n{}Sending notification to discord{}'.format(Colors.GREEN, Colors.BLUE, Colors.RESET))
        webhook.set_content(title='Class joined successfully!', description=className)

    webhook.send()