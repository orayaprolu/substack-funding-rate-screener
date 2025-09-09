from config import EXCHANGE
from libraries.orchestrator import Orchestrator


print(f'Getting funding rates for {EXCHANGE.id}...')
orchestrator = Orchestrator(EXCHANGE)
orchestrator.display()
orchestrator.save_to_csv(f"funding_rates_{EXCHANGE.id}.csv")
