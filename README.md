# paired-claim-bootstrap

## Français

Estimer les différences appariées avec blocs et hypothèses explicites.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m paired_claim_bootstrap examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Bootstrap apparié par blocs avec graine fixe : conserve ensemble les observations corrélées d’un bloc et expose le sens B−A, le nombre réel d’unités de rééchantillonnage et l’intervalle percentile.

### Limites

Hypothèses de blocs indépendants et représentatifs à vérifier ; pas d’inférence causale, de correction multiple ou de garantie universelle de couverture. Un seul bloc reste signalé non informatif.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Estimate paired differences with blocks and explicit assumptions.

Synthetic data; no network access or secret required.

```sh
python -m paired_claim_bootstrap examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Seeded paired block bootstrap keeps correlated observations together and exposes B−A direction, actual resampling-unit count and percentile interval.

### Limits

Independent representative block assumptions require verification; no causal inference, multiple-testing correction or universal coverage guarantee. One block remains flagged uninformative.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Estimar diferencias emparejadas con bloques e hipótesis explícitas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m paired_claim_bootstrap examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Bootstrap emparejado por bloques con semilla conserva observaciones correlacionadas y expone dirección B−A, número real de unidades y intervalo percentil.

### Límites

Requiere verificar bloques independientes y representativos; sin inferencia causal, corrección múltiple ni garantía universal de cobertura. Un solo bloque se marca no informativo.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/gbesse/decision-claim-card
- https://artowen.su.domains/mc/
