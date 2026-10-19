# MNQ News-Bias

Handy-App für Termine und Nachrichten mit Einfluss auf den Micro-Nasdaq-100-Future (MNQ). Jede Meldung ist grün (bullish) oder rot (bearish) eingestuft, daraus berechnet die App einen Tages- und einen Wochen-Bias. Große Termine wie Inflationsdaten oder der Fed-Zinsentscheid stehen in einem eigenen Feld mit Ergebnis und Prognose.

- `index.html`: die App
- `data/news.json`: die Meldungen. Claude aktualisiert die Datei an jedem Handelstag vor der Asien-, London- und New-York-Session.
- `manifest.webmanifest`, `sw.js`, `icons/`: Installation auf dem Home-Bildschirm und Offline-Speicher
- `.github/workflows/claude-suchen.yml`: startet eine neue Claude-Prüfung, wenn du in der App auf „Aktualisieren“ tippst. Dafür braucht das Repository das Secret `ROUTINE_TOKEN` (Claude-Schlüssel der Prüfung) und die App einmal einen GitHub-Schlüssel mit der Berechtigung „Actions: Read and write“ für dieses Repository. Der GitHub-Schlüssel bleibt nur auf dem Handy.

Installieren auf dem iPhone: Seite in Safari öffnen, Teilen-Symbol, „Zum Home-Bildschirm“.

Keine Anlageberatung.
