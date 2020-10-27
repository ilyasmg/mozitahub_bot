# Mozilla Italia Bot - @MozItaBot
Questo è il repository del bot di Mozilla Italia "@MozItaBot" su Telegram.

# Questo è il branch beta.
#Eventuali cambiamenti modifiche ecc sono da considerarsi non stabili.

pip install -r requirements.txt

Definire il file .env in questo modo e metterlo nella root del progetto:

```
TOKEN=your-token
NEWS_CHANNEL=@your-news-channel
```

# Differenze con il vecchio bot
I file sono gestiti tramite TinyDB, un database.

Ogni file ha il suo DB.

Sono sempre JSON ma rendono più semplice la cancellazione, l'inserimento ecc. inoltre vengono gestite mediante semplici query.
