# Simple Address Parser

## Note
This is intended only as a personal project and a proof of concept

## Usage
Just clone and execute in your terminal as follows

```
python -m address_parser "Musterstrasse 45"
```

which would yield a tuple denoting (house, street)

```
('45', 'Musterstrasse')
```

## Summary
Address parsing cli app that takes a raw informal address string and returns valid house number and street name

It neither follows any heuristics (trained or direct) nor cross verifies with an address repository of any sort

## Takeaway
Better ways to handle address parsing would be as follows; ranked.

1. Ask house and street directly to the user in concern
2. Use heuristics - either apply some direct ones or use a ML model that's trained for such data
3. Use utilities that have verbose and extensive set of keywords that help narrow down a single string into house and street names
4. Use utilities that matches the given addresses against a geospatial or address database of some sort