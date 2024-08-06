# Liquid Staking Tokens (LSTs) Schema

This is the OpenBlock Labs standard schema for liquid staking tokens.

## Schema

### Position Snapshot

**Description:** User level snapshot of holders in this protocol.

| Property       | Description                                                      | Type   |
|----------------|------------------------------------------------------------------|--------|
| timestamp      | The timestamp of the snapshot.                                   | number |
| chain_id       | Standard chain ID.                                               | number |
| token_address  | The contract address of the LST.                                 | string |
| token_symbol   | The symbol of the token.                                         | string |
| user_address   | The address of the user holding the LST.                         | string |
| amount         | The amount of LST tokens held in the protocol, decimal normalized.| number |
| amount_usd     | The amount held in USD.                                          | number |
