"""Configuration only: no offense data or screen access."""
from dataclasses import dataclass
from datetime import date
from pathlib import Path
import tomllib

AREAS = ('Central', 'Rampart', 'Southwest', 'Hollenbeck', 'Harbor', 'Hollywood',
         'Wilshire', 'West LA', 'Van Nuys', 'West Valley', 'Northeast', '77th Street',
         'Newton', 'Pacific', 'N Hollywood', 'Foothill', 'Devonshire', 'Southeast',
         'Mission', 'Olympic', 'Topanga')

@dataclass(frozen=True)
class Defaults:
    default_area: str
    start: date
    end: date

def load_defaults(path: Path = Path('configs/default.toml')) -> Defaults:
    with path.open('rb') as handle:
        values = tomllib.load(handle)
    expected = {'default_area', 'start', 'end'}
    if set(values) != expected:
        raise ValueError(f'config keys: missing {expected - set(values)}, unknown {set(values) - expected}; values={values!r}')
    if values['default_area'] not in AREAS:
        raise ValueError(f'default_area: {values["default_area"]!r} is not a LAPD Area')
    parsed = {}
    for key in ['start', 'end']:
        try:
            parsed[key] = date.fromisoformat(str(values[key]))
        except (ValueError, TypeError):
            raise ValueError(f'{key}: invalid date {values[key]!r}') from None
    if parsed['start'] < date(2025, 2, 1):
        raise ValueError(f'start: {values["start"]!r} must be on or after 2025-02-01')
    if parsed['end'] <= parsed['start']:
        raise ValueError(f'end: {values["end"]!r} must be after start {values["start"]!r}')
    return Defaults(values['default_area'], **parsed)
