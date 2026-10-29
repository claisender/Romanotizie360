# Roma Notizie 360 — romanotizie360.it

Sito dimostrativo predisposto per pubblicare automaticamente titoli e collegamenti alle notizie su Roma da feed RSS Google News. Gli articoli completi restano sui siti delle fonti.

## Attivazione
1. Verifica la disponibilità e acquista **romanotizie360.it** presso un registrar (il dominio NON è stato acquistato né attivato).
2. Crea un repository GitHub pubblico e carica il contenuto di questa cartella, inclusa `.github/workflows`.
3. In GitHub, Settings > Pages, scegli Deploy from a branch, `main`, `/ (root)`.
4. In Settings > Actions > General abilita i permessi di scrittura dei workflow se richiesto.
5. In Actions avvia manualmente **Aggiorna notizie Roma Notizie 360**: il workflow genera `news.json` e tenta un aggiornamento ogni 2 ore. GitHub può ritardare o sospendere i job programmati.
6. In Settings > Pages configura il dominio personalizzato `romanotizie360.it`. Presso il registrar configura i record DNS A per GitHub Pages secondo le istruzioni ufficiali aggiornate di GitHub e, se desideri, il CNAME `www` verso `<nomeutente>.github.io`. Attendi propagazione e abilita HTTPS. Verifica che il dominio sia tuo prima di puntarlo.

## Importante
La pagina mostra contenuti dimostrativi finché `news.json` non è stato generato. La disponibilità dei feed e i diritti di utilizzo vanno verificati prima dell'impiego commerciale. Le foto sono illustrative. Nessuna notizia è stata verificata editorialmente. Il progetto non è stato pubblicato online e non è ancora collegato al dominio.
