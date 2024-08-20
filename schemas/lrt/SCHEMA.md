# Liquid Restaking Tokens (LRTs)

Standard table definitions for LRTs (liquid restaking tokens)

## Version: 1.0.0-alpha

### Position Snapshot

User level snapshot of holders in this protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| chain_id                 | Standard chain ID.                                        | number |
| token_address            | The contract address of the LRT.                          | string |
| token_symbol             | The symbol of the token.                                  | string |
| user_address             | The address of the user holding the LRT.                  | string |
| amount                   | The amount of LRT tokens held in the protocol, decimal normalized. | number |
| amount_usd               | The amount held in USD.                                   | number |

### Protocol Snapshot

Snapshot at the protocol level, including, TVL and fees data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| chain_id                 | Standard chain ID.                                        | number |
| total_value_locked_usd   | The total value locked in USD (ie, the value of the liquid restaking tokens in the protocol). | number |
| fees_usd                 | The fees collected in USD in the given snapshot period.   | number |

> Note: This markdown file is auto-generated.
