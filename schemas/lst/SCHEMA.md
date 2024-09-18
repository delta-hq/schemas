# Liquid Staking Tokens (LSTs)

Standard table definitions for LSTs (liquid staking tokens)

## Version: 1.0.0-alpha

### Position Snapshot

User level snapshot of holders in this protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain ID.                                        | number |
| token_address            | The contract address of the LST token.                    | string |
| token_symbol             | The symbol of the token.                                  | string |
| user_address             | The address of the user holding the LST.                  | string |
| amount                   | The amount of LST tokens held in the protocol, decimal normalized. | number |
| amount_usd               | The amount held in USD.                                   | number |

### Protocol Snapshot

Snapshot at the protocol level, including, TVL and fees data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain ID.                                        | number |
| total_value_locked_usd   | The total value locked in USD (ie, the value of the liquid staking tokens in the protocol). | number |
| fees_usd                 | The fees collected in USD in the given snapshot period.   | number |

### Events

All user events in the lending protocol (ie, Mint, Burn, Transfer)

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | number |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The address that the event is from (ie, 0x00... address if a Mint). | string |
| to_address               | The address receiving the tokens (ie, the 0x000... address if a Burn). | string |
| token_address            | The contract address of the LST token.                    | string |
| amount                   | The amount of token_address transacted, decimal normalized. | number |
| amount_usd               | The amount of token_address transacted, in USD.           | number |
| event_type               | The type of event, corresponds to the action taken by the user (ie, mint, burn, transfer). | string |

> Note: This markdown file is auto-generated.
