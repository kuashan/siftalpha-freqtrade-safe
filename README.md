# SiftAlpha Freqtrade Safe Adapter V1

Public, non-trading adapter used to validate:

SiftAlpha → Coolify → Docker Compose → FreqUI

## Safety boundaries

- Uses the official `freqtradeorg/freqtrade:stable` image.
- Starts `freqtrade webserver`, not `freqtrade trade`.
- `dry_run=true`.
- Exchange API key and secret are empty.
- No live trading process is started.
- `force_entry_enable=false`.
- Initial state is `stopped`.
- Port 8080 is exposed only inside the Compose network; there is no host `ports:` publication.
- The committed FreqUI credentials are pilot-only public test credentials. Do not reuse them for live trading.

## SiftAlpha import

- Repository: `https://github.com/kuashan/siftalpha-freqtrade-safe`
- Branch: `main`
- Web port: `8080`
- Suggested project name: `freqtrade-safe-v1`

## Completion gate

The deployment passes only when SiftAlpha can:

1. import this public repository through Coolify,
2. deploy the Compose service,
3. reach RUNNING,
4. configure the WireGuard-only private domain,
5. Open FreqUI,
6. preserve no-API-key and no-live-trading boundaries.
